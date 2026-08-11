# Installation

This is a plug-and-play Skill. It has no mandatory third-party runtime dependencies.

## ChatGPT Skills

Install the packaged `skill.zip` through the Skills interface.

## Codex / agent workspace

Copy the `storyboard/` folder into the project or Skill location used by your agent. Keep `SKILL.md`, `references/`, and `scripts/` together.

## Claude Code / similar filesystem agents

Copy the complete folder and point the agent to `SKILL.md` / `CLAUDE.md`.

## Optional image generation

No image generator is required. If the host provides a native image tool, MCP, or other compatible generator, the Skill can use it for storyboard previsualization. Otherwise it produces `STORYBOARD_PROMPT_PACK.md` and `storyboard-prompts.json` for external execution.

## Optional local validation

Requires only Python 3 standard library:

```bash
python scripts/validate_storyboard.py storyboard.json storyboard-prompts.json
```

## Optional workspace scaffold

```bash
python scripts/scaffold_workspace.py ./storyboard
```
