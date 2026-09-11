# Superdock growth research, 11 September 2026

Sources: Google Search Console (sc-domain:superdock.app), GA4 (552581768),
and ~15 live SERP pulls via TinyFish. Everything below is measured or quoted,
not assumed. Volume estimates are NOT available (no keyword tool), treat
topic picks as directional, CTR/position facts as hard.

## 1. Where we actually are

Site live 27 Aug, real content 3 Sep. 8 days of search history.

| Day | Impr | Pos |
|-----|------|-----|
| 3 Sep | 2 | 30.0 |
| 4 Sep | 26 | 16.8 |
| 5 Sep | 32 | 13.4 |
| 6 Sep | 47 | 15.8 |
| 7 Sep | 58 | 17.7 |
| 8 Sep | 51 | 22.0 |

90-day totals: 216 impressions, 2 clicks, **0.93% CTR**, avg pos 17.7, 27 queries.
GA4 28d: 101 page views, 83 sessions, **78 direct vs 3 organic**, 1 file_download.

**Verdict: indexing and ranking are working; clicking is not.**
Homepage sits at pos 6.6 with 26 impressions and 1 click. A normal CTR at
that position is 5-8%. This is the single measured failure.

## 2. The CTR leak (highest-value fix, minutes of work)

Ours vs the two pages that outrank us:

- Superdock: "Superdock: one Dock icon per Chrome profile" …desc ends "Profiles $7.99 once."
- DockDoor: "DockDoor - Free Alt+Tab and Native Dock Previews for Mac" …ends "Download instantly!"
- ExtraDock: "8 Best macOS Dock Alternatives in 2026"

Two defects, both ours:
1. Title leads with a feature nobody searches; no "free", no category term.
2. Description **closes on a price**. Last thing read before the click decision
   is a charge. DockDoor closes by removing friction.

## 3. Trust gap on the homepage (funnel leak #2)

Fetched all three homepages. Social proof count:

| Site | Proof elements |
|------|----------------|
| DockDoor | 8 press quotes (Lifehacker, Yahoo, GroovyPost, Medium, AppAddict…) |
| ExtraDock | 17-testimonial "Wall of Love" + screenshots section |
| **Superdock** | **0** |

We ask for Accessibility permission, the most invasive grant on macOS, from
an unknown developer, with zero third-party validation on the page. DockDoor
explicitly weaponises trust: a whole FAQ entry on *only* downloading from
official sources because cracked builds carry malware.

