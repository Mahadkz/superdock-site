<!-- Markdown twin of https://superdock.app/answers/separate-dock-icon-for-each-chrome-profile-mac.html -->

# Can I have a separate Dock icon for each Chrome profile on a Mac?

By Mahad Kazmi, developer of Superdock. Updated 3 September 2026.

Short answer. Yes. macOS shows one Dock icon per running process and every Chrome profile runs inside the same process, so Apple's Dock cannot do it. Superdock draws its own Dock and gives each profile its own icon, with the profile's avatar, its own window list and its own previews, while Chrome keeps running as one app.

## Why Apple's Dock merges Chrome profiles

The Dock keys a tile to a process, not to a window. Google Chrome opens all your profiles, work, personal, client, inside one process, so the Dock sees one app and stacks every window under a single icon. Right-clicking it lists windows by title with no hint of which profile owns them, and clicking it brings forward whichever window was last in front.

## The three ways to get one icon per profile

| Method | Extra login? | Extra memory? | Extensions and sync | Cost |

| Superdock (own Dock, one Chrome process) | No | No | Unchanged | $7.99 once after a 14-day trial; the rest of the dock is free |

| Separate Chrome instances (--user-data-dir, Automator wrapper, Parallel Spaces, chrome-schismator) | Yes, one per instance | Yes, roughly one full Chrome per instance | Set up again per instance | Free to scripted, or a paid wrapper |

| Chrome's own profile shortcuts | No | No | Unchanged | Free, but not available on macOS: the Dock still merges them |

## How Superdock does it

- Download and open Superdock. It replaces the system Dock with one that looks identical, and asks for Accessibility so it can read window titles.

- Open a second profile in Chrome. Chrome adds the profile name to every window title. Superdock reads that name, matches it against Chrome's profile list, and adds a tile with that profile's avatar.

- Use the tiles like any app. Click to bring that profile's windows forward, right-click for only that profile's windows, hover for previews, drag to pin or reorder.

Under the hood Chrome is untouched: one process, one set of extensions, one sign-in per profile as before. Superdock attributes windows to profiles by title, which is why two profiles with the same name cannot be told apart and grouping is disabled for them.

## When a separate instance is the better answer

If you need hard isolation, for example a browser that must never share cookies or extensions with your main one, a separate --user-data-dir instance is the right tool and Superdock shows each instance as its own tile too. For the common case, several Google accounts you switch between all day, the profile approach costs nothing extra and keeps sync working.

## Frequently asked questions

### Does this work with Chrome Beta, Canary, Brave or Edge?
Profile tiles are for Google Chrome. Other Chromium browsers appear as normal app tiles with window previews and the switcher.

### Does Superdock change Chrome?
No. It reads window titles through Accessibility and Chrome's own profile list on disk. Nothing is installed into Chrome and no extension is needed.

### What happens after the 14-day trial?
The dock keeps working for free. Only the per-profile icons need a licence, $7.99 once for up to five Macs.

### Can I pin a profile to the Dock?
Yes. A pinned profile behaves like a pinned app: click it to open that profile, and it stays in place when closed.

Download free The dock is free. Chrome profile icons: 14 days free, then $7.99 once. macOS 14 or later.

## Continue reading

- [Step-by-step: a separate Dock icon for each Chrome profile](../blog/chrome-profile-dock-icons-mac.html)
- [Chrome profiles vs separate instances: memory, logins and Dock icons](../blog/chrome-profiles-vs-separate-instances.html)
- [Superdock vs Parallel Spaces](../compare/superdock-vs-parallel-spaces.html)

Source: https://superdock.app/answers/separate-dock-icon-for-each-chrome-profile-mac.html
Superdock: the dock is free to download; Chrome profile icons are $7.99 once after a 14-day trial. https://superdock.app/
