# Blog production pipeline

Adapted 12 September 2026 from a spec that has been run in production on another
brand. The split that matters: **stages 2 and 8 are deterministic scripts,
everything else is judgment.** Do not let an agent do the counting, and do not
let a script do the thinking.

## What this fixes

Running the first ten pieces without this pipeline produced exactly the failures
it predicts. The cannibalization screen, run retrospectively, found **four of ten
had real overlap with live pages**, including one sharing a literal H2 with a
page that already ranks. See `cannibalization-audit-2026-09-12.md`.

## Stages

| # | Stage | Output | Who |
|---|---|---|---|
| 1 | Topic candidates | ranked list | human, from Search Console |
| 2 | **Cannibalization screen** | WRITE / RESHAPE / SKIP / FOLD | `tools/cannibalization-check.py` + human verdict |
| 3 | SERP teardown | competitor structure | script, not yet built |
| 4 | Research brief + checklist | binary checklist | agent |
| 5 | Fact verification | verified claims with sources | agent, primary sources only |
| 6 | Write | draft HTML | `tools/mkpage.py` |
| 7 | Judge | scored, corrected HTML | a DIFFERENT agent than the writer |
| 8 | **Mechanical QA** | pass/fail | `tools/qa.py` |
| 9 | Cover concept | 3 prompt variants | agent + human pick |
| 10 | Render + composite | branded image | image model |
| 11 | Final QA | ship or fix | human |

## Stage 2, the highest-value check

    tools/cannibalization-check.py <slug>...
    tools/cannibalization-check.py --all-drafts

Fetches the **live** sitemap, not a local copy, because a stale sitemap is a
silent failure. Compares slug tokens, then pulls the actual H2 set of any near
match, because a slug can look unrelated while the page already owns your angle
in a section.

It reports evidence. **A human assigns the verdict.**

| Verdict | Meaning |
|---|---|
| WRITE | No meaningful overlap |
| RESHAPE | Real overlap, distinct angle exists. Proceed ONLY with hard scoping rules |
| SKIP | Duplicate. Kill it |
| FOLD | The value belongs in an existing post. Update that page instead |

A RESHAPE verdict must carry scoping rules that survive into the writing. Those
rules are the difference between a page that ranks and one that splits authority
with a page you already own.

## Stage 8, mechanical QA

    tools/qa.py <slug>...
    tools/qa.py --all-drafts

Checks only what is objectively true or false: word count, title and description
length, one H1, no em dashes, banned words, banned section shapes, competitor
names in listicles, schema validity, author box, canonical, and every internal
link resolving.

**Check your checker.** The first version of this script failed all ten pages on
their own footer links, because it validated against the sitemap rather than the
filesystem. Utility pages like `about.html` are real but deliberately unlisted.
The second version failed them again because it did not resolve `../` relative to
`answers/`. Both times the pages were fine and the checker was wrong.

## Rules this project has learned

- **No em dashes anywhere**, including titles and meta descriptions. Also trips
  Reddit's spam filters.
- **Never name a direct dock competitor in a listicle.** They belong on
  comparison and alternative pages. Non-competing apps are praised freely.
- **Link only backwards**, to pages already published. Content ships on a
  schedule, so a link to next week's piece is a 404 today.
- **Never invent a statistic.** The 2.8x memory figure is ours, measured, and the
  method is published. Anything unverifiable is omitted rather than hedged.
- **Cover images illustrate the reader's task, not a noun from the headline.**

## Not yet built

- **Stage 3, SERP teardown.** The research advantage. Would scrape the top ~30
  results per topic and count heading frequency, word count medians and table
  counts, so the writer is told what the battleground actually is.
- **Stage 5, fact verification as a gate.** Currently done ad hoc. It caught the
  false "macOS removed per-profile Dock icons" claim only because two agents
  independently checked it.
- **Stage 7, a separate judge agent.** Currently the writer self-checks, which
  the spec says does not work.
