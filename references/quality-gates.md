# Storyboard Quality Gates

## Gate 1 — Narrative coverage

Pass when:
- every meaningful upstream beat/script unit is accounted for;
- no panel exists without a narrative/visual purpose;
- coverage does not mechanically mirror sentence boundaries;
- climax/turns have appropriate visual emphasis.

## Gate 2 — Temporal coherence

Pass when:
- panel order is coherent;
- timed panels do not accidentally overlap;
- gaps are deliberate/covered by holds, graphics, or audio-led visuals;
- duration density is plausible for readability;
- energy changes follow narrative needs.

## Gate 3 — Visual canon

Pass when:
- canon fragments are preserved;
- semi-canonical overrides have reasons;
- recurring entities use approved IDs;
- forbidden patterns are absent;
- format/reframe rules are respected.

## Gate 4 — Continuity

Pass when:
- characters, wardrobe, props/project versions, environments, technology, UI, screen direction, and time state evolve coherently;
- recurring evidence/motifs return intentionally;
- scene geography is understandable or deliberately withheld.

## Gate 5 — Storyboard image prompts

Pass when:
- every active `SBxxx` has one active `previz_prompt_en`;
- prompt IDs/revisions match panel revisions;
- prompts are visually concrete and in technical English;
- prompts inherit canon and entity state;
- provisional camera is marked provisional;
- prompts do not claim final production readiness.

## Gate 6 — Human authority

Pass when:
- `human_locked` is only used after explicit approval;
- human corrections are preserved and superseded decisions remain traceable;
- partial image approval is not misrepresented as full panel approval.

## Gate 7 — Downstream safety

Pass when:
- final technical implementation is not falsely locked here;
- Technical Shot Plan receives enough structure to refine without reinterpretation;
- open technical decisions are explicit.

## Failure conditions

Do not declare ready-for-handoff if:
- a locked upstream constraint is contradicted;
- prompt pack is missing selected panels;
- panel/entity refs are broken;
- continuity-critical prop/entity state is undefined;
- storyboard status claims approval not given by human;
- final technical specs are presented as approved when only provisional.
