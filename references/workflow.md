# Storyboard Workflow

## 1. Source audit

Create a source table and load active constraints. Confirm master duration/aspect only when present; otherwise mark provisional.

## 2. Coverage map

For each narrative unit, classify visual treatment as one of:
- `new_visual_unit`;
- `continuation`;
- `visual_bridge`;
- `graphic_support`;
- `implicit`;
- `audio_led`.

No category automatically means one shot.

## 3. Sequence architecture

Use `SQxx` for macro narrative phases. A sequence can inherit `VAxx` but does not have to match it one-to-one.

For each sequence define:
- beginning viewer state;
- end viewer state;
- visual change;
- dominant world/entities;
- energy behavior;
- continuity obligations;
- escalation or release logic.

## 4. Scene architecture

Use `SCxx` for a coherent location/time/action context. A scene may span several beats and several shots.

Scene boundaries should be motivated by:
- location/time shift;
- new action system;
- continuity reset;
- narrative turn;
- visual-world change.

## 5. Panel architecture

Use `SBxxx` for the selected storyboard shot/panel unit.

A good panel answers:
- Why this shot now?
- What changes during it?
- What must be readable?
- Why this scale/perspective instead of another?
- What state must carry into the next shot?

## 6. Prompt/image review loop

For every selected panel:
1. Compose `previz_prompt_en`.
2. Generate an image if a tool exists and review benefits.
3. Present or record the result as unapproved.
4. Capture human corrections.
5. Rewrite only affected panel fields/prompt fragments.
6. Increment revision.
7. Regenerate when useful.

## 7. Lock and handoff

Do not export a final-status handoff until:
- every narrative unit has coverage;
- continuity is coherent;
- image prompts exist for all selected panels;
- human approval state is truthful;
- downstream permissions/refinement boundaries are explicit.
