#!/usr/bin/env python3
"""Install the repository's agent layer into a Hermes profile.

Copies the skill and writes pm.yaml with an absolute vault path. The bundle
template is never left with the <absolute path ...> placeholder.

Usage:
    python3 scripts/install_agent_layer.py --vault . --hermes-home ~/.hermes
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

PLACEHOLDER = "<absolute path to the vault root>"


def main() -> int:
    parser = argparse.ArgumentParser(description="Install the PM agent layer")
    parser.add_argument("--vault", default=".", help="vault root")
    parser.add_argument(
        "--hermes-home",
        default=os.environ.get("HERMES_HOME") or str(Path.home() / ".hermes"),
        help="Hermes profile root (default: $HERMES_HOME or ~/.hermes)",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    vault = Path(args.vault).expanduser().resolve()
    hermes_home = Path(args.hermes_home).expanduser().resolve()

    source_skill = repo / "agent" / "skills" / "productivity" / "product-management"
    source_bundle = repo / "agent" / "skill-bundles" / "pm.yaml"
    if not source_skill.exists() or not source_bundle.exists():
        print("Run this from the repository checkout.", file=sys.stderr)
        return 2
    if not (vault / "99-Playbook" / "Rules.md").exists():
        print(f"Not a PM vault: {vault}", file=sys.stderr)
        return 2

    target_skill = hermes_home / "skills" / "productivity" / "product-management"
    target_bundle = hermes_home / "skill-bundles" / "pm.yaml"
    target_skill.parent.mkdir(parents=True, exist_ok=True)
    target_bundle.parent.mkdir(parents=True, exist_ok=True)

    shutil.copytree(source_skill, target_skill, dirs_exist_ok=True)
    bundle = source_bundle.read_text()
    if PLACEHOLDER not in bundle:
        print(f"Bundle template is missing the placeholder: {source_bundle}", file=sys.stderr)
        return 2
    target_bundle.write_text(bundle.replace(PLACEHOLDER, str(vault)))

    print(f"skill:  {target_skill}")
    print(f"bundle: {target_bundle}")
    print(f"vault:  {vault}")
    print("Next: hermes bundles reload")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
