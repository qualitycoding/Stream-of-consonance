# Gates

`G-001` and `G-002` are not defined in this run (they belong to protocol v3.1, which was not the protocol used; see A-003).

## G-003 Lessons & knowledge push (all agents)
- **When:** the last step of implementation, after `S-RETRO`.
- **Request:** the implementer writes `GATE-G-003.md` listing the lessons and knowledge items to push (IDs, titles, tags) and asks for the target, proposing the knowledge store recorded at intake (A-001).
- **Allowed responses:** `push-to-proposed`, `push-to: <target>`, `do-not-push`.
- **Action:** push only after sign-off (S-KNOW, 3.7.2). The push holds back nothing else; implementation is complete once `S-RETRO` is done.
- **Fallback:** if the push fails, the target is unreachable or no response arrives, a git bundle with the lessons and knowledge commits is written and its path reported.
