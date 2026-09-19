# consonance — reversible consonance model & consonance-targeted tone streams

Scores chords with the Harrison & Pearce (2020) composite model (Hutchinson-Knopoff roughness + pitch-class harmonicity
+ corpus familiarity) and *inverts* it by conditional sampling: given a target consonance c*, pick each new tone so the
sounding sonority stays near c*.

```python
import numpy as np
from consonance.timbre import harmonic_timbre
from consonance.composite import CompositeModel
from consonance.sampler import generate_stream

timbre = harmonic_timbre(11, 1.0)                    # use the SAME timbre for synthesis (render.render_stream checks this)
model = CompositeModel(timbre)
hz = lambda c: 220.0 * 2 ** (np.asarray(c, float) / 1200)
efs = lambda state: (lambda c: model.score_with_candidates(hz(list(state)), hz(c)))
r = generate_stream(efs, np.arange(-600., 1800., 5.), n_steps=24, target=1.6, sigma=0.1, rng_seed=7,
                    start=(0.0, 700.0), window=4, min_separation_cents=30, novelty_weight=1.5)
```
- `sigma` = how tightly the level set {C = c*} is enforced (score units). `window` = notes sounding together.
- Whole-chord sampling: `sampler.metropolis_chord`; dyads: exact lookup `sampler.dyad_level_set`.
- Resumable runs: pass `Checkpoint(path)`; interrupted runs resume bit-identically.
- Demo audio: `python examples/generate_demo.py` (already rendered in `examples/out/`).

Run tests: `sh scripts/verify_frozen.sh && python -m pytest` (42 tests; `tests/` is FROZEN, see tests/FROZEN.md).
Calibration: `python scripts/calibration_report.py docs` -> docs/CALIBRATION.md.

**Scale:** score = the published regression output (about -0.7 to 3.1; higher = more consonant). It is *model*-consonance
fitted to Western listeners' ratings of 12-TET chords, not a guarantee of perceived consonance for other tunings or
timbres (see IMPLEMENTATION_REPORT.md, docs/LISTENING_PROTOCOL.md). Attribution: NOTICE.
