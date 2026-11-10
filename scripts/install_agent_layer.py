#!/usr/bin/env python3
"""Install the repository's agent layer into a Hermes profile.

Copies the skill and writes pm.yaml with an absolute vault path. The bundle
template is never left with the <absolute path ...> placeholder.

Refuses to overwrite an existing skill or bundle unless --update is passed.
The source bundle is validated before anything is copied.

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

try:
    import yaml
except ImportError:  # pragma: no cover - reported in main()
    yaml = None

PLACEHOLDER = "<absolute path to the vault root>"


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
        help="overwrite an existing skill and pm.yaml in the target profile",
    )
    args = parser.parse_args()

    if yaml is None:
        print(
            "PyYAML is required. Run: python3 -m pip install -r scripts/requirements.txt",
            file=sys.stderr,
        )
        return 2

    repo = Path(__file__).resolve().parent.parent
    vault = Path(args.vault).expanduser().resolve()
    hermes_home = Path(args.hermes_home).expanduser().resolve()

    source_skill = repo / "agent" / "skills" / "productivity" / "pm"
    source_bundle = repo / "agent" / "skill-bundles" / "pm.yaml"
    if not source_skill.exists() or not source_bundle.exists():
        print("Run this from the repository checkout.", file=sys.stderr)
        return 2
    if not (vault / "99-Playbook" / "Rules.md").exists():
        print(f"Not a PM vault: {vault}", file=sys.stderr)
        return 2

    bundle = source_bundle.read_text()
    if bundle.count(PLACEHOLDER) != 1:
        print(f"Bundle template must contain exactly one placeholder: {source_bundle}", file=sys.stderr)
        return 2
    try:
        parsed = yaml.safe_load(bundle)
    except yaml.YAMLError as exc:
        print(f"Bundle template is not valid YAML: {exc}", file=sys.stderr)
        return 2
    if not isinstance(parsed, dict):
        print("Bundle template is not a mapping.", file=sys.stderr)
        return 2
    skills = parsed.get("skills")
    if not isinstance(skills, list) or "pm" not in skills:
        print("Bundle template does not declare the pm skill.", file=sys.stderr)
        return 2
    instruction = str(parsed.get("instruction", ""))
    if PLACEHOLDER not in instruction or "99-Playbook/Rules.md" not in instruction:
        print("Bundle template is missing the vault root or Rules.md instruction.", file=sys.stderr)
        return 2

    target_skill = hermes_home / "skills" / "productivity" / "pm"
    target_bundle = hermes_home / "skill-bundles" / "pm.yaml"
    collisions = [p for p in (target_skill, target_bundle) if p.exists()]
    if collisions and not args.update:
        print("Refusing to overwrite existing agent layer:", file=sys.stderr)
        for path in collisions:
            print(f"  {path}", file=sys.stderr)
        print("Re-run with --update to replace it.", file=sys.stderr)
        return 2
    if target_skill.exists() and not target_skill.is_dir():
        print(f"Target skill path is not a directory: {target_skill}", file=sys.stderr)
        return 2
    if target_bundle.exists() and not target_bundle.is_file():
        print(f"Target bundle path is not a file: {target_bundle}", file=sys.stderr)
        return 2

    target_skill.parent.mkdir(parents=True, exist_ok=True)
    target_bundle.parent.mkdir(parents=True, exist_ok=True)

    shutil.copytree(source_skill, target_skill, dirs_exist_ok=args.update)
    target_bundle.write_text(bundle.replace(PLACEHOLDER, str(vault)))

    print(f"skill:  {target_skill}")
    print(f"bundle: {target_bundle}")
    print(f"vault:  {vault}")
    if args.update and collisions:
        print("updated existing layer")
    print("Next: hermes bundles reload")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
