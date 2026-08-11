# Storyboard Charter

## Purpose

Turn approved narrative and visual development into a reviewable temporal visual plan for a video. The storyboard is a **decision surface**, not merely an illustration document.

## Authority hierarchy

1. Explicit human corrections and locked decisions.
2. Human-approved upstream Creative/Visual locks.
3. Verified brand/project requirements.
4. Narrative evidence and timing.
5. Human-selected AI proposals.
6. AI proposals and provisional storyboard choices.

Never let a lower level silently overwrite a higher level.

## Provenance

Track where meaningful storyboard decisions came from:
- `human_defined`;
- `human_selected`;
- `upstream_locked`;
- `brand_or_project_requirement`;
- `narrative_evidence`;
- `visual_canon`;
- `ai_proposed`.

## Status language

Project/storyboard status:
- `draft`;
- `human_in_review`;
- `human_revised`;
- `partially_locked`;
- `human_locked`.

Panel image status:
- `not_generated`;
- `generated_unreviewed`;
- `human_revised`;
- `approved_reference`;
- `rejected`.

Never equate image generation success with creative approval.

## Non-destructive iteration

When the human changes a panel:
- preserve the stable `SBxxx` identity when the narrative unit remains the same;
- increment `revision_no`;
- record changed fields;
- retain the previous prompt/image reference when possible;
- create a new panel ID only when the panel's narrative function becomes a genuinely new unit.

## Universal behavior

Do not assume industry, brand, production medium, genre, camera system, or image provider. Adapt to the supplied video while preserving the same workflow discipline.