Assets we own and do not use: GitHub (Mahadkz), LinkedIn (in/syed-mahad-kazmi),
company page (company/super-dock), Developer ID + notarization, real measured
engineering (pixel-matched to Apple's Dock).

## 4. Wedges found, ranked by (evidence × lack of competition)

### W1. macOS broke per-profile Dock icons, NOBODY owns this
Apple Discussions, 3 Dec 2025, **ranks #1** for the query:
> "In recent macOS versions, certain system changes have removed the ability
> for browsers to offer separate launchers or Dock icons for different profiles."

A dated, Apple-confirmed regression with a first-ranking complaint thread and
**no solution attached**. Every competitor's answer (Parallel Spaces, chrome-schismator)
is separate instances = ~2.8x RAM + re-login. Ours is the only no-second-Chrome answer.

### W2. macOS 26 Dock instability, large, fresh, commercially answered by rivals
"Dock disappears randomly on macOS Tahoe 26.0", Apple Discussions, macreports,
iBoysoft, MacObserver, 9to5Mac, r/MacOSBeta all cover it. Only workarounds exist
(disable screensaver, toggle autohide, killall Dock).
Note: **docklockpro.com already publishes a "this is a macOS bug, not us" page**, a competitor monetising this exact anxiety. We hide the system Dock and run our
own, so we are structurally immune. That is a sales argument nobody is making.

### W3. Windows switchers, our true audience, confirmed twice
- r/MacOS "Must Have Apps for Windows Switchers" top answers: Rectangle,
  LinearMouse, Maccy, Ice, all *free utilities restoring Windows behaviour*.
- How-To Geek / Yahoo, Jul 2026, "5 native Windows features I desperately miss
  on my Mac" lists **"Alt+Tab for windows, not just apps"** as a headline gap.
This explains our alt-tab impressions: not wrong queries, our buyers arriving
via the door they know. Windows gives per-profile taskbar entries; macOS does not.

### W4. Arc is dead and its users want profile separation
The Browser Company announced 27 May 2025 no further Arc development.
r/ArcBrowser: "Why do no other browsers have spaces/profiles". MPU: "The best
thing about Arc, to me, is profile management."
A displaced, high-intent audience whose #1 loved feature was profile separation.
We deliver that *on Chrome, in the Dock*. No competitor targets this migration.

### W5. Mac mini / external-mouse users
r/macmini "If you are coming to macOS from Windows like me, install…",
MacRumors, HN. Without a trackpad you lose Mission Control swipes and App Exposé,
so **the Dock becomes the only window-management surface**. LinearMouse and
Mac Mouse Fix own scrolling; neither touches window switching. Narrow but uncontested.

### W6. Dock clutter, big demand, we have the feature, we say nothing
r/macapps "My dock is getting cluttered", the asker explicitly says
"Many of these apps are paid. I would like to try out a free option first."
Thread recommends DockFlow, ExtraDock, Dockify. We have folders, spacers and
pinning and do not compete here at all. Our free tier is the exact answer to
that sentence.

## 5. The listicle format: proven, and we can repurpose it

Every page ranking for "best Mac apps 2026" is **a small app site**, not a publisher:
noticky.app (notes app) #1, notchia.app (notch utility) #2, chronoid.app (timer) #3.

notchia.app technique, reverse-engineered, copy this exactly:
- FAQ entry: "Is NotchIA among the best Mac apps to install in 2026?" → answers by
  listing Raycast, Rectangle, CleanShot X, 1Password, Things 3, then claims the
  one category those five leave empty.
- FAQ entry: "What is the difference between NotchIA, Raycast, Rectangle and CleanShot X?"
  → "These four are complementary, not competitors."

You rank for big app names by being genuinely useful about them, then claim the
empty slot. **Our empty slot is browser profiles**, absent from every list found.

Community-curated Reddit lists (r/MacOS 2026 Essentials) are the same shape and
carry real referral weight. AltTab and Rectangle appear on every one.

**Repurposing works**, but update the SAME URL. Authority accrues to an address.
Adding a future app as an entry to an already-ranking list is correct; spawning a
new URL each time is not.

## 6. Affiliates: deprioritise (maths, not opinion)

affiliates.html already exists at 30%. At $7.99 that is **$2.40/sale**, and
Lemon Squeezy adds 2% on referred orders. No serious affiliate builds content
for $2.40. Affiliate programmes work on recurring revenue or high ticket; we
have neither by design.

Keep the page (costs nothing, signals openness). Do not invest in recruitment.

**Better channel: Setapp.** Pays from a monthly pool on usage, reaches exactly
this audience, needs no price change. Worth submitting once we have reviews.
(docs.setapp.com: bundle ≤1 GB, quality review required.)

## 7. Recommended order

1. **Title + meta description rewrite**, fixes the one measured failure, affects
   every impression already earned. Minutes.
2. **Social proof block on homepage**, GitHub, notarization, built-in-public,
   any real user quote. Unblocks the install decision.
3. **W1 page** (macOS removed per-profile Dock icons), dated pain, #1-ranking
   complaint, zero competition, our differentiator *is* the answer.
4. **W3 page** (Mac apps for Windows switchers), our audience, proven format.
5. **"Best Mac apps 2026" hub**, notchia technique; the URL we reuse forever.
6. **W2 page** (Dock disappears on Tahoe), big fresh demand; we are immune by design.
7. **W4 page** (Arc is dead, profile separation on Chrome), displaced high-intent users.
8. **W5 page** (Mac mini + mouse), small, uncontested, sharp argument.

## 8. Honest caveats

- No keyword volumes. Topic picks are reasoned from SERP evidence, not measured demand.
- 216 impressions is a tiny sample; position figures move a lot at this size.
- New pages take weeks to rank. They add impressions to a funnel that currently
  leaks 99% of clicks, hence fixing CTR first.
- The "alt-tab is unwinnable" call from 10 Sep was WRONG: an 8-day-old domain at
  position 44 is unranked, not beaten. Keep publishing there.

---

# Part 2, Competitor site teardowns, Arc wedge, open-source question
(added same day, after deeper SERP + page pulls)

## 9. What small Mac app sites actually do (4 teardowns)

Pulled noticky.app, snapbackapp.com, supasidebar.com, notchia.app, dockdoor.net,
extradock.app in full. The repeatable patterns:

### 9.1 Named "killer feature" first, numbered sections after
Noticky labels sections `01 / Killer Feature`, `02 / Context`, `03 / Workspace`…
One feature is explicitly crowned. We list features flat with no hierarchy, so
nothing is the reason to install.

### 9.2 Before/After problem framing (the highest-converting pattern found)
Noticky runs four literal Before → With Noticky pairs:
> "1. Working fullscreen, Apple Stickies disappears when an app enters
> fullscreen. Your context disappears with it." → "With Noticky: Notes stay
> above every window, even in fullscreen."

Snapback opens with a **cost calculation**:
> "Every context switch costs you 5 minutes. That's 25 minutes a day."

We state what we do; they state what it costs you not to have it. Ours is
strictly worse for conversion.

### 9.3 Honest social proof beats no social proof
Snapback has no users yet and says so, out loud, as a section:
> "Social proof, No fake testimonials. Yours is the one that matters. We're not
> going to make up quotes."
Noticky uses **soft numbers**: "250+ Mac users", plus 4 named quotes with role
(Kevin H. / macOS user, Dasol Y. / CS student, Gonzalo A. / Developer).

So the options are not "testimonials or nothing". A stated-honest placeholder is
an available, credible move for us right now.

### 9.4 The comparison table against the category, not one rival
Snapback: "Most window managers move windows. Snapback remembers them." then a
two-column Other apps / Snapback tick table. Cheap, scannable, positions the
whole category as the alternative.

### 9.5 Blog → product funnel done properly (supasidebar)
supasidebar.com/blog/too-many-tabs-open-mac is the best single page found:
- Author byline with real name + founder role, "Last updated June 12, 2026"
- TL;DR block at the top
- "Where this fits" internal-link cluster to 3 sibling posts
- An **honest table of competing fixes including where each one breaks**
- Quotes real Reddit users verbatim, with attribution
- Only pitches its own product in a clearly-labelled "Why we recommend" section
  near the END, after genuinely solving the problem
- Closes by segmenting the reader: single-browser users need layers 1-2 and
  **no third-party app**, explicitly tells some readers not to buy

That last move is the trust mechanism. It is EEAT executed, not claimed.

### 9.6 Keyword stuffing in meta keywords is alive in this niche
notchia: `meilleure app Mac, best Mac apps 2026, macOS, MacBook…`
dockdoor: `free mac app, alt tab mac, window switcher macOS, dock previews…`
Low value for Google, but it reveals the terms they are *targeting*. Both target
"best Mac apps 2026" and "alt tab mac", confirming our topic list.

## 10. THE ARC WEDGE, strongest single finding today

r/ArcBrowser "I need an Arc alternative" (Jul 2026), user **RonTem1**, verbatim:

> "Who else, besides Arc, supports Space+Profiles in the same way? I want to be
> able to set up spaces that have an assigned profile, that have their own set
> of cookies, etc."

That is our customer describing our product in a browser subreddit. The whole
thread is Arc refugees listing browsers (Zen, Dia, Vivaldi, Helium, Floorp, Phi,
Orion), and the recurring complaints are:
- **memory**: "I love the UI, I hate the memory management. It sucks battery."
- "Zen can consume up to three times as much memory as Arc"
- "I won't do AI browsers" (Dia rejected repeatedly)

### The pitch nobody is making
Every answer in that thread is **"install a different browser"**, which means
re-login, re-extension, new memory profile, new battery behaviour.

Ours is the only answer that is **"keep the Chrome you already have"**:
- no new browser to learn or trust
- no re-login to every account
- no extra memory (our whole FAQ argument: separate instances cost ~2.8x)
- no AI bolted on
- profiles get what Arc Spaces gave them, a visible, separate place to switch to

Search competition for "Arc browser alternative": supasidebar (#1 and #10),
kosmik, sigmabrowser, browser.horse. **Every one is a browser or a sidebar app.
None is a dock.** The angle "you don't need a new browser" is unoccupied.

## 11. Open source: the honest answer

Asked whether open-sourcing would increase trust. Three separate facts:

**a) The trust problem is real and Apple amplifies it.**
support.apple.com: "Be cautious and grant access only to apps that you know and
trust." securemac.com (Apr 2026): "Be extra cautious with apps that ask for
Accessibility, Screen Recording, Full Disk Access." We ask for Accessibility.

**b) Open source is a *proven* differentiator in THIS niche.**
DockDoor leads with it everywhere: "Privacy-first, open-source", "Full
transparency. Review our code", "no telemetry, not even crash reports". It works
for them, they are the free/open option on every list, including the
community-curated r/MacOS Essentials list (AltTab, Rectangle, Ice: all free/open).

