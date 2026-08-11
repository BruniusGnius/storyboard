# Storyboard Output Schema

## Standard files

### `STORYBOARD.md`
Human-readable storyboard containing:
- project/status summary;
- upstream locks and visual canon summary;
- sequence architecture;
- scene summaries;
- ordered `SBxxx` panel cards;
- timing and narrative refs;
- visual action/readability;
- continuity notes;
- provisional camera note;
- image/prompt status;
- Storyboard Lock/review state.

If generated panel images are available, embed/link them by stable panel ID. If not, do not invent paths.

### `storyboard.json`
Machine-readable source of truth for storyboard semantics.

Recommended top-level structure:

```json
{
  "schema": "storyboard/v1",
  "project": {},
  "storyboard_status": "draft",
  "approval": {},
  "sources": [],
  "upstream": {},
  "active_constraints": {},
  "visual_inheritance": {},
  "coverage_matrix": [],
  "sequences": [],
  "scenes": [],
  "panels": [],
  "decision_ledger": [],
  "open_questions": [],
  "quality_checks": {},
  "handoff": {}
}
```

### `STORYBOARD_PROMPT_PACK.md`
Human-reviewable image-prompt book ordered by `SBxxx`.

### `storyboard-prompts.json`
Machine-readable prompt pack.

Recommended:

```json
{
  "schema": "storyboard/prompts/v1",
  "purpose": "storyboard_previsualization",
  "production_ready": false,
  "canon_fragment": "...",
  "look_default_fragment": "...",
  "prompts": [
    {
      "panel_id": "SB001",
      "prompt_revision": 1,
      "prompt_en": "...",
      "negative_prompt_en": "...",
      "entity_refs": [],
      "continuity_refs": [],
      "camera_preview": {},
      "technical_status": "provisional_storyboard",
      "image_status": "not_generated",
      "image_refs": []
    }
  ]
}
```

### `handoff.json`
Compact contract for Technical Shot Plan.

## Sequence object

Recommended fields:
- `sequence_id`;
- `label`;
- `source_refs`;
- `tc_in`, `tc_out`;
- `viewer_start_state`, `viewer_end_state`;
- `visual_progression`;
- `energy_progression`;
- `dominant_entities`;
- `continuity_obligations`.

## Scene object

Recommended fields:
- `scene_id`;
- `sequence_id`;
- `label`;
- `environment_ref`;
- `time_state`;
- `source_refs`;
- `tc_in`, `tc_out`;
- `scene_action`;
- `geography_notes`;
- `continuity_entry`, `continuity_exit`.

## Panel object

Recommended fields:

```json
{
  "panel_id": "SB001",
  "revision_no": 1,
  "sequence_id": "SQ01",
  "scene_id": "SC01",
  "tc_in": "00:00:00.000",
  "tc_out": "00:00:03.600",
  "duration_s": 3.6,
  "source_refs": ["B01"],
  "narrative_purpose": "...",
  "visible_action": "...",
  "representative_instant": "...",
  "readability_target": "...",
  "voice_image_relationship": "evidentiary",
  "entity_refs": ["CHR01"],
  "environment_ref": "ENV01",
  "prop_state_refs": ["PRP01:V1"],
  "shot_scale": "medium-wide",
  "composition_intent": "...",
  "camera_preview": {},
  "lighting_adjustment": "...",
  "continuity_in": {},
  "continuity_out": {},
  "transition_intent": "...",
  "avoid": [],
  "prompt_id": "SB001-P1",
  "approval_status": "draft"
}
```

## Timecode format

Use `HH:MM:SS.mmm` when exact upstream timing exists. Preserve milliseconds. Do not fabricate exact milliseconds from untimed scripts; use relative timing or mark provisional.

## Referential integrity

- Every `SBxxx.sequence_id` must exist.
- Every `SBxxx.scene_id` must exist.
- Every prompt `panel_id` must match a selected panel.
- Every selected panel must have exactly one active prompt revision.
- Every referenced upstream ID must remain unchanged.
- Every approved entity ID must match upstream Visual Development when provided.
