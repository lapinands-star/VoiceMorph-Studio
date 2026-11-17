# VoiceMorph Studio — documentation index
Forked from `shirohata/vc-rs` v0.5.5, source license MIT. Existing Windows
RVC/TensorRT implementation is the initial audio engine: no greenfield rewrite.

**Project contract:** `Request.md`, `requirements.md`, `Goals.md`, `Plan.md`,
`ProjectFinishCriteria.md`, `docs/RequirementsTraceability.md`.
**Code agent governance:** `AGENTS.md`, `.codex/config.toml`,
seven `.codex/agents/*.toml`. Configured does not mean invoked.
**Security posture:** `Security.md`, `SecurityAudit.md`,
`SecurityReview.md`, `audit.md`, `result.md`.
**Architecture/QA:** `docs/VoiceMorphArchitecture.md`,
`docs/VoiceMorphTestMatrix.md`, `docs/Decisions.md`,
`docs/UpstreamBaseline.md`.
**Executed checks:** `docs/P0-LineScan-2026-11-17.md`,
`docs/P0-SourceAudit-2026-11-17.md`,
`docs/P0-PTHFixturesAudit-2026-11-17.md`.

The five checked-in PTH test fixtures have passed a non-executing integrity
inspection, **not malware clearance of unrelated voice models**.
Published EXEs/DLLs and real Windows/GPU/OBS functionality remain UNTESTED.
All governance changes live in a Draft PR; upstream `main` stays unchanged.
