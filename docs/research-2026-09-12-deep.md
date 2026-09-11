# Deep research, 12 September 2026

Six parallel research agents, ~160 SERP pulls and full-page reads. Everything
below is sourced. Where an agent could not verify something, that is stated.

---

## 0. First: the 2.8x memory claim SURVIVES scrutiny, with a caveat

A research agent reported it could find **no public source** for the 2.8x figure
and recommended we stop publishing it. That recommendation is **wrong**, because
the agent could only search the open web and our measurement was never published.

The measurement exists and is recorded in `archive/Split-Dock/docs/learnings.md`:

> Separate `--user-data-dir` instances: works (real processes, real tiles) but
> costs ~2.8x RAM, measured: normal Chrome with 3 profiles and ~35 tabs =
> 1.67 GB across 11 processes; three isolated instances = ~4.6 GB across ~33.

4.6 / 1.67 = 2.75. The figure is ours, first-hand, and accurate.

**The caveat is real though.** The agent's underlying point stands: an
unsourced-looking precise multiplier is the easiest thing for a skeptical HN or
Reddit commenter to attack. Our pages already say "in our measurement" on the
blog and compare pages, but `index.html` and the author page state it flatly.

ACTION: make the measurement conditions visible wherever the number appears
(3 profiles, ~35 tabs, 11 vs 33 processes, 1.67 GB vs 4.6 GB), and publish the
full methodology as its own page. **Nobody else has published this benchmark.**
That turns our most attackable claim into our most citable asset.

---

## 1. The "macOS removed per-profile Dock icons" claim is FALSE. Do not publish it.

This was item #2 in the previous build order. It must be rewritten.

The Apple Discussions thread (256202449, Dec 2025) says macOS "removed the
ability for browsers to offer separate launchers or Dock icons for different
profiles." An agent tried to verify this and found:

- No Chromium bug tracker entry
- No Chrome release note
- No Apple documentation
- No independent corroboration anywhere

Apple Discussions answers are often written by other users. A vague "recent
macOS versions / certain system changes" with no version number and no mechanism
is the signature of a guess.

**What is actually true, and is a BETTER story:** Chrome's "Add desktop shortcut"
in profile settings is a Windows/Linux feature that **has never existed on macOS**.
Apple StackExchange has been asking since 2012. Google's own support forum
(thread 463951481, Aug 2026) states it plainly:

> "On Windows, the taskbar groups by window, so each Chrome profile window can
> get its own icon. On Mac, the Dock groups by application, not by [profile]"

So the accurate framing is **"macOS never supported this"**, not "macOS removed
it." That is stronger: it explains why the gap is durable rather than a
regression someone might fix next release.

Chromium's own docs give the cleanest statement of the mechanism:
profiles "associate a set of preferences with a specific set of browser windows,
rather than with an entire running instance" (chromium.org multi-profile design
doc). Profiles are a *window-level* identity inside one process, which is exactly
why a *process-level* Dock collapses them.

---

## 2. A competitor publicly declared our feature impossible

The boringBar developer, on Hacker News:

> "I reckon peeking into the individual iTerm/Brave/Chrome tabs would not be
> possible without disabling SIP. I need to research this a bit though."

Superdock reaches per-profile granularity through title-based attribution with
**no SIP changes**. A competing developer has stated on the record that this
cannot be done. Nobody is making this claim. It is the strongest available.

---

## 3. Users ask for this constantly, in words we are not using

Eleven years of unanswered requests (2015 to 2026), and the demand is **unnamed**:
people ask for "one icon per window", not "per-profile tiles". We should rank for
the phrase they actually type.

The single best artifact, r/MacOS 2022, a user writing our product spec:

