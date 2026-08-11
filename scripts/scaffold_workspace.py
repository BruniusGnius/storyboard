#!/usr/bin/env python3
"""Create a minimal storyboard workspace without external dependencies."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", nargs="?", default="storyboard")
    args = parser.parse_args()

    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    (root / "panels").mkdir(exist_ok=True)
    (root / "revisions").mkdir(exist_ok=True)

    files = {
        "STORYBOARD.md": "# Storyboard\n\nStatus: draft\n",
        "STORYBOARD_PROMPT_PACK.md": "# Storyboard Prompt Pack\n\nPurpose: storyboard previsualization\n",
        "storyboard.json": {
            "schema": "storyboard/v1",
            "storyboard_status": "draft",
            "sources": [],
            "sequences": [],
            "scenes": [],
            "panels": [],
            "decision_ledger": [],
            "open_questions": [],
        },
        "storyboard-prompts.json": {
            "schema": "storyboard/prompts/v1",
            "purpose": "storyboard_previsualization",
            "production_ready": False,
            "prompts": [],
        },
        "handoff.json": {
            "schema": "storyboard/handoff/v1",
            "storyboard_status": "draft",
        },
    }

    for name, value in files.items():
        path = root / name
        if path.exists():
            continue
        if isinstance(value, str):
            path.write_text(value, encoding="utf-8")
        else:
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Storyboard workspace ready: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
