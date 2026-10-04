# Retrospective: gen-20260919T204010Z-consonance-inverse

## Inputs used
`git log` (commits bfc418a, ab1b417, a445f41, 9c8e5e1), `IMPLEMENTATION_REPORT.md`, `PLAN.md`, `research/RESEARCH_LOG.md`, `.checkpoints/state.json`, `pytest --collect-only -q` per file, `ls`/`grep` checks of plan controls, and this conversation. Not available: `EXECUTION_LOG.md`, `BLOCKED.md`, `TEST_CHALLENGE.md`, `GATE-*.md`, CI history (none of these existed; A-003).

## Limitations of this retrospective
- Run by the implementing agent in its own context, not a fresh Opus context, and the digest was not built by a separate Haiku agent. Treat it as a first pass that deserves an independent read.
- The sandbox was reset before this step, and the earlier tool outputs are no longer visible. Corrections from the early phases were reconstructed from the repository, the reports and the conversation, which is why each such lesson says "recorded retroactively". Some corrections may be missing.
- The origin of `consonance/pitchgrid.py` cannot be reconstructed from these records.

## Q1. What went wrong and was corrected? Is each correction a lesson?
Yes. Corrections: wrong recalled facts (`L-20261004T102001Z-recalled-literature-facts-wrong`), the invalid first performance test (`L-20261004T102002Z-perf-test-budget-not-derived`), the window off-by-one (`L-20261004T102003Z-window-semantics-off-by-one`), the checkpoint backup logic (`L-20261004T102004Z-checkpoint-rotated-corrupt-file`), unattainable calibration targets (`L-20261004T102005Z-calibration-targets-before-attainable-range`), placeholder arithmetic (`L-20261004T102006Z-placeholder-arithmetic-left-in-code`), the sandbox reset (`L-20261004T102007Z-sandbox-reset-lost-working-tree`).

## Q2. What was overlooked?
- No test for `window` semantics or save-after-corruption (`L-20261004T102003Z-window-semantics-off-by-one`, `L-20261004T102004Z-checkpoint-rotated-corrupt-file`).
- Plan controls never delivered: CI hash check, domain-of-validity warning, S6 design note and diversity thresholds, sequential terms (`L-20261004T102010Z-plan-controls-not-traced-to-delivery`).
- A duplicate pitch module with its own tests (`L-20261004T102008Z-duplicate-pitch-modules-shipped`).
- Counts and freeze status stated wrongly (`L-20261004T102009Z-stale-test-counts-in-reports`).
- The harmonicity default used (11 harmonics, composite wrapper) differs from the one the research log records (12, standalone) and was never documented (`K-20261004T102016Z-milne-harmonicity-parameters-and-defaults`).
- An untested causal explanation (`L-20261004T102011Z-untested-causal-explanation-stated-as-fact`).
- Knowledge rediscovered during the run: how to reach GitHub from the sandbox and how to list incon files (`K-20261004T102023Z-github-access-from-sandbox`), reading `.rda` files (`K-20261004T102025Z-rdata-reads-rda-in-python`), sandbox persistence (`K-20261004T102024Z-sandbox-working-directory-resets`).

## Q3. Lessons loaded in R0 that were not applied or recurred
None: no store was readable and R0 was skipped (A-001, A-005).

## Q4. New facts about the Subject not yet knowledge items
All now recorded: `K-20261004T102012Z-hp2020-composite-model-structure`, `K-20261004T102013Z-incon-composite-coefficients`, `K-20261004T102014Z-hutchinson-knopoff-roughness-mashinter`, `K-20261004T102015Z-sethares-roughness-uses-min-amplitude`, `K-20261004T102016Z-milne-harmonicity-parameters-and-defaults`, `K-20261004T102017Z-billboard-chord-type-corpus-encoding`, `K-20261004T102018Z-cousineau-2012-amusia-consonance`, `K-20261004T102019Z-hp2018-energy-based-sequence-model`, `K-20261004T102020Z-harmonic-entropy-erlich`, `K-20261004T102021Z-milne-laney-sharp-2016-microtonal-harmonicity`, `K-20261004T102022Z-composite-score-attainable-range`, `K-20261004T102023Z-github-access-from-sandbox`, `K-20261004T102024Z-sandbox-working-directory-resets`, `K-20261004T102025Z-rdata-reads-rda-in-python`.

## Findings
| # | Finding | Linked to |
|---|---|---|
| F1 | Four recalled literature facts were wrong | `L-20261004T102001Z-recalled-literature-facts-wrong`, `K-20261004T102012Z-hp2020-composite-model-structure`, `K-20261004T102013Z-incon-composite-coefficients`, `K-20261004T102014Z-hutchinson-knopoff-roughness-mashinter`, `K-20261004T102015Z-sethares-roughness-uses-min-amplitude` |
| F2 | First performance test dictated an unattainable budget | `L-20261004T102002Z-perf-test-budget-not-derived` |
| F3 | `window` scored one extra note and no test covered it | `L-20261004T102003Z-window-semantics-off-by-one` |
| F4 | Checkpoint save could overwrite the only good backup | `L-20261004T102004Z-checkpoint-rotated-corrupt-file` |
| F5 | Calibration targets chosen before the attainable range | `L-20261004T102005Z-calibration-targets-before-attainable-range`, `K-20261004T102022Z-composite-score-attainable-range` |
| F6 | Placeholder arithmetic left in code | `L-20261004T102006Z-placeholder-arithmetic-left-in-code` |
| F7 | Working tree lost to a sandbox reset; export stale | `L-20261004T102007Z-sandbox-reset-lost-working-tree`, `K-20261004T102024Z-sandbox-working-directory-resets` |
| F8 | Duplicate pitch modules shipped | `L-20261004T102008Z-duplicate-pitch-modules-shipped` |
| F9 | Test counts and freeze status stale or wrong | `L-20261004T102009Z-stale-test-counts-in-reports` |
| F10 | Plan controls not traced to delivery | `L-20261004T102010Z-plan-controls-not-traced-to-delivery` |
| F11 | Causal explanation stated without a test | `L-20261004T102011Z-untested-causal-explanation-stated-as-fact` |
| F12 | Harmonic-count default undocumented | `K-20261004T102016Z-milne-harmonicity-parameters-and-defaults` |
| F13 | Knowledge had to be rediscovered | `K-20261004T102023Z-github-access-from-sandbox`, `K-20261004T102025Z-rdata-reads-rda-in-python`, `K-20261004T102017Z-billboard-chord-type-corpus-encoding` |

## Done check
Every finding links to an `L-` or `K-` file. Run `python scripts/check_knowledge_schema.py` from the repository root; the result of this run is in the hand-off message.
