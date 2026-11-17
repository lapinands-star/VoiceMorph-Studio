# audit.md — actual evidence log, 2026-11-17
- VERIFIED GitHub repo is fork of shirohata/vc-rs, main SHA `a396451a4e1330323f060f8f217bd315dc7db830`.
- VERIFIED GitHub App installation now lists the new fork; create_branch `chore/bootstrap-governance` succeeded.
- OBSERVED source-read via GitHub connector: `crates/vc-convert/src/pickle.rs`, `torch.rs`, `zip.rs`, `crates/vc-gui/src/model_setup.rs`, `crates/vc-models/src/lib.rs`, `crates/vc-core/src/model_rvc/native_tensorrt.rs`, `download-models.ps1`, `scripts/bootstrap.ps1`, `scripts/release.ps1`, CI, cargo policy, AGENTS.
- VERIFIED upstream run `https://github.com/shirohata/vc-rs/actions/runs/42074716951` succeeded for pinned commit (CPU/stub tests; not GPU).
- NOT_RUN fork GitHub Actions until PR opens; no independent manual reviewer invoked.
- NOT_TESTED release binary, Defender, DNS/network, native DLLs, full code execution, RTX 4080, OBS, actual audio latency.
- SCAN_PENDING: run checkout-based `scripts/security_source_scan.py` via `.github/workflows/security-source-review.yml`, read artifact and report how many text files/lines were actually scanned, which were skipped.
