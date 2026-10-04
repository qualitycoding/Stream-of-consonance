---
id: L-20261004T102011Z-untested-causal-explanation-stated-as-fact
title: "A causal explanation for the pitch-mode results was stated as fact without a test"
status: active
supersedes: []
recurrence_of: null
occurrences: 1
severity: Low
tags: [domain:music-perception, phase:verification, kind:verification-gap]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:11Z
---
## Trigger
Explaining why an experiment came out as it did, in a reply or report.
## What went wrong
The pitch-mode reply said coarse grids lose little because the score landscape is smooth in log-frequency. No run varied smoothness or grid spacing to test that, so it was a hypothesis presented as a finding.
## Correction
Recorded here; the claim was not repeated in any file. A test would compare accuracy across several grid spacings on the same seeds.
## Prevention rule
Label any causal explanation not backed by a run in the same session as a hypothesis and name the test that would check it.
## Detection check
Scan the reply or report for 'because' and 'since'; each must carry a hypothesis label or cite a run.
## Evidence
Pitch-mode reply; docs/PITCH_MODES.md contains only the accuracy numbers. Recorded during S-RETRO.
