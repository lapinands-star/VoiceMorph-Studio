# Plan — VoiceMorph Studio
Version 0.2, 2026-11-17. Project goal: fastest safe usable existing app, not greenfield.
P0: verify exact fork and upstream; full text-file/line inventory, human targeted code review, CI, dependencies, input/supply-chain; update security evidence. Do not auto-run a release ZIP.
P1: verify signed/unsigned binary asset, vendor DLLs, hashes; isolated Windows startup as standard user, licensed models provisioned explicitly; choose TensorRT GUI.
P2: test MAONO PD400X mic, GPU inference, VB-CABLE to OBS and Discord, three voice targets and Russian/emotional speech. Measure real latency, 30min soak and GPU game load.
P3: make only necessary small source changes (prefer configuration, then smallest patch); test regression, compare upstream.
P4: pack portable release with SHA/license manifest and independent QA/Security/Goals/ReviewMaster decision.
Sequence: CONFIGURE > PATCH > ADAPT > REPLACE. Freeze `main` unless reviewed; drafts first. After two identical failed attempts, BLOCKED_REPEAT and one diagnostic. Source-line scanner coverage is not a malware guarantee. Do not mark agents invoked without logs.
