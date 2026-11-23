#!/usr/bin/env python3
"""Create a blank problem scaffold with the next live PROB-NNN ID.

The operator supplies the observed problem in conversation; this script handles
the mechanical parts: ID allocation, filename, folder, and frontmatter.

Usage:
    python3 scripts/new_artifact.py --vault . --type problem \
        --title "Patients cannot predict imaging cost" --slug imaging-cost
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ID_RE = re.compile(r"^id:\s*(PROB-(\d{3,4}))\s*$", re.MULTILINE)


def next_problem_id(repo: Path) -> str:
    highest = 0
    for folder in (repo / "02-Problems", repo / "99-Playbook" / "Templates"):
        if not folder.exists():
            continue
        for path in folder.glob("PROB-*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            for match in ID_RE.finditer(text):
                highest = max(highest, int(match.group(2)))
    return f"PROB-{highest + 1:03d}"


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value or "untitled"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a blank PM problem note")
    parser.add_argument("--vault", default=".", help="vault root")
    parser.add_argument("--type", default="problem", choices=["problem"])
    parser.add_argument("--title", required=True, help="short problem title")
    parser.add_argument("--slug", help="filename slug; derived from the title if omitted")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    vault = Path(args.vault).expanduser().resolve()
    if not (vault / "99-Playbook" / "Rules.md").exists():
        print(f"Not a PM vault: {vault}", file=sys.stderr)
        return 2

    problem_id = next_problem_id(repo)
    slug = slugify(args.slug or args.title)
    target = vault / "02-Problems" / f"{problem_id}-{slug}.md"
    if target.exists():
        print(f"Refusing to overwrite: {target}", file=sys.stderr)
        return 2

    today = dt.date.today().isoformat()
    title = args.title.strip()
    body = f'''---
type: problem
project: pm-harness
artifact: problem
id: {problem_id}
status: discovery
priority: unset
confidence: low
frequency: unknown
severity: unknown
created: {today}
updated: {today}
framework: none
---

# Problem — {title}

## Problem Statement

[FILL: who experiences what problem, when, and at what cost. Do not include a solution.]

## User / Segment

[FILL: target user and segment. Link a live persona if one exists.]

## JTBD

[FILL: when ______, I want ______, so I can ______.]

## Evidence

| Type | Source | Date | Says what | Strength |
|---|---|---|---|---|
| | | | | |

Evidence unavailable. Leave this row empty until a source exists.

## Next evidence

[FILL: the cheapest observation that would change this problem's confidence.]

## Frequency

Unknown.

## Severity

Unknown.

## Current workaround

[FILL: what people do today instead.]

## Business impact

Evidence unavailable.

## Assumptions / Unknowns

- [FILL]

## Related Opportunities

- None yet. Add an opportunity only after the problem is evidenced.

## Buyer

Unresolved.
'''
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8")
    print(f"created: {target}")
    print(f"id:      {problem_id}")
    print("Next: fill the [FILL] sections, then run python3 scripts/validate_vault.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
