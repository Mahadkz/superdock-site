#!/usr/bin/env python3
"""Query the TinyFish API directly, rotating across every configured key.

Subagents inherit the MCP servers the parent session loaded at startup, so keys
registered mid-session are invisible to them and every agent shares one 30/min
budget. This bypasses MCP and talks to the endpoint directly, which makes all
ten keys usable and gives roughly 300 requests a minute.

  tools/fanout.py queries.txt --out research/raw/serps.json
"""
import argparse
import concurrent.futures as cf
import hashlib
import json
import pathlib
import re
import sys
import threading
import time
import urllib.request

MCP = "https://agent.tinyfish.ai/mcp"
_sessions: dict[str, str] = {}
_lock = threading.Lock()
_last: dict[str, float] = {}


def keys() -> list[str]:
    cfg = json.loads((pathlib.Path.home() / ".claude.json").read_text())
    return [v["headers"]["X-API-Key"] for k, v in cfg.get("mcpServers", {}).items()
            if "tinyfish" in k and v.get("headers", {}).get("X-API-Key")]


def session(key: str) -> str:
    with _lock:
        if key in _sessions:
            return _sessions[key]
    body = json.dumps({"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {
        "protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "fanout", "version": "1"}}}).encode()
    req = urllib.request.Request(MCP, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
        "X-API-Key": key})
    with urllib.request.urlopen(req, timeout=60) as r:
        sid = r.headers.get("Mcp-Session-Id", "")
        r.read()
    with _lock:
        _sessions[key] = sid
    return sid


def throttle(key: str, min_gap: float = 2.1) -> None:
    """Keep each key under 30 requests a minute."""
    with _lock:
        gap = time.time() - _last.get(key, 0)
        if gap < min_gap:
            time.sleep(min_gap - gap)
        _last[key] = time.time()


def search(query: str, key: str) -> dict:
    throttle(key)
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {
        "name": "search", "arguments": {"query": query, "location": "US"}}}).encode()
    req = urllib.request.Request(MCP, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
        "X-API-Key": key, "Mcp-Session-Id": session(key)})
    with urllib.request.urlopen(req, timeout=120) as r:
        raw = r.read().decode()
    for line in raw.splitlines():
        if line.startswith("data: "):
            raw = line[6:]
            break
    for c in json.loads(raw).get("result", {}).get("content", []):
        if c.get("type") == "text":
            try:
                return json.loads(c["text"])
            except ValueError:
                return {}
    return {}


def classify(results: list[dict]) -> str:
    doms = [re.sub(r"^https?://(www\.)?([^/]+).*", r"\2", r.get("url", "")) for r in results[:3]]
    if not doms:
        return "none"
    if all(any(f in d for f in ("reddit", "discussions.apple", "stackexchange", "superuser", "quora", "forums.")) for d in doms):
        return "forum-only"
    if any("reddit" in d or "discussions.apple" in d for d in doms):
        return "forum-mixed"
    if any(p in " ".join(doms) for p in ("pcmag", "zapier", "techradar", "cnet", "tomsguide", "makeuseof", "lifehacker", "digitaltrends")):
        return "publisher"
    return "small-site"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("queries")
    ap.add_argument("--out", default="research/raw/serps.json")
    args = ap.parse_args()

    ks = keys()
    qs = [q.strip() for q in pathlib.Path(args.queries).read_text().splitlines() if q.strip() and not q.startswith("#")]
    print(f"{len(qs)} queries across {len(ks)} keys")

    out = {}

    def run(q: str) -> tuple[str, dict]:
        key = ks[int(hashlib.sha1(q.encode()).hexdigest(), 16) % len(ks)]
        try:
            res = search(q, key)
            items = res.get("results", [])
            return q, {"holder": classify(items),
                       "top3": [r.get("url", "") for r in items[:3]],
                       "count": len(items)}
        except Exception as e:
            return q, {"error": str(e)[:80]}

    with cf.ThreadPoolExecutor(max_workers=len(ks)) as ex:
        for i, (q, data) in enumerate(ex.map(run, qs), 1):
            out[q] = data
            tag = data.get("holder", data.get("error", "?"))
            print(f"  [{i}/{len(qs)}] {tag:<12} {q[:60]}")

    p = pathlib.Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2))
    forum = sum(1 for v in out.values() if v.get("holder") == "forum-only")
    print(f"\nwrote {p}")
    print(f"  forum-only SERPs (cheapest wins): {forum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
