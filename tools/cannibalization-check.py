#!/usr/bin/env python3
"""Stage 2: screen candidate topics against the LIVE sitemap.

The single most valuable check in the pipeline. Skipping it means competing
against yourself, and the damage is invisible until rankings split.

  tools/cannibalization-check.py <slug> [<slug>...]
  tools/cannibalization-check.py --all-drafts

Fetches the live sitemap (not a local copy, which goes stale), pulls the actual
H2 set of any near match, and reports the overlap. A slug can look unrelated
while the page already owns your angle in a section, so slug comparison alone
is not enough.

Verdicts are for a human to assign. This reports evidence, it does not decide.
"""
import argparse
import pathlib
import re
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITEMAP_URL = "https://superdock.app/sitemap.xml"
STOP = {"the", "a", "an", "on", "in", "for", "to", "of", "and", "is", "it", "mac", "macos", "how", "why", "does", "do", "with", "your", "my"}


def live_urls() -> list[str]:
    with urllib.request.urlopen(SITEMAP_URL) as r:
        xml = r.read().decode()
    return re.findall(r"<loc>https://superdock\.app/(.*?)</loc>", xml)


def tokens(slug: str) -> set[str]:
    return {t for t in slug.split("-") if t not in STOP and len(t) > 2}


def headings(path: pathlib.Path) -> list[str]:
    if not path.exists():
        return []
    return [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<h2>.*?</h2>", path.read_text(), re.S)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all-drafts", action="store_true", help="check every uncommitted answers page")
    args = ap.parse_args()

    slugs = args.slugs
    if args.all_drafts:
        out = subprocess.run(["git", "status", "--short", "answers/"], cwd=ROOT, capture_output=True, text=True).stdout
        slugs = [re.sub(r".*answers/(.*)\.html", r"\1", l) for l in out.splitlines() if l.startswith("??") and l.endswith(".html")]
    if not slugs:
        print("nothing to check")
        return 0

    urls = live_urls()
    print(f"live sitemap: {len(urls)} urls\n")
    risky = 0

    for slug in slugs:
        mine = tokens(slug)
        my_h2 = {h.lower() for h in headings(ROOT / "answers" / f"{slug}.html")}
        hits = []
        for u in urls:
            other = re.sub(r"^(answers|blog|compare)/", "", u).replace(".html", "")
            if other == slug:
                continue
            shared = mine & tokens(other)
            if len(shared) < 2:
                continue
            their_h2 = {h.lower() for h in headings(ROOT / u)}
            same = my_h2 & their_h2 - {"frequently asked questions", "continue reading"}
            hits.append((u, sorted(shared), sorted(same)))

        if not hits:
            print(f"CLEAN    {slug}")
            continue

        risky += 1
        print(f"OVERLAP  {slug}")
        for u, shared, same in hits:
            print(f"           {u}")
            print(f"             shared slug terms: {', '.join(shared)}")
            if same:
                print(f"             IDENTICAL H2s: {', '.join(same)}   <-- likely SKIP or FOLD")
        print()

    print(f"\n{risky} of {len(slugs)} need a human verdict: WRITE / RESHAPE / SKIP / FOLD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
