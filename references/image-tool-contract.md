# Optional Image Tool / MCP Contract

## Principle

Image generation enriches storyboard review but is not required for the Skill to function.

## Capability detection

If the host exposes a compatible native image generator, MCP, connector, or local image service:
- use it only through its documented interface;
- do not assume a provider by name;
- do not require API keys unless the user/environment already supplies the integration;
- preserve provider-neutral semantic prompts in the output regardless of provider.

## Generation workflow

For a selected panel:
1. Compose/validate `previz_prompt_en`.
2. Pass user-supplied approved images/entity sheets as references when the tool supports them.
3. Generate the smallest useful number of variants.
4. Record generation provenance when exposed: tool/provider, prompt revision, references, seed/settings, output identity.
5. Mark results `generated_unreviewed`.
6. Ask for/accept human correction before approval.

## No image tool

Do not stop. Export:
- `STORYBOARD_PROMPT_PACK.md`;
- `storyboard-prompts.json`;
- reference image IDs/paths when supplied;
- explicit notes about which references should be passed to a future generator.

## User-supplied generated image

If the user returns an image generated elsewhere:
- map it to `SBxxx` and prompt revision;
- analyze only what is visible/provided;
- record human feedback;
- do not assume the external generator respected hidden settings.

## Final-production boundary

Storyboard images are review assets. A technically approved production prompt may later inherit storyboard semantics, but must be rebuilt after Technical Shot Plan finalizes camera/exposure/motion/production values.
