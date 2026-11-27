# Atlas YouTube Intelligence

**Candidate portable skill pack — draft-only, model-independent.** Eleven skills and six upstream Python utilities for research, script development, packaging, editing decisions, SEO, planning, comments, chapters, shorts, retention and audit. No publishing or account access is included. Not yet deployed in AtlasBOT.

Source: [Jakeschincariol/chatgpt-youtube-agent-skill](https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill/tree/6314d3c17dfa1e596096654204e8a09e28cdfd74), MIT. See LICENSE, UPSTREAM-README.md and manifest.json for provenance. Original scripts, template and data remain unchanged; SKILL.md files adapt workspace paths, authorized inputs, draft-only gates and agent handoff. Keep sibling directories together: swipe.py uses yt-script/hooks.json; chapters.py and retention.py use yt-edit/deadair.py.

## Runtime

Python 3, UTF-8 inputs, a scoped workspace with read access to the pack and task files. No Python packages required for the six utilities. Transcripts, channel research and analytics exports are supplied by separately authorized tools. No credentials belong in this package. English hook/title heuristics and timing thresholds are not calibrated for Portuguese or French; label those scores advisory.

## AtlasBOT

See [adapter](adapters/atlasbot/README.md). Register skills only on intended existing agents. Research: yt-viral, yt-audit, yt-seo. Production: yt-script, yt-package, yt-edit, yt-shorts, yt-chapters. Editorial/community/analytics: yt-plan, yt-comment, yt-retention. AtlasClub/AtlasNews reuse; PSI may use read-only audit and research. No new bots or schedules are created by this pack.

## Codex and other runtimes

Use the runtime's supported skill loader or register each SKILL.md and preserve its scripts and sibling tree on the execution host. Supply a private per-channel voice.md using templates/voice.md. Never copy private profiles or analytics into Git. Do not use the upstream installation instructions unchanged: this pack uses workspace-scoped profiles.

## Verification

Run `python3 tests/smoke.py` from the pack root. Synthetic offline checks do not validate scoring quality or live model behavior. Before enabling, confirm the AtlasBOT loader and tool execution host, run tests and verify an agent can call the scripts and pass a draft to review. Runtime validation pending.
