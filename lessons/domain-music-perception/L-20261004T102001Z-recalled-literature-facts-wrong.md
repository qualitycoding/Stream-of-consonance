---
id: L-20261004T102001Z-recalled-literature-facts-wrong
title: "Literature facts recalled from memory were wrong four times; retrieve them before stating or coding"
status: active
supersedes: []
recurrence_of: null
occurrences: 4
severity: Medium
tags: [applies:all, domain:music-perception, phase:research, kind:wrong-assumption]
recorded_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:01Z
---
## Trigger
About to state a citation year or venue, a formula constant, or a default parameter for a paper or software package from recollection (here: consonance literature, the R package incon).
## What went wrong
Four recalled facts were wrong. (1) Harrison & Pearce's composite model was cited as 2018; it is Psychological Review 2020 (the 2018 paper is a separate ISMIR model). (2) Stolzenburg's periodicity work was placed 'around 2012'; it is 2015. (3) Sethares pair roughness was stated with the product a1*a2; incon's default uses min(a1,a2). (4) Hutchinson-Knopoff roughness was attributed to the Bigand/Parncutt/Lerdahl approximation; incon uses Mashinter's parametrisation (CBW 1.72*f^0.65, cut-off 1.2). The wrong year was also written into a memory file before it was corrected.
## Correction
Searched and fetched the primary sources (PMC article, arXiv, incon and hrep sources), corrected the year, and recorded S0 results in research/RESEARCH_LOG.md with VERIFIED/UNVERIFIED tags before any code depended on them.
## Prevention rule
Before a citation year, venue, formula constant or default value appears in an answer, test or code, retrieve it from the primary source in the same turn and record its locator; otherwise label it UNVERIFIED in the text.
## Detection check
Run: grep -nE '^R[0-9]+' research/RESEARCH_LOG.md | grep -vE 'VERIFIED' ; empty output means every source entry is tagged. Then check that each constant in consonance/*.py has a K- item or a source comment.
## Evidence
Conversation turn 2 (answer corrected Harrison & Pearce 2018 to 2020); research/RESEARCH_LOG.md entries R7-R9 and the 'S0 verification' section; consonance/interference.py in commit ab1b417. Recorded retroactively when the addendum was adopted mid-run.
