---
id: L-20261004T102003Z-window-semantics-off-by-one
title: "Sliding-window sampler scored one more note than it claimed; no test covered the parameter"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: High
tags: [domain:audio, tech:python, phase:verification, kind:verification-gap]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:03Z
---
## Trigger
A parameter defines which notes are scored together (window, sonority size) and calibration is measured with a separate routine.
## What went wrong
generate_stream(window=w) scored each candidate against the last w notes, so w+1 notes sounded, while the calibration harness measured windows of w. The first calibration run exposed the mismatch. None of the 42 frozen tests exercised `window`, so the bug passed the whole suite.
## Correction
Changed the state passed to the energy function to state[-(window-1):] in consonance/sampler.py and documented the semantics in the docstring. A regression test was NOT added because the suite was frozen; it is recorded as an open item.
## Prevention rule
For every parameter that defines the scored state, add a test asserting how many notes the energy function receives before writing calibration or demo code.
## Detection check
Run: grep -n 'window' tests/*.py ; there must be a test asserting len(state) + 1 == window for the first full-window step.
## Evidence
commit ab1b417 (consonance/sampler.py); IMPLEMENTATION_REPORT.md finding 1; .checkpoints/state.json open_items. The regression test is still absent. Recorded retroactively when the addendum was adopted mid-run.
