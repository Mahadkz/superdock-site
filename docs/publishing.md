# How publishing works

## The two-stage model, and why it avoids 404s

A page exists in two states.

**Written.** The HTML sits in `answers/` and is committed. The URL returns 200,
but it appears in no sitemap, no index and no llms.txt, so nothing links to it
and search engines have no path to it. It is live but undiscoverable.

**Published.** `tools/publish.py` registers it in `sitemap.xml`,
`answers/index.html` and `llms.txt`. Only now can anything find it.

The ordering matters and is the point of the design: **a listing is only ever
added to a page that already works.** We never advertise a URL before it exists.

## The guard

`publish.py` runs `git ls-files` on each page before listing it. If the HTML is
not committed, it refuses and exits 1.

Without that check, listing an untracked page would point the sitemap at a URL
GitHub Pages has never seen, which is a real 404. The HTML must be pushed before,
or in the same push as, the listing that advertises it.

## The linking rule this enforces

**Every piece links only backwards.** Content ships on a schedule, so a link to
a piece due next week is a 404 until it arrives. Each new page links to
already-published pages only, and we never retrofit inbound links into live pages
ahead of a publication. Discovery comes from the sitemap, not from links planted
early.

Practical consequence: later pieces can link more richly, because more targets
exist by then.

## Running it

    tools/publish.py                 publish whatever today's date calls for
    tools/publish.py --day 2         publish a specific scheduled day
    tools/publish.py --dry-run       report changes, touch nothing

It exits 0 with "nothing due" when today has no entry, so a daily run is safe.
It is idempotent: re-running a published day reports "already published" and
changes nothing.

## The automation

`.github/workflows/publish-scheduled-content.yml` runs daily at 09:00 UTC. It:

1. checks out the repo,
2. runs `publish.py` for today,
3. validates the sitemap is well-formed XML and that no em dash has crept in,
   because an em dash violates house style and also trips Reddit's spam filters,
4. commits and pushes only if something changed.

It also has a manual trigger taking a `day` number and a `dry_run` toggle, for
catching up after a missed day or testing without consequence.

**The workflow needs `contents: write`**, which is declared in the file. If the
repository has stricter defaults, enable read and write for Actions under
Settings, Actions, General, Workflow permissions.

## The schedule

`tools/schedule.json` holds the dates, slugs, titles and index blurbs. To add a
day, append an entry. To move a piece, change its date. Nothing else needs
editing.
