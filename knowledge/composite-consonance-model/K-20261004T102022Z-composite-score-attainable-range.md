---
id: K-20261004T102022Z-composite-score-attainable-range
statement: "With a harmonic 11-partial 1/h timbre and default weights, 1500 random chords per size gave composite scores (median, p95, max) of 1.88/2.29/3.06 for 2 notes, 1.28/1.80/2.98 for 3 notes and 0.81/1.29/2.02 for 4 notes, so 4-note sonorities rarely exceed about 2.0 and a target of 2.4 collapses onto 3-4 repeated pitch classes."
status: current
supersedes: []
tags: [subject:composite-consonance-model, domain:music-perception, tech:python, tech:numpy, phase:verification]
applies_to_version: "consonance 0.1.0, default Weights, harmonic_timbre(11, 1.0)"
source: { url: "", doi: "", title: "docs/CALIBRATION.md in qualitycoding/Stream-of-consonance", locator: "attainable-range table; calibration row for target 2.4", accessed: "2026-09-20", tier: 3 }
confidence: verified
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:22Z
---
Random-search extremes underestimate the true maximum. At target 2.4 the sampler reached the tolerance 76% of the time with 4.3 distinct quarter-tone pitch classes per 30 notes.
