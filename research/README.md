# Content plan research

`content-plan.csv` is the output. 355 unique page ideas, each with a SERP-verified
target query, an honest angle, and a cannibalization flag.

## How it was built

Eight research agents, one per territory, each returning pipe-separated rows.
`tools/build-content-plan.py` deduplicates by slug, merges rows found in more than
one territory, and screens every slug against the LIVE sitemap.

| Territory | Rows |
|---|---|
| Troubleshooting | 83 |
| Dock and window management | 62 |
| Chrome profiles and identity | 59 |
| Switchers and Windows migration | 59 |
| Alternative and versus pages | 54 |
| Trust and buying objections | 16 |
| Audience verticals | 12 |
| Listicles | 10 |

## The columns

- **cannibalization**: `clean`, or `CHECK: <live page>` when slug tokens overlap a
  published page. **A CHECK needs a human verdict before writing:** WRITE,
  RESHAPE, SKIP or FOLD. 135 rows carry one.
- **our_angle**: one sentence, or `NONE` where a dock utility does not honestly
  solve the problem. **46 rows say NONE and that is deliberate.** Recording where
  we do not belong is as useful as recording where we do, and a listicle we are
  absent from is the page other people can link to.
- **priority**: 1 to 5, 5 highest. 60 rows are priority 5 with an honest angle, and 32 of those are also free of any cannibalization flag. Those 32 are the build-first set.

## What the research overturned

- **Alternative pages were the gap.** We had 12 `superdock-vs-X` pages and zero
  `X-alternative` pages. Somebody searching "Superdock vs uBar" already knows we
  exist; somebody searching "uBar alternative" does not, and there are more of them.
  64 alternative pages are now mapped.
- **Dead incumbents with live searchers are the cheapest wins.** cDock's last build
  is from November 2020 and needs SIP disabled. HyperDock and HyperSwitch are
  unmaintained. Contexts was discontinued in 2026. All four still have people
  asking what replaced them, and no vendor is defending those queries.
- **Three audiences were dropped on evidence.** Media buyers and Amazon
  multi-account sellers need fingerprint isolation, which is an antidetect browser
  problem we do not solve, and the Amazon case means writing for people working
  around platform policy. Recruiters and realtors produced no usable evidence: the
  recruiter quote turned out to be a job seeker.
- **Two audiences invented our product by hand.** MSPs juggling client tenants and
  bookkeepers switching QuickBooks practices both describe our exact workflow in
  their own words, which is the strongest signal in the set.


## The three clusters worth building first

1. **Chrome profiles.** The head queries are held by a 2012 Stack Exchange thread
   and a 2025 Apple thread that wrongly claims macOS removed the ability. No
   product ranks, and this is directly monetisable against the paid feature.
2. **Per-display docks.** Every forum answer on "dock on all monitors" ends in
   "you cannot", which is true of Apple's Dock and false of ours. The strongest
   honest gap in the set.
3. **Permissions.** `accessibility-permission-keeps-resetting` and
   `screen-recording-permission-not-working` are pure confusion SERPs. The real
   causes, that TCC is keyed to the code signature and that the screen-recording
   grant is cached per process until relaunch, are in our own learnings and stated
   plainly nowhere on page one.

Apple Discussions holds position one on almost every troubleshooting query
sampled, with Reddit and Stack Exchange at two to four and publishers only from
four down. Forum-held is the default state of this territory rather than the
exception, which is why priority rather than forum-only separates the winners.

## Honest caveats

- **No keyword volumes.** Displaceability is inferred from SERP composition, not
  measured demand. Validate in a keyword tool before committing budget.
- **Not every row was individually SERP-checked.** Agents hit rate limits and
  extrapolated some rows from a verified parent query within the same cluster. One
  agent that re-checked its own inferences found two of three were optimistic.
  **Treat non-priority-5 rows as needing a spot-check.**
- **Three rows need social proof we do not have** and are flagged in place.
- `superdock-review` should never be written by us.
