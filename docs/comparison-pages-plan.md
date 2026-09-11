# Alternative and versus pages
12 September 2026. From 10 SERP probes and 3 page dissections.
Companion to `content-clusters.md` and `listicle-plan.md`.

## The strategic read, up front

The dock-replacement **alternative** queries are a thin, well-contested market
where we would be the sixth indie vendor writing the same page. The **Chrome
profile** queries are where we have a defensible technical claim nobody else can
make, and the SERP is still held by StackExchange answers.

Spend effort there. Write "uBar alternative" because the price gap makes it easy.
Skip most of the rest.

## An independent confirmation worth noting

This agent searched for the claim that macOS or Chrome "removed support for
separate browser-profile launchers", fetched the Google support page a snippet
attributed it to, and found **the text is not on the live page.** A stale or
fabricated index entry.

That is the second independent confirmation. `content-clusters.md` already
rewrites this page as "never supported". Keep it that way.

---

## Table 1. Alternative pages, ranked

| # | Target query | Incumbent status | Who holds the SERP | Ease | Note |
|---|---|---|---|---|---|
| 1 | uBar alternative | **Alive but resented.** v4.2.4 Sept 2026, Tahoe supported, but $50 for 2 Macs and a Reddit thread calling support "dead... abandonware that ships updates to milk the product" | Reddit #1, extradock, lawand.io, alternativeto | **High** | Best target. $50 versus $7.99 is the whole angle. Two indie vendor pages already rank, proving a vendor-authored page wins here |
| 2 | cDock alternative | **Effectively dead.** Repeated threads asking for a macOS 15 support ETA, nothing newer | Reddit + ActiveDock's own page | **High** | Genuinely stranded users, zero vendor competition, pure capture intent |
| 3 | Chrome profiles as separate Dock icons | The category query, not an alternative query | parallelspaces, shiftplus, StackExchange, superuser | **Medium** | **Highest commercial value in the report.** Exactly our paid feature. Every competitor uses `--user-data-dir`, which we beat on RAM and re-login |
| 4 | HyperDock alternative | **Dead**, ActiveDock's own copy calls it "legacy Hyperdock" | ActiveDock, alternativeto | High | Long-tail, cheap to write, expect little |
| 5 | Parallel Spaces alternative | Alive, actively doing SEO | Their own site | Medium | Direct rival on the paid feature, with a real technical argument to make |
| 6 | Epichrome alternative | Alive, open source, technical | StackExchange + vendors | Medium | Audience will ask why they should pay for what a script does free. Argue carefully |
| 7 | ActiveDock alternative | Alive, actively marketing | noteifyapp | Medium | They rank for everyone else's brand, so taking theirs is symmetric |
| 8 | DockDoor alternative | Alive, now has a paid tier that ships "Dock profiles" | Their own site | Medium-hard | Open source and well liked, so hostility backfires. **Note the feature overlap** |
| 9 | AltTab alternative | **Very alive**, free, beloved | Four vendor pages already fighting | **Low** | No unhappiness to capture, and switcher users are not dock buyers |
| 10 | Shift / Rambox / Station alternative | Alive | Mailbird, ClickUp, Biscuit | **Low** | Unified inbox products. A dock utility is not a substitute |

**Not worth a row:** ExtraDock, DockFix, InfyniDock, boringBar, Taskbar, Sidebar.
All brand-new indie apps with **no installed base**, so there are no stranded
users to capture. They are competitors running our playbook, not incumbents.

---

## Table 2. Versus pages, ranked

The test of "neither vendor's own site ranks" is satisfied in fewer places than
hoped, because in this niche the vendors are the SEO players.

