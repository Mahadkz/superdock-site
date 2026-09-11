#!/usr/bin/env python3
"""Assemble agent research rows into one deduplicated content plan CSV.

Agents return pipe-separated rows. This normalises them, drops duplicates by
slug, screens every row against the live sitemap for cannibalization, and writes
research/content-plan.csv.

  tools/build-content-plan.py research/raw/*.txt
"""
import argparse
import csv
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "research" / "content-plan.csv"

COLUMNS = ["slug", "title", "target_query", "intent", "page_type", "serp_holder",
           "displaceable", "our_angle", "priority", "territory", "cannibalization", "status"]

STOP = {"the","a","an","on","in","for","to","of","and","is","it","mac","macos","how","why","does","do","with","your","my","best"}


def live_slugs() -> set[str]:
    try:
        with urllib.request.urlopen("https://superdock.app/sitemap.xml", timeout=30) as r:
            xml = r.read().decode()
    except Exception:
        xml = (ROOT / "sitemap.xml").read_text()
    return {re.sub(r"^(answers|blog|compare)/", "", u).replace(".html", "")
            for u in re.findall(r"<loc>https://superdock\.app/(.*?)</loc>", xml)}


def tokens(slug: str) -> set[str]:
    return {t for t in slug.split("-") if t not in STOP and len(t) > 2}


def parse(path: pathlib.Path) -> list[dict]:
    territory = path.stem
    rows = []
    for line in path.read_text().splitlines():
        if line.count("|") < 5 or line.strip().startswith(("#", "slug |", "slug|", "---")):
            continue
        parts = [p.strip() for p in line.split("|")]
        slug = re.sub(r"[^a-z0-9-]", "", parts[0].lower().replace(" ", "-"))
        if not slug or len(slug) < 5:
            continue
        row = {c: "" for c in COLUMNS}
        row["slug"] = slug
        row["territory"] = territory
        # field order varies by agent, so map by position with sane fallbacks
        keys = ["title", "target_query", "intent", "serp_holder", "displaceable", "our_angle", "page_type", "priority"]
        for i, k in enumerate(keys, start=1):
            if i < len(parts):
                row[k] = parts[i]
        m = re.search(r"\b([1-5])\b", parts[-1])
        row["priority"] = m.group(1) if m else "3"
        rows.append(row)
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()

    live = live_slugs()
    seen, out = {}, []
    for f in args.files:
        for row in parse(pathlib.Path(f)):
            if row["slug"] in seen:
                seen[row["slug"]]["territory"] += f"+{row['territory']}"
                continue
            t = tokens(row["slug"])
            clash = [s for s in live if len(t & tokens(s)) >= 2]
            row["cannibalization"] = f"CHECK: {clash[0]}" if clash else "clean"
            row["status"] = "planned"
            seen[row["slug"]] = row
            out.append(row)

    out.sort(key=lambda r: (r["priority"], r["territory"]))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(out)

    print(f"{len(out)} unique rows -> {OUT}")
    print(f"  needing a cannibalization verdict: {sum(1 for r in out if r['cannibalization'] != 'clean')}")
    print(f"  with no honest angle (NONE): {sum(1 for r in out if r['our_angle'].upper().startswith('NONE'))}")
    for p in "12345":
        n = sum(1 for r in out if r["priority"] == p)
        if n:
            print(f"  priority {p}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
