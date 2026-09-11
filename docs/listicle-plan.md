# Listicle plan

> **DRAFT, 12 September 2026.** Built from 12 measured SERPs. Four research
> agents are currently mapping the space properly: more listicle queries, page
> teardowns, alternative and versus pages, and problem-shaped queries. Expect
> this file to be substantially expanded and possibly reordered.

Written 12 September 2026 from measured SERPs. Companion to `content-clusters.md`.

## Why listicles are the easiest SEO we have

Every page ranking for "best mac apps" style queries is **a small app site, not a
publisher**. Verified across 8 SERP pulls. The winners are notes apps, notch
utilities, timers and sidebars ranking for terms far bigger than themselves.

| SERP | Who holds #1 | What they actually are |
|---|---|---|
| best mac apps 2026 | noticky.app | a sticky notes app |
| best mac apps (complete guide) | notchia.app | a notch utility (French language) |
| best mac apps for designers | supasidebar.com | a browser sidebar |
| best mac apps for remote workers | supasidebar.com | same |
| best mac apps for consultants | supasidebar.com | same |
| manage multiple google accounts | supasidebar.com | same |
| best free mac apps | getdroppy.app | a drag-and-drop shelf |
| best open source mac apps | snapzy.app | a screenshot tool |
| best mac apps for developers | usevoicy.com | a dictation app |
| best mac menu bar apps | timingapp.com | a time tracker |
| best freelance apps for mac | timingapp.com | same |
| best mac productivity picks | chronoid.app | a timer |

**supasidebar.com holds #1 on four of these.** One app, many audience-sliced
listicles, all pointing at the same product. That is the model to copy.

Two consequences:
1. The format is winnable by a two-week-old app site. It is being won by them now.
2. The moat is not domain authority. It is **one specific slot we can claim that
   the incumbents cannot**: browser profiles. Absent from every list found.

## The technique, reverse-engineered from notchia.app (#2 for "best mac apps 2026")

Two FAQ entries do all the work:
- "Is [app] among the best Mac apps to install in 2026?" answered by naming
  Raycast, Rectangle, CleanShot X, 1Password and Things 3, then claiming the one
  category those five leave empty.
- "What is the difference between [app], Raycast, Rectangle and CleanShot X?"
  answered with "these four are complementary, not competitors."

You rank for the big app names by being genuinely useful about them, then take the
empty slot. **Our empty slot is browser profiles.**

---

## Table 1. Listicles ranked by ease

