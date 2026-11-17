# audit.md — verified chronological evidence log
**Date: 2026-11-17.** The status below is not retroactively rewritten as PASS.

## Provenance
- Real GitHub fork of `shirohata/vc-rs`, main SHA
  `a396451a4e1330323f060f8f217bd315dc7db830`, v0.5.5.
- Governance changes are published in `chore/bootstrap-governance`, PR #1 draft.
- Five fixture Git blob SHAs in the fork equal original upstream repository's
  blobs on same source commit. Original generators stored in
  `crates/vc-convert/tests/fixtures/make_*_pth.py`.

## Automated verification
- Static source scanner PASS: run
  https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44169677800
  (commit `f90d94a51a62951333131fb0b0c70d7806191e5a`):
  **246 tracked files, 241 UTF-8 text, 78,640 lines, 5 binary PTH, 0 read errors**.
  Matches are review triggers, not confirmed vulnerabilities.
- Five PTH ZIP / CRC / SHA-256 / pickle-opcode non-executing inspections PASS:
  https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44169677915
  artifact https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44169677915/artifacts/14367790936 .
  Exact per-file evidence in `docs/P0-PTHFixturesAudit-2026-11-17.md`.
- Earlier fork cargo-deny run passed for unchanged dependencies at
  https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44168179935
  (overall CI later CANCELLED by new PR commit). Latest complete CI not yet accepted.
- Original upstream baseline CPU/stub CI success:
  https://github.com/shirohata/vc-rs/actions/runs/42074716951 .

## Manual targeted source review
Examined Rust PTH parser, `zip.rs`, `torch.rs`, model downloaders,
TensorRT builder process, Windows ML DLL bootstrap, C++ DLL loader fallback,
PowerShell bootstrap/release and GitHub CI controls.
Findings SR-001, SR-002, SR-009, SR-010 in `SecurityReview.md`.

## Not yet examined
- Published 1.97GB Windows TensorRT EXE/DLL ZIP and signatures/AV scanning.
- Full adversarial model fuzzing, native GPU DLL execution/memory safety.
- Actual Windows 11 mic/OBS/Discord operation, GPU stress, network PID tracing.
- Independent subagent reviews; configurations alone are NOT_INVOKED.
