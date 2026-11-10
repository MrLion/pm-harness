#!/usr/bin/env python3
"""Install the repository's PM skill into a Hermes profile.

The skill is the command layer: Hermes registers it as `/pm` on every surface.
There is no separate bundle, so the desktop and the classic CLI expose one
command, not two.

Refuses to overwrite an existing skill unless --update is passed.

Usage:
    python3 scripts/install_agent_layer.py --vault . --hermes-home ~/.hermes
    python3 scripts/install_agent_layer.py --vault . --hermes-home ~/.hermes --update
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Install the PM agent layer")
    parser.add_argument("--vault", default=".", help="vault root")
    parser.add_argument(
        "--hermes-home",
        default=os.environ.get("HERMES_HOME") or str(Path.home() / ".hermes"),
        help="Hermes profile root (default: $HERMES_HOME or ~/.hermes)",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="overwrite an existing skill in the target profile",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    vault = Path(args.vault).expanduser().resolve()
    hermes_home = Path(args.hermes_home).expanduser().resolve()

    source_skill = repo / "agent" / "skills" / "productivity" / "pm"
    if not source_skill.exists():
        print("Run this from the repository checkout.", file=sys.stderr)
        return 2
    if not (vault / "99-Playbook" / "Rules.md").exists():
        print(f"Not a PM vault: {vault}", file=sys.stderr)
        return 2

    target_skill = hermes_home / "skills" / "productivity" / "pm"
    if target_skill.exists() and not args.update:
        print("Refusing to overwrite existing agent layer:", file=sys.stderr)
        print(f"  {target_skill}", file=sys.stderr)
        print("Re-run with --update to replace it.", file=sys.stderr)
        return 2
    if target_skill.exists() and not target_skill.is_dir():
        print(f"Target skill path is not a directory: {target_skill}", file=sys.stderr)
        return 2

    target_skill.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_skill, target_skill, dirs_exist_ok=args.update)

    print(f"skill: {target_skill}")
    print(f"vault: {vault}")
    if args.update:
        print("updated existing layer")
    print("Next: start a new Hermes chat so the skill command list refreshes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
