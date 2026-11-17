#!/usr/bin/env python3
"""Inventory every tracked source line and flag code security review surfaces.
This is deterministic static triage, NOT a malware detector or full manual review.
Only stdlib; no network or subprocess execution except git ls-files metadata.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

BIN_EXT = {".pth", ".onnx", ".safetensors", ".gguf", ".zip", ".dll", ".exe",
           ".png", ".jpg", ".jpeg", ".webp", ".ico", ".gif", ".wav", ".mp3", ".bin"}
PATTERNS = {
 "process_exec": r"Command::new|Process\.Start|Start-Process|subprocess\.(?:run|Popen)|CreateProcess|ShellExecute|\bos\.system\b|Invoke-Expression|\biex\b|\bwinget\b|\bgit\s+push\b",
 "network": r"reqwest|ureq|TcpStream|TcpListener|UdpSocket|Invoke-WebRequest|Invoke-RestMethod|https?://|\bcurl\b|\bwget\b",
 "dynamic_native": r"LoadLibrary|GetProcAddress|libloading|\bdlopen\b|VC_RS_TENSORRT_BUILDER_HELPER|\.dll\b",
 "unsafe_ffi": r"\bunsafe\b|extern\s+\"(?:C|system)\"|from_raw_parts|transmute|memcpy\s*\(",
 "persistence_security": r"Register-ScheduledTask|schtasks|RunOnce|CurrentVersion\\Run|Add-MpPreference|Set-MpPreference|DisableRealtimeMonitoring|CreateService|New-NetFirewallRule|Set-ExecutionPolicy",
 "model_input": r"pickle|pth_to_onnx|ZipArchive|read_to_end|deserialize|tensor_rt_builder|f0_model|onnx",
 "credentials": r"password|api[_-]?key|secret|token|credential",
}
COMPILED = {key: re.compile(expr, re.IGNORECASE) for key, expr in PATTERNS.items()}
def git_files(root):
    data = subprocess.check_output(["git", "-C", str(root), "ls-files", "-z"])
    return sorted(Path(s.decode("utf-8", errors="replace")) for s in data.split(b"\0") if s)
def scan(root):
    result = {"schema": 1, "claim": "automated text-line scan, not expert line-by-line review",
              "file_count": 0, "text_files": 0, "text_lines": 0,
              "binary_files": [], "errors": [], "files": [], "findings": []}
    for rel in git_files(root):
        result["file_count"] += 1
        path = root / rel
        try:
            data = path.read_bytes()
        except (OSError, ValueError) as exc:
            result["errors"].append({"file": str(rel), "error": str(exc)})
            continue
        if rel.suffix.lower() in BIN_EXT or b"\x00" in data[:16384]:
            result["binary_files"].append({"file": str(rel), "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest()})
            continue
        try:
            decoded = data.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            result["errors"].append({"file": str(rel), "error": "non-UTF8: "+str(exc)})
            continue
        lines = decoded.splitlines()
        hits = []
        for index, line in enumerate(lines, 1):
            flags = [name for name, rx in COMPILED.items() if rx.search(line)]
            if flags:
                hits.append({"line": index, "rules": flags, "snippet": line[:280]})
        result["text_lines"] += len(lines)
        result["text_files"] += 1
        result["files"].append({"file": str(rel), "lines": len(lines),
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "flagged_lines": len(hits)})
        if hits:
            result["findings"].append({"file": str(rel), "hits": hits})
    return result
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--output", default="security-source-scan.json")
    args = p.parse_args()
    report = scan(Path(args.root).resolve())
    dest = Path(args.output).resolve()
    dest.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"scanned {report['text_files']} text files, {report['text_lines']} lines "
          f"of {report['file_count']} tracked files")
    print(f"binary/not-line-scanned={len(report['binary_files'])} errors={len(report['errors'])} "
          f"files_with_flags={len(report['findings'])}")
    if report["errors"]:
        for issue in report["errors"]:
            print("UNREADABLE",issue, file=sys.stderr)
        return 2
    return 0
if __name__ == "__main__":
    sys.exit(main())
