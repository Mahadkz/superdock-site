# Vertical and wedge research, 12 September 2026

Six agents dispatched. Three reported before this file was written. **All three
hit the same infrastructure problem: the nine extra TinyFish keys were
registered mid-session and MCP servers only load at session start, so every
agent fell back to the one shared key and worked throttled.** The keys are
correctly registered in `~/.claude.json` and will be available to any new
session. Re-run this research after a restart for the full-throughput version.

Despite the throttling, the findings below are sourced and several change the plan.

---

## 1. THE BIGGEST FINDING: a feature we can ship almost free, that the
## category leader publicly does not have

**Dim or hide Dock icons for apps that are not running.**

- r/macapps, 2025-11-20: "Looking for an App that dim apps that are not opened in
  dock." Every answer in the thread fails on inspection. **The DockFlow/ExtraDock
  developer replies in-thread: "That's a great idea. I wonder if it can be done
  natively. I'll check"** — the category leader had not built it.
- r/macapps, 2026-04-03, from a user who already owns a five-app dock stack:
  "Icons that turn grey when the app is not open. This is probably **my most
  requested feature for any of these apps**."
- r/MacOS, 2026-05-23: "How to hide apps from Dock when all their windows are
  closed?" on Tahoe, ~20 replies, no good answer.
- A commenter proposes the exact implementation: "a brilliant optional use of the
  macOS 26 app styles, clear for not running, colored for running."

**Why this matters to us specifically:** Superdock already draws every tile
itself and already tracks running state (`accessibilityValue("running")`, the
dot, the active highlight). This is a rendering toggle over data we already hold.
The asks come from people who ALREADY PAY for dock apps, which is buying intent
rather than idle curiosity.

This is the highest value-per-effort item found in any research so far.

---

## 2. Rosetta 2 removal is a dated, OS-delivered distribution event

macOS 28 removes Intel translation. macOS 27 "Golden Gate" is the last release
with it, and Golden Gate shows every user a list at System Settings, General,
About, **Intel-Based Apps**, which "may try to suggest where you can find an
Apple silicon native replacement." Rosetta is NOT auto-restored on upgrade.

