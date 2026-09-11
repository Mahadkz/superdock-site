# Content clusters
Rewritten 12 September 2026 from the research in `research-2026-09-11.md`,
`research-2026-09-12-deep.md` and `research-2026-09-12-verticals.md`.
Supersedes the earlier version of this file and `content-queue.md`.

## The one decision that shapes everything

Four separate vertical studies (agencies, developers, enterprise, focus) each
concluded the same thing independently: **they all converge on the same core
queries about Chrome profiles and the macOS Dock.** Developers do not search in
QA language. Agencies do not search for "Dock icon". Enterprise users search as
individuals, not as enterprises.

So this is **not** four parallel clusters. It is a small number of clusters where
the verticals appear as persona-specific spokes and as the voice of the writing.

Two verticals were dropped on evidence and should not be revisited without new
data: **students** (pain not felt, Setapp owns the SERP and the discount play, a
discount on $7.99 is worth $1.60) and **privacy** (the informed position is that
profiles are useless against fingerprinting, and that audience is leaving Chrome).

## Rules for every page

1. Answer completely in the first ~60 words. Label it TL;DR on listicles.
2. 1,200 to 2,500 words. Pages beating publishers measure 1,100 to 3,500.
3. Byline linking to `/author/mahad-kazmi.html`. Author box at the end.
4. Disclose bias in the first screen, first person, and invite the reader to
   discount it.
5. Give at least one rival a genuine unqualified win. Recommend a free competitor
   where it is honestly the better choice.
6. One comparison table, after the entries, with a conditional verdict column
   ("#1 if you want X"), never bare checkmarks.
7. Date and source the method in a footer.
8. Write in their vocabulary, never ours. See the glossary at the end.
9. No em dashes anywhere, including titles and meta descriptions.
10. **Never promise faster switching.** For ADHD readers friction is the feature.
    Promise knowing where you are.
11. Do NOT add FAQPage JSON-LD. Google retired the rich result in May 2026 and
    deleted the docs in June. Keep visible FAQ sections.

---

# Cluster A. Chrome profiles and the Dock (the core, and the only one that
# describes our actual mechanism)

**Why this is first.** The SERP is a graveyard: a 2012 Apple StackExchange
question, a 2015 shell script, and Reddit threads whose answers are "No" repeated
four times. Fourteen years of unresolved demand and **no commercial page owns it.**
We already rank on a variant.

**Pillar:** `/chrome-profiles-on-mac/` targeting the head terms.

**Published already (4):** separate-dock-icon-for-each-chrome-profile-mac,
chrome-profiles-on-mac-like-windows, chrome-profiles-vs-separate-instances,
chrome-profile-dock-icons-mac.

**To write, in order:**

| Slug | Target | Why it wins |
|---|---|---|
| `why-chrome-profiles-share-one-dock-icon` | "chrome profiles grouping together in dock" | The mechanism page. Google's own forum says "the Dock groups by application, not by profile". Compare all four workarounds honestly, including Safari Shortcuts which genuinely works and is free. |
| `macos-never-supported-per-profile-dock-icons` | "macos removed separate dock icons" | **Corrects a false claim we nearly published.** No Chromium bug, no Apple doc supports "removed". The truth is better: Chrome's "Add desktop shortcut" is a Windows and Linux feature that never existed on macOS. "Never supported" explains why the gap is durable. |
| `chrome-user-data-dir-what-it-costs` | "run multiple chrome instances mac" | Our measured benchmark: 1.67 GB across 11 processes becomes 4.6 GB across 33. **Nobody has published this.** Unbundle's own FAQ concedes "about 500MB per profile". Demotes every competitor at once. |
| `tell-which-chrome-profile-you-are-in` | "how to tell which chrome profile i'm in" | Weak incumbents. A user already described our feature from the demand side: "the only way I can tell at a glance which profile I'm in... obvious even in peripheral vision". |
| `chrome-has-no-multi-account-containers` | "chrome multi account container equivalent" | Reaches developers in **their own vocabulary**. Google's support forum says Chrome has no equivalent "yet". Every current answer is "you can't". |
| `switch-chrome-profiles-keyboard-shortcut-mac` | "switch chrome profiles hotkey mac" | Confirmed 2026: no View menu item, no assignable shortcut, no chrome:// flag. Honest answer, then the Dock as the alternative path. |

