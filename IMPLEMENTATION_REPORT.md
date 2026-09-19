# Implementation report — gen-20260919T204010Z-consonance-inverse
Result: all 42 frozen tests pass (0 skipped, 0 modified; `sha256sum -c tests/FROZEN.sha256` OK). Not pushed to GitHub (no access) — see hand-off files.

## Steps executed
| Step | Status | Notes |
|---|---|---|
| S0 verify constants | Done | Read incon/hrep (MIT) sources; all formulas/coefficients verified; real Billboard counts extracted. See research log. |
| S1 scaffold | Done | package `consonance`, pytest.ini, pyproject, NOTICE, `scripts/verify_frozen.sh` |
| S2 interference | Done | sethares (min-amp), hutchinson, vassilakis; vectorised batch |
| S3 harmonicity | Done | Milne/H&P KL harmonicity; scalar + vectorised-over-candidates |
| S4 familiarity | Done | real corpus table; 12-TET detection tolerance 20 cents; `drop`/`strict` |
| S5 composite | Done | published coefficients; `score_with_candidates`; timbre guard |
| S6/S7 sampler | Done | candidate softmax (log-sum-exp), Metropolis chords, dyad level sets, sliding-window streams, novelty prior |
| S8 checkpoint | Done | atomic `os.replace`, `.bak` fallback, schema versioning; bit-identical resume |
| S9 validation | Partly | calibration harness run (docs/CALIBRATION.md); listening test only *designed* (docs/LISTENING_PROTOCOL.md) |
| S10 docs/demo | Done | README, WAV demos (examples/out) |
| GATE | NOT done | requires Mythos/Fable review — not available here |

## Findings and deviations (honest list)
1. **Bug found by the S9 harness, fixed:** `window=w` originally scored the candidate against the last `w` notes (w+1 sounding) while calibration measured `w`. Fixed: candidate is scored with the last `w-1` notes. Frozen tests do not cover `window`, so no test change was needed (a regression test for it should be added in the *next* protocol run).
2. **Mode collapse (risk R7) confirmed** at high targets (target 2.4 for 4-note sonorities: ~3-4 distinct quarter-tone pitch classes in 30 notes). Novelty prior (`novelty_weight`) improves diversity up to target 2.0 (9 -> 13 distinct) but cannot fix targets near the attainable maximum, where few sonorities qualify (4-note random-search max ≈ 2.0). Use lower targets or smaller windows for variety.
3. **Achieved accuracy** (novelty 1.5, sigma 0.1, tol ±0.25, 3 seeds x 30 steps): 100/99/99/91/90/76% within tolerance for c* = 0.4/0.8/1.2/1.6/2.0/2.4; realised mean sits 0.02–0.2 *below* target at high c* (sampler bias toward the many lower-scoring candidates; reduce sigma to tighten).
4. **Not implemented:** gradient/Langevin refinement (design-only in the plan; interference/harmonicity are smooth, familiarity is not).
5. **Not validated:** agreement with R `incon` outputs (no R here; risk R8). My harmonicity uses continuous Gaussians on a 1-cent grid, whereas hrep rounds partial positions to bins, so tiny numeric differences are expected. Qualitative ordering is sane (octave 3.06 > fifth 2.47 > major triad 2.02 > minor 1.88 > sus4 1.83 > aug 1.27 > dim 1.06 > cluster -0.36).
6. `familiarity_mode='drop'` substitutes the corpus mean log-probability (-2.34), not zero, to keep scores on the same scale; microtonal scores are therefore approximate. Perceptual validity outside 12-TET/harmonic timbres is unmeasured (risk R1).
7. Chord size effect disabled by default (incon does the same); enable via `Weights(n_notes=0.422267698605598)`.
8. Performance: 1200-candidate step with 6 held notes ≈ 0.45 s (budget 2 s) — fine offline, too slow for an audio thread; precompute or run off-thread.
9. Pre-mortem was authored at Sonnet tier; the required higher-tier review has not happened.
