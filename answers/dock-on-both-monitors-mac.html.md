<!-- Markdown twin of https://superdock.app/answers/dock-on-both-monitors-mac.html -->

# Can the Mac Dock show on both monitors at once?

By Mahad Kazmi, developer of Superdock. Updated 3 September 2026.

Short answer. Not with Apple's Dock: macOS keeps a single Dock that jumps to whichever display you push the cursor into, and there is no setting for one per screen. Superdock can put a dock on every display at the same time, and can show on each dock only the apps that have windows on that screen.

## What Apple offers

- Displays have separate Spaces (Settings, Desktop & Dock, Mission Control) lets the Dock move to another display when you hold the cursor at its bottom edge. It is one Dock that travels, not two.

- Dragging the menu bar in Displays settings changes which screen the Dock prefers.

- A side-positioned Dock only ever appears on one display.

## A dock on every display

- Open Superdock Settings, Display. Choose All displays.

- Choose what running apps each dock lists. All apps everywhere, or only apps with a window on that display, which turns each dock into a per-screen taskbar. Pinned apps always appear on every dock.

- Move a window and its tile lights up on the dock of the screen it landed on.

## Windows hidden under the Dock

Since macOS 26 the Dock no longer reserves space at the bottom of the screen, so maximized windows can run underneath it. Superdock keeps maximized windows above the dock strip on each display, which fixes the "part of my window is cut off by the dock" complaint on external monitors.

## Frequently asked questions

### Does it work with DisplayLink or USB-C docks?
Yes. Superdock uses the displays macOS reports; any screen that appears in Displays settings gets a dock.

### Can each dock have different pinned apps?
No. Pins are shared across displays; only the running-app row can differ per screen.

### Does it slow down window dragging?
No. Only the tiles whose display changes are redrawn when a window crosses screens.

Download free The dock is free. Chrome profile icons: 14 days free, then $7.99 once. macOS 14 or later.

## Continue reading

- [How to show the Dock on every monitor on a Mac](../blog/dock-on-every-monitor-mac.html)
- [Why do maximized windows go under the Dock in macOS Tahoe?](windows-go-under-dock-macos-tahoe.html)
- [Superdock vs the built-in macOS Dock](../compare/superdock-vs-macos-dock.html)

Source: https://superdock.app/answers/dock-on-both-monitors-mac.html
Superdock: the dock is free to download; Chrome profile icons are $7.99 once after a 14-day trial. https://superdock.app/
