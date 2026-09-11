<!-- Markdown twin of https://superdock.app/answers/dock-not-showing-on-second-monitor-mac.html -->

# Why is the Dock not showing on my second monitor?

By Mahad Kazmi, developer of Superdock. Updated 10 September 2026.

Short answer. Because macOS has only one Dock and moves it between displays rather than showing one per screen. It appears on whichever display you push the cursor to the bottom edge of, and returns to the display holding the menu bar. There is no Apple setting for a dock on each monitor, so a Dock replacement is the only way to have both at the same time.

## How Apple's Dock behaves with two displays

- There is exactly one Dock. It is not per display.

- It lives by default on the display with the menu bar, set in Settings, Displays, by dragging the white bar.

- It moves when you push the cursor to the bottom edge of another display and hold briefly.

- A Dock positioned left or right only ever appears on one display.

## Moving it to the other monitor

- Push the cursor to the bottom of the second display and hold it there past the edge. The Dock follows.

- Make it permanent by opening Settings, Displays, and dragging the menu bar onto the display you want, which moves the Dock's home screen with it.

- Check Mission Control settings if nothing happens. "Displays have separate Spaces" affects this behaviour and needs a log out to change.

## Why it keeps jumping back

The Dock returns to the menu bar display after the cursor leaves, and a display that sleeps or disconnects sends it home too. Changing resolution or unplugging a monitor mid session commonly leaves the Dock on the wrong screen until you push it back.

## A dock on every display at once

- Open Superdock Settings, Display, and choose All displays.

- Choose what each dock lists. Every running app, or only apps with a window on that screen, which makes each dock a per screen taskbar.

- Pinned apps stay on every dock, so your most used apps are always in reach on both monitors.

This part of Superdock is free. It also keeps maximized windows from sliding under the dock strip, which is a separate macOS 26 change that affects external monitors.

## Frequently asked questions

### Is there an Apple setting for a Dock on every display?

No. macOS has one Dock that moves between displays, and no preference adds a second one.

### Why does my Dock move to the wrong screen when I wake the Mac?

Displays wake in an unpredictable order, and the Dock returns to whichever display holds the menu bar. Reconnecting a monitor can also shift it.

### Does hiding the Dock help?

Autohide does not change which display it belongs to. It only changes when it appears.

### Does a second dock use much memory?

No. Each display draws its own tile row from one shared list of apps.

