#!/usr/bin/env python3
"""Check the local PM harness setup and print the next action.

This is the human-operator doctor, not a validator replacement. It answers:
"is my vault wired, is the agent installed, and what should I do next?"
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - reported as a failed check
    yaml = None


def _frontmatter(path: Path) -> dict:
    if yaml is None or not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    try:
        _, raw, _ = text.split("---\n", 2)
        data = yaml.safe_load(raw)
        return data if isinstance(data, dict) else {}
    except (ValueError, yaml.YAMLError):
        return {}


def _dataview_root(vault: Path) -> Path | None:
    for candidate in (vault, *vault.parents[:3]):
        if (candidate / ".obsidian" / "plugins" / "dataview").exists():
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the PM harness setup")
    parser.add_argument("--vault", default=".", help="vault root")
    parser.add_argument(
        "--hermes-home",
        default=os.environ.get("HERMES_HOME") or str(Path.home() / ".hermes"),
        help="Hermes profile root (default: $HERMES_HOME or ~/.hermes)",
    )
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    hermes_home = Path(args.hermes_home).expanduser().resolve()
    failures = 0
    warnings = 0

    def report(status: str, label: str, detail: str = "") -> None:
        nonlocal failures, warnings
        if status == "FAIL":
            failures += 1
        elif status == "WARN":
            warnings += 1
        suffix = f" — {detail}" if detail else ""
        print(f"{status:<4} {label}{suffix}")

    print("PM harness doctor")
    print(f"vault:  {vault}")
    print(f"profile: {hermes_home}")
    print()

    rules = vault / "99-Playbook" / "Rules.md"
    if rules.exists():
        report("PASS", "Vault root", "99-Playbook/Rules.md found")
    else:
        report("FAIL", "Vault root", "99-Playbook/Rules.md not found")

    if (vault / "Dashboard.md").exists():
        report("PASS", "Dashboard", "Dashboard.md found")
    else:
        report("FAIL", "Dashboard", "Dashboard.md not found")

    if sys.version_info >= (3, 9):
        report("PASS", "Python", sys.version.split()[0])
    else:
        report("FAIL", "Python", "Python 3.9+ required")

    if yaml is None:
        report("FAIL", "PyYAML", "run: python3 -m pip install -r scripts/requirements.txt")
    else:
        report("PASS", "PyYAML", "frontmatter checks available")

    skill = hermes_home / "skills" / "productivity" / "pm" / "SKILL.md"
    if skill.exists():
        meta = _frontmatter(skill)
        if meta.get("name") == "pm":
            report("PASS", "pm skill", str(skill))
        else:
            report("FAIL", "pm skill", "SKILL.md does not declare name: pm")
    else:
        report("FAIL", "pm skill", "run: python3 scripts/install_agent_layer.py --vault . --hermes-home \"$HERMES_HOME\"")

    if shutil.which("hermes"):
        report("PASS", "Hermes CLI", shutil.which("hermes") or "hermes")
    else:
        report("WARN", "Hermes CLI", "not on PATH; the vault still works")

    dataview = _dataview_root(vault)
    if dataview:
        report("PASS", "Dataview", f"plugin found under {dataview}")
    else:
        report("WARN", "Dataview", "not found in vault or parent; enable it in Obsidian")

    project_notes = 0
    for path in vault.rglob("*.md"):
        if ".obsidian" in path.parts:
            continue
        if _frontmatter(path).get("project") == "pm-harness":
            project_notes += 1
    if project_notes:
        report("PASS", "Project marker", f"{project_notes} notes carry project: pm-harness")
    else:
        report("WARN", "Project marker", "no notes found; empty vault is a valid start")

    problems = sorted((vault / "02-Problems").glob("PROB-*.md"))
    if problems:
        report("PASS", "First problem", f"{len(problems)} live problem note(s)")
    else:
        report("WARN", "First problem", "none yet; run /pm start")

    compliance = None
    for candidate in (vault / "11-Compliance").glob("COMP-*-Compliance-Scope.md"):
        if candidate.name.startswith("COMP-003"):
            compliance = candidate
            break
    if compliance:
        meta = _frontmatter(compliance)
        if meta.get("status") == "draft" or meta.get("owner") in (None, "", "Unassigned"):
            report("WARN", "Compliance gate", f"{compliance.name} is draft/Unassigned; health-data work is blocked")
        else:
            report("PASS", "Compliance gate", f"{compliance.name}: {meta.get('status')}")
    else:
        report("WARN", "Compliance gate", "no live compliance scope found")

    if (vault / ".git").exists():
        try:
            dirty = subprocess.run(
                ["git", "-C", str(vault), "status", "--porcelain"],
                check=True,
                text=True,
                capture_output=True,
            ).stdout.strip()
            if dirty:
                report("WARN", "Git", "working tree has uncommitted changes")
            else:
                report("PASS", "Git", "working tree clean")
        except (OSError, subprocess.CalledProcessError):
            report("WARN", "Git", "could not read status")
    else:
        report("WARN", "Git", "no .git in this folder; external git pointer or not cloned")

    print()
    if failures:
        print(f"Next: fix the {failures} failed check(s) above.")
        return 1
    if problems:
        print("Next: run /pm status, then /pm review when you have artifacts.")
    else:
        print("Next: run /pm start, or open START-HERE.md.")
    if warnings:
        print(f"({warnings} warning(s); warnings do not block the vault.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
