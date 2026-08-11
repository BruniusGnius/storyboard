---
name: storyboard
description: Universal plug-and-play audiovisual storyboard workflow for converting a narrative map, script, approved creative direction, and visual-development handoff into a time-aligned sequence of storyboard scenes and panels for a video. Use to map beats into visual coverage, preserve visual canon and entity continuity, design scene/shot progression, create high-fidelity English image prompts for every storyboard panel, optionally generate or review storyboard images through available native/MCP image tools, record human corrections, and export a structured handoff to Technical Shot Plan. Works with or without the upstream Skills and never requires image-generation connectivity.
---

# Storyboard

Translate an approved audiovisual narrative and visual world into a temporal plan of **what the audience sees, in what order, and why**. Create a storyboard that is useful for human review and downstream technical planning without silently changing upstream locks or pretending provisional camera choices are final production specifications.

## Operating constitution

1. Keep the target a finished video. Every panel must serve narrative comprehension, emotion, evidence, rhythm, continuity, or transition through time.
2. Keep the human as creative authority. Produce a strong first pass, invite concrete corrections, preserve revisions, and never claim `human_locked` without explicit approval.
3. Preserve upstream truth. Treat `Bxx`, `Pxx`, `VAxx`, `CDxxx`, `VDxxx`, timecodes, entity IDs, source IDs, forbidden patterns, and locked decisions as immutable references unless the human explicitly supersedes them.
4. Preserve Visual Canon. Never reinvent approved characters, environments, props, technology, UI, palette, capture identity, or continuity rules shot by shot.
5. Separate **storyboard visualization** from **final technical execution**. Storyboard may assign exact provisional focal length, aperture, angle, camera height, movement intent, and lighting adjustment when needed to visualize/generate a panel, but mark them `provisional_storyboard`. Technical Shot Plan may refine them while preserving the panel's narrative and visual intent.
6. Generate reviewable image prompts for the storyboard. Every selected `SBxxx` panel must have a high-fidelity English `previz_prompt_en`, even when no image tool is connected.
7. Never make image generation a hard dependency. If a native or MCP image generator exists, use it when useful for review; otherwise export prompt packs that another generator can execute.
8. Do not expose private chain-of-thought. Use explicit decision criteria, alternatives, trade-offs, continuity checks, and concise rationales instead.
9. Avoid literal illustration. Do not create one shot per sentence, one shot per noun, or visually repeat the voiceover word-for-word unless that is intentionally chosen.
10. Keep the storyboard editable. Drafts are hypotheses. Human corrections can replace, split, merge, reorder, or reframe panels without destroying provenance.

## Load references progressively

Read only what the current step requires:

- `references/storyboard-charter.md` — authority, scope, provenance, status model, and non-destructive rules.
- `references/input-contract.md` — supported upstream combinations and normalization rules.
- `references/workflow.md` — complete adaptive workflow and checkpoints.
- `references/role-system.md` — multi-role lenses and synthesis discipline.
- `references/scene-architecture.md` — sequence/scene/panel hierarchy and visual progression.
- `references/beat-to-shot.md` — mapping narrative beats to coverage without literalism.
- `references/continuity-state.md` — entity, environment, prop, wardrobe, screen-direction, and temporal continuity.
- `references/camera-preview.md` — canonical, semi-canonical, and provisional storyboard camera behavior.
- `references/storyboard-image-prompts.md` — high-fidelity panel prompt metaprompts and correction workflow.
- `references/image-tool-contract.md` — optional native/MCP image generation and fallback behavior.
- `references/human-review.md` — human correction loops and visual review protocol.
- `references/storyboard-lock.md` — `SBDxxx` decision ledger, revision history, and approval semantics.
- `references/output-schema.md` — required Markdown/JSON files and fields.
- `references/technical-handoff.md` — exact contract for Technical Shot Plan and later Generative Production.
- `references/quality-gates.md` — validation and failure conditions.
- `references/examples.md` — compact examples of panels, prompt inheritance, and corrections.

## Input decision tree

Use the richest available combination; do not require a fixed stack.

**Preferred full pipeline**
- Locution/Narrative handoff or narrative map.
- Creative Direction handoff.
- Visual Development handoff with Visual Canon, approved entities, concept frames, prompt fragments, and continuity rules.

**Partial pipeline**
- Script + Creative Direction.
- Narrative Map + user references.
- Visual Development + script/voiceover.

**Standalone**
- Script, treatment, voiceover, brief, or sufficiently clear description of a video.
- Extract only the minimum provisional narrative and visual assumptions required to storyboard. Mark missing upstream decisions as provisional; do not recreate entire prior Skills unless the user asks.

## Core workflow

### 1. Audit and normalize

- Inventory all sources and active locks.
- Preserve all upstream IDs and timecodes.
- Identify the master duration and format/reframe rules.
- Load approved Visual Canon fragments and entity IDs when available.
- Separate `locked`, `preferred`, `flexible`, `open`, and `superseded` decisions.
- Identify unresolved choices that materially block storyboard architecture. Prefer a strong reversible first pass over unnecessary questioning.

### 2. Build a narrative coverage matrix

For every upstream beat or meaningful script unit, record:
- what the audience must understand/feel;
- visual role;
- continuity requirement;
- whether it needs a new shot, can continue an existing shot, can be handled by graphics, can be implicit, or can remain audio-led.

Do not equate beat boundaries with cuts. A single panel can bridge beats; a beat can require multiple panels.

### 3. Design sequence and scene architecture

Use stable IDs:
- `SQxx` — sequence or macro-phase;
- `SCxx` — scene/location-time unit;
- `SBxxx` — selected storyboard panel/shot unit.

