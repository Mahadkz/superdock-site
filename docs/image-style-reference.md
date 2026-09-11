# Image style reference

Status: **SETTLED 12 September 2026.** Palette and object vocabulary decided
from the app icon. Prompts are in `image-prompts-batch-1.md` onward.

## Why this doc exists
The owner generates images in bulk via Gemini using long, highly specified
single-line prompts. The prompt format is proven and should be reused. What is
NOT yet decided is our palette, our object vocabulary, and which pages need art.

## The reference format (from the owner's other project)
That project used a blue-violet palette. **It is a format reference, not our
palette.** Superdock images will look different. What to carry over:

1. **One line per prompt.** No line breaks inside a prompt.
2. **Fixed opening clause**: render type, aspect and exact pixel size.
3. **Named background gradient with hex codes**, plus "not pure white" or
   "not pure black" to stop the model flattening it.
4. **Explicit empty region for text**: "leaving the entire left third completely
   empty for text". This is what makes an image usable as a hero or OG card.
5. **A crop-at-the-edge scale device** so the object reads as physical.
6. **One object cluster, never a scene.** A single idea, caught mid-action.
7. **Mid-action framing**: "caught at the exact instant", "mid-rotation",
   "caught mid-lift". The frozen moment is what gives these images tension.
8. **Blank surfaces stated repeatedly**: rows as "soft blank lines with no
   readable text". Generators produce garbled text otherwise.
9. **Hard negatives at the end**: no text, no words, no letters, no numbers,
   no logos, no people.
10. **Fixed closing clause**: "Photorealistic, high detail, octane render, clean".
11. **Variants per concept** (a/b/c): right-half light, left-half dark,
    low-in-frame light. Gives layout options without re-specifying the concept.

## What must change for Superdock

### Palette
The site is a dark UI: `--bg #08080a`, `--bg-soft #0f0f13`, accent `--accent
#2e93ff`, button `--accent-btn #1669e0`. Existing art is `assets/hero.jpg`,
`hero-wall.jpg`, `overview.jpg`, `compare.jpg`.

Open question for the owner: do images match the dark UI, or contrast with it?
Decide before writing prompts. Do not assume the reference project's
blue-violet.

### Object vocabulary
The reference project's objects were freight and paperwork: trailers, kingpins,
receipt spikes, fuel cards. None of that applies here.

Superdock's actual subject matter is windows, tiles, profiles, displays and
identity. Candidate objects, to be agreed before prompts:
- stacked translucent panes separating into distinct labelled-but-blank cards
  (one Chrome icon becoming several profile tiles)
- a row of chrome tiles on a rail, one lifting or lighting
- two identical panes with one gaining a distinguishing mark (work vs personal)
- a single pane duplicating across two or three separate surfaces (multi display)
- a fan of panes collapsing into one, or one fanning out (the switcher)
- a chrome rail with an empty slot at each end catching light (edge actions)

### Where images are actually needed
Unknown until topics are final. Likely: one OG card per listicle, one hero per
pillar page. Answer pages currently use the app icon and may not need art.

## Before writing prompts, settle
1. Final topic list (in progress, `content-queue.md`).
2. Light or dark images against a dark site.
3. The object vocabulary above, agreed or replaced.
4. How many images per piece, and at what sizes (OG is 1200x630, hero is wider).
5. Whether images are decorative (then `alt=""`) or informative (then real alt
   text, which affects SEO and accessibility).

---

# SETTLED DECISIONS (12 September 2026)

## Palette, taken from the app icon

The icon answered the open question. It is **three white tiles on near-black**:
one upright in the centre, two fanning outward. That is the brand in one image,
and it is also literally what the product does.

| Role | Hex | Where it comes from |
|---|---|---|
| Deep ground | `#08080a` | site `--bg` |
| Raised ground | `#0f0f13` | site `--bg-soft` |
| Icon charcoal | `#343437` to `#3a3a3e` | sampled from the icon body |
| Tile white | `#ffffff` | the icon's tiles |
| Warm ink | `#f4f4f6` | site `--ink` |
| Accent blue | `#2e93ff` | site `--accent` |
| Deep accent | `#1669e0` | site `--accent-btn` |

**Images are dark and match the UI.** A light image on this site would read as a
foreign object. Blue is an accent only, used for the one lit element, never as a
field.

## Object vocabulary, locked

Derived from the icon rather than invented. Every prompt uses these and nothing
else, so the set stays coherent across sixty images.

| Object | Means |
|---|---|
| **Upright white tile** | one app, one identity, the thing that is yours |
| **Tiles fanning outward from one** | one icon becoming several profiles. The core product idea |
| **A rail of tiles** | the dock itself |
| **Two identical tiles, one gaining a mark** | work versus personal |
| **One tile duplicated across separate planes** | a dock on every display |
| **A fan of panes collapsing into one** | the window switcher |
| **An empty lit slot at the end of a rail** | edge actions |
| **A tile dimming while its neighbours stay lit** | running versus not running |

Materials: matte charcoal grounds, milk-white tiles with soft edge bevels, a
single blue light source. No chrome, no glass, no freight, no paperwork.

## Sizes

| Use | Size | Empty region |
|---|---|---|
| OG card, every page | 1200x630 | left third |
| Blog hero | 1536x1024 | left third or top third |
| Inline diagram | 1200x800 | none, object centred |
