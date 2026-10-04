---
id: K-20261004T102015Z-sethares-roughness-uses-min-amplitude
statement: "In incon the default Sethares pair roughness uses the smaller of the two partial amplitudes, min(a1,a2)*(exp(-3.5*s*d) - exp(-5.75*s*d)) with s = 0.24/(0.021*f_lo + 19), rather than the product a1*a2; its Vassilakis variant uses s = 0.24/(0.0207*f_lo + 18.96)."
status: current
supersedes: []
tags: [subject:roughness-models, tech:r-incon, domain:music-perception, phase:implementation]
applies_to_version: "incon 0.5.0 (MIT)"
source: { url: "https://github.com/pmcharrison/incon/blob/master/R/model-dycon.R", doi: "", title: "incon R/model-dycon.R", locator: "sethares and vassilakis dissonance functions", accessed: "2026-10-04", tier: 1 }
confidence: verified
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:15Z
---
Found while verifying the formula recalled from memory (see the lesson on recalled literature facts). The constants 3.5 and 5.75 were re-confirmed in the S0 reading.
