# Human Storyboard Review

## Goal

Make the storyboard easy to direct, not merely easy to read.

## Review order

Prefer reviewing in this order:
1. sequence logic;
2. scene continuity;
3. high-impact/key panels;
4. generated images/prompts;
5. pacing and shot count;
6. detailed panel corrections.

Do not force the human to approve every routine field separately.

## Human correction vocabulary

Accept natural language such as:
- "SB004 is too close; I need to understand the room."
- "Keep this composition but use CHR02 instead."
- "The prototype looks finished too early; go back to V1."
- "I like the light, not the wardrobe."
- "Merge SB008 and SB009."
- "This should feel calmer; hold longer."
- "Use the image from revision 1 but the camera from revision 3."

Translate feedback into structured fields and provenance.

## Attribute-level image approval

A generated image can be approved only for specific attributes:
- composition;
- performance;
- lighting;
- environment;
- prop state;
- color;
- camera perspective;
- full panel.

Do not turn partial approval into full approval.

## Correction loop

For each correction:
- identify affected `SBxxx`;
- preserve upstream locks;
- update panel semantics first;
- regenerate prompt from semantics;
- increment revision;
- optionally regenerate image;
- record `SBDxxx` if the change is material;
- surface conflicts rather than hiding them.

## Human lock

Require explicit approval language before `human_locked`, such as:
- approved;
- lock it;
- this storyboard is final;
- these panels are approved.

Approval of one image does not lock the full storyboard.