**c) But we cannot open-source and keep selling this feature.**
Superdock is a clean-room rewrite, closed source, private repo. The paid feature
is Chrome profile tiles. Open-sourcing the app means anyone can strip
`LicenseService` and redistribute. The earlier fork (`archive/Split-Dock/`) is
GPL-3.0 precisely because it inherited upstream code; the rewrite exists to
escape that. **Open-sourcing would undo the entire reason the rewrite happened.**

### What to do instead: sell the *outcomes* of open source without the code
Every trust signal DockDoor gets from being open, we can claim truthfully:
- **No telemetry / no analytics in the app**, verify and then say it plainly
- **No account, no email to download**, already true, barely stated
- **Offline licence check**, Ed25519 verified on-device; the network is touched
  only for the 5-Mac activation cap, and it **fails open**
- **Developer ID signed + notarized by Apple**, stated once, should be a badge
- **Named developer with a public face**, GitHub Mahadkz, LinkedIn
  in/syed-mahad-kazmi, company/super-dock. DockDoor trades hard on "built by a
  solo developer"; we have the same asset and hide it.
- **A published privacy page that says "we collect nothing"** in one line

Optional middle path worth considering (NOT a recommendation yet):
open-source a *component*, e.g. the probe tools, or `PreviewCaption`, as a
public repo under Mahadkz. Signals openness, costs no revenue. Low effort,
non-zero payoff.

