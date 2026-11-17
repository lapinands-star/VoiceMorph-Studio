# SecurityReview — source findings (preliminary; not independent reviewer approval)
| ID | Severity | Status | Location / evidence | Mitigation |
|---|---|---|---|---|
| SR-001 | Medium | CONFIRMED | `download-models.ps1:53-86` downloads and skips cached files without comparing SHA-256 | Do not use helper for MVP; prefer GUI pinned-hash fetch or vetted manual model provision |
| SR-002 | Medium | SURFACE | `crates/vc-core/src/model_rvc/native_tensorrt.rs:866-920` executes TensorRT helper, including env override | Verify builder EXE/DLLs, clear untrusted env override, narrow path lookup if required |
| SR-003 | TBD | NOT_TESTED | `crates/vc-convert/src/pickle.rs`, `torch.rs`, `zip.rs` parse hostile PTH | Rust interpreter reduces Python code exec; requires malicious-input fuzz/allocation testing |
| SR-004 | TBD | NOT_TESTED | Published 1.97GB TensorRT ZIP and native Nvidia DLLs | Independently download/hash/inventory/AV + source-build comparison |
| SR-005 | Low | REVIEW | `.github/workflows/ci.yml` uses some version tags for actions | Consider pinning in future small patch; not malware evidence |
| SR-006 | TBD | NOT_TESTED | `crates/vc-gui/src/model_setup.rs` and `crates/vc-models/src/lib.rs` have explicit HTTPS model acquisition | Distinguish setup from normal runtime with PID/DNS/TCP/UDP trace |
| SR-007 | TBD | NOT_TESTED | `Cargo.lock`, native TensorRT, Windows ML, third-party weights | Run cargo-deny on our fork and inventory all component licences |
| SR-008 | TBD | NOT_TESTED | Entire actual GUI/worker/FFI audio paths | Source scanner + manual review + Windows memory/runtime testing |
Assessment is **GO_WITH_CONTROLS for continued audit only**; **NO_GO_YET for trusted executable release**.
