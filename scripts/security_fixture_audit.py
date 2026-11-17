#!/usr/bin/env python3
"""Non-executing inspection of the five checked-in RVC PTH test fixtures.

Never call pickle.load, torch.load, import model weights, or import fixture generators.
This validates Git artifact integrity, ZIP layout and CRC, and the pickle opcode
stream as DATA. It cannot establish a general guarantee against hostile checkpoints.
"""
import collections
import hashlib
import json
from pathlib import Path, PurePosixPath
import pickletools
import stat
import sys
import zipfile

BASE = Path(__file__).resolve().parent.parent
FIXTURES = {
    "tiny_applio_mrf.pth": "7d176512f18e39dc72d040d897fd51197c4fd08dfb2a2329cfd51689fbddbf57",
    "tiny_applio_refine.pth": "63505eed39f2bcff737c2da57c2559509007f774c0543c32d9a849affc1cca98",
    "tiny_v1.pth": "f2a304da63585c80b597eae58013d3e462b2d48dc67970551c60f59c6f1af53f",
    "tiny_v2_f0.pth": "e3ffe6c8affe5830212b242b4dabdae84dddeeec122794a753a2d7c2918c6517",
    "tiny_v2_nof0.pth": "5f663c9436a54cebbb85d90ef09c1170be92ed1b6b5c3b2508fa5079cbef1d35",
}
ALLOWED_GLOBALS = {
    "collections OrderedDict",
    "torch._utils _rebuild_tensor_v2",
    "torch._utils _rebuild_tensor_v3",
    "torch._utils _rebuild_parameter",
    "torch FloatStorage",
    "torch HalfStorage",
    "torch LongStorage",
    "torch BFloat16Storage",
    "torch DoubleStorage",
    "torch IntStorage",
    "torch ShortStorage",
    "torch ByteStorage",
    "torch BoolStorage",
    "_codecs encode",
    "builtins dict",
    "builtins set",
}

def inspect(path, expected):
    data = path.read_bytes()
    found = hashlib.sha256(data).hexdigest()
    r = {
        "name": path.name, "file_bytes": len(data), "sha256": found,
        "sha256_matches_pinned_source_scan": found == expected,
        "zip": zipfile.is_zipfile(path), "entries": [], "pickle": [],
        "issues": [], "runtime_executed": False
    }
    if found != expected:
        r["issues"].append("SHA256_MISMATCH")
    if not r["zip"]:
        r["issues"].append("NOT_ZIP_FORMAT")
        return r
    with zipfile.ZipFile(path, "r") as z:
        seen = set()
        infos = z.infolist()
        if len(infos) > 5000:
            r["issues"].append("EXCESSIVE_ENTRY_COUNT")
        total_unpacked = 0
        for info in infos:
            p = PurePosixPath(info.filename)
            mode = (info.external_attr >> 16) & 0xFFFF
            total_unpacked += info.file_size
            if (p.is_absolute() or ".." in p.parts or "\\" in info.filename or
                    info.filename in seen or info.flag_bits & 1 or
                    info.file_size > 8 * 1024 * 1024 or
                    info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED) or
                    stat.S_IFMT(mode) == stat.S_IFLNK):
                r["issues"].append("UNSAFE_OR_UNSUPPORTED_ENTRY:" + info.filename)
            seen.add(info.filename)
            r["entries"].append({
                "name": info.filename, "bytes": info.file_size,
                "compressed_bytes": info.compress_size,
                "crc32": f"{info.CRC:08x}", "compression": info.compress_type
            })
        r["unpacked_bytes"] = total_unpacked
        if total_unpacked > 32 * 1024 * 1024:
            r["issues"].append("EXPANDED_SIZE_EXCEEDED")
        try:
            bad = z.testzip()
        except Exception as exc:
            r["issues"].append("ZIP_CRC_EXCEPTION:" + type(exc).__name__)
        else:
            r["zip_crc_ok"] = bad is None
            if bad is not None:
                r["issues"].append("ZIP_CRC_FAILURE:" + bad)
        pkls = [i for i in infos if i.filename.endswith(".pkl")]
        if len(pkls) != 1:
            r["issues"].append("PICKLE_ENTRY_COUNT_" + str(len(pkls)))
        for item in pkls:
            if item.file_size > 2 * 1024 * 1024:
                r["issues"].append("PICKLE_TOO_LARGE")
                continue
            raw = z.read(item)
            counts = collections.Counter()
            globals_seen = []
            parse_status = "OK"
            try:
                for opcode, arg, pos in pickletools.genops(raw):
                    counts[opcode.name] += 1
                    if opcode.name == "GLOBAL":
                        globals_seen.append(arg)
                        if arg not in ALLOWED_GLOBALS:
                            r["issues"].append("UNKNOWN_PICKLE_GLOBAL:" + str(arg))
                    if opcode.name in {"STACK_GLOBAL", "EXT1", "EXT2", "EXT4", "INST", "OBJ"}:
                        r["issues"].append("UNRESOLVED_PICKLE_OPCODE:" + opcode.name)
            except Exception as exc:
                parse_status = type(exc).__name__ + ": " + str(exc)[:160]
                r["issues"].append("PICKLE_PARSE_ERROR")
            r["pickle"].append({
                "name": item.filename, "parse_status": parse_status,
                "opcode_count": sum(counts.values()),
                "opcodes": dict(counts),
                "globals": sorted(set(globals_seen)),
                "has_reduce": "REDUCE" in counts,
                "has_binary_persistent_id": "BINPERSID" in counts
            })
    r["static_integrity_pass"] = len(r["issues"]) == 0
    return r

def main():
    root = BASE / "crates" / "vc-convert" / "tests" / "fixtures"
    results = [inspect(root / name, sha) for name, sha in FIXTURES.items()]
    report = {
        "type": "PTH_TEST_FIXTURES_STATIC_INSPECTION",
        "scope": "tracked test fixtures, NOT external voice models or downloadable EXEs",
        "no_pickle_or_torch_execution": True,
        "results": results,
        "all_static_integrity_checks_pass": all(r.get("static_integrity_pass") for r in results)
    }
    Path("pth-fixture-audit.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for r in results:
        gs = sorted({g for p in r["pickle"] for g in p["globals"]})
        print(f"{r['name']}: bytes={r['file_bytes']} sha256={r['sha256']} "
              f"ZIP={r['zip']} members={len(r['entries'])} crc={r.get('zip_crc_ok')} "
              f"pickle_globals={gs} issues={r['issues']}")
    print("ALL_STATIC_CHECKS_PASS=", report["all_static_integrity_checks_pass"])
    return 0 if report["all_static_integrity_checks_pass"] else 1

if __name__ == "__main__":
    sys.exit(main())