> "each chrome profile shows up as seperate dock items using their chrome profile
> icon (or a chrome icon tinted with the profile's color). The hotkey Control-Down
> Arrow only shows chrome windows of the current chrome profile. The Alt Tab
> screen does not merge them all into one big useless chrome blob."

Answers given in that thread: "No" x4.

Others:
- "I need something that actually makes a separate app in the dock that persists
  rather than just open a browser that's already in my dock. The hunt continues."
  (r/macapps 2025, explicitly rejecting every shipping competitor)
- "all windows are combined into the same Chrome icon and switching between them
  is confusing" (r/MacOS, same user asked twice, Oct 2024 and Jun 2025, never answered)
- "in Windows, not only can you have each profile in the task bar, you can change
  the icon of the app so it's VERY clear which profile you are working in...
  i switch between 4 different profiles daily due to work requirements"
- "the wrong client tab panic" (r/ProductivityApps 2026, agency worker)
- "I'd have to be running a minimum of six browsers which I just don't think is
  actually feasible" (r/chrome, rejecting the separate-instance approach)

**Their vocabulary, to use verbatim:** "collapse into a single Chrome icon",
"one big useless chrome blob", "hunting", "the hunt continues", "hacky
workaround", "jank", "you have to live with it", "it groups by application, not
by window".

**Words they never use:** productivity, workflow optimization, context switching.

---

## 4. macOS 26 Tahoe: the blurry Chrome icon is a visual, provable wedge

r/MacOS thread running Jan to Aug 2026, unfixed across 26.2, 26.3, 26.4.1, 26.5.1:

> "The blurriness of the dock icons... The icon for chrome is particularly
> egregious, the four sharply divided colors are now blurring together like
> Vaseline was spread over it."

Reply: "Mac Tahoe is Vaseline Screen. You said it perfectly."

Superdock draws its own tiles at measured sharpness. **A side-by-side screenshot
of the Chrome tile, Apple's vs ours, is the single best marketing asset available
and costs nothing to produce.**

Also confirmed: the Dock disappearing after sleep/screensaver with auto-hide OFF,
widely reported, never acknowledged by Apple, unfixed as of Feb 2026. A
competitor (docklockpro.com) already publishes a "this is a macOS bug, not us"
page. We hide the system Dock and draw our own, so we are structurally immune.

Launchpad removal in macOS 26 is confirmed and controversial.

---

## 5. Distribution: r/macapps has a hard gate we do not currently pass

r/macapps "Phase 3" rules (Mar 2026) run a three-tier trust system:

- **Tier 1** (main feed): Mac App Store distribution, OR an established GitHub
  project (1yr+ history, 100+ stars), OR developer flair. **Notarization does
  not count** (mod: "notarization itself really only checks malicious code").
  We cannot reach Tier 1: SkyLight SPI rules out the App Store.
- **Tier 2** (main feed): requires BOTH a real-identity developer portfolio with
  LinkedIn and contact details, AND **a website with a Privacy Policy and Terms
  of Service**. We have privacy.html and terms.html, plus the new author page.
  **We likely already qualify.** Worth confirming before posting.
- **Tier 3**: relegated to a megathread.

Also required: 10+ local comment karma (70% of zero-karma promo posts are
auto-rejected), PCP post format (Problem, Comparison, Pricing), and max one
promo post per developer per 30 days, counted even if removed.

**Critical warning from the mods, verbatim:** "AI assisted comments are a huge
trigger for Reddit auto-removals because of recognizable patterns (e.g. '—' em
dashes)." Our no-em-dash rule matters here too.

Other channels, ranked:
- **Hacker News**: boringBar's Show HN hit 520 points, so the category performs.
  But the thread was dominated by a pricing revolt that forced a live pivot from
  subscription to perpetual. $7.99 one-time sits below every price commenters
  called acceptable. Device caps drew real hostility ("I despise 2-device limits...
  It's where I stop reading"), so our 5-Mac fail-open design must be stated
  explicitly. Expect "why not open source it" and a clone attempt.
- **Homebrew cask**: ineligible for now (needs 75+ stars or equivalent public
  notability; our app repo is private). Our trial model IS eligible per their
  policy. Ship a third-party tap now instead.
- **Product Hunt**: one documented Mac launch got top 5, 294 votes, ~800
  visitors, ~100 downloads, with a Discord and two newsletters behind it. Worth
  one shot for the backlink, not a strategy.
- **Setapp**: 25% commission on one-time sales, pays by usage. Developers appear
  to be contractually barred from discussing it, so evidence is thin. Defer.
- **AlternativeTo + awesome-mac**: an hour of work, mainly for positioning
  against uBar.

---

## 6. Competitors: uBar and ActiveDock are open goals

**uBar ($30) is effectively abandonware.** Release history: 4.2.1 Oct 2022,
4.2.2 Oct 2023, 4.2.3 Aug 2025, 4.2.4 Sep 2026. Users:

> "support requests were simply ignored. I reluctantly deleted it several months
> ago and now use Sidebar."
> "This company takes money and does not fix many, many issues (critical). Their
> support is dead (tickets from 2019). Consider it abandonware."

**ActiveDock (3.6/5)** has documented refund misconduct.

**Nobody does what we do.** Every rival separating Chrome profiles uses separate
`--user-data-dir` instances or duplicates Chrome.app: Parallel Spaces ($4.99),
Parall ($9.99), unbundle.app, Coherence, Epichrome, chrome-schismator. DockDoor
Pro badges window *previews* with the profile, which is not a tile. DockFlow
switches profiles as a launch *action*, and explicitly needs no permissions, so
it cannot attribute windows.

**Price anchor caution:** since our dock is free and $7.99 buys only profile
tiles, buyers compare us to Parallel Spaces at $4.99, not to $20-30 docks.

**Universal category complaints** (our QA checklist): doesn't feel native;
dock vanishes or settings don't persist; CPU burn; breaks every macOS release;
maximized windows slide behind the bar; multi-monitor windows on the wrong
display; uninstall leaves debris; **notification badges without the app open are
unsolved by every competitor** and were called a dealbreaker twice.

---

## 7. Content rules, from Google's own docs

**Hard, Google-stated:**
- **FAQPage schema is DEAD.** Google's changelog: the FAQ rich result stopped
  showing 7 May 2026 and the docs were deleted 15 Jun 2026. We ship FAQPage
  JSON-LD on ~36 pages. It is now inert. Keep visible FAQ sections; the markup
  earns nothing.
- **Structured data does not improve ranking.** Mueller, Apr 2025: "Structured
  data won't make your site rank better." Our Person schema is for attribution
  and AI extraction, not rank. Keep it, expect nothing from it directly.
- **llms.txt does nothing for Google Search**, by Google's own June 2026
  changelog. Keep it for other services, do not count it as SEO.
- **EEAT is not a ranking factor**, but Google "strongly encourage[s] adding
  accurate authorship information, such as bylines." Experience explicitly
  substitutes for credentials: "expertise that comes from having actually used
  a product." Our author work is correctly aimed.
- **No preferred word count.** Pages beating publishers measure 1,100 to 3,500
  words.

**Observed across six ranking small-app sites:**
- The complete answer appears in the first ~60 words, often labelled TL;DR.
- Exactly one comparison table, placed after the entries, with a *conditional*
  verdict column ("#1 if you want X"), never checkmarks alone.
- Scope and exclusions declared explicitly.
- Method and date footnoted ("Reviewed 6 Sep 2026 using developer feature lists,
  release notes, App Store listings and public source code").
- **Bias disclosed in the first screen, first person.** Droppy: "I build Droppy,
  one of those six, and you are reading this on Droppy's own website, so discount
  my conclusions as hard as you think is fair."
- **Rivals given genuine unqualified wins**, including recommending a free
  competitor. Droppy ranks himself LAST of four on clipboard managers and omits
  himself entirely from his free-apps listicle. That page is the one third
  parties can link to without it looking like an ad.
- Pricing shown as 3-year total cost vs named subscription rivals, with a dated
  footnote.
- Social proof as named Reddit commenters with permalinks, not anonymous quotes.
- Three-tier structure: /compare hub, per-competitor pages, listicles linking
  into both. ~50 internal links per article is normal in this pattern.

**Information gain:** pursue originality because Google's helpful-content doc
demands it, NOT because of the "information gain patent", which governs automated
assistants rather than organic ranking and is widely misread.

Our unfair, uncopyable facts: the measured Apple Dock fidelity numbers (pitch 37,
icon 35, glass 49/5, dot rows 9-12), that the fork's AX-derived numbers were
wrong, that macOS posts NO notification when icon style changes (verified over 60
seconds of toggles), that two AX-polling docks froze a desktop, and the memory
benchmark in section 0.

---

## 8. Revised priorities

1. **Fix the 2.8x presentation** everywhere, adding measurement conditions, and
   publish the benchmark methodology as its own page. Turns our weakest-looking
   claim into a citable asset nobody else has.
2. **Rewrite the planned "macOS removed profile icons" page** as "macOS never
   supported this, and here is why" with the Chromium and Google sources.
3. **Shoot the Tahoe blurry-Chrome-icon comparison.** Free, visual, current.
4. **Drop FAQPage JSON-LD** from the template. It is inert as of May 2026.
5. **Confirm r/macapps Tier 2 eligibility**, build comment karma, then post once
   in PCP format.
6. **State the 5-Mac fail-open licence on the pricing page.** It answers the
   loudest objection in the category and is currently invisible.
7. Keep the cluster plan from `content-clusters.md`, with "one icon per window"
   added as a target phrase throughout.

## 9. What could not be verified
- Whether chrome-schismator and Automator wrappers still work under current
  Gatekeeper rules. Needs hands-on testing before we write about them.
- MacUpdate's current submission flow (their /submit-app 404s).
- MacMenuBar, unresearched.
- No conversion case study for indie Mac landing pages was found. Treat
  before/after framing and social proof as convention, not proven lift.
