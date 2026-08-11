# Storyboard

Universal plug-and-play audiovisual Storyboard Skill.

It converts narrative timing + approved creative direction + visual development into an ordered, editable video storyboard with stable panel IDs, continuity state, provisional camera choices, and a high-fidelity English image prompt for every selected panel.

## Core outputs

- `STORYBOARD.md`
- `storyboard.json`
- `STORYBOARD_PROMPT_PACK.md`
- `storyboard-prompts.json`
- `handoff.json`
- optional generated images in `panels/`

## Pipeline position

`Locution Narrative Map -> Creative Direction Map -> Visual Development -> Storyboard -> Technical Shot Plan -> Generative Production -> Edit/Assembly`

The Skill can also run standalone from a script/brief. Image-generation tools/MCPs are optional; without them it exports complete prompt packs.
