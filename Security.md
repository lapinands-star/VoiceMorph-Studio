# Security.md — current posture and audit gate
Date 2026-11-17. **STATUS: STATIC_REVIEW_IN_PROGRESS / BINARY_NOT_TESTED / WINDOWS_NOT_TESTED.**
This Markdown file is a living security policy, NOT an executable. The full tracked-source inventory and line scanner are in `scripts/security_source_scan.py`, whose CI output must be examined independently.
Source fork `lapinands-star/VoiceMorph-Studio` pins upstream v0.5.5 at `a396451a4e1330323f060f8f217bd315dc7db830`. Main branch is deliberately untouched.
Observed from targeted source review: own Rust PTH interpreter (not Python eval), bounded ZIP input and guarded model downloads with SHA/size; external TensorRT builder process; optional PowerShell download helper lacks digest verification.
Unverified: released EXE/DLLs, arbitrary hostile PTH/ONNX model fuzz, secrets/telemetry via runtime, complete dependency threat review, machine/user driver, live voice and GPU. Do NOT claim clean/no virus.
No go for untrusted binary execution on primary PC until reviewed. Findings in `SecurityReview.md`, evidence in `audit.md`; project control in `Plan.md`.
