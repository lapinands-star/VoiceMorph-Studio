# SecurityAudit — mandatory scope and methods
Source target: `lapinands-star/VoiceMorph-Studio`, pinned upstream SHA `a396451a4e1330323f060f8f217bd315dc7db830`.
1. Inventory every tracked file, code and script; scan every line with `scripts/security_source_scan.py`. Binary checkpoints, archives, DLLs and EXEs require separate analysis, not line scanning.
2. Manually review every location that can execute code, launch process, dynamically load DLLs, fetch network content, parse untrusted models, allocate from untrusted sizes, install drivers, persist data, or weaken protection.
3. Verify SHA and provenance of release asset, source/build mismatch, model downloader, `.pth` Rust ZIP/pickle parsing, ONNX, TensorRT builder, native libraries and caches.
4. Inspect Cargo.lock / dependency advisories and licenses, CI workflow actions, PowerShell bootstrap/release and VST3 packaging scripts.
5. Runtime: process tree, filesystem, services/autorun, DNS/TCP/UDP/PID/time, Defender scan, GPU audio, virtual cable; record exactly what was measured.
6. Findings: stable ID, path:line, reachable exploit preconditions, risk, evidence, mitigation, actual review/test result.
Only executed checks can be PASS; static absence of a signature never proves benign behavior. No auto network/model download on app normal run.
