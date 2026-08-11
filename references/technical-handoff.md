# Technical Shot Plan Handoff

## Purpose

Technical Shot Plan should receive a storyboard whose **meaning, order, continuity, and visual identity are already resolved enough to engineer**, while knowing which camera/timing values remain provisional.

## Schema

Use `storyboard/handoff/v1`.

Include:
- storyboard approval status;
- upstream Narrative/Creative/Visual source refs;
- active human locks;
- Visual Canon and prompt inheritance fragments;
- ordered `SQxx`, `SCxx`, `SBxxx` architecture;
- timecode/duration allocation and timing confidence;
- panel narrative purpose and visible action;
- approved entities and continuity state per panel;
- panel shot scale/composition intent;
- provisional storyboard camera per panel;
- semi-canonical overrides with reasons;
- lighting adjustment intent;
- movement intent;
- transition/edit intent;
- prompt IDs and optional generated image refs;
- storyboard decision refs `SBDxxx`;
- unresolved technical questions;
- permissions for downstream refinement.

## Technical refinement permissions

Technical Shot Plan MAY refine:
- final focal length/T-stop within canon;
- camera body/lens model when not upstream locked;
- precise camera height/distance;
- rig/movement mechanics;
- focus behavior/marks;
- shutter/ISO/ND/exposure implementation;
- lighting fixtures/positions/ratios;
- frame-accurate duration;
- edit transition implementation;
- generation/video tool settings.

Technical Shot Plan MUST NOT silently change:
- narrative purpose;
- shot order when human locked;
- subject/action;
- approved entity identity;
- project/prop continuity state;
- environment identity/geography;
- Visual Canon;
- forbidden constraints;
- human-approved framing intent when the proposed technical change materially alters it.

## Image-prompt inheritance

Storyboard prompt is not final production prompt.

Carry forward:
- panel semantics;
- `CANON_FRAGMENT`;
- `ENTITY_FRAGMENT` refs;
- continuity state;
- negative constraints;
- representative instant/composition intent.

Technical Shot Plan replaces/refines provisional technical fields. Later Generative Production may then compose:

`FINAL_VISUAL_PROMPT = CANON + ENTITIES + STORYBOARD_CONTENT + APPROVED_TECHNICAL_SHOT_SPEC + CONTINUITY + NEGATIVES`

Do not copy a storyboard previz prompt blindly into final production if technical values changed.
