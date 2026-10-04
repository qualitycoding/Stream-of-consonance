# Deviations

- **D-001 Adopted the lessons & knowledge addendum** (mid-run, implementing agent). Appended `S-RETRO` and `S-KNOW` to `PLAN.md`, defined `G-003` in `plan/GATES.md`, recorded A-001 to A-005. No frozen test was touched (`tests/FROZEN.sha256` still verifies); no security, data-integrity, public-interface or evidence-class change.
- **D-002 Protocol variant.** The run did not use v3.1; artefact names were mapped as in A-003. `plan/PLAN.md` was not created; `PLAN.md` at the root remains the plan.
- **D-003 Lesson directory names.** `lessons/<facet>-<value>/` (for example `lessons/domain-music-perception/`) instead of `lessons/<facet>:<value>/`, because a colon is not a valid character in Windows paths. Knowledge items are filed under the bare subject value.
- **D-004 R0 skipped** (research complete; implementing-agent rule). No lessons were loaded.
- **D-005 Earlier deviations** are listed in `IMPLEMENTATION_REPORT.md` (findings 1-10).

## Open items from the retrospective (nothing below has been changed)
1. Consolidate `consonance/pitchset.py` and `consonance/pitchgrid.py` and their test files (L-20261004T102008Z-duplicate-pitch-modules-shipped).
2. Correct the test counts and the "tests/ is FROZEN" wording in `README.md` and `IMPLEMENTATION_REPORT.md` item 9 (L-20261004T102009Z-stale-test-counts-in-reports).
3. Plan controls not delivered (L-20261004T102010Z-plan-controls-not-traced-to-delivery): a CI workflow that runs `sh scripts/verify_frozen.sh` before pytest (S1, risk R12); a domain-of-validity warning for non-12-TET tunings and non-calibrated timbres (risk R1); the S6 design note with numeric diversity thresholds (risk R7); sequential terms (voice-leading and spectral distance).
4. Regression tests, which need a new freeze: `window` semantics (L-20261004T102003Z-window-semantics-off-by-one) and save-after-corruption for the checkpoint (L-20261004T102004Z-checkpoint-rotated-corrupt-file).
5. Refresh the exported bundle and tarball after each push (L-20261004T102007Z-sandbox-reset-lost-working-tree).
6. Still open from the implementation report: Langevin refinement, comparison with R `incon`, the listening test, and the Mythos/Fable review gate.
