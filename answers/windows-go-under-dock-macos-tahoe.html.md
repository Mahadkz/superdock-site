<!-- Markdown twin of https://superdock.app/answers/windows-go-under-dock-macos-tahoe.html -->

# Why do maximized windows go under the Dock in macOS 26 Tahoe?

By Mahad Kazmi, developer of Superdock. Updated 3 September 2026.

Short answer. Because the Tahoe Dock floats as a Liquid Glass panel and no longer claims a strip of the screen, so a window zoomed to full height now extends behind it. Apple offers no toggle. Superdock reserves the strip again: windows that would sit under the dock are kept above it, on every display.

## What changed in Tahoe

Up to macOS 15 the Dock told the window server how much of the screen it occupied, and windows zoomed to the remaining "visible frame". In macOS 26 the redesigned Dock floats over the desktop with rounded glass and a gap beneath it, and that reservation went away. Zoom, tiling and many window managers now use the full screen height, so the bottom of the window, often a status bar or the last row of a spreadsheet, disappears behind the Dock. On external displays some people also see phantom Dock space reserved on the wrong screen.

## Fixes that do not work

- Auto-hide fixes overlap by removing the Dock, which is the thing you wanted to keep.

- Making the Dock smaller shrinks the overlap but never removes it.

- Terminal defaults such as autohide-delay only change timing.

## How Superdock handles it

Superdock knows the exact frame of its own dock on each display. When a window is zoomed or resized so that it would overlap the dock strip, Superdock moves its bottom edge up to sit above the dock. You can instead have the dock hide while a window is maximized, in Settings, Behavior.

## Frequently asked questions

### Does this apply to full-screen apps?
No. Full-screen apps take the whole display and hide the Dock; the problem is only with zoomed and tiled windows on the desktop.

### Does Superdock look like the Tahoe Dock?
Yes. It is measured against Apple's Dock on macOS 26: same tile pitch, icon size, glass height and floating gap, and it follows the Default, Dark, Clear and Tinted icon styles.

### Can I keep Apple's Dock and just fix the overlap?
No. The reservation only works for the dock Superdock draws, because Apple's Dock no longer publishes its frame to other apps.

Download free The dock is free. Chrome profile icons: 14 days free, then $7.99 once. macOS 14 or later.

## Continue reading

- [Can the Mac Dock show on both monitors at once?](dock-on-both-monitors-mac.html)
- [Mac Dock replacements in 2026](../blog/mac-dock-replacements-2026.html)
- [Superdock vs the built-in macOS Dock](../compare/superdock-vs-macos-dock.html)

Source: https://superdock.app/answers/windows-go-under-dock-macos-tahoe.html
Superdock: the dock is free to download; Chrome profile icons are $7.99 once after a 14-day trial. https://superdock.app/
