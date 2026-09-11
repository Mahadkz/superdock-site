# Image style reference

Status: reference only. No prompts written yet. Prompts get built once the
topic list in `content-queue.md` is finalised, so each image is made for a
specific page rather than generated speculatively.

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