| # | Comparison | Who ranks now | Ease | Verdict |
|---|---|---|---|---|
| 1 | **AltTab vs DockDoor** | A Reddit thread with 40 comments, translated into Korean, German and Dutch, plus one thin affiliate blog. **Neither vendor ranks.** | **High** | The clearest gap found. Real international demand, no defender, and we are a credible third party |
| 2 | Chrome profiles vs separate Chrome instances | Fragmented across StackExchange and superuser | **High** | Not brand versus brand, but the highest-intent concept page available, and it maps exactly onto our architecture |
| 3 | uBar vs ActiveDock | Nothing direct | High | Two incumbents, neither defending it. Third-party framing is credible |
| 4 | Superdock vs Parallel Spaces | Their site only | Medium | Must write. Closest substitute for the paid feature, and one-process-versus-N is measurable |
| 5 | uBar vs Taskbar | lawand.io owns it, weakly | Medium | Enterable, not free |
| 6 | Superdock vs DockDoor | Their site | Medium | Now defensive, since DockDoor Pro ships dock profiles |

**Note the asymmetry in row 1 versus alternative-table row 9.** "AltTab vs
DockDoor" is a great target while "AltTab alternative" is a bad one. The
comparison query has demand and no defender; the alternative query has a happy
incumbent and five defenders.

---

## Table 3. Comparison page template

Derived from lawand.io (~900 words, ranks #3 for "uBar alternative") and
infyniclick.com (~450 words, ranking). The structural difference is instructive:
**lawand.io argues, infyniclick.com segments.** Argue when targeting a resented
incumbent; segment when you are genuinely a different shape of product.

| Section | What it does | Words |
|---|---|---|
| Disclosure, first paragraph | "Transparency is important to me. I am the independent developer behind Taskbar." Strongest trust move on the page and costs nothing | 30 |
| H2 restating the query | "Looking for a uBar Alternative for Mac?" Matches intent literally | 10 |
| One-sentence differentiator | Ours: per-profile Chrome tiles with no duplicate instance | 30 |
| Feature table, 7 to 9 rows | Both columns get real entries. No empty cells, no all-green column. **Price is the last row**, where it lands hardest | 150 |
| Why choose us, 5 bullets | Each a concrete mechanism, never an adjective | 150 |
| Why choose them, honest | lawand.io concedes uBar wins on theming and legacy macOS support | 120 |
| Who should NOT use us | infyniclick.com names users who should not buy. **Most transferable move in the report:** conceding a segment is what makes the rest believable | 80 |
| Pricing, both products, plainly | No coyness | 60 |
| Conclusion | Give the incumbent a genuine win condition FIRST, then state ours | 80 |
| 3 FAQs | One should be "Is X a replacement for Y?" answered "not a clone" | 150 |
| CTA | A single download link, repeated twice | 20 |

**Target 450 to 950 words. Do not pad to 2,000.** Both ranking pages are short.

**Tone finding:** neither page is hostile. The harshest line on either is
"Infrequent updates; slower bug fixes", stated once, in a table cell. Copy that
register. Our price is 6x cheaper than uBar's, so **the price row does the
aggression for us** and the prose should stay generous.

**CTA finding:** neither page uses urgency, discounts, countdowns or buttons in
the comparison table. Low pressure is the convention here and breaking it reads
as spam.

---

## Table 4. Not worth writing, and why

| Skip | Reason |
|---|---|
| Antidetect browsers (Multilogin, GoLogin, AdsPower, Dolphin) | They sell fingerprint spoofing and proxy rotation at $9 to $100+/month for multi-account farming. We change Dock icons and spoof nothing. Saturated SERP, traffic would bounce, and the association is bad for a $7.99 utility |
| Unified inbox tools (Shift, Rambox, Station, Wavebox, Coherence) | Not substitutes. Someone wanting Slack and Gmail in one window is not served by dock tiles. SERP owned by high-authority content marketers |
| AltTab alternative | Free, open source, loved. No unhappiness to capture, four vendors already fighting, wrong audience |
| Dead incumbents beyond cDock and HyperDock | Dead means no searchers. cDock earns its slot only because live threads prove people are still looking |
| New indie apps | No installed base. Writing "Superdock vs ExtraDock" mostly builds **their** awareness; we would be the first to establish the comparison exists |
| Anything premised on "macOS removed per-profile Dock icons" | Unverified and contradicted by the live Google support page |

## Caveat
No keyword volume data was available. Ease ratings are SERP-structure based, so
treat them as ordinal rather than absolute.
