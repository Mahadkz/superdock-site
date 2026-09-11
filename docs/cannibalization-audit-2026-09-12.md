# Cannibalization audit, the first ten pieces
Run 12 September 2026, retrospectively, against the LIVE sitemap (50 URLs).

This screen should have run BEFORE writing. It did not, and it found four real
problems in ten pieces. Recording the verdicts honestly rather than quietly
shipping them.

## Verdicts

| Piece | Overlaps with | Verdict | Reason |
|---|---|---|---|
| `cmd-tab-skips-minimized-windows` | `why-cmd-tab-does-not-show-minimized-windows-mac` | **FOLD** | Shares the literal H2 "The Option trick" and covers the same mechanism. The live page already owns this query. The new material (hidden versus minimized as distinct states) belongs as a section in the live page, not as a new URL |
| `why-chrome-profiles-share-one-dock-icon` | `separate-dock-icon-for-each-chrome-profile-mac` | **RESHAPE** | Live page already has "Why Apple's Dock merges Chrome profiles" and "The three ways to get one icon per profile". Real overlap, but the new page has a distinct asset: correcting the false "macOS removed this" claim. Scope to that |
| `shortcut-toggle-windows-same-app` | `switch-between-windows-same-app-mac` | **RESHAPE** | Live page covers the same shortcuts. The distinct angle is the identical-windows failure case, which the live page touches only in passing. Scope hard to that |
| `chrome-user-data-dir-what-it-costs` | `blog/chrome-profiles-vs-separate-instances` | **RESHAPE** | The live blog post already contains "How did we measure the memory figure?". The new page is the full methodology. Either fold the numbers in, or scope the new page to method only and have the blog link to it |
| `best-mac-apps-8gb-ram` | `best-dock-app-for-mac` | **WRITE** | Slug tokens overlap but intent is different. A memory-constrained utility list is not a dock app roundup |
| `best-mac-apps-under-10-dollars` | `best-dock-app-for-mac` | **WRITE** | Same. Price-defined list, different intent |
| `best-mac-apps-work-personal-accounts` | `best-dock-app-for-mac` | **WRITE** | Same |
| `why-clicking-dock-icon-brings-all-windows` | three live pages, loosely | **WRITE** | Token overlap only. No live page answers why a Dock click activates the whole app |
| `restore-minimized-window-shortcut` | `why-cmd-tab-does-not-show-minimized-windows-mac` | **RESHAPE** | Adjacent to the same live page as the FOLD above. Keep only if scoped to the how-to, with the why left to the live page |
| `add-spacers-between-dock-icons` | none | **WRITE** | Clean |

## Scoping rules that must survive into the pages

These are the Stage 2 rules that make a RESHAPE safe. They are binding.

**`why-chrome-profiles-share-one-dock-icon`**
> The live page `separate-dock-icon-for-each-chrome-profile-mac` owns "how do I
> get one icon per profile". Do NOT re-rank the workarounds as the page's spine.
> Lead with the correction of the false "macOS removed this" claim, which nothing
> else on the site covers, and link to the live page for the how-to.

**`shortcut-toggle-windows-same-app`**
> The live page `switch-between-windows-same-app-mac` owns the shortcut list.
> State Command-Backtick once, then spend the page on the identical-windows
> failure case. Link to the live page rather than restating its list.

**`chrome-user-data-dir-what-it-costs`**
> The live blog post already answers "How did we measure the memory figure?".
> This page is the full method and the two hidden costs. The blog post should
> link here for the method rather than both carrying the numbers.

**`restore-minimized-window-shortcut`**
> The live page owns "why Command-Tab ignores minimized windows". This page is
> the how-to only. One sentence on the why, then a link.

## Decisions taken

- **`cmd-tab-skips-minimized-windows` is pulled from the schedule.** It is a
  duplicate of a live page. Its one genuinely new idea, that hiding and
  minimizing are different states, is worth adding to the live page instead.
- The three RESHAPE pages ship with the scoping rules above applied.
- Day 4's small slot needs a replacement piece.

## What this cost

Four of ten pieces were written before screening. One is unusable, three needed
rework. Running Stage 2 first would have cost one script run.
