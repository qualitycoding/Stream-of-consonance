---
id: K-20261004T102016Z-milne-harmonicity-parameters-and-defaults
statement: "Pitch-class harmonicity in incon/hrep (Milne 2013 spectrum, Harrison & Pearce 2018 KL variant) uses Gaussian smoothing sigma 6.83 cents on a 1200-bin circle, partial weights 1/h^rho with rho 0.75, a harmonic template swept by cosine similarity, and the KL divergence in bits of the normalised profile from uniform; the standalone default is 12 harmonics, while the composite wrapper passes num_harmonics (top-level default 11) and rho = roll_off*0.75 (roll_off default 1)."
status: current
supersedes: []
tags: [subject:pitch-class-harmonicity, tech:r-incon, domain:music-perception, phase:implementation]
applies_to_version: "incon 0.5.0 (MIT); hrep (version not recorded)"
source: { url: "https://github.com/pmcharrison/incon/blob/master/R/model-har18.R", doi: "", title: "incon R/model-har18.R, R/models.R; hrep R/milne-pc-spectrum.R", locator: "num_harmonics, rho, sigma defaults; har_18_harmonicity wrapper in models.R", accessed: "2026-10-04", tier: 1 }
confidence: verified
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:16Z
---
This project's Python harmonicity takes its partials from the Timbre (11 harmonics, amplitude 1/h, exponent 0.75), which matches the composite wrapper, not the 12-harmonic standalone default. It uses continuous Gaussians on a 1-cent grid rather than hrep's bin rounding. research/RESEARCH_LOG.md records only the 12-harmonic default; agreement with the R output has not been tested.