Group panels by narrative movement, world/location, continuity, and rhythm. Preserve the upstream visual arc rather than generating a disconnected montage.

### 4. Draft visual coverage

For each `SBxxx`, define at minimum:
- time window;
- source beat/script refs;
- narrative purpose;
- visible action and micro-narrative;
- entities/environment/prop state;
- relationship to voiceover/dialogue;
- shot scale and composition intent;
- camera perspective and provisional visualization spec;
- lighting/look adjustment relative to canon;
- continuity in/out;
- transition intent;
- what must be readable in the frame;
- what to avoid.

Use alternative panel variants only where a human decision benefits from comparison. Do not multiply options for routine coverage.

### 5. Apply rhythm and edit logic

- Let cut density follow narrative energy, comprehension, evidence, and emotional turns.
- Use holds when the audience needs to inspect evidence or behavior.
- Use visual bridges when continuity matters more than a literal beat boundary.
- Treat acoustic pauses as evidence, not automatic cut commands.
- Record transition **intent**; leave final edit mechanics to later layers unless visually necessary to understand the storyboard.

### 6. Build continuity state

Use `references/continuity-state.md`.

Track current state for recurring entities and worlds, including:
- character identity, wardrobe, side of frame, action state;
- environment/location/time state;
- project/prop/version state;
- technology/UI state;
- lighting/time-of-day state;
- screen direction and spatial relation;
- previous-panel dependency and next-panel obligation.

### 7. Assign provisional storyboard camera

Use inherited `CANON_FRAGMENT`, `LOOK_DEFAULT_FRAGMENT`, and `SHOT_VARIABLE_SCHEMA` when available.

For image generation and human review, specify enough camera detail to make the panel visually deterministic. Mark exact shot values as `provisional_storyboard` unless they are already human-locked upstream.

A provisional focal length must remain inside the approved lens-family behavior unless a deliberate override includes a reason.

### 8. Create storyboard image prompt pack

Read `references/storyboard-image-prompts.md`.

Every selected panel must export:
- `previz_prompt_en` — one dense technical English block for a still storyboard/previsualization image;
- structured prompt fragments and IDs;
- negative/avoid constraints;
- provisional camera metadata;
- continuity state;
- prompt revision number;
- image status (`not_generated`, `generated_unreviewed`, `human_revised`, `approved_reference`, `rejected`).

These are **storyboard review prompts**, not final production-generation prompts.

### 9. Optional image generation

If a compatible native or MCP image generator is available:
1. Read `references/image-tool-contract.md`.
2. Generate storyboard images from `previz_prompt_en` when they materially help human review.
3. Preserve canon/entity fragments and revision IDs.
4. Never auto-approve generated images.
5. Record provider/tool/output identity/settings when exposed.

If no generator is available, continue normally and export the complete prompt pack.

### 10. Human storyboard review

Use `references/human-review.md`.

The human may:
- approve a panel;
- change subject/action;
- widen/tighten framing;
- change perspective;
- replace a character/environment/prop state;
- alter pacing or shot order;
- split/merge panels;
- reject a generated image but keep the panel idea;
- approve only an attribute of an image;
- propose a completely new visual idea.

Apply requested changes surgically. Do not drift unrelated canon.

### 11. Storyboard lock

Only after explicit human approval, classify the storyboard as `human_locked`.

Before lock, valid statuses include:
- `draft`;
- `human_in_review`;
- `human_revised`;
- `partially_locked`.

Preserve decisions and corrections with `SBDxxx` entries.

### 12. Export downstream handoff

Default filesystem output:

```text
storyboard/
├── STORYBOARD.md
├── storyboard.json
├── STORYBOARD_PROMPT_PACK.md
├── storyboard-prompts.json
├── handoff.json
├── panels/                # optional generated storyboard images
└── revisions/             # optional review artifacts
```

Read `references/technical-handoff.md` before export.

## Storyboard panel image rule

A storyboard panel prompt must be visually specific enough to generate a useful review image while remaining semantically subordinate to upstream canon.

Compose:

`STORYBOARD_PREVIZ_PROMPT = CANON_FRAGMENT + ENTITY_FRAGMENTS + SCENE_STATE + PANEL_ACTION + PANEL_COMPOSITION + PROVISIONAL_CAMERA + SHOT_LIGHTING_ADJUSTMENT + CONTINUITY_STATE + NEGATIVE_CONSTRAINTS`

Do not silently modify `CANON_FRAGMENT` or entity invariants.

## Scope boundary

**Resolve here**
- what is seen;
- shot/panel order;
- narrative coverage;
- scene grouping;
- action and performance intent;
- shot scale/framing intention;
- spatial continuity;
- screen direction;
- provisional storyboard camera needed for deterministic visualization;
- visual transition intent;
- storyboard image prompts and review images;
- initial duration/timecode allocation aligned to upstream audio.

**Defer to Technical Shot Plan**
- final camera body / sensor package choice when not canonical;
- final focal length/T-stop confirmation;
- exact rig and movement mechanics;
- focus-pull marks;
- shutter/ISO/ND/exposure implementation;
- lighting fixture/placement plan;
- final shot duration and frame-accurate edit timing;
- production feasibility details;
- final image/video generation prompt assembly with technical plan values.

The later technical layer may refine provisional values but must not change storyboard meaning, canon, entities, or approved continuity without a recorded human-approved revision.

## Validation

If local files exist, run:

```bash
python scripts/validate_storyboard.py storyboard.json storyboard-prompts.json
```

Fix errors before handoff. Warnings may remain only for intentionally open or unapproved human decisions.
