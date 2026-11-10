#!/usr/bin/env python3
"""Validate the PM harness.

Checks:
- relative Markdown links and anchors resolve
- frontmatter parses
- artifact IDs are unique and match filenames
- artifact notes have project, type, status, and a real calendar updated date
- approved compliance scopes have a named owner, data classification, and jurisdiction
- the live compliance gate is visibly open when it is still draft
- accepted decisions with an overdue review are reported
- product templates contain no unresolved [FILL] markers

The validator does not judge product quality. It only checks the contract the
vault depends on. Warnings are informational; errors exit 1.

Usage:
    python3 scripts/validate_vault.py [vault-root]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - reported in main()
    yaml = None

LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ID_IN_NAME_RE = re.compile(r"^([A-Z]+(?:-[A-Z]+)?-\d{3,4}(?:-\d{2})?)")
CONTENT_DIR_RE = re.compile(r"^\d{2}-")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"\s+", "-", value).strip("-")


def strip_code(line: str) -> str:
    return re.sub(r"`[^`]*`", "", line)


def read_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(errors="ignore")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML error: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data, text


def is_content_note(path: Path, root: Path) -> bool:
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    return any(CONTENT_DIR_RE.match(part) for part in rel.parts[:-1])


def collect_links(path: Path) -> list[str]:
    links: list[str] = []
    in_fence = False
    for line in path.read_text(errors="ignore").splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(strip_code(line)):
            links.append(match.group(2).strip())
    return links


def check_links(root: Path, files: list[Path]) -> tuple[list[str], list[str], dict[Path, int]]:
    errors: list[str] = []
    warnings: list[str] = []
    inbound: dict[Path, int] = defaultdict(int)
    headings_by_file: dict[Path, set[str]] = {}

    for path in files:
        headings: set[str] = set()
        for line in path.read_text(errors="ignore").splitlines():
            match = HEADING_RE.match(line)
            if match:
                headings.add(slugify(match.group(2)))
        headings_by_file[path] = headings

    for path in files:
        for raw in collect_links(path):
            if raw.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                continue
            target, _, anchor = raw.partition("#")
            target = urllib.parse.unquote(target).strip().strip("<>")
            if not target:
                target_path = path
            else:
                target_path = (path.parent / target).resolve()
            if not target_path.exists():
                errors.append(f"{path}: missing link target: {raw}")
                continue
            if target_path.is_file() and target_path.suffix.lower() == ".md":
                inbound[target_path] += 1
                if anchor:
                    anchor = urllib.parse.unquote(anchor).strip()
                    headings = headings_by_file.get(target_path, set())
                    if not headings:
                        for line in target_path.read_text(errors="ignore").splitlines():
                            match = HEADING_RE.match(line)
                            if match:
                                headings.add(slugify(match.group(2)))
                        headings_by_file[target_path] = headings
                    if anchor not in headings:
                        errors.append(f"{path}: missing anchor #{anchor} in {target_path}")
    return errors, warnings, inbound


def check_frontmatter(root: Path, files: list[Path]) -> tuple[list[str], list[str], dict[str, list[Path]]]:
    errors: list[str] = []
    warnings: list[str] = []
    ids: dict[str, list[Path]] = defaultdict(list)
    today = dt.date.today()

    for path in files:
        try:
            data, _ = read_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue
        if not data:
            continue
        note_id = data.get("id")
        if note_id:
            ids[str(note_id)].append(path)
            filename_match = ID_IN_NAME_RE.match(path.name)
            if not filename_match:
                errors.append(f"{path}: artifact id {note_id!r} is not encoded in the filename")
            elif filename_match.group(1) != str(note_id):
                errors.append(
                    f"{path}: frontmatter id {note_id!r} does not match filename id "
                    f"{filename_match.group(1)!r}"
                )
            if not data.get("type"):
                errors.append(f"{path}: artifact with id {note_id!r} has no type")
            if not data.get("project"):
                errors.append(f"{path}: artifact with id {note_id!r} has no project marker")
            if data.get("type") != "feedback" and not data.get("status"):
                errors.append(f"{path}: artifact with id {note_id!r} has no status")
            updated = data.get("updated")
            if not updated:
                errors.append(f"{path}: artifact with id {note_id!r} has no updated date")
            elif isinstance(updated, dt.date):
                pass
            elif isinstance(updated, str):
                try:
                    dt.date.fromisoformat(updated)
                except ValueError:
                    errors.append(f"{path}: updated is not a real YYYY-MM-DD date: {updated!r}")
            else:
                errors.append(f"{path}: updated is not YYYY-MM-DD: {updated!r}")
        if data.get("type") == "decision" and data.get("status") == "accepted":
            review_date = data.get("review_date")
            actual = data.get("actual_outcome")
            if review_date and (actual is None or str(actual).strip().lower() == "pending"):
                try:
                    if dt.date.fromisoformat(str(review_date)) < today:
                        warnings.append(f"{path}: accepted decision review is overdue ({review_date})")
                except ValueError:
                    errors.append(f"{path}: invalid review_date {review_date!r}")
        if data.get("type") == "compliance-scope":
            status = str(data.get("status", ""))
            if status == "draft" and "99-Playbook/Templates" not in path.as_posix():
                warnings.append(f"{path}: compliance gate is open (status: draft)")
            if status in {"approved", "active"}:
                owner = str(data.get("owner", "")).strip()
                if not owner or owner.lower() in {"unassigned", "unknown", "unsure", "tbd", "todo"} or "[FILL" in owner:
                    errors.append(f"{path}: approved compliance scope has no named owner")
                classification = str(data.get("data_classification", "")).strip()
                if not classification or classification.lower() in {"unknown", "unsure", "tbd", "todo"} or "[FILL" in classification:
                    errors.append(f"{path}: approved compliance scope has no data classification")
                jurisdiction = str(data.get("jurisdiction", "")).strip()
                if not jurisdiction or jurisdiction.lower() in {"unknown", "unsure", "none", "tbd", "todo"} or "[FILL" in jurisdiction:
                    errors.append(f"{path}: approved compliance scope has no jurisdiction")
    return errors, warnings, ids


def check_product_templates(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if "99-Playbook/Templates" not in path.as_posix():
            continue
        if "Operating-Models" in path.as_posix() or "Compliance" in path.as_posix():
            continue
        if path.name in {"_Templates.md", "Dashboard-Example.md"}:
            continue
        text = path.read_text(errors="ignore")
        if "[FILL" in text:
            errors.append(f"{path}: product template still contains an unresolved [FILL] marker")
    return errors


def check_orphans(root: Path, files: list[Path], inbound: dict[Path, int]) -> list[str]:
    warnings: list[str] = []
    for path in files:
        if not is_content_note(path, root):
            continue
        try:
            data, _ = read_frontmatter(path)
        except ValueError:
            continue
        if not data.get("type"):
            continue
        if path.name.startswith("_") or path.name in {"README.md", "Dashboard.md"}:
            continue
        if inbound.get(path, 0) == 0:
            warnings.append(f"{path}: no inbound Markdown link (orphan candidate)")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the PM harness")
    parser.add_argument("root", nargs="?", default=".", help="vault root")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args()

    if yaml is None:
        print(
            "PyYAML is required. Run: python3 -m pip install -r scripts/requirements.txt",
            file=sys.stderr,
        )
        return 2

    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        print(f"Vault not found: {root}", file=sys.stderr)
        return 2

    files = sorted(
        p
        for p in root.rglob("*.md")
        if ".git" not in p.parts
        and ".obsidian" not in p.parts
        and not ((root / "examples").is_dir() and "examples" in p.parts)
    )
    link_errors, link_warnings, inbound = check_links(root, files)
    fm_errors, fm_warnings, ids = check_frontmatter(root, files)
    template_errors = check_product_templates(root, files)
    orphan_warnings = check_orphans(root, files, inbound)

    duplicate_errors = [
        f"duplicate id {note_id!r}: {', '.join(str(p) for p in paths)}"
        for note_id, paths in ids.items()
        if len(paths) > 1
    ]
    errors = link_errors + fm_errors + template_errors + duplicate_errors
    warnings = link_warnings + fm_warnings + orphan_warnings

    if args.json:
        print(json.dumps({
            "root": str(root),
            "files": len(files),
            "errors": errors,
            "warnings": warnings,
            "summary": {"errors": len(errors), "warnings": len(warnings)},
        }, indent=2))
    else:
        for message in errors:
            print(f"ERROR {message}")
        for message in warnings:
            print(f"WARN  {message}")
        print(
            f"Checked {len(files)} Markdown files: "
            f"{len(errors)} error(s), {len(warnings)} warning(s)."
        )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
