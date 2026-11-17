# VoiceMorph Studio — architecture decisions
**Status:** APPROVED_FOR_MVP_SCOPE, not proof of a working application. 2026-11-17.

## ADR-001 — Fork vc-rs instead of building from scratch
Use the original Rust/ONNX/TensorRT vc-rs GUI and inference stack at v0.5.5.
Keep upstream code and history, MIT license and third-party notices intact.
CONFIGURE > PATCH > ADAPT > REPLACE. Only add essential patches after a reproducible blocker.

## ADR-002 — Do not add new neural voice engines to MVP
MeanVC2/audio.cpp, Seed-VC and Beatrice remain fallback candidates for future
comparative benchmarks. No additional inference backend before proving RVC unsuitable
for one of the three requested voices.

## ADR-003 — Reuse a trusted virtual-audio cable
Use OBS/Discord via existing local playback and a separately installed virtual
cable, such as VB-CABLE. No custom kernel driver in the fork; any driver install
requires an explicit user action and a separate provenance check.

## ADR-004 — Fully local routine operation
No cloud inference or runtime-required network traffic. Auxiliary model
downloads are explicit setup activities. The existing optional PowerShell
download-models.ps1 is NOT approved until digest verification is added.

## ADR-005 — External models are untrusted
Prefer inspected ONNX weights. Five synthetic PTH test fixtures passed static
checks; this does not clear third-party .pth files for import or execution.
Continue with source parser fuzzing and binary/DLL runtime validation before release.

## ADR-006 — Objective quality and performance
Measure true mic-to-virtual-output latency p50/p95 and 30-minute stability.
Target p95 under one second; preserve intelligibility of Russian and expressive
speech. No claims of zero audible artifacts without measurement.
