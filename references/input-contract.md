# Input Contract

## Preferred upstream payloads

### Narrative
May include:
- `narrative-map.json`;
- locution handoff;
- transcript/voiceover/script;
- `Bxx`, `Pxx`, speaker IDs, timecodes, emotion, energy, subtext, visual opportunities.

### Creative Direction
May include:
- governing concept;
- visual promise;
- visual arc `VAxx`;
- `CDxxx` ledger;
- constraints and forbidden territory;
- production envelope.

### Visual Development
Prefer a `visual-development/handoff/v1` containing:
- Visual Canon `canonical`;
- `semi_canonical` look defaults;
- `SHOT_VARIABLE_SCHEMA`;
- `CANON_FRAGMENT`;
- `LOOK_DEFAULT_FRAGMENT`;
- stable `ENTITY_FRAGMENT[ID]` blocks;
- approved `CHRxx`, `ENVxx`, `PRPxx`, `TECxx`, `UIxx`, `WRDxx`;
- approved concept frames `KFxx` as look anchors;
- continuity rules;
- forbidden patterns;
- open decisions and storyboard permissions.

## Missing upstream layers

The Skill must still work when one or more layers are absent.

- If no narrative map exists, derive provisional story units from the script/brief.
- If no Creative Direction exists, capture only minimum visual intent; mark it provisional.
- If no Visual Development exists, use user references/brief to establish temporary visual assumptions; do not claim a Visual Lock.
- If no exact timing exists, build relative timing and mark `timing_status: provisional`.

## Source preservation

Never modify upstream IDs. If a source uses `S01` for a speaker, do not reuse `S01` for a storyboard element. Use `SQxx`, `SCxx`, and `SBxxx`.
