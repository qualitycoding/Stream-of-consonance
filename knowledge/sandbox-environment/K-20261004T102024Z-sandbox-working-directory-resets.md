---
id: K-20261004T102024Z-sandbox-working-directory-resets
statement: "Files under /home/claude can disappear between turns (observed 2026-10-04: the repository directory was gone), while /mnt/user-data/outputs persisted, so a run needs a remote or a freshly exported bundle to survive."
status: current
supersedes: []
tags: [subject:sandbox-environment, tech:git, phase:implementation]
applies_to_version: "sandbox observed 2026-10-04"
source: { url: "", doi: "", title: "Observed in this run", locator: "first command of the turn on 2026-10-04", accessed: "2026-10-04", tier: 3 }
confidence: single-source
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:24Z
---
Observed once; how long the filesystem persists is unknown. Related lesson: the working tree was assumed to persist.
