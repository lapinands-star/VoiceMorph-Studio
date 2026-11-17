# Security.md — current posture and audit gate
Date 2026-11-17. **STATUS: AUTOMATED_TEXT_LINE_SCAN_PASS / HUMAN_REVIEW_PARTIAL / BINARY_NOT_TESTED / WINDOWS_NOT_TESTED.**
This Markdown file is a living security policy, NOT an executable. The full tracked-source inventory and line scanner are in `scripts/security_source_scan.py`, whose CI output must be examined independently.
Source fork `lapinands-star/VoiceMorph-Studio` pins upstream v0.5.5 at `a396451a4e1330323f060f8f217bd315dc7db830`. Main branch is deliberately untouched.
Observed from targeted source review: own Rust PTH interpreter (not Python eval), bounded ZIP input and guarded model downloads with SHA/size; external TensorRT builder process; optional PowerShell download helper lacks digest verification.
Unverified: released EXE/DLLs, arbitrary hostile PTH/ONNX model fuzz, secrets/telemetry via runtime, complete dependency threat review, machine/user driver, live voice and GPU. Do NOT claim clean/no virus.
No go for untrusted binary execution on primary PC until reviewed. Findings in `SecurityReview.md`, evidence in `audit.md`; project control in `Plan.md`.

## Latest actual evidence
CI source scanner PASS: https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44168180268
It examined 238 UTF-8 text files and 78,429 lines of 243 tracked files, with 0 read errors.
Five PTH binary fixtures were inventoried and SHA-256 hashed, not decoded/executed.
147 files contained one or more heuristic keyword hits; these are NOT 147 vulnerabilities.
Human review concentrated on PTH ZIP/pickle, model downloader, external process execution, DLL resolution and scripts; every source line has NOT been individually adjudicated by a human.
Release EXE/DLL package (approx 1.97 GB), model inference, Windows AV, GPU and DNS/TCP/UDP live traces remain NOT_TESTED.
