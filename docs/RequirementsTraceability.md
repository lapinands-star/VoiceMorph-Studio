# Requirement → goal → acceptance gate
**Scope:** design traceability; tests are not implicitly done.

| Requirement | Demonstrated behavior | Goal | Acceptance |
|---|---|---|---|
| FR-01 | Windows live microphone and selected device | G-004 / G-006 | CP-04 / CP-06 |
| FR-02 | Three compatible authorized RVC voices on RTX GPU | G-005 | CP-05 |
| FR-03 | Existing pitch/F0/chunk/denoise/start-stop control | G-004 / G-005 | CP-04 / CP-05 |
| FR-04 | OBS/Discord virtual-cable audio | G-006 | CP-06 |
| FR-05 | Local conversion and no outbound traffic | G-008 | CP-08 |
| FR-06 | Compatible model import with errors and boundaries | G-002 / G-005 | CP-02 / CP-05 |
| NFR-01 | Measured end-to-end p95 < 1,000ms / 30min | G-007 | CP-07 |
| NFR-02 | No growing queue; test underruns and long-run stability | G-007 | CP-07 |
| NFR-03 | Windows 11 RTX4080 game stress, no OOM | G-006 / G-007 | CP-06 / CP-07 |
| NFR-04 | A/B Russian, emotion, laughter, whisper | G-005 / G-007 | CP-05 / CP-07 |
| SEC-01 | Hostile input and EXE/DLL review | G-002 / G-003 | CP-02 / CP-03 |
| SEC-02 | User-level operation, no autoupdate or unexpected network | G-004 / G-008 | CP-04 / CP-08 |
| SEC-03 | Source/asset SHA and license inventory | G-001 / G-003 / G-010 | CP-01 / CP-03 / CP-10 |
| SEC-04 | Independent evidence and signed-off release decision | G-010 | CP-10 |

Source of truth: `Request.md`, `requirements.md`, `Plan.md`,
`ProjectFinishCriteria.md`; actual outcomes in `result.md`.
