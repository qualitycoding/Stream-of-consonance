---
id: L-20261004T102002Z-perf-test-budget-not-derived
title: "First performance test dictated an unattainable budget instead of deriving it from the requirement"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Medium
tags: [tech:pytest, phase:specification, kind:verification-gap]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:02Z
---
## Trigger
Writing a frozen performance-budget test before any implementation or measurement exists.
## What went wrong
The first draft of tests/test_operational.py timed 6000 Python-level m.score calls inside the energy function against a 1 s budget. The budget came from the test's own shape, not from a requirement or a measurement, so no reasonable implementation could meet it. It was caught on self-review before the first commit.
## Correction
Invoked the plan's Reset Rule while nothing was committed: replaced the test with a call through a vectorised public API (CompositeModel.score_with_candidates) over 1200 candidates with a 2 s budget, and recorded the reset in PLAN.md.
## Prevention rule
Derive every performance budget from a measured reference run or a stated requirement, and time only the public API that is meant to serve that workload.
## Detection check
Run: grep -B3 'mark.perf' tests/*.py ; each perf test should have an adjacent comment naming the measured baseline or the requirement.
## Evidence
PLAN.md 'Reset log' under Phase 2; commit bfc418a (final test); tests/test_operational.py. Recorded retroactively when the addendum was adopted mid-run.
