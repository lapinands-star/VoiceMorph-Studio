# SecurityReview — findings, 2026-11-17
**Classification:** source-based preliminary findings, not independent reviewer sign-off.
**Decision:** GO_WITH_CONTROLS for continued audit; NOT_CLEARED for binary release.

| ID | Severity | Status | Code/scope | Evidence and next action |
|---|---|---|---|---|
| SR-001 | Medium | CONFIRMED | `download-models.ps1:53-86` | Optional downloader skips existing weights and downloads without independent SHA-256; avoid this script in MVP |
| SR-002 | Medium (conditional) | REVIEW_REQUIRED | `crates/vc-core/src/model_rvc/native_tensorrt.rs:866-920` | TensorRT builder subprocess and env path override; verify builder EXE and DLL provenance |
| SR-003 | TBD | TEST_FIXTURES_PASS, HOSTILE_INPUT_NOT_TESTED | `crates/vc-convert/src/{pickle,torch,zip}.rs` | Five synthetic PTH files passed static SHA/ZIP/CRC/pickle-opcode checks; arbitrary malicious checkpoint fuzzing still required |
| SR-004 | TBD | NOT_TESTED | Official TensorRT Windows ZIP / EXE / DLL | Independently download, hash, inventory and Defender scan; do not equate publisher digest with independently verified bytes |
| SR-005 | Low | REVIEW | `.github/workflows/ci.yml` | Some Actions references use version tags; optional future pinning after functional gate |
| SR-006 | TBD | STATIC_REVIEW_PARTIAL | `crates/vc-gui/src/model_setup.rs`, `crates/vc-models/src/lib.rs` | Explicit HTTPS downloads with size/SHA; ordinary runtime DNS/TCP/UDP not tested |
| SR-007 | TBD | DEPENDENCY_REVIEW_PARTIAL | `Cargo.lock`, GPU native components and model weights | Prior cargo-deny success for unchanged Cargo.lock, complete third-party binary/weights verification pending |
| SR-008 | TBD | STATIC_SCAN_PASS, RUNTIME_NOT_TESTED | GUI/audio/FFI/source tree | Latest completed line scan 44169677800: 241 text files, 78,640 lines, zero unreadable; 5 binary PTH fixtures separately inspected |
| SR-009 | Low (conditional) | REVIEW_REQUIRED | `crates/vc-convert/src/lib.rs:139-150` | Fixed `*.onnx.tmp` path with ordinary `std::fs::write`; inspect pre-existing file/symlink overwrite if importing untrusted PTH in writable directories |
| SR-010 | Medium (conditional) | REVIEW_REQUIRED | `crates/vc-core/src/windows_ml.rs:29,533-546`; `native_tensorrt_shim.cpp:861-897` | Env DLL override and native loader fallback; avoid untrusted env/PATH and validate shipped DLLs |
| SR-011 | Informational | PASS_SCOPE_ONLY | `scripts/security_fixture_audit.py` | Exact five known PTH fixtures all static integrity checks PASS; no model code was executed |

A source signature scan cannot rule out hidden malicious behavior, unsafe native
dependencies or data-dependent vulnerabilities. No evidence-based conclusion
of release safety is possible until binary and Windows runtime assessment.
