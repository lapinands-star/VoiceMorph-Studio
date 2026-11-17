# Requirements
FR-01: Select real microphone and playback/virtual cable via existing vc-gui.
FR-02: GPU RVC v2 (ONNX/TensorRT), 3 authorized models (female, anime female, deep male).
FR-03: Control available pitch/F0, chunking, input gain, denoise and stop/passthrough; use existing UI/config.
FR-04: Route to OBS/Discord through externally installed virtual cable.
FR-05: Remain fully local without mandatory network during normal voice conversion.
FR-06: Load models only through validated formats, provide useful errors.
NFR-01: p95 mic->virtual output latency under 1000ms, 30min test; targets 300/150ms.
NFR-02: No growing backlog, repeated clicks or sustained dropouts; measure actual results.
NFR-03: Windows 11 x64 RTX 4080 16GB; benchmark while game uses GPU.
NFR-04: Russian speech, whisper, laugh, shout A/B; report inevitable artifacts honestly.
SEC-01: Native code, TensorRT helper/DLLs, model imports, downloads and scripts audited before approval.
SEC-02: Offline normal runtime; no persistence, forced updates or administrative operations.
SEC-03: Exact Git SHA, license inventory and release SHA-256; user consent for any model provisioning.
SEC-04: No release PASS without scoped independent static/dependency/binary/Windows/runtime evidence.
