# Security.md — current evidence-based posture
**2026-11-17 | P0 IN PROGRESS**

| Area | Status | Evidence |
|---|---|---|
| Text source-line scanner | PASS (automated; no claim of manual per-line review) | Run 44169677800: 241 text files / 78,640 lines / 0 read failures |
| Five checked-in synthetic `.pth` fixtures | PASS (non-executing ZIP/CRC/digest/pickle opcode inspection) | Run 44169677915, details: docs/P0-PTHFixturesAudit-2026-11-17.md |
| Untrusted external PTH/ONNX models | NOT_CLEARED | Rust ZIP/pickle parser requires adversarial fuzz and model isolation |
| Official Windows TensorRT ZIP, EXE/DLLs | NOT_TESTED | Publisher SHA known, archive not independently downloaded/inspected |
| Windows 11 / GPU / Defender / network telemetry | HARDWARE_REQUIRED | No RTX 4080 / VM execution or DNS/TCP/UDP trace |
| Complete dependency/security sign-off | IN_PROGRESS | cargo-deny passed earlier unchanged code graph; full CI on newest commit check pending |
| Seven reviewer agents | NOT_INVOKED | Files configured; no independent agent decisions produced |

The source application is `shirohata/vc-rs` v0.5.5, fork
`lapinands-star/VoiceMorph-Studio`, upstream `main` SHA
`a396451a4e1330323f060f8f217bd315dc7db830`. 
Main remains unmodified; changes are in `chore/bootstrap-governance`.

**Confirmed surfaces:** optional `download-models.ps1` does not verify downloaded
hashes; native TensorRT builder process and Windows ML bootstrap DLL can be
selected by environment; converted ONNX output uses predictable `*.tmp` staging.
See `SecurityReview.md`, `SecurityAudit.md`, `audit.md`.

**Decision:** continue scoped audit. **Do not claim malware-free**, and do not
trust/run the unverified release EXE on the primary PC until binary and runtime
checks are complete. Pre-provisioned models may enable offline runtime, but
absence of outgoing traffic has not yet been measured.
