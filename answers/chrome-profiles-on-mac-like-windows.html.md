<!-- Markdown twin of https://superdock.app/answers/chrome-profiles-on-mac-like-windows.html -->

# How do I make Chrome profiles on a Mac work like they do on Windows?

By Mahad Kazmi, developer of Superdock. Updated 3 September 2026.

Short answer. On Windows, Chrome registers each profile as its own taskbar entry, so a pinned Chrome becomes the first profile you open and further profiles appear beside it. macOS has no equivalent, so the Dock shows one Chrome. Superdock reproduces the Windows model exactly: the pinned Chrome slot becomes the first profile opened, other profiles appear next to it, and each can be pinned, unpinned and dragged.

## What Windows does that macOS does not

Windows lets an application tag each window with an AppUserModelID. Chrome uses one per profile, so the taskbar groups windows by profile, shows the profile avatar on the icon, and lets you pin a profile as a first-class shortcut. The macOS Dock has no such hook: it groups by process, full stop. Google could not add per-profile Dock icons even if it wanted to, which is why the Chrome team has never shipped them on Mac.

## The taskbar rule, implemented in a Mac Dock

- Pinned Chrome becomes the first profile you open. Its avatar appears on the tile and a dot marks it running.

- Further profiles appear as their own running tiles beside it, each with its own avatar, right-click window list and hover previews.

- Pin any profile and it becomes a permanent shortcut that opens that profile directly.

- Drag to reorder, drag off the dock to unpin, exactly as on Windows.

## Why not just run several copies of Chrome?

That is what every Windows-style workaround on the Mac does, and it is why they feel wrong: each copy is a separate browser with its own login, extensions, passwords and memory. Windows never asked you to do that, and Superdock does not either. Chrome stays one app; only the Dock changes.

## Frequently asked questions

### Does Alt-Tab work like Windows too?
Superdock includes a window switcher that lists every window with a thumbnail, most recent first, on Option-Tab or Command-Tab. Chrome windows are labelled by profile.

### Can I have the Dock on both monitors, like the Windows taskbar?
Yes. Choose All displays in Settings and each screen gets its own dock; optionally each dock shows only the apps with windows on that screen.

### Does it look like the Windows taskbar?
No. It looks exactly like Apple's Dock, measured pixel for pixel against the real one. Only the behaviour is borrowed.

Download free The dock is free. Chrome profile icons: 14 days free, then $7.99 once. macOS 14 or later.

## Continue reading

- [Can I have a separate Dock icon for each Chrome profile on a Mac?](separate-dock-icon-for-each-chrome-profile-mac.html)
- [How do I Alt-Tab between windows on a Mac like Windows?](alt-tab-between-windows-on-mac.html)
- [Why one Dock icon per Chrome profile](../blog/why-superdock.html)

Source: https://superdock.app/answers/chrome-profiles-on-mac-like-windows.html
Superdock: the dock is free to download; Chrome profile icons are $7.99 once after a 14-day trial. https://superdock.app/
