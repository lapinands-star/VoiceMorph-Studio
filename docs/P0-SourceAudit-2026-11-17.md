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

## Completed tracked-file scan, with exact boundaries
All tracked text files were scanned using a line-by-line deterministic rule pass on Actions runner, https://github.com/lapinands-star/VoiceMorph-Studio/actions/runs/44168180268. It processed 238 text files containing 78,429 lines, 0 unreadable source files, five excluded binary PTH test fixtures with hashes. 147 files matched review rules, mostly normal source patterns and docs; this is not a malicious-file count.

### Five binary fixtures NOT opened as source lines
- `crates/vc-convert/tests/fixtures/tiny_applio_mrf.pth`, SHA-256 `7d176512f18e39dc72d040d897fd51197c4fd08dfb2a2329cfd51689fbddbf57`
- `crates/vc-convert/tests/fixtures/tiny_applio_refine.pth`, SHA-256 `63505eed39f2bcff737c2da57c2559509007f774c0543c32d9a849affc1cca98`
- `crates/vc-convert/tests/fixtures/tiny_v1.pth`, SHA-256 `f2a304da63585c80b597eae58013d3e462b2d48dc67970551c60f59c6f1af53f`
- `crates/vc-convert/tests/fixtures/tiny_v2_f0.pth`, SHA-256 `e3ffe6c8affe5830212b242b4dabdae84dddeeec122794a753a2d7c2918c6517`
- `crates/vc-convert/tests/fixtures/tiny_v2_nof0.pth`, SHA-256 `5f663c9436a54cebbb85d90ef09c1170be92ed1b6b5c3b2508fa5079cbef1d35`

### Additional manual risk observations
- `windows_ml.rs:29,533-546`: env `VC_RS_WINDOWSML_BOOTSTRAP_DLL` can select a DLL path; avoid untrusted override.
- `native_tensorrt_shim.cpp:861-897`: bundled native DLL location is preferred; returns default OS loader fallback if unavailable.
- `vc-convert/src/lib.rs:139-150`: fixed `*.onnx.tmp` staging file; use verified ONNX in MVP, revisit if hostile directories supported.

### Not within this pass
The distributed TensorRT Windows release ZIP, DLL/EXE behavior, full advisories, local Defender, binary source reproducibility and real Windows mic/GPU/network tests. A deterministic static line scan cannot prove malicious intent absent.
