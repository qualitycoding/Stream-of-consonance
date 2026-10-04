---
id: L-20261004T102010Z-plan-controls-not-traced-to-delivery
title: "Several plan and pre-mortem controls were never delivered and were not listed as deviations"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Medium
tags: [applies:all, phase:verification, kind:scope]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:10Z
---
## Trigger
Closing implementation of a plan whose steps and pre-mortem controls were written before the code.
## What went wrong
Checked against the repository: no CI workflow runs the frozen-hash check (plan S1, risk R12; only scripts/verify_frozen.sh exists); no domain-of-validity warning is emitted (risk R1); no S6 design note or numeric diversity thresholds exist (risk R7); the sequential terms (voice-leading, spectral distance) are not implemented. IMPLEMENTATION_REPORT.md lists the Langevin step, listening test, incon comparison and review gate as not done, but not these.
## Correction
Not corrected in code. Listed in DEVIATIONS.md as open items; S-RETRO changes no deliverable.
## Prevention rule
Before closing implementation, map every plan step and pre-mortem control to a file or test that delivers it, and list each unmapped one in DEVIATIONS.md.
## Detection check
Check that DEVIATIONS.md has a section naming each unmapped control; ls .github/workflows and grep -rni warn consonance show whether the CI and warning controls exist.
## Evidence
PLAN.md steps S1, S6 and the Phase 4 tables; ls -a; grep results in this turn. Recorded during S-RETRO.
