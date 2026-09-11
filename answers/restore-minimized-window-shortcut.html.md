<!-- Markdown twin of https://superdock.app/answers/restore-minimized-window-shortcut.html -->

# Keyboard shortcut to restore a minimized window

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. Hold Command and Tab to reach the app, then hold Option as you release Command. macOS restores one minimized window instead of just activating the app. It only ever restores one, and you cannot choose which. For anything more than that the Window menu lists every minimized window by name, and a window switcher lists them with thumbnails.

## Why Command-Tab ignores minimized windows

Command-Tab switches applications, not windows. When you release it, macOS activates the app and brings forward whatever windows are already open. A minimized window is not open in that sense. macOS treats it as parked in the Dock, so activating the app leaves it parked.
If every window of an app is minimized, Command-Tab appears to do nothing at all. The app becomes frontmost with no visible window, which is exactly the confusing behaviour that sends people searching for this shortcut.

## The Option trick, precisely

- Hold Command and press Tab until the app you want is selected.

- Before releasing Command, press and hold Option.

- Release Command while still holding Option.

One minimized window comes back. Which one is not something you control, and there is no way to step through them from here.

## When you have several

The Window menu is the reliable native answer. Every app lists its windows at the bottom of that menu, minimized ones included, by name. It is slower than a shortcut and it always works.
App Expose, Control and Down arrow, shows the front app's windows. In current macOS versions minimized windows appear in a separate row beneath the others, so this is worth trying before reaching for the menu.
What none of these give you is one keystroke to a specific minimized window. That is the gap, and five of the six top results for this question are forum threads rather than products, which suggests it has never been answered well.

## The switcher approach

A window switcher enumerates windows rather than applications, so minimized windows are simply part of the list, usually dimmed to show their state. Selecting one restores it.
AltTab does this, is free and open source, and is the answer for most people reading this. Superdock has a switcher too, off by default, which behaves the same way. If switching is the only thing you need, install AltTab rather than a whole dock replacement.

## Frequently asked questions

### Why does Command-Tab do nothing for some apps?

Because every window of that app is minimized or hidden. The app becomes frontmost but has nothing to show. Hold Option as you release Command to bring one window back.

### Can I restore all minimized windows at once?

Not with a native shortcut. The Window menu restores them one at a time, and some window managers can restore a saved layout.

### Is minimizing worth avoiding?

Many people switch to hiding an app with Command and H instead, because hidden apps come straight back with Command-Tab. Minimizing is the one that creates this problem.

### Does the Option trick work on every macOS version?

It has worked for many releases and still does in macOS 26. If it fails, check that Command-Tab itself is not being intercepted by another utility.

