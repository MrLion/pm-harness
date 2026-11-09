#!/usr/bin/env python3
"""Check Obsidian wikilinks inside the PM vault.

Usage:
    python scripts/check_wikilinks.py [vault-root]

Defaults to the PM vault path on this machine. Prints unresolved links, ambiguous
file targets, and broken heading/block anchors. Exit code 1 when anything fails.

Handles Obsidian table-cell aliases written as [[Note\\|Alias]].
"""

from pathlib import Path
import re
import sys
import urllib.parse

DEFAULT_VAULT = Path.cwd()

LINK_RE = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
# Image/attachment embeds (![[...]]) are not wikilinks; they are checked by
# Obsidian itself and are not Markdown resolution targets.
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def split_link(raw):
    """Return (file target, heading/block anchor, alias) from an Obsidian link body.

    Obsidian table cells escape the alias separator as \\|. Normalize that
    before splitting; otherwise [[Problem\\|PROB-001]] resolves as a file
    named "Problem\\".
    """
    raw = re.sub(r"\\+\|", "|", raw)
    if "|" in raw:
        target_part, alias = raw.split("|", 1)
    else:
        target_part, alias = raw, None
    if "#" in target_part:
        target, anchor = target_part.split("#", 1)
    else:
        target, anchor = target_part, None
    return target.strip(), (anchor.strip() if anchor else None), (alias.strip() if alias else None)


def resolve_target(target, by_rel, by_base, prefix):
    if not target:
        return []
    if "/" in target:
        if not target.startswith(prefix):
            return []
        path = by_rel.get(target)
        return [path] if path else []
    return by_base.get(target, [])


def anchor_exists(path, anchor):
    if not anchor:
        return True
    anchor = urllib.parse.unquote(anchor).strip()
    text = path.read_text(errors="ignore")
    if anchor.startswith("^"):
        block = anchor[1:]
        return bool(re.search(r"\^" + re.escape(block) + r"\b", text))
    headings = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            headings.append(match.group(2).strip())
    return anchor in headings or anchor.lower() in [h.lower() for h in headings]


def main():
    root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_VAULT
    if not root.exists():
        print(f"Vault not found: {root}", file=sys.stderr)
        return 2

    md_files = [p for p in root.rglob("*.md")]
    parent = root.parent
    by_rel = {p.relative_to(parent).with_suffix("").as_posix(): p for p in md_files}
    by_base = {}
    for path in md_files:
        by_base.setdefault(path.stem, []).append(path)

    unresolved = []
    ambiguous = []
    bad_anchors = []
    total_links = 0

    for path in md_files:
        text = path.read_text(errors="ignore")
        for match in LINK_RE.finditer(text):
            total_links += 1
            target, anchor, alias = split_link(match.group(1))
            matches = resolve_target(target, by_rel, by_base, root.name + "/")
            source = path.relative_to(root).as_posix()
            if not matches:
                unresolved.append((source, target))
            elif len(matches) > 1:
                ambiguous.append((source, target, [m.relative_to(root).as_posix() for m in matches]))
            elif anchor and not anchor_exists(matches[0], anchor):
                bad_anchors.append((source, target, anchor, matches[0].relative_to(root).as_posix()))

    print(f"Markdown files: {len(md_files)}")
    print(f"Wikilinks: {total_links}")
    print(f"Unresolved: {len(unresolved)}")
    for source, target in unresolved:
        print(f"  UNRESOLVED {source} -> {target}")
    print(f"Ambiguous: {len(ambiguous)}")
    for source, target, matches in ambiguous:
        print(f"  AMBIGUOUS {source} -> {target}: {', '.join(matches)}")
    print(f"Broken anchors: {len(bad_anchors)}")
    for source, target, anchor, resolved in bad_anchors:
        print(f"  BAD_ANCHOR {source} -> {resolved}#{anchor}")

    return 0 if not unresolved and not ambiguous and not bad_anchors else 1


if __name__ == "__main__":
    raise SystemExit(main())
