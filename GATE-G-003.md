# GATE G-003: lessons & knowledge push

Status: **signed off and pushed.** Response received: `push-to` two targets (below).

## Proposed target
`qualitycoding/agent-knowledge` on GitHub (A-001). It could not be read without credentials, so it may not exist yet. If it does not, S-KNOW creates it with the Appendix C layout and `TAXONOMY.md`.

## Allowed responses
- `push-to-proposed`
- `push-to: <target>`
- `do-not-push`

Pushing needs a token with write access to the chosen repository. The token pasted earlier in this run was for `Stream-of-consonance` only and should be revoked, so a new one is needed.

## Lessons (11)
| ID | Title | Severity | Tags |
|---|---|---|---|
| `L-20261004T102001Z-recalled-literature-facts-wrong` | Literature facts recalled from memory were wrong four times; retrieve them before stating or coding | Medium | applies:all, domain:music-perception, phase:research, kind:wrong-assumption |
| `L-20261004T102002Z-perf-test-budget-not-derived` | First performance test dictated an unattainable budget instead of deriving it from the requirement | Medium | tech:pytest, phase:specification, kind:verification-gap |
| `L-20261004T102003Z-window-semantics-off-by-one` | Sliding-window sampler scored one more note than it claimed; no test covered the parameter | High | domain:audio, tech:python, phase:verification, kind:verification-gap |
| `L-20261004T102004Z-checkpoint-rotated-corrupt-file` | First checkpoint save would have rotated a corrupt file over the only good backup | Medium | tech:python, phase:implementation, kind:integrity |
| `L-20261004T102005Z-calibration-targets-before-attainable-range` | Calibration targets were chosen before measuring the attainable score range | Low | domain:music-perception, tech:python, phase:verification, kind:wrong-assumption |
| `L-20261004T102006Z-placeholder-arithmetic-left-in-code` | Placeholder arithmetic was written into a function and replaced only on review | Low | tech:python, phase:implementation, kind:process |
| `L-20261004T102007Z-sandbox-reset-lost-working-tree` | Assumed the working tree persisted across turns; the sandbox had been reset | Medium | applies:all, tech:git, tech:github, phase:implementation, kind:environment |
| `L-20261004T102008Z-duplicate-pitch-modules-shipped` | Two overlapping pitch-mode modules and test files were shipped; one is dead code | Medium | tech:python, phase:implementation, kind:scope |
| `L-20261004T102009Z-stale-test-counts-in-reports` | Reported test counts and freeze status were wrong or stale in the report, README, state file and a reply | Medium | tech:pytest, phase:verification, kind:verification-gap |
| `L-20261004T102010Z-plan-controls-not-traced-to-delivery` | Several plan and pre-mortem controls were never delivered and were not listed as deviations | Medium | applies:all, phase:verification, kind:scope |
| `L-20261004T102011Z-untested-causal-explanation-stated-as-fact` | A causal explanation for the pitch-mode results was stated as fact without a test | Low | domain:music-perception, phase:verification, kind:verification-gap |

