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

| SR-009 | Low, conditional | CODE_RISK | `crates/vc-convert/src/lib.rs:139-150` uses a fixed `*.onnx.tmp` path with `std::fs::write`; assess pre-existing-file/symlink overwrite in attacker-writable model directory | For normal use import preverified ONNX; if PTH enabled, use unique create_new staging/rename after focused test |
| SR-010 | Medium, conditional | CODE_SURFACE | `crates/vc-core/src/windows_ml.rs:29,533-546` permits `VC_RS_WINDOWSML_BOOTSTRAP_DLL` override of bootstrapper path; native TensorRT shim `:861-897` falls back to DLL search | Avoid env overrides, inventory verified DLLs and normal PATH, prefer bundled TensorRT package; no evidence of exploitation |
| SR-011 | Info | SCAN_PASS | GitHub Actions 44168180268 scanned 238 text files / 78,429 lines; 5 PTH binary fixtures only hashed; 0 open/read failures | Independently adjudicate flagged paths; automatic matches are NOT vulnerability proof |
No direct code-level evidence of credential exfiltration, persistence installation or Defender-disabling commands was found in the **automated pattern pass**. This statement does not exclude obfuscated behavior, dependency exploits or malware in native release binaries.
