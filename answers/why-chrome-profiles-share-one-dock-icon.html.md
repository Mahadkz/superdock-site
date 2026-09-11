<!-- Markdown twin of https://superdock.app/answers/why-chrome-profiles-share-one-dock-icon.html -->

# Why do all my Chrome profiles share one Dock icon?

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. Because the macOS Dock gives one tile per running process, and every Chrome profile runs inside a single Chrome process. Google's own support forum puts it plainly: on Windows the taskbar groups by window, so each profile window can have its own icon, while on Mac the Dock groups by application. There are four workarounds and every one of them has a real cost.

A disclosure before the workarounds. The fourth option below is my own app, and I have tried to be straight about where the other three are the better answer. Two of them are free, and one of them is built into macOS.

## The mechanism, exactly

The Dock is a list of running applications. macOS identifies an application by its process, and creates one tile for each. Chrome runs all of your profiles inside one browser process, so macOS sees one application and draws one tile.
This is not a Chrome bug and it is not an oversight. It follows from the Dock being application-centric, the same design that makes Command-Tab switch apps rather than windows.
Windows made the opposite choice. Its taskbar tracks windows, which is why Chrome can register each profile as its own taskbar button there, complete with a distinct icon. People switching to a Mac notice this within a day and often assume something is misconfigured.

## A claim worth correcting

You will find forum posts saying recent macOS versions removed the ability for browsers to give profiles their own Dock icons. I went looking for evidence and there is none: no Chromium bug, no Chrome release note, no Apple documentation.
What is actually true is duller and more useful. Chrome's Add desktop shortcut button in profile settings is a Windows and Linux feature that has never existed on macOS. Questions about it go back to 2012. Nothing was taken away, which also means nothing is likely to be handed back.

## The four workarounds

1. Use Safari profiles instead
Safari gained profiles recently, and because Shortcuts can open a specific Safari profile, you can put a Shortcut in the Dock with its own custom icon. It genuinely works, it is built into macOS, and it costs nothing.
Cost: you have to move to Safari, and Safari profiles do not separate extensions as thoroughly as Chrome's do.

2. Launch separate Chrome instances
Start Chrome with --user-data-dir pointing at a different folder and macOS treats it as a separate application, so you get a real Dock icon. Usually wrapped in an Automator app or a shell script.
Cost: a lot. Separate data means signing in to every account again, including two-factor. It duplicates the browser, GPU and network processes, which we measured at 1.67 GB becoming about 4.6 GB for three profiles. The community scripts also share one flaw their own authors admit: both icons look identical, so you have solved the count and not the recognition.

3. Duplicate Chrome.app
Copy the application, change its bundle identifier, give it a new icon. Some paid tools automate this.
Cost: roughly 500 MB of disk per copy by one vendor's own admission, the same re-login problem, and the update mechanism usually has to be disabled, which leaves a browser that stops getting security updates.

4. Replace the Dock
A dock that draws its own tiles is not bound to one tile per process, so it can show one tile per profile with that profile's avatar while Chrome carries on as a single process. This is what my app does.
Cost: you are replacing a system component, which is a bigger commitment than a shell script. It needs Accessibility permission to see windows at all. And the profile tiles are the paid feature, at $7.99 once after a 14-day trial, though the dock itself is free.

## At a glance

ApproachCostRe-login?Verdict
Safari profiles and ShortcutsFreeNoBest if you are willing to use Safari
Separate instancesFreeYes, every accountBest if you need true isolation
Duplicated Chrome.appFree or paidYes, every accountHard to recommend, updates break
Dock replacement$7.99 onceNoBest if you want to stay on one Chrome

## What none of them fix

Command-Tab still groups all your Chrome windows under one entry, whichever route you take, unless you also add a window switcher. And no approach changes Chrome itself, so the profile menu inside the browser works exactly as it always did.

## Frequently asked questions

### Can I get separate Dock icons without any third-party software?

Yes, in two ways. Safari profiles with Shortcuts, or launching Chrome with a separate user data directory using a script. Both are free and both have the costs described above.

### Did macOS remove this ability recently?

No. That claim circulates on forums but has no supporting evidence in Chromium's bug tracker, Chrome's release notes or Apple's documentation. Chrome's desktop shortcut feature never existed on macOS.

### Does the same problem affect Edge and Firefox?

Yes. It is a consequence of how the macOS Dock works rather than anything specific to Chrome, so every Chromium browser and Firefox behave the same way.

### Why can Windows do this?

The Windows taskbar groups by window rather than by application, so a browser can register each profile window as its own entry. The two systems made different choices early on.

### Is there a keyboard shortcut to switch Chrome profiles?

No. Chrome offers no menu item, no assignable shortcut and no flag for it. A launcher like Raycast can open a named profile, which is the closest practical substitute.

