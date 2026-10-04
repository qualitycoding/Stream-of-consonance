---
id: K-20261004T102013Z-incon-composite-coefficients
statement: "incon 0.5.0 har_19_composite_coef: intercept 0.628434666589357; chord_size 0.422267698605598; hutch_78_roughness -1.62001025973261; har_18_harmonicity 1.77992362857478; har_19_corpus -0.0892234643584134, applied to corpus dissonance (= -log P), so +0.0892 on log P."
status: current
supersedes: []
tags: [subject:composite-consonance-model, tech:r-incon, domain:music-perception, phase:implementation]
applies_to_version: "incon 0.5.0 (MIT)"
source: { url: "https://github.com/pmcharrison/incon/blob/master/R/model-har-2019.R", doi: "", title: "incon R/model-har-2019.R", locator: "har_19_composite_coef tribble", accessed: "2026-10-04", tier: 1 }
confidence: verified
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:13Z
---
Re-fetched 2026-10-04 and the numbers match the S0 reading. Per the S0 reading in research/RESEARCH_LOG.md, incon leaves the chord_size term off by default; this project does the same (Weights.n_notes = 0).
