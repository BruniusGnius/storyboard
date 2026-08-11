# Storyboard Decision Ledger and Lock

## Storyboard decisions

Use `SBDxxx` for material storyboard decisions and corrections.

Recommended fields:
- `decision_id`;
- `statement`;
- `category`;
- `origin`;
- `commitment`;
- `status`;
- `rationale`;
- `source_refs`;
- `panel_refs`;
- `implications`;
- `avoid`;
- `supersedes`;
- `superseded_by`.

## Commitment

Use:
- `locked` — downstream cannot change without human-approved revision;
- `preferred` — approved/default direction;
- `flexible` — later technical layer may optimize;
- `open` — deliberately unresolved.

## Panel approval

A panel may have:
- `draft`;
- `human_revised`;
- `approved_panel`;
- `locked_panel`;
- `rejected`;
- `superseded`.

## Revision identity

Keep `panel_id: SB012` stable across normal revisions. Add `revision_no` and prompt/image revision refs.

If one panel is split into two, mark original `SB012` superseded and create new IDs. If two panels merge, preserve source refs in the merged panel and mark originals superseded.

## Lock summary

The final Storyboard Lock should state:
- locked sequence/scene order;
- locked narrative coverage;
- locked panel intentions;
- locked entity/continuity choices;
- flexible technical values;
- open technical questions;
- rejected/superseded alternatives.