Ease = (small app site holds #1) + (no publisher in top 3) + (we have a real slot).

| # | Slug | Target query | Who holds #1 now | Ease | Our slot in the list |
|---|---|---|---|---|---|
| 1 | `best-mac-apps-for-windows-switchers` | mac apps for windows users | Reddit thread | **Easiest** | The dock is the thing switchers miss most. We are the answer, not a footnote |
| 2 | `best-mac-utility-apps` | best mac utility apps | woorkup (blog) | **Easiest** | The category we literally belong to |
| 3 | `best-mac-apps-multiple-monitors` | mac apps for multiple monitors | mixed forums | **Easiest** | DisplayBuddy, Lunar, SwitchResX all do brightness. None puts a dock on every display |
| 4 | `best-mac-apps-multiple-google-accounts` | manage multiple google accounts mac | supasidebar | **Easy** | **Closest listicle to our paid feature.** A small app site already proved it ranks |
| 5 | `best-free-mac-apps` | best free mac apps | getdroppy | **Easy** | Our free tier is the whole pitch |
| 6 | `mac-apps-for-power-users` | mac power user apps | timingapp | **Easy** | Raycast, Hazel, BetterTouchTool recur. We fill the dock gap |
| 7 | `best-mac-apps-for-developers` | best mac apps for developers | usevoicy | Medium | Secondary Chrome instances, dev/staging/prod profiles |
| 8 | `best-mac-apps-for-freelancers` | best mac apps for freelancers | supasidebar | Medium | One profile per client. Timing owns the invoicing slot, not ours |
| 9 | `best-mac-menu-bar-apps` | best mac menu bar apps | timingapp | Medium | Weakest fit. We are a dock app, not a menu bar app. Only if we have something honest to say |
| 10 | `best-mac-apps-2026` | best mac apps 2026 | noticky | Hardest | The pillar. Write last, once the others link to it |

## Table 2. What goes in each list

Every listicle shares a spine of genuinely good apps. This is what makes the page
useful rather than an ad. Icons are already fetched in `assets/apps/`.

| App | Have icon | Category | Appears in |
|---|---|---|---|
| Raycast | yes | Launcher | 1, 2, 6, 7, 10 |
| Rectangle | yes | Window management | 1, 2, 3, 5, 6, 10 |
| AltTab | yes | Window switching | 1, 2, 5, 10 |
| Maccy | yes | Clipboard | 1, 2, 5, 6, 10 |
| Ice | yes | Menu bar | 2, 5, 9, 10 |
| LinearMouse | yes | Input | 1, 2, 3, 5 |
| DockDoor | yes | Dock previews | 1, 2, 3, 5 |
| Superdock | app icon | Dock + profiles | all |
| **Still to fetch** | | | |
| CleanShot X | no | Screenshots | 6, 7, 8, 10 |
| Hazel | no | Automation | 6, 10 |
| BetterTouchTool | no | Input | 6, 7 |
| Karabiner-Elements | no | Keyboard | 1, 6, 7 |
| IINA | no | Media | 5, 10 |
| Homebrew | no | Package manager | 7 |
| Bartender | no | Menu bar | 9 |
| iStat Menus | no | Monitoring | 6, 9 |

Add these to `tools/fetch-icons.mjs` before writing the pages that need them.

## Table 3. Per-page structure

Identical skeleton for every listicle, so they can be produced quickly and read
consistently.

| Section | Content | Words |
|---|---|---|
| TL;DR | The complete answer, naming the top 3 picks and who each is for | 60 |
| Bias disclosure | First person, first screen. "I build one of these, discount me accordingly" | 40 |
| Scope | What is covered and explicitly what is not | 40 |
| The apps | 8 to 12 entries, official icon, one-line verdict, honest limitation each | 900 to 1,400 |
| Comparison table | One table, after the entries, conditional verdict column | 150 |
| Where each wins | Reader-sorting: "if you only want X, get Y instead" | 200 |
| FAQ | Visible h3 questions. **No FAQPage schema**, retired May 2026 | 250 |
| Method footer | Date, what was tested, what was not | 40 |
| Author box | Byline linking to the profile page | existing |

Target 1,400 to 2,200 words. Measured range for pages beating publishers is
1,100 to 3,500, and Google disclaims any preferred count.

## Table 4. The honesty devices that make these rank

From six teardowns of sites outranking publishers. These are not optional garnish,
they are the mechanism.

| Device | Example found | Our version |
|---|---|---|
| Rank yourself last sometimes | Droppy ranks itself 4th of 4 on clipboard managers | In `best-mac-menu-bar-apps` we are not the best answer. Say so |
| Omit yourself entirely | Droppy is absent from its own free-apps listicle | **Write one listicle without Superdock in it.** That is the page others can link to |
| Give a rival an unqualified win | "The Boring Notch is the best free starting point for most people" | "If you only want window previews on Apple's Dock, DockDoor is free and open source. Install that instead" |
| Name your own bias as the reason a trial exists | "I would say that, which is exactly why the 3-day trial exists" | Ours is 14 days and the dock is free forever. Same move, stronger hand |
| Conditional verdicts | "#1 if you want X without switching browsers" | Never a bare "best". Always "best if" |

## Table 5. Internal linking

Each listicle links up to a pillar, sideways to two siblings, and down to the
specific answer page for any claim it makes.

| Listicle | Links up to | Sideways | Down to |
|---|---|---|---|
| windows-switchers | best-mac-apps | utility-apps, multiple-monitors | alt-tab-not-working, chrome-profiles-like-windows |
| utility-apps | best-mac-apps | power-users, free-mac-apps | free-mac-dock-alternative |
| multiple-monitors | best-mac-dock-apps | utility-apps, windows-switchers | dock-on-both-monitors, dock-keeps-moving |
| multiple-google-accounts | chrome-profiles-on-mac | freelancers, developers | separate-dock-icon-per-profile, user-data-dir-cost |
| free-mac-apps | best-mac-apps | utility-apps, power-users | free-mac-dock-replacement-no-subscription |
| power-users | best-mac-apps | utility-apps, developers | mac-app-switcher-with-thumbnails |
| developers | best-mac-apps | power-users, multiple-google-accounts | chrome-has-no-multi-account-containers |
| freelancers | keep-work-personal-separate | multiple-google-accounts | one-chrome-profile-per-client, wrong-client-tab |

## Table 6. Publishing order, one per day

Interleaved with the answer pages from `content-clusters.md` so the site does not
look like a listicle farm.

| Day | Piece | Type |
|---|---|---|
| 1 | why-chrome-profiles-share-one-dock-icon | answer |
| 2 | best-mac-apps-for-windows-switchers | listicle |
| 3 | chrome-user-data-dir-what-it-costs | answer |
| 4 | best-mac-utility-apps | listicle |
| 5 | wrong-client-tab-screen-share | answer |
| 6 | best-mac-apps-multiple-monitors | listicle |
| 7 | macos-never-supported-per-profile-dock-icons | answer |
| 8 | best-mac-apps-multiple-google-accounts | listicle |
| 9 | dock-keeps-moving-between-monitors | answer |
| 10 | best-free-mac-apps | listicle |
| 11 | browser-profiles-for-focus-adhd | answer |
| 12 | mac-apps-for-power-users | listicle |
| 13 | tell-which-chrome-profile-you-are-in | answer |
| 14 | best-mac-apps-for-developers | listicle |
| 15 | mac-dock-blurry-icons-tahoe | answer + screenshot |
| 16 | best-mac-apps-for-freelancers | listicle |
| 17 | chrome-has-no-multi-account-containers | answer |
| 18 | best-mac-apps-2026 | PILLAR |

## Caveats
- **No keyword volumes.** Ease is inferred from SERP composition, not measured
  demand. Worth validating in a keyword tool before committing to the order.
- The menu bar listicle is the weakest fit and may be worth dropping. We are a
  dock app; forcing our way into that list would break the honesty rule that makes
  the others work.
- supasidebar is running this exact playbook and ranking. Speed matters.
