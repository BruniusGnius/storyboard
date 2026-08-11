# Compact Examples

## Example 1 — One beat, multiple panels

Narrative need: show that an idea is tested rather than magically completed.

Possible coverage:
- `SB004`: medium-wide — team assembles V1 and checks a sensor value.
- `SB005`: detail — test result exposes a problem.
- `SB006`: medium — student marks the correction and rebuilds.

All may map to the same beat if the timing and importance justify it.

## Example 2 — One panel spans two beats

`SB009` begins while the voice closes a statement about independence and continues into the question of guidance. The same composition holds long enough for a mentor to enter the interaction. The cut occurs on the answer, not on the beat boundary.

## Example 3 — Provisional camera

```json
{
  "shot_scale": "medium",
  "focal_length_mm": 50,
  "aperture": "T2.8",
  "camera_height": "seated eye level",
  "camera_angle": "three-quarter profile",
  "movement_intent": "subtle lateral observation",
  "technical_status": "provisional_storyboard"
}
```

This is precise enough for a review image but Technical Shot Plan may later choose 45 mm/T4 if the image intent remains intact.

## Example 4 — Storyboard previz prompt

Panel semantics: recurring student adjusts V2 of a prototype after reviewing a failed test.

Prompt pattern:

`Recurring teenage student CHR01 in approved WRD01, focused three-quarter profile as she steadies PRP01-V2 with her left hand and repositions one sensor module with a small precision tool, annotated failed-test values visible beside the prototype, ENV01 bright contemporary workshop remains spatially identical to prior panels, medium close three-quarter composition, 50mm spherical-like perspective, T2.8, seated eye-level camera, moderate depth with hands and prototype equally readable, soft warm-neutral window ambience reinforced by clean overhead practicals, controlled highlight roll-off and natural skin tones from CANON_FRAGMENT, restrained observational energy, visible continuity of the same cable routing and component colors from V1, no futuristic HUD, no unexplained hardware, no wardrobe drift, no generic smiling-at-camera performance.`

## Example 5 — Human correction

Human:
"SB006: I like the action but it's too close. I need to see the teammate observing the test."

Revision behavior:
- keep `SB006`;
- `revision_no: 2`;
- widen from close-up to medium-wide;
- add approved teammate entity;
- preserve prototype V2 and environment;
- update camera preview;
- regenerate complete prompt;
- record change as an `SBDxxx` decision only if material to future continuity.

## Example 6 — Attribute-only approval

Human:
"The lighting is right but the classroom is wrong."

Record:
- image full status remains unapproved;
- `lighting: approved_reference`;
- `environment: rejected`;
- keep lighting reference ID available for future prompts;
- regenerate environment without losing approved lighting behavior.
