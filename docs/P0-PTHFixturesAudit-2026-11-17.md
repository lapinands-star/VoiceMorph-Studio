# Five PTH fixtures — completed non-executing inspection
**Date:** 2026-11-17
**GitHub Actions:** https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44169677915
**Artifact:** https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44169677915/artifacts/14367790936
**Source commit for this execution:** `f90d94a51a62951333131fb0b0c70d7806191e5a`
**Method:** `python3 scripts/security_fixture_audit.py` (stdlib `zipfile`,
`hashlib`, `pickletools.genops`). **No `pickle.load()` or `torch.load()`.**

## Independent checks
- Exact file SHA-256 matches hashes recorded by source-line inventory;
  fork Git blob SHAs match original upstream v0.5.5.
- All five files open as ZIP and `zipfile.testzip()` passes CRC.
- No archive traversal paths, duplicate/encrypted/symlink entries or
  unsupported methods under the scanner's rules.
- Data pickle streams can be parsed into opcodes without executing them.
- Encoded `GLOBAL` references limited to expected collection/torch constructors
  per the inspector; no unexpected `STACK_GLOBAL` or pickle extension opcodes.
- Synthetic generator scripts `make_tiny_pth.py` and `make_applio_pth.py`
  explicitly create dummy weights without importing real PyTorch at generation time.
  The generator scripts were **inspected, not executed** during this audit.

| Fixture | Size (bytes) | ZIP entries | SHA-256 | Static integrity |
|---|---:|---:|---|---|
| tiny_applio_mrf.pth | 222772 | 371 | `7d176512f18e39dc72d040d897fd51197c4fd08dfb2a2329cfd51689fbddbf57` | PASS |
| tiny_applio_refine.pth | 380015 | 396 | `63505eed39f2bcff737c2da57c2559509007f774c0543c32d9a849affc1cca98` | PASS |
| tiny_v1.pth | 663 | 2 | `f2a304da63585c80b597eae58013d3e462b2d48dc67970551c60f59c6f1af53f` | PASS |
| tiny_v2_f0.pth | 221189 | 368 | `e3ffe6c8affe5830212b242b4dabdae84dddeeec122794a753a2d7c2918c6517` | PASS |
| tiny_v2_nof0.pth | 663 | 2 | `5f663c9436a54cebbb85d90ef09c1170be92ed1b6b5c3b2508fa5079cbef1d35` | PASS |

**Intended usage:** synthetic/untrained parser and conversion test vectors.
`tiny_v1` and `tiny_v2_nof0` are negative compatibility test cases; these are not
working audio voices. No included fixture is approved as a production voice.

## Important security boundary
PASS means **static hash/integrity/structural audit of exactly five known
fixtures**, not a general malware-free verdict, and not a fuzz test of the Rust
converter. Untrusted third-party `.pth` files, GPU ONNX inference and the binary
Windows release remain unapproved until separately examined. Finding SR-003
is narrowed for the bundled fixture set, not closed for hostile PTH.
