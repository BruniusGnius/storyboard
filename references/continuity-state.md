# Continuity State System

## Purpose

A storyboard must encode enough state that later image/video generation does not treat every panel as a fresh universe.

## State dimensions

Track only dimensions relevant to the project, but include these when applicable.

### Character
- stable `CHRxx` identity;
- wardrobe `WRDxx` and variation;
- hair/accessories;
- emotional/performance state;
- body orientation;
- screen side;
- held objects;
- dirt/wear/injury/wetness or other accumulated state.

### Environment
- stable `ENVxx` identity;
- time of day;
- practical lights on/off;
- weather;
- geography and entrances/exits;
- recurring object positions;
- crowd/background density.

### Prop / project
- stable `PRPxx` identity;
- version/stage (`V1`, `V2`, etc.);
- modifications already made;
- damage/wear;
- location/owner;
- evidence that must persist.

### Technology / UI
- `TECxx` / `UIxx` identity;
- current screen/state;
- correct function;
- connection to physical action;
- forbidden functionality.

### Photographic state
- narrative phase look variation;
- local exposure/light condition;
- color-temperature relationship;
- time-of-day continuity;
- deliberate semi-canonical override.

### Spatial continuity
- screen direction;
- eyeline;
- movement direction;
- relative geography;
- axis/180-degree relationship when relevant.

## Panel continuity object

Recommended:

```json
{
  "continuity_in": {
    "characters": ["CHR01:WRD01:v1:left_of_frame"],
    "environment": "ENV01:day:stateA",
    "props": ["PRP01:V2:on_workbench"],
    "screen_direction": "left_to_right"
  },
  "continuity_out": {
    "characters": ["CHR01:WRD01:v1:right_of_frame"],
    "environment": "ENV01:day:stateA",
    "props": ["PRP01:V2:held_by_CHR01"],
    "screen_direction": "left_to_right"
  }
}
```

Use semantic strings or structured objects; consistency matters more than one exact serialization.

## Continuity exceptions

If a panel intentionally breaks continuity for montage, dream, conceptual insert, flashback, jump cut, or graphic transition, record the reason. Never let a generation artifact masquerade as an intentional change.
