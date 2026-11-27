# AtlasBOT adapter

1. Export the current team with the deployed CLI and back up the export privately. Confirm CLI version and actual execution host. Stage the entire pack on that host in a read-only directory accessible to selected bots. Do not assume SKILL.md registration copies supporting files.
2. Add only selected skill entries to an existing bot's team YAML, using paths relative to the team YAML. Example fragment (not a standalone team configuration):

```yaml
skills:
  - file: packages/atlas-youtube-intelligence/skills/yt-viral/SKILL.md
    enabled: true
  - file: packages/atlas-youtube-intelligence/skills/yt-audit/SKILL.md
    enabled: true
```

3. Provide each bot the actual absolute package location and authorized workspace voice profile location in its standing instructions. Run Python from the skill folder or use absolute script paths. Keep sibling folders available. Do not grant shell access beyond existing execution policy. Inputs are scoped, size-limited, untrusted files. No sending tools required.
4. Run `openmausbot team apply <existing-team-file> --dry-run`, inspect changes; only apply after reviewing the diff and verifying the target workspace. Do not replace teams, change models or activate publishing. Verify `team apply --check` after apply and run a synthetic draft task. Rollback using the reviewed backup of the team configuration, disabling newly added skills explicitly if required (omitted skills are not deleted).

Source CLI contract: https://github.com/AtlasHub-Si/Atlas-Bot/blob/main/docs/headless-cli.md . Integration guide, not automated installer. Runtime compatibility must be confirmed on the deployed version.
