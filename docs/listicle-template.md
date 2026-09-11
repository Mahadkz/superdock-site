# Listicle page template
Measured 12 September 2026 from six pages that outrank publishers: supasidebar
(designers), noticky (new MacBook), timingapp (menu bar), chronoid (best apps),
getdroppy (free apps), extradock (dock alternatives). Word counts are +/- 5%.

## Measured reality, not guesses

| | supasidebar | noticky | timing | chronoid | droppy | extradock |
|---|---|---|---|---|---|---|
| Words | 2,400 | 2,183 | 7,419 | 4,665 | **1,151** | 2,103 |
| H2 / H3 | 9 / 7 | 15 / 32 | 7 / 11 (+20 H4) | 30 / 5 | 7 / 0 | 12 / 1 |
| First app named at word | ~30 | ~15 | ~416 | ~160 | ~110 | ~210 |
| Apps listed | 8 | 32 | 20 | 12 | 8 | 8 |
| **Own product rank** | **5 of 8** | **2 of 32** | **2 of 20** | **1 of 12** | **absent** | **4 of 8** |
| Tables | 1 | 1 | 3 | 14 | 1 | 0 (cards) |
| Internal links | 14 | 58 | 58 | 42 | 40 | ~12 |
| Links to rivals' official sites | sources only | **none** | **all 21** | **all 11** | **all 8** | 2 partners only |
| FAQ / FAQPage | 6 / yes | 5 visible, 20 in schema | 3 / yes | 4 / yes | **none** | 12 / yes |
| Byline | yes, twice | yes | yes | org only | yes | **none** |

**Target 2,000 to 2,600 words.** Four of six sit in 2,100 to 2,400. Droppy ranks
at 1,151 and Timing at 7,419, so the band is wide, but the middle is safe.

## The five things all six do that a naive listicle omits

1. **The answer is above the fold, in bold, before any reasoning.** Every page
   names specific apps within the first 30 to 200 words. None opens with throat
   clearing. Four label it: "TL;DR", "Quick answer", "at a Glance".
2. **A fixed field template per entry, never freeform prose.** "Best for:",
   "Price:", "Standout feature:" repeat identically down the page. **The repeated
   label is what makes an entry extractable by a snippet or an LLM.** Freeform
   paragraphs are not.
3. **Own product ranked 2nd to 5th, not 1st, and rivals given explicit wins.**
   ExtraDock hands the budget category to free DockDoor. Timing calls its own top
   pick unstable on Tahoe. Only Chronoid self-ranks first, and it is the most
   transparently promotional page of the six.
4. **A second table that sorts by the reader's problem, not by the app.** The
   first table ranks; the second routes. "If your problem is X, get Y."
5. **Heavy internal linking.** Median around 40 internal links per page.

## The template

| # | Section | Level | Words | Must contain |
|---|---|---|---|---|
| 0 | Byline and date | | 15 | "By Mahad Kazmi, developer of Superdock. Last updated YYYY-MM-DD." Repeat at the foot. The one page with no byline is also the one with no editorial voice |
| 1 | **Quick answer / TL;DR** | H2 | 90 to 150 | Name 4 to 6 apps **in bold inside the first 30 words**. Median across the six is word 110. State the stack's total cost |
| 2 | Scope and exclusions | | 30 | One sentence on what is not covered |
| 3 | **Why the default is broken** | H2 | 200 to 300 | Three specific macOS gaps. This earns the page's right to exist. Five of six have it |
| 4 | Selection method | H2 | 80 to 120 | Criteria plus a dated "reviewed [month year]" |
| 5 | **At-a-glance table** | H2 | table | 8 to 12 rows, 3 to 4 columns. **Final column is a verdict, never a spec** |
| 6 | **App entries by category** | H2 category, H3 app | 90 to 160 each | Rigid order: **Name (price)**, what it is, "Best for:", "Standout:", optional pros and cons, **link to the official site** |
| 7 | **Our entry** | same H3 | same length | **Position 2 to 5. Never 1.** Position 2 is the sweet spot |
| 8 | **Pick by situation** | H2 | 200 to 350 | "If your problem is X, get Y". **Hand at least one situation to a rival by name** |
| 9 | Setup order | H2 | 150 to 250 | Numbered install order. Converts a list into an action |
| 10 | **Why we recommend Superdock** | H2 | 120 to 180 | Isolate the pitch in one labelled section rather than spreading it |
| 11 | **FAQ** | H2 + H3 each | 300 to 500 | 5 to 8 questions phrased as search queries. Keep FAQPage markup |
| 12 | Related guides | | | 3 to 6 siblings |

**Schema minimum:** BlogPosting or TechArticle, BreadcrumbList, FAQPage, ItemList
of the ranked apps, SoftwareApplication and Offer for ours. ExtraDock and
Chronoid carry the richest markup and rank for the hardest terms.

## FAQPage: the correction

An earlier plan said do not use it. That was half right and I checked Google's
changelog directly. Verbatim:

> **Deprecating the FAQ rich result feature.** This feature will no longer appear
> in Google Search starting May 7, 2026.

> **Removing documentation for the FAQ rich result feature.** The FAQ rich result
> feature is no longer shown in Google Search results.

So the rich result is genuinely dead. **But the markup is harmless and five of
six ranking pages still ship it**, and it still feeds AI extraction. Keep it.
Just do not expect a search feature from it.

## Edges held by exactly one page, worth stealing

| Page | Edge | Take it? |
|---|---|---|
| **Droppy** | **Excludes itself from its own list entirely.** Declares bias: "here I have a bias to declare... it is a paid app. I will not pretend otherwise." Closes: "Most people never reach the paid column, and that is exactly how it should be." Shortest page in the set and links every app to its official site | **Yes.** Maximum credibility per word. Use for one listicle |
| **Noticky** | Buttons handing ChatGPT, Claude and Perplexity a pre-written prompt asking for "who should skip it" | **Yes.** Cheap, and aims at the AI answer surface directly |
| **Noticky** | An "Open Source" yes/no column in the comparison table | **Yes.** A buying criterion nobody else exposes |
| **Timing** | A "Power-user tip:" field on every entry | **Yes.** Turns a list into a manual, and justifies length honestly |
| **ExtraDock** | Taxonomy before the list: "The Three Flavors of Dock Apps", then a badge on every card | **Yes.** Teaches a frame the reader lacked, then ranks inside it |
| **supasidebar** | A routing box above the TL;DR bouncing wrong-intent readers to sibling guides | **Yes.** Keeps a mismatched reader on the site |
| **Chronoid** | Review and AggregateRating schema | **Not yet.** Gated on having real reviews, which we do not |

## How to beat ExtraDock specifically

They own `/alternatives/best-macos-dock-alternatives` with 8 apps, 12 FAQ entries
and a taxonomy frame. Their weaknesses are precise:

- **No author byline at all.** No editorial voice.
- **Links only their two partner apps.** The other six rivals get no link.
- **No per-profile Chrome capability listed**, because none of them have it.

A page that takes Droppy's honesty posture, Noticky's field template with price
in the heading, and ExtraDock's own taxonomy frame beats them on the axis they
are weakest: editorial trust.
