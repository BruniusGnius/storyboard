#!/usr/bin/env python3
"""Validate storyboard semantic JSON and storyboard prompt-pack JSON."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TC_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}$")
PANEL_RE = re.compile(r"^SB\d{3,}$")
SEQ_RE = re.compile(r"^SQ\d{2,}$")
SCENE_RE = re.compile(r"^SC\d{2,}$")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"Cannot parse {path}: {exc}") from exc


def tc_seconds(tc: str) -> float:
    h, m, rest = tc.split(":")
    s, ms = rest.split(".")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("storyboard_json")
    ap.add_argument("prompts_json")
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    try:
        sb = load_json(Path(args.storyboard_json))
        pp = load_json(Path(args.prompts_json))
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    if sb.get("schema") != "storyboard/v1":
        errors.append("storyboard.json schema must be storyboard/v1")
    if pp.get("schema") != "storyboard/prompts/v1":
        errors.append("storyboard-prompts.json schema must be storyboard/prompts/v1")
    if pp.get("purpose") != "storyboard_previsualization":
        errors.append("prompt pack purpose must be storyboard_previsualization")
    if pp.get("production_ready") is True:
        errors.append("storyboard prompt pack must not claim production_ready=true")

    sequences = sb.get("sequences", [])
    scenes = sb.get("scenes", [])
    panels = sb.get("panels", [])
    prompts = pp.get("prompts", [])

    seq_ids = set()
    for item in sequences:
        sid = item.get("sequence_id")
        if not isinstance(sid, str) or not SEQ_RE.match(sid):
            errors.append(f"Invalid sequence_id: {sid!r}")
        elif sid in seq_ids:
            errors.append(f"Duplicate sequence_id: {sid}")
        else:
            seq_ids.add(sid)

    scene_ids = set()
    for item in scenes:
        sid = item.get("scene_id")
        if not isinstance(sid, str) or not SCENE_RE.match(sid):
            errors.append(f"Invalid scene_id: {sid!r}")
        elif sid in scene_ids:
            errors.append(f"Duplicate scene_id: {sid}")
        else:
            scene_ids.add(sid)
        if item.get("sequence_id") not in seq_ids:
            errors.append(f"Scene {sid} references missing sequence {item.get('sequence_id')}")

    panel_ids = set()
    timed = []
    for panel in panels:
        pid = panel.get("panel_id")
        if not isinstance(pid, str) or not PANEL_RE.match(pid):
            errors.append(f"Invalid panel_id: {pid!r}")
            continue
        if pid in panel_ids:
            errors.append(f"Duplicate panel_id: {pid}")
        panel_ids.add(pid)
        if panel.get("sequence_id") not in seq_ids:
            errors.append(f"Panel {pid} references missing sequence {panel.get('sequence_id')}")
        if panel.get("scene_id") not in scene_ids:
            errors.append(f"Panel {pid} references missing scene {panel.get('scene_id')}")
        if not panel.get("narrative_purpose"):
            errors.append(f"Panel {pid} missing narrative_purpose")
        if not panel.get("visible_action"):
            errors.append(f"Panel {pid} missing visible_action")
        cam = panel.get("camera_preview", {})
        if cam and cam.get("technical_status") not in {"provisional_storyboard", "upstream_locked"}:
            warnings.append(f"Panel {pid} camera_preview technical_status should be provisional_storyboard or upstream_locked")
        tcin, tcout = panel.get("tc_in"), panel.get("tc_out")
        if tcin is not None or tcout is not None:
            if not isinstance(tcin, str) or not TC_RE.match(tcin) or not isinstance(tcout, str) or not TC_RE.match(tcout):
                errors.append(f"Panel {pid} has invalid timecode format")
            else:
                a, b = tc_seconds(tcin), tc_seconds(tcout)
                if b <= a:
                    errors.append(f"Panel {pid} tc_out must be after tc_in")
                timed.append((a, b, pid))

    timed.sort()
    for (_, prev_end, prev_id), (cur_start, _, cur_id) in zip(timed, timed[1:]):
        if cur_start < prev_end - 0.001:
            warnings.append(f"Primary panel windows overlap: {prev_id} -> {cur_id}; document compositing/layer intent if deliberate")

    prompt_ids = set()
    active_prompt_by_panel: dict[str, int] = {}
    for p in prompts:
        pid = p.get("panel_id")
        if pid not in panel_ids:
            errors.append(f"Prompt references missing panel {pid}")
            continue
        active_prompt_by_panel[pid] = active_prompt_by_panel.get(pid, 0) + 1
        prompt = p.get("prompt_en")
        if not isinstance(prompt, str) or len(prompt.strip()) < 120:
            errors.append(f"Prompt for {pid} is missing or too underspecified")
        if p.get("technical_status") != "provisional_storyboard":
            warnings.append(f"Prompt for {pid} should mark technical_status=provisional_storyboard")
        if p.get("prompt_id"):
            if p["prompt_id"] in prompt_ids:
                errors.append(f"Duplicate prompt_id: {p['prompt_id']}")
            prompt_ids.add(p["prompt_id"])

    for pid in panel_ids:
        count = active_prompt_by_panel.get(pid, 0)
        if count == 0:
            errors.append(f"Selected panel {pid} has no active storyboard prompt")
        elif count > 1:
            warnings.append(f"Panel {pid} has {count} prompt records; ensure exactly one is active")

    status = sb.get("storyboard_status")
    approval = sb.get("approval", {})
    if status == "human_locked" and not approval.get("human_approved"):
        errors.append("storyboard_status=human_locked requires approval.human_approved=true")

    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARNING: {msg}")
    print(f"Validation complete: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
