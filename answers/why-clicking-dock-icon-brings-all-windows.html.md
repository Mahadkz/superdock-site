<!-- Markdown twin of https://superdock.app/answers/why-clicking-dock-icon-brings-all-windows.html -->

# Why does clicking a Dock icon bring all windows to the front?

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. Because the Dock activates an application, not a window. Clicking an icon tells macOS to bring that app forward, and macOS brings every unminimized window it owns. Windows does the opposite, giving each window its own taskbar button. There is no setting in macOS that changes this, so the workarounds are Command and backtick, App Expose, and the Window menu.

## What the click actually does

macOS is built around applications. The Dock is a list of applications, Command-Tab switches applications, and quitting happens to an application. A window is something an application owns rather than a thing the system tracks for you.
So a Dock click means activate this application. Bringing all of its windows forward is the correct behaviour for that instruction, not a bug.
Windows works the other way around. Its taskbar lists windows, which is why each one gets its own button and its own preview. Neither model is wrong, but if you learned the second one first, the first feels broken for months.

## The four native ways to reach one window

- Command and backtick cycles the windows of the app you are already in. Add Shift to go backwards. It skips minimized windows entirely.

- App Expose, which is Control and Down arrow, spreads the front app's windows out so you can click the one you want. This is the closest native answer to the question.

- The Window menu lists every window of the app, including minimized ones, at the bottom. Reliable, and slow.

- Mission Control, Control and Up arrow, shows everything at once but does not let you cycle with the keyboard.

## Where they stop working

All four are adequate for two or three windows that look different. They break in one specific case, and it is a common one: several windows of the same app with near-identical titles. Four browser windows signed into four accounts, or several terminal windows in different directories, look the same in every one of those tools.
App Expose gives you thumbnails, which helps, but you still have to open it, scan and click.

## What actually fixes it

Two approaches genuinely change the click itself rather than adding a step after it.
Hover previews attach a window list to the Dock icon, so pointing at it shows what it owns before you commit to clicking. DockDoor adds this to Apple's own Dock, it is free and open source, and if this is the only thing you want then it is the right tool and you can stop reading here.
A dock that draws its own tiles can go further, because it is not bound to one tile per application. That is what Superdock does, and it is how Chrome profiles get separate tiles. It is also a bigger change to your Mac than DockDoor, so it is only worth it if you want the rest of what it does.

## Frequently asked questions

### Is there a macOS setting to bring only one window forward?

No. There is no preference, hidden default or Terminal command that changes what a Dock click activates. The closest native tool is App Expose on Control and Down arrow.

### Why does Windows do this differently?

The Windows taskbar tracks windows and the macOS Dock tracks applications. Each design follows from that one decision, including why Windows can give every Chrome profile its own button and macOS cannot.

### Does Command and backtick include minimized windows?

No. It cycles only unminimized windows of the front app. The Window menu lists minimized ones, and holding Option while releasing Command-Tab restores one.

### Can I make clicking a Dock icon minimize the app instead?

There is a System Settings option to minimize a window into the app icon, but no native toggle that makes a Dock click hide the app. Some third-party docks add one. Superdock does not.

