#!/usr/bin/env python3
"""Stage 3: SERP teardown. Scrape and count. No agent.

This is the stage where agents burn context parsing HTML for no benefit, and
the stage that tells a writer what the battleground actually is. Without it you
guess at word counts and heading coverage.

  tools/serp-teardown.py "best mac apps for 8gb ram" --slug best-mac-apps-8gb-ram
  tools/serp-teardown.py --from-schedule          # every scheduled slug

Writes one JSON per topic to research/teardown/<slug>.json containing:
  - median and range of competitor word counts
  - table count across the corpus
  - heading phrases used by 3+ distinct pages (table stakes)
  - heading phrases used by exactly 1 page (possible gaps)
  - whether any primary source ranks
  - per-1000-word rate for the top terms

Rotates across the TinyFish keys in ~/.claude.json by topic hash, so a parallel
batch does not hammer one key.
"""
import argparse
import collections
import hashlib
import json
import os
import pathlib
import re
import statistics
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "research" / "teardown"
MCP = "https://agent.tinyfish.ai/mcp"

STOP = set("""a an the and or but if then than that this these those is are was were be been being of in on at to for
with from by as it its it's you your we our they their he she his her i me my not no do does did doing have has had
what which who whom when where why how all any both each few more most other some such only own same so too very can
will just should now about into over under again further once here there because while during before after above below
up down out off between against through
""".split())

PRIMARY = ("apple.com", "developer.apple.com", "support.apple.com", "chromium.org",
           "google.com/support", "support.google.com", "mozilla.org", "w3.org")


def keys() -> list[str]:
    cfg = json.loads((pathlib.Path.home() / ".claude.json").read_text())
    return [v.get("headers", {}).get("X-API-Key") for k, v in cfg.get("mcpServers", {}).items()
            if "tinyfish" in k and v.get("headers", {}).get("X-API-Key")]


_SESSIONS: dict[str, str] = {}


def session(key: str) -> str:
    """MCP requires an initialize handshake before any tools/call.

    Without the Mcp-Session-Id this returns 400, which is the error you get if
    you assume a plain JSON-RPC endpoint.
    """
    if key in _SESSIONS:
        return _SESSIONS[key]
    body = json.dumps({"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {
        "protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "serp-teardown", "version": "1"}}}).encode()
    req = urllib.request.Request(MCP, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
        "X-API-Key": key})
    with urllib.request.urlopen(req, timeout=60) as r:
        sid = r.headers.get("Mcp-Session-Id", "")
        r.read()
    _SESSIONS[key] = sid
    return sid


def call(tool: str, args: dict, key: str) -> dict:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": tool, "arguments": args}}).encode()
    req = urllib.request.Request(MCP, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
        "X-API-Key": key, "Mcp-Session-Id": session(key)})
    with urllib.request.urlopen(req, timeout=180) as r:
        raw = r.read().decode()
    # the endpoint may answer as SSE
    for line in raw.splitlines():
        if line.startswith("data: "):
            raw = line[6:]
            break
    payload = json.loads(raw)
    content = payload.get("result", {}).get("content", [])
    for c in content:
        if c.get("type") == "text":
            try:
                return json.loads(c["text"])
            except ValueError:
                return {"text": c["text"]}
    return {}


def ngrams(words: list[str], n: int) -> collections.Counter:
    return collections.Counter(" ".join(words[i:i + n]) for i in range(len(words) - n + 1))


