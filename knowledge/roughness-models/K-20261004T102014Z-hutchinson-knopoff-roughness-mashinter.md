---
id: K-20261004T102014Z-hutchinson-knopoff-roughness-mashinter
statement: "incon's Hutchinson-Knopoff roughness uses Mashinter's parametrisation: critical bandwidth CBW = 1.72*mean_f^0.65, y = |f1-f2|/CBW, g(y) = ((y/0.25)*exp(1 - y/0.25))^2 with g = 0 for y > 1.2, and roughness = sum of a_i*a_j*g over partial pairs divided by the sum of squared amplitudes."
status: current
supersedes: []
tags: [subject:roughness-models, tech:r-incon, domain:music-perception, phase:implementation]
applies_to_version: "incon 0.5.0 (MIT)"
source: { url: "https://github.com/pmcharrison/incon/blob/master/R/model-dycon.R", doi: "", title: "incon R/model-dycon.R", locator: "hutch_dissonance_function, hutch_g (cbw_cut_off = 1.2, a = 0.25, b = 2)", accessed: "2026-10-04", tier: 1 }
confidence: verified
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:14Z
---
The 1.2 cut-off is documented in the source as necessary to replicate Mashinter's results and as also used by Bigand et al. (1996). The normalisation by the sum of squared amplitudes is from the S0 reading of the source.