---

# Cluster B. Context separation and focus (the persona cluster)

**Why.** Twelve years of consistent evidence, 2014 to 2026, and it maps directly
onto the paid feature. Incumbents are thin SEO blogs, not Setapp.

**Pillar:** `/keep-work-and-personal-separate-on-mac/`, a recurring r/MacOS and
r/mac question with no canonical answer.

| Slug | Target | Anchor |
|---|---|---|
| `browser-profiles-for-focus-adhd` | "browser profiles for adhd focus" | "Out of sight, out of mind." **Must address the objection that easier switching invites goofing off.** Answering it honestly is what earns this audience. |
| `wrong-client-tab-screen-share` | "avoid showing wrong tab screen share" | The strongest emotional hook found. The r/ProductivityApps title already contains "the 'wrong client tab' panic". A tiny app site already ranks here, proving it is winnable. |
| `one-chrome-profile-per-client` | "chrome profiles for multiple clients" | Agency and freelancer persona. Their own stated downside, "multiple browser windows and it can feel a bit heavy... not elegant but it works", is the setup for our fix. |
| `you-dont-need-an-antidetect-browser` | "multilogin alternative" | The wedge into high-volume territory. Be scrupulous: if you need fingerprint isolation to avoid bans, you DO need Multilogin. If you just need to not mix clients up, you are paying $10 a month for the wrong tool. |
| `work-personal-chrome-on-a-work-macbook` | "separate work and personal browser work macbook" | The Windows-refugee frame, which is the most consistent phrasing across five years and four browsers. |

---

# Cluster C. The Dock itself (where we are already ranking)

**Why.** Our best non-brand positions, 7 to 11, are here. The apps ranking for
multi-monitor queries (DisplayBuddy, Lunar, SwitchResX, Stay) all solve
brightness and window position. **None puts a dock on every display.** That slot
is uncontested and we already built it.

**Pillar:** `/best-mac-dock-apps/`. We have 12 comparison pages and no hub, which
is the format Google rewards.

**Published (6):** best-dock-app-for-mac, free-mac-dock-alternative,
free-mac-dock-replacement-no-subscription, dock-on-both-monitors-mac,
dock-not-showing-on-second-monitor-mac, dock-on-every-monitor-mac.

| Slug | Target | Why |
|---|---|---|
| `dock-keeps-moving-between-monitors` | "mac dock keeps jumping to other monitor" | 12+ months of threads. The ExtraDock developer names this as one of only four categories of dock user. We do not fix it, it ceases to exist. Includes the vertically-stacked-monitor case a rival says is "still under development". |
| `hide-apps-from-dock-when-not-running` | "dim dock icons apps not running" | **Tied to the feature worth shipping.** Write after the feature lands. Asked for by people already paying for rival dock apps. |
| `organise-cluttered-mac-dock` | "mac dock cluttered too many icons" | The r/macapps asker explicitly wants "a free option first", which is exactly our free tier. |
| `mac-dock-blurry-icons-tahoe` | "tahoe dock icons blurry" | Unfixed across 26.2, 26.3, 26.4.1, 26.5.1. Chrome named as the worst-affected icon. **Ship the side-by-side screenshot with it.** |

---

# Cluster D. Window switching and alt-tab (already strong, finish it)

**Why.** How-To Geek and Yahoo list "Alt+Tab for windows, not just apps" as a
headline missing Windows feature, July 2026. Our positions of 44 to 69 on a
two-week-old domain mean unranked, not beaten.

**Pillar:** `/alt-tab-for-mac/`.

**Published (5):** alt-tab-between-windows-on-mac, alt-tab-not-working-on-mac,
mac-app-switcher-with-thumbnails, switch-between-windows-same-app-mac,
why-cmd-tab-does-not-show-minimized-windows-mac, plus the alt-tab blog post.