## 12. Query list for listicle pages (from SERP evidence, volumes UNVERIFIED)

Confirmed as live formats with small-app-site winners:
- best mac apps 2026 / best mac apps for a new macbook
- best mac apps for windows switchers / switching from windows to mac apps
- best free mac apps / free and open-source mac apps
- best menu bar apps for mac
- best mac window manager / rectangle vs magnet
- best macos dock alternatives
- arc browser alternative (+ "arc is dead", "arc discontinued")
- mac apps for developers
- best mac apps for multiple monitors ← we should own this
- mac apps for mouse users / linearmouse alternatives ← thin but uncontested

## 13. Revised build order (supersedes §7)

1. **Title + meta description**, the one measured failure. Minutes.
2. **Homepage: Before/After block + honest social-proof section + trust badges**
   (no telemetry, no account, notarized, named developer). Copy Snapback's
   honesty framing; we do not have to fake quotes.
3. **Arc wedge page**, "Arc is gone. Keep Chrome." Strongest unoccupied angle,
   a verbatim customer quote to answer, and every rival says "switch browsers".
4. **macOS-removed-profile-icons page** (W1), dated, #1-ranking complaint.
5. **Windows switchers listicle** (W3).
6. **Best Mac apps 2026 hub**, notchia technique, the reusable URL.
7. **Dock-disappears-on-Tahoe page** (W2), we are structurally immune.
8. **Multi-monitor listicle**, extends the cluster already at pos 7-11.

## 14. Caveats on Part 2
- Still no keyword volumes. Everything topical is SERP-reasoned, not demand-measured.
- The Arc thread is one thread; the quote is real but n=1 for that exact phrasing.
  The *migration* itself is well-evidenced (Browser Company statement, many threads).
- Open-source conclusion is a business judgement from repo facts, not market data.

---

# Part 3, Implementation brief (what we are changing and why)

## 15. Verified credibility inventory

Every claim below was checked before use. Do not add one that is not on this list.

| Claim | Verified how | Safe to publish |
|---|---|---|
| No analytics/telemetry in the app | `grep -ri "analytics\|telemetry\|mixpanel\|amplitude\|firebase\|sentry\|crashlytics"` over `superdock-app/Sources/` returns only `amplitude` as a magnification-maths variable | YES |
| Only 3 outbound hosts | grep of all `https://` literals in Sources/: github.com, license.superdock.app, superdock.app | YES |
| Signed with Apple Developer ID + notarized | CLAUDE.md: Developer ID QXZG3R725Z, notarized + stapled, Gatekeeper accepted | YES |
| Offline licence verification | `LicenseService` verifies Ed25519 on-device; network only for the 5-Mac cap, and it fails open | YES |
| No account / no email to download | download.html is a direct .dmg link | YES |
| Named developer, public profiles | github.com/Mahadkz, linkedin.com/in/syed-mahad-kazmi, linkedin.com/company/super-dock | YES |
| Pixel-matched to Apple's Dock | CLAUDE.md fidelity notes: glass 49/5, pitch 37, icon 35, dot rows 9-12, measured from screenshots | YES |
| 5 Macs per licence, self-serve removal | LicenseService + manage.html | YES |
| ~2.8x memory for separate-instance rivals | existing homepage FAQ claim, carried over | YES (already published) |
| User counts / testimonials / press | **NONE EXIST** | **NO, never invent** |

## 16. Founder story (the credibility asset we were not using)

Requested by owner, and it is also the single strongest EEAT signal available:
a first-person account of hitting the problem personally.

Narrative spine (true, per owner):
- switched to Mac from Windows
- the Dock collapsed every Chrome profile into one icon
- navigating between spaces/windows was the daily friction
- built the app for that frustration, not as a product idea first

