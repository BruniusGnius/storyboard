# Storyboard Camera Preview Contract

## Why provisional camera exists here

Storyboard images need specific perspective and optical behavior to be useful. Generic prompts such as "cinematic medium shot" are too ambiguous for reliable review. However, the final production camera plan belongs downstream.

## Inheritance levels

### Canonical
Never change silently:
- capture/render medium;
- aspect/reframe rules;
- sensor/color response intention;
- lens-family character when locked;
- core distortion policy;
- texture/diffusion/grain policy;
- locked composition rules;
- world/entity identity.

### Semi-canonical
Use as default unless a panel has a narrative reason to vary:
- focal-length family;
- depth-of-field philosophy;
- camera energy;
- contrast family;
- preferred camera height;
- subject/background separation;
- diffusion/grain intensity.

### Provisional storyboard variables
Set concrete values when needed for deterministic panel generation:
- exact focal length;
- approximate T-stop/f-number;
- camera height;
- angle;
- distance;
- movement/rig intent;
- focus behavior;
- local lighting adjustment.

Store `technical_status: provisional_storyboard` unless a value is explicitly upstream locked.

## Camera preview object

Recommended fields:

```json
{
  "shot_scale": "medium-wide",
  "focal_length_mm": 35,
  "aperture": "T2.8",
  "camera_height": "student eye level",
  "camera_angle": "slight three-quarter",
  "camera_distance": "approx 2.4 m",
  "movement_intent": "slow observational push-in",
  "focus_behavior": "subject and project readable, moderate separation",
  "technical_status": "provisional_storyboard",
  "override_reason": null
}
```

Do not fabricate numeric values merely to appear technical. Use them when they materially constrain the generated frame or communicate intended perspective.

## Lens consistency

If Visual Development defines a preferred family such as 28–50 mm spherical-like optics, keep preview lenses inside it. An intentional 18 mm or 85 mm departure requires a reason such as spatial compression, isolation, or a deliberate perspective break.

## Camera movement in still panels

A still cannot prove motion. Encode movement as **intended shot behavior**, while the generated image should show a composition compatible with that movement. Avoid fake motion blur unless the look requires it.

## Downstream refinement

Technical Shot Plan may change exact lens/T-stop/rig values if it preserves:
- shot scale;
- perspective intent;
- subject relation;
- geography;
- narrative purpose;
- Visual Canon.

If a technical change materially changes the image, send it back as a storyboard revision.
