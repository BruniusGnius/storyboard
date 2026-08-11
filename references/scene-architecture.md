# Scene and Panel Architecture

## Hierarchy

`SQxx` Sequence -> `SCxx` Scene -> `SBxxx` Storyboard panel/shot.

## Sequence

A sequence expresses a macro movement such as uncertainty -> proof, pursuit -> confrontation, setup -> reveal, or build -> payoff.

Do not create sequences merely because a source file has sections.

## Scene

A scene is a coherent visual event in place/time. Preserve geography and entity state across its panels unless the story intentionally changes them.

## Panel/shot

Each `SBxxx` represents one intended moving-image shot for storyboard purposes, even if its review asset is a still image.

Required conceptual fields:
- `panel_id`;
- `sequence_id`;
- `scene_id`;
- `tc_in`, `tc_out`, `duration_s` when timing exists;
- `source_refs`;
- `narrative_purpose`;
- `visible_action`;
- `readability_target`;
- `voice_image_relationship`;
- `entity_refs`;
- `environment_ref`;
- `prop_state_refs`;
- `shot_scale`;
- `composition_intent`;
- `camera_preview`;
- `lighting_adjustment`;
- `continuity_in`, `continuity_out`;
- `transition_intent`;
- `avoid`;
- `revision_no`;
- `approval_status`.

## Coverage variety

Avoid mechanical alternation such as wide-medium-close-up. Vary scale and perspective only when it changes audience access to information, emotion, evidence, or geography.

## Establishing geography

When spatial comprehension matters, establish enough geography before cutting into detail. When mystery/disorientation is intentional, document that intent.

## Repeated motifs

If an object, composition, gesture, or environment returns later, record the callback relationship. Repetition should show persistence, evolution, contrast, or payoff rather than accidental duplication.