Why this matters beyond warmth: Google's EEAT "Experience" is precisely
first-hand use. DockDoor trades on "Built by a solo developer" and it is on
every free-apps list. We have the identical asset and hide it.

Placement: a short, signed section on the homepage above pricing, plus expansion
on about.html. Signed with the developer's name and linked to GitHub/LinkedIn so
the claim is checkable.

## 17. Header: 8 links → 4

Before: Answers · Compare · Stacks · Switcher · Overview · Displays · Pricing · Blog
(4 of these, Stacks, Switcher, Overview, Displays, are in-page anchors to the
same scroll, competing with the one CTA.)

After: Features · Compare · Pricing · Blog  + Download free

Rationale: every extra nav link is a competing exit from the conversion path.
Feature anchors belong in the page flow, not the global header. Answers moves
into the footer, where reference content belongs; it keeps its internal links
from every answer page, so no SEO value is lost.

## 18. Metadata rewrite

| | Before | After |
|---|---|---|
| Title | Superdock: one Dock icon per Chrome profile on your Mac | Superdock, Free Mac Dock Alternative with Chrome Profile Icons |
| Desc ends | "Profiles $7.99 once." | "Free to download, no account." |

Two defects fixed: (1) no "free" and no category term in the title, (2) the
description **closed on a price**, i.e. the last thing read before the click
decision was a charge. DockDoor closes with "Download instantly!" and outranks us.

Target terms added: "free mac dock alternative", "mac dock replacement".
Both are category terms we currently rank for nowhere.

## 19. What we are deliberately NOT doing
- Not open-sourcing (see §11, it would void the paid feature and the whole
  reason for the clean-room rewrite).
- Not inventing testimonials, user counts, or press quotes. Snapback proves an
  honest "no testimonials yet" section is a credible alternative.
- Not touching the Answers/Compare/Blog page templates in this pass.

---

# Part 4, content pipeline decisions (2026-09-11)

## 20. Cadence: one piece per day

Owner chose one per day over three. Correct call for a domain that is two weeks
old. Reasoning kept here so it is not relitigated:

- 47 pages today. Three a day reaches ~140 pages in a month, a 3x jump in
  footprint on a domain with no authority yet. That pattern is what spam systems
  look for, especially when pages share one template.
- One per day still means ~30 pages a month, which is ahead of every competitor
  found (extradock, dockdoor, notchia all publish far slower).
- Quality per piece is the actual ranking lever. supasidebar's single tab, overload
  post outranks whole sites because it is genuinely the best answer on the page.

## 21. Icons in listicles: approved by owner

Owner: "adding icons is not an issue we are basically promoting them."

Practical guidance to follow when building listicles:
- Use each app's own official icon, fetched from its official site or its
  GitHub releases, never a competitor's screenshot of it.
- Link the icon and the app name to the official site. Promotion plus attribution
  is the posture that makes nominative use defensible.
- Store locally under `assets/apps/<slug>.png` rather than hotlinking, so pages
  do not break when a third, party site moves a file, and so page weight is ours
  to control.
- Keep icons small (64, 96 px) and lazy, loaded.
- Never imply endorsement, partnership, or that a listed app is ours.

## 22. Style rule, hard

NO EM DASHES anywhere: page copy, titles, meta descriptions, OG tags, CSS
comments, docs. Colon, comma or full stop instead. Audit before shipping:

    find . \( -name '*.html' -o -name '*.css' -o -name '*.txt' -o -name '*.xml' \) \
      ! -path './node_modules/*' -print0 | xargs -0 grep -l '—'

Expect zero matches.

## 23. Homepage changes shipped 2026-09-11

- Title: "Superdock: Free Mac Dock Alternative with Chrome Profile Icons"
  (was "Superdock: one Dock icon per Chrome profile on your Mac")
- Meta description now ends "Free to download, no account." (was "Profiles $7.99 once.")
- Header cut 8 links to 4: Features, Compare, Pricing, Blog. Answers moved to footer.
- New `.founder` section: first, person account of switching from Windows, signed,
  linked to GitHub and LinkedIn. This is EEAT "Experience", not decoration.
- New `.trust` section: six verified claims (see §15) plus an explicit "no
  testimonials yet" note rather than invented quotes.
- JSON, LD: added a Person node (#mahad) with sameAs to GitHub and LinkedIn,
  wired as author/creator of the SoftwareApplication and WebSite.

Verified: 1 H1, no horizontal overflow at 1280 and 390 px, no console errors,
JSON, LD parses, 5 schema nodes.
