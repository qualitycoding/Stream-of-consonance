---
id: K-20261004T102023Z-github-access-from-sandbox
statement: "In this Claude sandbox, unauthenticated api.github.com returned HTTP 403, but github.com pages, raw.githubusercontent.com and anonymous git clone or ls-remote of public repositories worked; a personal access token pushes through git -c http.extraHeader with a Basic x-access-token header, which leaves nothing in .git/config; raw file names guessed from memory returned 404, so list a directory by scraping github.com/<owner>/<repo>/tree/<branch>/<dir>."
status: current
supersedes: []
tags: [subject:github-access-from-sandbox, tech:git, tech:github, phase:implementation]
applies_to_version: "sandbox observed 2026-09-19 to 2026-10-04"
source: { url: "", doi: "", title: "Observed in this run", locator: "tool outputs 2026-09-19, 2026-09-20 and 2026-10-04", accessed: "2026-10-04", tier: 3 }
confidence: verified
derived_from: []
discovered_by: implementer
run: gen-20260919T204010Z-consonance-inverse
recorded_at: 2026-10-04T10:20:23Z
---
Tokens must never be written to files or lessons; use a placeholder such as github_pat_***.
