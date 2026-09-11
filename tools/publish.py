#!/usr/bin/env python3
"""Publish a scheduled day's pages.

A page's HTML sits in answers/ from the moment it is written, but it is invisible
until this runs: it is absent from sitemap.xml, answers/index.html and llms.txt,
so nothing links to it and Google has no way to find it.

Publishing therefore means registering it in those three places.

  tools/publish.py            publish whatever today's date calls for
  tools/publish.py --day 2    publish a specific day
  tools/publish.py --dry-run  show what would change, touch nothing

Exits 0 with "nothing due" when today has no entry, so a daily cron or workflow
can run harmlessly every day.
"""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEDULE = ROOT / "tools" / "schedule.json"


def already_published(slug: str) -> bool:
    return f"answers/{slug}.html" in (ROOT / "sitemap.xml").read_text()


def is_committed(rel_path: str) -> bool:
    """True when git tracks this file.

    Listing an untracked page would point the sitemap at a URL GitHub Pages has
    never seen, which is a real 404. The HTML must be pushed before, or in the
    same push as, the listing that advertises it.
    """
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", rel_path],
        cwd=ROOT, capture_output=True, text=True,
    )
    return result.returncode == 0


def add_to_sitemap(slug: str, date: str, dry: bool) -> str:
    path = ROOT / "sitemap.xml"
    text = path.read_text()
    url = f"https://superdock.app/answers/{slug}.html"
    if url in text:
        return "already in sitemap"
    entry = f"<url><loc>{url}</loc><lastmod>{date}</lastmod></url>\n"
    if not dry:
        path.write_text(text.replace("</urlset>", entry + "</urlset>"))
    return "added to sitemap"


def add_to_index(slug: str, title: str, blurb: str, dry: bool) -> str:
    path = ROOT / "answers" / "index.html"
    text = path.read_text()
    if f'href="{slug}.html"' in text:
        return "already in index"
    item = (
        f'<li><img src="../assets/icon-96.png" width="28" height="28" alt="">'
        f'<div><a href="{slug}.html">{title}</a><p>{blurb}</p></div></li>'
    )
    cut = text.rfind("</li>") + len("</li>")
    if not dry:
        path.write_text(text[:cut] + item + text[cut:])
    return "added to answers index"


def add_to_llms(slug: str, title: str, dry: bool) -> str:
    path = ROOT / "llms.txt"
    text = path.read_text()
    url = f"https://superdock.app/answers/{slug}.html"
    if url in text:
        return "already in llms.txt"
    line = f"- [{title}]({url})\n"
    match = re.search(r"(## Answers\n\n)((?:- \[.*\n)+)", text)
    if match:
        text = text[: match.end(2)] + line + text[match.end(2) :]
    else:
        text = text.rstrip() + "\n" + line
    if not dry:
        path.write_text(text)
    return "added to llms.txt"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", type=int, help="publish this scheduled day rather than today's")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    schedule = json.loads(SCHEDULE.read_text())
    today = datetime.date.today().isoformat()

    if args.day:
        due = [d for d in schedule["days"] if d["day"] == args.day]
    else:
        due = [d for d in schedule["days"] if d["date"] == today]

    if not due:
        print(f"nothing due ({'day ' + str(args.day) if args.day else today})")
        return 0

    published = 0
    skipped = 0
    for entry in due:
        print(f"day {entry['day']}, {entry['date']}")
        for page in entry["pages"]:
            slug = page["slug"]
            html = ROOT / "answers" / f"{slug}.html"
            if not html.exists():
                print(f"  MISSING {slug}.html, skipping")
                continue
            if not is_committed(f"answers/{slug}.html"):
                print(f"  {slug}: NOT COMMITTED, refusing to list a page that is not live")
                skipped += 1
                continue
            if already_published(slug):
                print(f"  {slug}: already published")
                continue
            for note in (
                add_to_sitemap(slug, entry["date"], args.dry_run),
                add_to_index(slug, page["title"], page["blurb"], args.dry_run),
                add_to_llms(slug, page["title"], args.dry_run),
            ):
                print(f"  {slug}: {note}")
            published += 1

    print(("would publish " if args.dry_run else "published ") + f"{published} page(s)")
    if skipped:
        print(f"{skipped} page(s) skipped because their HTML is not committed yet")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
