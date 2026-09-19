"""Generate consonance-targeted tone streams and render them to WAV with the same timbre the model scores.
Usage: python examples/generate_demo.py [out_dir]"""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from consonance.composite import CompositeModel
from consonance.render import render_stream
from consonance.sampler import generate_stream
from consonance.timbre import harmonic_timbre

out = sys.argv[1] if len(sys.argv) > 1 else "examples/out"
os.makedirs(out, exist_ok=True)
REF = 220.0
hz = lambda c: REF * 2.0 ** (np.asarray(c, float) / 1200.0)
timbre = harmonic_timbre(11, 1.0)
model = CompositeModel(timbre)
efs = lambda state: (lambda c: model.score_with_candidates(hz(list(state)), hz(c)))
cands = np.arange(-600.0, 1800.0, 5.0)
summary = {}
for target in (0.8, 1.6, 2.0):
    r = generate_stream(efs, cands, 24, target, 0.1, rng_seed=7, start=(0.0, 700.0), window=4,
                        min_separation_cents=30.0, tolerance=0.25, novelty_weight=1.5)
    state, scores = [0.0, 700.0], []
    for n in r.notes:
        state = (state + [n])[-4:]
        scores.append(float(model.score(hz(state))))
    name = f"stream_target_{target:.1f}"
    render_stream(r.notes, timbre, os.path.join(out, name + ".wav"), model=model, ref_hz=REF, sustain_notes=4)
    summary[name] = {"target": target, "notes_cents_re_220Hz": r.notes, "realised_scores": scores,
                     "mean_realised": float(np.mean(scores))}
    print(name, "mean realised", round(float(np.mean(scores)), 3), flush=True)
json.dump(summary, open(os.path.join(out, "streams.json"), "w"), indent=1)