def teardown(query: str, slug: str, key: str, variants: list[str]) -> dict:
    urls, seen_domain = [], set()
    for q in variants:
        res = call("search", {"query": q, "location": "US"}, key)
        for r in res.get("results", []):
            u = r.get("url", "")
            dom = re.sub(r"^https?://(www\.)?([^/]+).*", r"\2", u)
            if not u.startswith("http") or dom in seen_domain:
                continue
            if any(b in dom for b in ("youtube", "reddit", "facebook", "instagram", "linkedin", "indeed", "superdock.app")):
                continue
            seen_domain.add(dom)
            urls.append(u)
    urls = urls[:20]
    if not urls:
        return {"slug": slug, "query": query, "error": "no results"}

    pages = []
    for batch in [urls[i:i + 5] for i in range(0, len(urls), 5)]:
        res = call("fetch_content", {"urls": batch, "format": "markdown",
                                     "links": False, "image_links": False, "page_metadata": False}, key)
        for p in res.get("results", []):
            text = p.get("text", "")
            if len(text.split()) < 150:
                continue
            heads = re.findall(r"^#{2,3}\s+(.+)$", text, re.M)
            pages.append({
                "url": p.get("final_url", p.get("url", "")),
                "words": len(text.split()),
                "headings": [h.strip() for h in heads],
                "tables": text.count("\n|"),
                "primary": any(s in p.get("final_url", "") for s in PRIMARY),
                "text": text,
            })

    if not pages:
        return {"slug": slug, "query": query, "error": "no pages fetched"}

    counts = [p["words"] for p in pages]
    head_pages = collections.Counter()
    for p in pages:
        for h in {h.lower() for h in p["headings"]}:
            head_pages[h] += 1

    # Count per page, then keep only terms appearing on 3+ DISTINCT pages.
    # A single site's chrome (nav, widgets, its own brand name) can otherwise
    # dominate the corpus and send the writer chasing a word nobody else uses.
    per_page, doc_freq = [], collections.Counter()
    for p in pages:
        w = [x for x in re.findall(r"[a-z][a-z'-]{2,}", p["text"].lower()) if x not in STOP]
        per_page.append(w)
        seen = set()
        for n in (1, 2, 3):
            seen |= set(ngrams(w, n))
        for t in seen:
            doc_freq[t] += 1
    total = max(sum(len(w) for w in per_page), 1)
    combined = collections.Counter()
    for w in per_page:
        for n in (1, 2, 3):
            combined += ngrams(w, n)
    terms = {t: round(c / total * 1000, 2)
             for t, c in combined.most_common(400)
             if doc_freq[t] >= 3 and c >= 5}

    return {
        "slug": slug,
        "query": query,
        "variants": variants,
        "pages_analysed": len(pages),
        "word_count": {"median": int(statistics.median(counts)), "min": min(counts), "max": max(counts)},
        "tables_total": sum(p["tables"] for p in pages),
        "pages_with_tables": sum(1 for p in pages if p["tables"] > 2),
        "primary_sources_ranking": sum(1 for p in pages if p["primary"]),
        "table_stakes_headings": [h for h, c in head_pages.most_common() if c >= 3][:15],
        "possible_gaps": [h for h, c in head_pages.items() if c == 1][:20],
        "term_rate_per_1000": dict(sorted(terms.items(), key=lambda x: -x[1])[:30]),
        "sources": [{"url": p["url"], "words": p["words"], "headings": len(p["headings"])} for p in pages],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?")
    ap.add_argument("--slug")
    ap.add_argument("--from-schedule", action="store_true")
    args = ap.parse_args()

    ks = keys()
    if not ks:
        print("no tinyfish keys found in ~/.claude.json", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)

    jobs = []
    if args.from_schedule:
        sched = json.loads((ROOT / "tools" / "schedule.json").read_text())
        for d in sched["days"]:
            for p in d["pages"]:
                jobs.append((p["title"], p["slug"]))
    elif args.query:
        jobs.append((args.query, args.slug or re.sub(r"[^a-z0-9]+", "-", args.query.lower()).strip("-")))
    else:
        ap.error("give a query or --from-schedule")

    for query, slug in jobs:
        key = ks[int(hashlib.sha1(slug.encode()).hexdigest(), 16) % len(ks)]
        variants = [query, f"{query} 2026", f"best {query}" if not query.lower().startswith("best") else query]
        variants = list(dict.fromkeys(variants))[:3]
        print(f"tearing down: {slug}")
        try:
            data = teardown(query, slug, key, variants)
        except Exception as e:
            print(f"  FAILED: {e}")
            continue
        if "error" in data:
            print(f"  {data['error']}")
            continue
        (OUT / f"{slug}.json").write_text(json.dumps(data, indent=2))
        wc = data["word_count"]
        print(f"  {data['pages_analysed']} pages | median {wc['median']}w (range {wc['min']}-{wc['max']}) "
              f"| {data['pages_with_tables']} with tables | {data['primary_sources_ranking']} primary sources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
