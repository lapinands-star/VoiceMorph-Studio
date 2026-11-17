# Upstream baseline and provenance — vc-rs
**Original:** https://github.com/shirohata/vc-rs
**Verified fork:** https://github.com/lapinands-star/VoiceMorph-Studio
**Upstream tag:** v0.5.5 (published 2026-11-05)
**Source commit / unchanged fork main:** `a396451a4e1330323f060f8f217bd315dc7db830`
**Software source license:** MIT (original LICENSE preserved). Voice models,
ContentVec, RMVPE, TensorRT, Windows ML and external virtual drivers have
independent redistribution/use terms; check individually.

## Release package awaiting binary examination
- Official asset: `vc-rs-tensorrt-v0.5.5-win-x64.zip`.
- Publisher-provided SHA-256:
`99011e0b6196c042cee214a19175d8d863af107889ba698c3e70f6d589ba7900`
- **Locally downloaded/hashed by our audit? NO.**
- **Contained EXE/DLL static inspection or Defender scan? NO.**
- **Windows standard-user / RTX 4080 smoke? NO.**

## Source test fixture provenance
All five tracked synthetic .pth test files have identical Git blob SHA in
upstream and fork; content hashes are documented in
`docs/P0-PTHFixturesAudit-2026-11-17.md`.
Their structure passes a non-executing ZIP/CRC/pickle-opcode audit, but these
random/untrained or deliberately incompatible examples are **not** voice profiles.