Sources: eclecticlight.co 2026-06-25; Apple support doc 2026-02-16; osxdaily
2026-08-11; r/macbookpro 2026-06-10 ("What are you replacing your Intel/Rosetta
apps with?").

Superdock is a native Apple silicon SwiftUI build, so it qualifies as the
replacement. **Before building a campaign, run `lipo -archs` on the competitors**
(cDock, ActiveDock, uBar, DockStar) to find which are Intel-only. That converts a
strong wedge into a precise one. Not yet verified.

---

## 3. Two corrections to earlier research

**uBar is NOT abandoned.** A dock roundup dated 2026-05-16 states development
"suddenly resumed in 2025 with several rapid updates." The previous research doc
treats stranded uBar users as an open goal. That wedge appears closed. Do not
build content on uBar abandonment without re-verifying.

**A live commercial competitor is now named "Docky".** Free basic version, $19.99
once, "replaces the default Dock so seamlessly you barely notice the switch."
Given our repo history with `josejuanqm/docky`, this is a naming collision worth
a deliberate decision.

---

## 4. The category got crowded fast

Two 2026 roundups enumerate 20+ live products: ExtraDock, DockDoor Pro, Sidebar,
MaxiDock, DockStar, DockFix, InfiniDock, ActiveDock 2, Another Dock, DockPops,
DockGroups, DockFlow, Parall, DockLock, SpatialDock, Taskbar, uBar, Dockspace,
DockThings, Docky. A commenter: "replace the dock entirely went from niche nerd
behavior to a legit category in like a short time."

Peers cluster at $13.99 to $30. **$7.99 one-time is at the very bottom of the
field.** That is a positioning advantage, but it also means we cannot win on
breadth of customisation. We win on the profile feature and the per-display
architecture.

---

## 5. Dock jumping between monitors: solved by us, unclaimed by us

12+ months of recurring threads (r/MacOS 2025-10-28, 2026-01-05, 2026-01-12;
r/applehelp 2025-08-09; Apple Discussions 2025-11-19). With "Displays have
separate Spaces" on, touching any screen's bottom edge yanks the Dock there, and
there is no native setting to stop it.

The ExtraDock developer names this as one of only four categories of dock user:
"Multiple monitors setup users, who get annoyed with their dock jumping around 3
monitors and hunting it down every time."

Current answer is DockLock, a bolt-on that wrestles Apple's Dock. **Superdock
draws one dock window per display and hides the system Dock, so the problem does
not get fixed, it ceases to exist.** A user with a monitor stacked vertically
above the MacBook cannot get the Dock onto the top screen at all; the DockLock
developer says that is "going to be solved in DockLock Pro, which is still under
development." We get that case free.

This is a positioning wedge, not a build. The work is done and unmarketed.

---

## 6. Per-Space dock contents: one incumbent, on a subscription

r/macapps 2026-05-16: a power user asks the category's most-read reviewer
"Do you happen to know if there's a dock app that can change its contents based
on spaces change?" The reviewer, who has tested nearly every dock app, does not
know of one.

Only ExtraDock answers it ("Dock Awareness"), at EUR 9.99/year, and its own FAQ
admits per-display attachment is unreliable on DisplayLink and docking stations
"especially after sleep."

We already filter the running row per display. Per-Space is the same filter on a
different axis. **Caveat: Space membership is harder to read than display
membership via public API. Scope before promising.**

---

## 7. Verticals: both agents recommend REFRAMING, not building as briefed

### Agencies, freelancers, consultants, social media managers
Verdict: **worth a cluster, but narrow it.**

The pain is real and the language is vivid. Best quote, r/ProductivityApps:
> "the number of times I've been in a screen share and had the wrong Gmail tab
> visible... was getting embarrassing. The thing that surprised me is how much
> calmer screen sharing got. I don't do the panicky pre-call check anymore
> because there physically can't be anything wrong in the client profile."

The post title itself contains "the 'wrong client tab' panic", a ready-made
headline someone else already validated.

But: **this vertical does not search for the product.** They search "how do I
stop getting flagged" and "how do I manage 10 client logins", not "Dock icon".
And the high-volume "multiple accounts" territory is fully colonised by
antidetect browser vendors (Multilogin, GoLogin, AdsPower, Dolphin Anty) running
industrial content operations for a different problem (avoiding platform bans).

**Willingness to pay is strong by analogy:** this group already pays $7 to $10
PER MONTH for antidetect browsers purely to keep client sessions apart. One
month of any of them exceeds our entire one-time price. That is the best pricing
argument available. Caveat: no one was found saying "I would pay for a
Dock-icon-per-profile tool" directly.

Narrow the vertical to **"people who run 3+ client Chrome profiles on a Mac all
day"** and treat agencies as the persona voice, not a keyword territory.

### Developers and QA
Verdict: **yes to a cluster, but the briefed framing is wrong.**

The agent searched r/QualityAssurance, r/softwaretesting, r/webdev and r/devops
and found the Dock problem essentially **absent** there. QA's multi-account
problem is already solved by Playwright contexts and Firefox containers. Their
words are "containers", "roles", "dev/stg/prd", never "Dock".

Two genuinely useful findings:
- **Chrome has no Multi-Account Containers equivalent, and Google says so.** From
  Chrome's own support forum, Aug 2026: "Chrome doesn't natively support
  multi-account containers like Firefox yet. Since managing multiple profiles is
  too clunky for your testing..." Firefox users have a good answer; Chrome users
  have a hack. We are a Chrome product, on the right side of that line.
- **There is no keyboard shortcut to switch Chrome profiles**, confirmed 2026: no
  View menu item, no assignable shortcut, no chrome:// flag.

**The DevTools/MCP angle has ZERO demonstrated demand.** The agent searched five
ways and found nobody complaining that tool-spawned Chrome instances clutter the
Dock. Our per-pid tiling is unique but unwanted. Ship it as a demo screenshot,
not a content cluster. Unique does not equal wanted.

Competitor found: **Unbundle, $6.99 one-time**, duplicates Chrome.app per
profile. Its own FAQ concedes "About 500MB per profile. Five profiles is about
2.5GB." That is a citable cost number from a competitor's own documentation.

---

## 8. Revised priority list

1. **Dim/hide non-running tiles.** Near-zero effort on existing state, asked for
   by paying customers of rival apps, category leader on record as not having it.
2. **Market the per-display architecture** against the dock-jumping pain. Already
   built, entirely unclaimed, 12 months of documented complaints.
3. **Verify competitor architectures with `lipo -archs`**, then decide on a
   Rosetta/macOS 28 campaign.
4. **Write the Chrome-profile cluster** around the uncontested Mac-specific
   queries, using agency and developer personas as voice rather than as separate
   keyword territories.
5. **Add "Chrome has no Multi-Account Containers"** as a target page. Google
   itself says so, and every current answer is "you can't."
6. Re-run the three unfinished agents (enterprise/Edge, students/privacy,
   discovery surfaces) in a fresh session with the ten keys live.

## 9. Explicitly unverified
- Which competitors are Intel-only. Needs `lipo -archs`.
- Whether uBar's resumed development is real. One source, needs checking.
- Space-membership API feasibility for per-Space dock filtering.
- The "wrong client tab" fear rests on one strong quote, not a documented pattern.

---

# Part 2, two more verticals reported (enterprise/Edge, students/focus/privacy)

## 10. EDGE SUPPORT IS THE BIGGEST PRODUCT FINDING IN ANY RESEARCH SO FAR

The Dock collapse is not a Chrome fact. It is a **Chromium plus macOS** fact, and
Edge is where the corporate user actually is.

Evidence, and note how badly unserved it is:
- r/edge (2021): "is it possible to have two separate Edge dock icons for two
  different profiles on Mac? In Windows, I am able to create two profiles and add
  two different icons to the taskbar for each (**one for work and one for
  personal**). It works beautifully." **ZERO comments. Nobody answered.**
- r/edge: "In Windows, Microsoft Edge creates additional instances of itself on
  the taskbar when you open a profile, however, on MacOS this is not the case."
  Best answers are App Expose and an Automator hack that **multiple commenters
  report does not work**: "The command executes but just doesn't do the thing."
- Microsoft's own Tech Community thread (Oct 2019, replies into 2021): same
  question, no product answer.
- Mozilla Connect, June 2026: an idea titled "MacOS, Per-profile Dock icons that
  launch the correct profile", stating "All profiles share a single Dock icon."

So Chrome, Edge and Firefox users are all asking, and the Edge threads are
**literally unanswered**. The asker's own framing is "one for work and one for
personal", which is the corporate use case in the user's own words.

**GATE BEFORE ANY EDGE WORK:** we attribute windows by title suffix resolved
against Chrome's `Local State`. Edge has an equivalent `Local State` under
`~/Library/Application Support/Microsoft Edge` and a ` - Microsoft Edge` title
suffix, but **it is NOT verified that Edge window titles embed the profile name
the way Chrome's do.** That is a 30-minute local probe and it gates the whole
expansion. Do it before writing a single Edge page.

## 11. Enterprise as a BUYER: no. As a persona: yes.

- Searched r/sysadmin and r/macsysadmin: **essentially nothing** on per-profile
  Dock icons. Admins care about policy (`RestrictSigninToPattern`), not Dock
  ergonomics.
- No demand signal at all for volume licensing of a $7.99 utility. Sysadmins do
  not raise purchase orders below that threshold.
- **Actively adversarial current:** admins discuss *restricting* personal profile
  sign-in. One sysadmin prefers Edge precisely because it "makes sure the users
  are signing in with a work account instead of some random personal Google
  account." A tool that makes running a personal profile alongside work more
  pleasant is, to that persona, unwelcome.
- Our SkyLight SPI use means an admin evaluating us sees a private-API app asking
  for Accessibility. That is a security review, not a purchase.

**One defensive page is justified, not a cluster:** "Does installing a Dock app on
a managed Mac break anything?" covering Accessibility, what we do and do not see,
and MDM compatibility. It serves real anxiety (r/AskNetsec: "Can my employers read
my personal mails if I login to my personal gmail on a company managed chrome
browser?") and removes a purchase blocker.

## 12. Students: DO NOT BUILD. Three independent reasons.

1. **The pain is not felt.** The best student thread on this exact topic
   (r/chrome, Sep 2025, incoming freshman asking whether to separate profiles)
   has one reply, "yes I find it works well", and ends. That is a
   solved-problem signature. A targeted search for student complaint language
   returned pure noise, which is itself evidence the vocabulary does not exist.
2. **Setapp owns the content and the offer.** They hold the "best mac apps for
   students" SERP with a funded content operation AND run the student-discount
   play through Student Beans. The listicle format is also hostile: readers of
   those pages want Notion and Zotero, not a Dock utility.
3. **A discount on $7.99 is worth $1.60**, below the threshold where a student
   bothers verifying status. Students are the lowest willingness-to-pay segment
   and route around friction rather than paying to remove it.

**Salvage:** students are a demographic inside the focus cluster, not a vertical.
The best ADHD quote found came from a student. Write for the problem and they
arrive free, with no seasonal SEO war.

## 13. PRIVACY: drop entirely. Publishing would invite a correct rebuttal.

The informed privacy position is that browser profiles are the WRONG TOOL. Top
answer in r/degoogle, August 2026:

> "different browser profiles within the same browser can lead to
> compartmentalization of local state (cookies, cache, service workers etc.), but
> are **largely useless vs. cookieless browser fingerprinting**."

And directly on profiles versus separate browsers: "In light of browser
fingerprinting, no, not better."

Worse, this audience is actively de-Googling, i.e. leaving Chrome. We would be
marketing a Chrome accessory to people whose stated project is abandoning Chrome.

This is the one angle where publishing invites a technically correct rebuttal
from the best-informed voices in the space. Do not write it.

## 14. ADHD AND FOCUS: strong, and it maps directly onto the paid feature

Twelve years of consistent evidence (2014 to 2026).

> "I have 2 google accounts, one for school and one for leisure... **I can't
> stress enough how helpful this is.**" (r/ADHD)

Top reply, and the sentence to build on:
> "even putting them in a different window really helps me focus. **Out of sight,
> out of mind.**"

Others: "set up a separate browser profile for social media, so you can't close a
work tab and find Facebook"; "I made a entirely separate profile just to
**firewall myself from video games**... My goofoff profile, obviously, is exactly
as it sounds."

**CRITICAL POSITIONING CONSTRAINT, do not get this wrong.** For some ADHD users
**friction is the feature**. From r/getdisciplined:

> "**Too much temptation to switch between Chrome users when I want to goof off.**"

So we must position on **visual separation and instant identification**, NEVER on
"switch faster". The ADHD user does not want a faster path to the leisure
profile. They want to always know which one they are in, and they want the
leisure one to feel far away. Any copy promising quicker switching actively
repels this segment.

## 15. The demand-side description of our paid feature

r/ProductivityApps, March 2026, a user inventing our feature from scratch:

> "**Different profile pictures for each. This sounds dumb but it's the only way
> I can tell at a glance which profile I'm in.** Chrome shows the avatar in the
> top right. **I use emoji-style images so they're obvious even in peripheral
> vision.**"

And their stated downside, which is exactly the gap we fill:
> "The downside, you end up with multiple browser windows and it can feel a bit
> heavy... **It's not elegant but it works.**"

Corroborated by a social media manager in r/MacOS:
> "I am logged in on her accounts in Safari and mine in Chrome. **I live in terror
> of accidentally posting my snark to her feeds**"

## 16. Consolidated verdict on verticals

| Vertical | Verdict |
|---|---|
| Agencies / freelancers / consultants | **Build**, but narrow to "people running 3+ client Chrome profiles on a Mac" and use agency as persona voice, not keyword territory |
| Developers / QA | **Build**, but reframed as "multiple Chrome profiles on macOS". The QA testing framing is absent from QA communities |
| ADHD / focus | **Build.** Strongest emotional evidence, direct feature mapping, weak incumbents. Position on identification, never on switching speed |
| Enterprise / IT as buyer | **No cluster.** One defensive MDM/permissions page |
| Edge support | **Product decision, highest upside.** Verify title attribution first |
| Students | **No.** Setapp owns it, pain not felt, discount meaningless |
| Privacy | **No.** Premise is technically contested and the audience is leaving Chrome |

The four buildable verticals all converge on the SAME core queries about Chrome
profiles and the Dock. That argues for ONE cluster with persona-specific spokes,
not four parallel clusters.
