# Request — VoiceMorph Studio
Status: project specification, not completion evidence. Date: 2026-11-17.
Build by forking and **minimally changing** shirohata/vc-rs v0.5.5; local real-time conversion on Windows 11 / RTX 4080 16GB.
Mic -> RVC/TensorRT -> Windows output/VB-CABLE -> OBS / Discord / voice chat.
Required voice targets: natural female, female anime, deep male. User provides licensed compatible models; preserve Russian speech intelligibility, emotion and reasonable timbre.
Hard target: measured microphone-to-virtual-output latency p95 < 1s; desired <=300ms and stretch <=150ms, not a promised result. No cloud inference, automatic runtime downloads, telemetry or mandatory accounts. Preserve all upstream code/licenses, use existing GUI and audio engine first. No custom driver, new speech model, AI avatar, or voice cloning marketplace in MVP.
