---
id: K-20261004T102017Z-billboard-chord-type-corpus-encoding
statement: "incon::popular_1_pc_chord_type holds counts for all 2048 bass-relative pitch-class chord types from the McGill Billboard corpus (total count 74,093), encoded as id = 1 + sum over non-bass pitch classes j of 2^(11-j)."
status: current
supersedes: []
tags: [subject:billboard-chord-corpus, tech:r-incon, tech:rdata, domain:music-perception, phase:implementation]
applies_to_version: "incon 0.5.0 (MIT)"
source: { url: "https://github.com/pmcharrison/incon/blob/master/data/popular_1_pc_chord_type.rda", doi: "", title: "incon data/popular_1_pc_chord_type.rda", locator: "decode_pc_chord_type in hrep R/coded-vec.R", accessed: "2026-10-04", tier: 1 }
confidence: verified
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:17Z
---
Corpus source: Burgoyne (2011), McGill Billboard. This project applies add-one smoothing before taking logs; incon's own handling of zero counts was not recorded.