| Slug | Target |
|---|---|
| `best-mac-window-management-apps` | "best mac window manager" (Rectangle and Magnet adjacency) |
| `alt-tab-does-not-fix-chrome-profiles` | Targets the most common bad advice. The proof case is four Azure profiles with identical window titles, where a switcher cannot help. |

---

# Cluster E. Best Mac apps (the reusable asset)

**Why.** Every page ranking for these terms is a small app site, not a publisher:
noticky, notchia, chronoid, getdroppy, snapzy, usevoicy. This is the most winnable
format and the pillar URL is the one we update forever as more apps ship.

**Pillar:** `/best-mac-apps/`, updated in place, never re-spawned at a new URL.

| Slug | Target |
|---|---|
| `best-mac-utility-apps` | "best mac utility apps". The category we actually belong to. |
| `mac-apps-for-power-users` | "mac power user apps" |
| `best-mac-apps-for-windows-switchers` | Our highest-intent audience |
| `best-free-mac-apps` | Our free positioning |
| `best-mac-apps-for-developers` | Secondary Chrome instances angle |
| `best-mac-apps-multiple-monitors` | Extends cluster C, uncontested slot |

Technique, from the site ranking #2 for "best Mac apps 2026": be genuinely useful
about Raycast and Rectangle, then claim the one category they leave empty. Ours
is browser profiles, absent from every list found.

**Write one listicle where Superdock is NOT in the list**, or appears only in a
coda. That is the page third parties can link to without it reading as an ad.

---

# Cluster F. Trust and objection handling (small, defensive, high conversion)

Not an SEO play. These remove purchase blockers.

| Slug | Purpose |
|---|---|
| `is-it-safe-to-grant-accessibility` | We ask for the most invasive permission on macOS from an unknown developer. Explain exactly why (without it the window registry is empty, so no lists, previews or profile tiles), what we never do, and give a test the reader can run. |
| `managed-mac-mdm-questions` | One page, not a cluster. Serves real anxiety ("Can my employer read my personal mail?"). Enterprise is not a buyer; the IT admin is a permission granter to route around. |
| `how-the-licence-works` | 5 Macs, offline verification, fails open on network errors. This answers the loudest objection in the category and is currently invisible. |

---

# Deliberately NOT building

- **Students.** Setapp owns the content and the discount play; the pain is not felt.
- **Privacy and anti-fingerprinting.** Technically contested premise, audience leaving Chrome.
- **Volume licensing and IT procurement.** Zero demand signal for a sub-$10 utility.
- **The DevTools and MCP secondary-instance angle.** Genuinely unique, **zero
  demonstrated demand.** Five searches found nobody complaining. Ship it as a demo
  screenshot inside another post. Unique does not mean wanted.
- **More alt-tab content beyond cluster D.** We have enough; finish, do not expand.
- **uBar abandonment content.** Development resumed in 2025. That wedge closed.

---

# Publishing order

Pillars publish once enough spokes point at them.

1. `why-chrome-profiles-share-one-dock-icon` (A) the money page, weakest SERP
2. `chrome-user-data-dir-what-it-costs` (A) our unique benchmark
3. `wrong-client-tab-screen-share` (B) strongest emotional hook
4. `macos-never-supported-per-profile-dock-icons` (A) corrects the record
5. `dock-keeps-moving-between-monitors` (C) built, unclaimed, 12 months of demand
6. `browser-profiles-for-focus-adhd` (B)
7. `best-mac-apps-for-windows-switchers` (E) our audience, proven format
8. `tell-which-chrome-profile-you-are-in` (A)
9. `mac-dock-blurry-icons-tahoe` (C) with the screenshot
10. `best-mac-utility-apps` (E) the category we belong to
11. `chrome-has-no-multi-account-containers` (A) developer vocabulary
12. `one-chrome-profile-per-client` (B)
13. `/chrome-profiles-on-mac/` PILLAR (A)
14. `is-it-safe-to-grant-accessibility` (F)
15. `/best-mac-dock-apps/` PILLAR (C)
16. `you-dont-need-an-antidetect-browser` (B)
17. `best-mac-apps-2026` PILLAR (E)
18. `organise-cluttered-mac-dock` (C)
19. `switch-chrome-profiles-keyboard-shortcut-mac` (A)
20. `/keep-work-and-personal-separate-on-mac/` PILLAR (B)

