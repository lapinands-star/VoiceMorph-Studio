# P0 source audit — 2026-11-17
Scope: repository metadata and targeted manual source reads + planned line-complete CI scanner. No Windows/GPU/binary analysis.
Verified fork main SHA: `a396451a4e1330323f060f8f217bd315dc7db830`.
Positive controls: native `vc-convert` Rust PTH parser without Python eval; bounded ZIP 2GB input, 64MB pickle, ZIP CRC; model GUI HTTPS + pinned SHA256 and unique temporary staging; separate audio worker as claimed upstream.
Finding SR-001: `download-models.ps1:53-86` invokes web download then moves into assets with **no independent SHA-256** and skips prior file unverified.
Finding SR-002: `native_tensorrt.rs:866-920` launches external executable, allows `VC_RS_TENSORRT_BUILDER_HELPER`; expected behavior, but executable provenance and env trust required.
Finding SR-003: untrusted `.pth` remains a parser/DoS/ONNX graph risk despite absence of Python eval. Fuzzing required.
Finding SR-004: releases bundle native TensorRT DLLs, 1.97GB ZIP digest published by owner but unverified locally. Scan and hash before execution.
CI: upstream success at https://github.com/shirohata/vc-rs/actions/runs/42074716951; it explicitly disables real NVIDIA hardware in CI. No proof of RTX startup.
GitHub access: installed GitHub App now includes fork; governance branch created. No release/executable run.
Decision: CONTINUE_SOURCE_AUDIT; NO_GO_YET for release on trusted Windows host.