## Knowledge items (14)
| ID | Statement (truncated) | Tags |
|---|---|---|
| `K-20261004T102012Z-hp2020-composite-model-structure` | Harrison & Pearce (2020, Psychological Review 127(2):216-244) model simultaneous consonance as a linear regression on fo... | subject:composite-consonance-model, domain:music-perception, tech:r-incon, phase:research |
| `K-20261004T102013Z-incon-composite-coefficients` | incon 0.5.0 har_19_composite_coef: intercept 0.628434666589357; chord_size 0.422267698605598; hutch_78_roughness -1.6200... | subject:composite-consonance-model, tech:r-incon, domain:music-perception, phase:implementation |
| `K-20261004T102014Z-hutchinson-knopoff-roughness-mashinter` | incon's Hutchinson-Knopoff roughness uses Mashinter's parametrisation: critical bandwidth CBW = 1.72*mean_f^0.65, y = |f... | subject:roughness-models, tech:r-incon, domain:music-perception, phase:implementation |
| `K-20261004T102015Z-sethares-roughness-uses-min-amplitude` | In incon the default Sethares pair roughness uses the smaller of the two partial amplitudes, min(a1,a2)*(exp(-3.5*s*d) -... | subject:roughness-models, tech:r-incon, domain:music-perception, phase:implementation |
| `K-20261004T102016Z-milne-harmonicity-parameters-and-defaults` | Pitch-class harmonicity in incon/hrep (Milne 2013 spectrum, Harrison & Pearce 2018 KL variant) uses Gaussian smoothing s... | subject:pitch-class-harmonicity, tech:r-incon, domain:music-perception, phase:implementation |
| `K-20261004T102017Z-billboard-chord-type-corpus-encoding` | incon::popular_1_pc_chord_type holds counts for all 2048 bass-relative pitch-class chord types from the McGill Billboard... | subject:billboard-chord-corpus, tech:r-incon, tech:rdata, domain:music-perception, phase:implementation |
| `K-20261004T102018Z-cousineau-2012-amusia-consonance` | Cousineau, McDermott & Peretz (2012, PNAS 109(48):19858-19863): listeners with congenital amusia show normal sensitivity... | subject:consonance-perception, domain:music-perception, phase:research |
| `K-20261004T102019Z-hp2018-energy-based-sequence-model` | Harrison & Pearce (2018, ISMIR) present an energy-based (exponential-family) generative model of chord sequences from co... | subject:composite-consonance-model, subject:consonance-perception, domain:music-perception, phase:research |
| `K-20261004T102020Z-harmonic-entropy-erlich` | Harmonic entropy (Erlich) is a continuous dyad measure: the Shannon entropy of a probability distribution over nearby ra... | subject:harmonic-entropy, domain:music-perception, phase:research |
| `K-20261004T102021Z-milne-laney-sharp-2016-microtonal-harmonicity` | Milne, Laney & Sharp (2016, Musicae Scientiae) tested the spectral pitch-class harmonicity model with microtonal melodie... | subject:pitch-class-harmonicity, domain:music-perception, phase:research |
| `K-20261004T102022Z-composite-score-attainable-range` | With a harmonic 11-partial 1/h timbre and default weights, 1500 random chords per size gave composite scores (median, p9... | subject:composite-consonance-model, domain:music-perception, tech:python, tech:numpy, phase:verification |
| `K-20261004T102023Z-github-access-from-sandbox` | In this Claude sandbox, unauthenticated api.github.com returned HTTP 403, but github.com pages, raw.githubusercontent.co... | subject:github-access-from-sandbox, tech:git, tech:github, phase:implementation |
| `K-20261004T102024Z-sandbox-working-directory-resets` | Files under /home/claude can disappear between turns (observed 2026-10-04: the repository directory was gone), while /mn... | subject:sandbox-environment, tech:git, phase:implementation |
| `K-20261004T102025Z-rdata-reads-rda-in-python` | The Python package rdata 1.1.0 reads R .rda files: rdata.read_rda(path)['popular_1_pc_chord_type'] returned a pandas Dat... | subject:r-data-in-python, tech:python, tech:rdata, phase:implementation |

## Fallback already prepared
A bundle of the working branch and a self-contained staging archive of `TAXONOMY.md`, `lessons/` and `knowledge/` were written to the outputs folder.

## Response and result
- **Response:** `push-to: lessons -> https://github.com/qualitycoding/Lessons ; knowledge -> https://github.com/qualitycoding/knowledge`. The proposed single store `qualitycoding/agent-knowledge` was not used.
- **Pushed:** `Lessons` main `e937197` (11 lessons, `TAXONOMY.md`, generated `lessons/INDEX.md`); `knowledge` main `16e9227` (14 items, `TAXONOMY.md`, generated `knowledge/INDEX.md`). Both repositories were private and empty beforehand; no force-push.
- **Done check:** fresh clones of both repositories pass `scripts/check_knowledge_schema.py`; each remote index lists every pushed ID (11 and 14); entry files are byte-identical to the working branch; no token appears in either repository or its history.
- The token used was supplied for this push only, was sent through a temporary header, and is not stored in any remote URL or config. It should be revoked.