Gated on work outside content:
- `hide-apps-from-dock-when-not-running` waits for the feature.
- Any Edge page waits on verifying Edge window-title attribution.

---

# Glossary: write in their words

**The problem:** "collapse into a single Chrome icon", "grouping together in the
dock", "all windows are combined into the same Chrome icon", "one big useless
chrome blob", "hidden behind a single app icon", "the Dock groups by application,
not by window".

**The cost:** "hunting", "the hunt continues", "so damn frustrating and slow",
"the wrong client tab panic", "I live in terror of accidentally posting",
"piss me off every day, all day", "confusing".

**The workarounds:** "hacky workaround", "jank", "same graphic", "not elegant but
it works", "good enough for me I guess", "you have to live with it".

**Focus:** "out of sight, out of mind", "firewall myself from", "goofoff profile",
"at a glance", "peripheral vision".

**Never use:** productivity, workflow optimization, context switching, seamless,
leverage, empower.

---

# How this expanded from the original 14-item queue

The first plan (`content-queue.md`, now superseded) was a flat list of 14 topics.
The research changed it in five specific ways.

## 1. Flat list became six clusters with pillars

A list does not build authority. Every small app site that outranks publishers in
this niche runs the same three-tier shape: a hub, per-competitor comparison pages,
and listicles linking into both. That structure makes ~50 internal links per
article natural rather than spammy. The old queue had no pillars and no link plan.

## 2. Three planned entries were WRONG and are corrected here

| Old queue said | Research found | Now |
|---|---|---|
| "macOS removed per-profile Dock icons", built on an Apple forum claim | No Chromium bug, no Chrome release note, no Apple doc. The claim is unsupported. Chrome's "Add desktop shortcut" is a Windows and Linux feature that **never existed on macOS** | Rewritten as `macos-never-supported-per-profile-dock-icons`. Stronger, because "never supported" explains why the gap is durable |
| An "Arc is dead, keep Chrome" page as item #1 | Arc refugees want profile switching **inside one window**. We give switching from the Dock. Adjacent, not equivalent | Demoted. The Arc angle survives only as a mention, not a pillar |
| Alt-tab as a major expansion area | We already have 6 alt-tab pages. How-To Geek and Yahoo confirm the demand, but our own coverage is nearly complete | Cluster D is now "finish, do not expand" |

## 3. Two verticals were dropped on evidence, and two more reframed

Dropped: **students** (the best student thread on this exact topic has one reply
saying "yes I find it works well" and ends; Setapp owns both the SERP and the
discount play) and **privacy** (the informed r/degoogle position is that profiles
are "largely useless vs cookieless browser fingerprinting", and that audience is
leaving Chrome).

Reframed: **developers** search in container and role vocabulary, never "Dock", so
the QA framing was wrong. **Agencies** do not search for the product at all, so
they became a persona voice rather than a keyword territory.

The old queue treated verticals as separate content areas. Four independent
studies found they all converge on the same core queries, which is why the
verticals are now spokes, not clusters.

## 4. New clusters the original queue did not contain at all

- **Cluster E, best Mac apps.** Absent from the original plan entirely. It is the
  most winnable format we have, and the pillar URL is reusable for every future app.
- **Cluster F, trust and objections.** Not an SEO play. We ask for the most
  invasive permission on macOS as an unknown developer and had nothing addressing it.
- **The `--user-data-dir` cost page.** Our measured benchmark (1.67 GB across 11
  processes becoming 4.6 GB across 33) is unpublished anywhere. It turns our most
  attackable claim into our most citable asset.

## 5. Rules the original queue had no way to know

- **Never promise faster switching.** ADHD readers told us friction is the feature.
- **No FAQPage schema.** Google retired the rich result in May 2026.
- **Disclose bias in the first screen** and give rivals genuine wins. The sites
  beating publishers here all do this, and one ranks itself last of four.
- **Write in their vocabulary.** The glossary at the end of this file did not exist.

## Scale

14 flat topics became **26 planned pages across 6 clusters**, on top of the 36
already published, with an explicit "not building" list so effort stops going
into dead ends.
