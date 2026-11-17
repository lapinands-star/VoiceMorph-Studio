# audit.md — actual evidence log, 2026-11-17
- VERIFIED GitHub repo is fork of shirohata/vc-rs, main SHA `a396451a4e1330323f060f8f217bd315dc7db830`.
- VERIFIED GitHub App installation now lists the new fork; create_branch `chore/bootstrap-governance` succeeded.
- OBSERVED source-read via GitHub connector: `crates/vc-convert/src/pickle.rs`, `torch.rs`, `zip.rs`, `crates/vc-gui/src/model_setup.rs`, `crates/vc-models/src/lib.rs`, `crates/vc-core/src/model_rvc/native_tensorrt.rs`, `download-models.ps1`, `scripts/bootstrap.ps1`, `scripts/release.ps1`, CI, cargo policy, AGENTS.
- VERIFIED upstream run `https://github.com/shirohata/vc-rs/actions/runs/42074716951` succeeded for pinned commit (CPU/stub tests; not GPU).
- NOT_RUN fork GitHub Actions until PR opens; no independent manual reviewer invoked.
- NOT_TESTED release binary, Defender, DNS/network, native DLLs, full code execution, RTX 4080, OBS, actual audio latency.
- SCAN_PENDING: run checkout-based `scripts/security_source_scan.py` via `.github/workflows/security-source-review.yml`, read artifact and report how many text files/lines were actually scanned, which were skipped.

- **AUTOMATED_LINE_SCAN_PASS:** Run https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44168180268 on commit `10a0e4c1295e930cad69d3ade6cf2f80891486d5`; 243 tracked files, 238 text, 78,429 lines, 0 file-read errors, 5 binary fixture PTH files skipped for text analysis and hashed.
- ARTIFACT: https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44168180268/artifacts/14365778770 ; workflow upload digest `sha256:c30f150891adf57a1a3b00a1a1fbff1f83353800b0d848b077720e23c34c5839`.
- PATTERN REVIEW: process execution 31 matches; networking 718; native dynamic 146; unsafe/FFI 122; persistence/security controls 1 (in scan script itself); 147 files with at least one trigger. Counts include comments/docs/tests and self scanner: not proven threats.
- **HUMAN_REVIEW_PARTIAL:** read targeted source ranges in windows_ml.rs, native_tensorrt.rs, native_tensorrt_shim.cpp, gpu.rs, process_priority.rs and PTH conversion, identified potential temp-file overwrite and Windows ML bootstrap override.
- **NOT_OPENED_AS_SOURCE:** 5 binary fixture .pth blobs. **NOT_DOWNLOADED/NOT_SCANNED:** actual 1.97GB upstream TensorRT Windows ZIP and all contained EXE/DLLs.
