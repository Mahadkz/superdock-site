#!/usr/bin/env python3
"""Stage 8: mechanical QA. Never trust an agent's self-report on what a script can count.

  tools/qa.py <slug> [<slug>...]
  tools/qa.py --all-drafts

Checks only things that are objectively true or false. Judgment belongs elsewhere.
The expensive failure this catches is a dead internal link: writers invent
plausible-looking slugs that were never published.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

BANNED_WORDS = [
    "game-changer", "game changer", "revolutionary", "robust", "leverage",
    "cutting-edge", "comprehensive", "click here", "read more",
    "in this post", "let's dive in", "the only platform", "seamless", "empower",
    "workflow optimization", "productivity hack",
]
BANNED_SHAPES = [
    "benefits of", "why it matters", "common mistakes", "conclusion", "final thoughts",
]
# Direct dock competitors. Allowed on compare/ pages, never in a listicle.
COMPETITORS = ["dockdoor", "ubar", "activedock", "dockfix", "extradock", "infynidock", "sidebar", "boringbar", "dockspark"]

TITLE_MAX, DESC_MIN, DESC_MAX = 60, 120, 160
WORDS_MIN, WORDS_MAX = 850, 2400


def resolvable() -> set[str]:
    """Every path that actually exists on disk.

    NOT the sitemap. Utility pages like about.html and terms.html are real and
    linked from every footer, but are deliberately absent from the sitemap. An
    earlier version of this check used the sitemap and failed all ten pages on
    their own footers, which is the checker being wrong, not the pages.
    """
    return {str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html") if "node_modules" not in str(p)}


def check(slug: str, exists: set[str], drafts: set[str]) -> list[str]:
    p = ROOT / "answers" / f"{slug}.html"
    if not p.exists():
        return [f"file missing: {p}"]
    s = p.read_text()
    text = re.sub(r"<[^>]+>", " ", s)
    fails = []

    title = re.search(r"<title>(.*?)</title>", s)
    if not title:
        fails.append("no <title>")
    elif len(title.group(1)) > TITLE_MAX:
        fails.append(f"title {len(title.group(1))} chars, max {TITLE_MAX}")
    if title and ":" in title.group(1):
        fails.append("colon in title (slug-unsafe)")

    desc = re.search(r'name="description" content="(.*?)"', s)
    if not desc:
        fails.append("no meta description")
    elif not (DESC_MIN <= len(desc.group(1)) <= DESC_MAX):
        fails.append(f"description {len(desc.group(1))} chars, want {DESC_MIN}-{DESC_MAX}")

    w = len(text.split())
    if not (WORDS_MIN <= w <= WORDS_MAX):
        fails.append(f"word count {w}, want {WORDS_MIN}-{WORDS_MAX}")

    if len(re.findall(r"<h1>", s)) != 1:
        fails.append(f"{len(re.findall(r'<h1>', s))} h1 tags, want exactly 1")

    if "—" in s or "–" in s:
        fails.append("em dash or en dash present")

    low = text.lower()
    for b in BANNED_WORDS:
        if b in low:
            fails.append(f"banned word: {b}")
    for h in re.findall(r"<h2>(.*?)</h2>", s, re.S):
        hl = re.sub(r"<[^>]+>", "", h).lower()
        for shape in BANNED_SHAPES:
            if hl.startswith(shape):
                fails.append(f"banned section shape: {hl}")

    # Competitor rule: not in listicles.
    if slug.startswith("best-") or "-apps-" in slug:
        for c in COMPETITORS:
            if c in low:
                fails.append(f"competitor named in a listicle: {c}")

    # Internal links must resolve, and must not point at unpublished pages.
    for href in re.findall(r'href="([^"#?]+\.html)"', s):
        if href.startswith("http"):
            continue
        # Resolve relative to answers/, where the page lives.
        target = os.path.normpath(os.path.join("answers", href))
        if target not in exists:
            fails.append(f"internal link does not resolve: {href}")
        elif target.replace("answers/", "").replace(".html", "") in drafts:
            fails.append(f"internal link points at an UNPUBLISHED page (would 404): {href}")

    try:
        g = json.loads(re.search(r'ld\+json">(.*?)</script>', s, re.S).group(1))["@graph"]
        if not any(n.get("@type") == "Person" for n in g):
            fails.append("no Person node in schema")
    except Exception:
        fails.append("JSON-LD missing or invalid")

    if 'class="authorbox"' not in s:
        fails.append("no author box")
    if 'rel="canonical"' not in s:
        fails.append("no canonical")

    return fails


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all-drafts", action="store_true")
    args = ap.parse_args()

    out = subprocess.run(["git", "status", "--short", "answers/"], cwd=ROOT, capture_output=True, text=True).stdout
    drafts = {re.sub(r".*answers/(.*)\.html", r"\1", l) for l in out.splitlines() if l.startswith("??") and l.endswith(".html")}
    slugs = sorted(drafts) if args.all_drafts else args.slugs
    if not slugs:
        print("nothing to check")
        return 0

    exists = resolvable()
    bad = 0
    for slug in slugs:
        fails = check(slug, exists, drafts)
        if fails:
            bad += 1
            print(f"FAIL  {slug}")
            for f in fails:
                print(f"        {f}")
        else:
            print(f"pass  {slug}")
    print(f"\n{len(slugs) - bad}/{len(slugs)} passed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
