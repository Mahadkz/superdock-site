<!-- Markdown twin of https://superdock.app/answers/cmd-tab-skips-minimized-windows.html -->

# Why does Command-Tab skip minimized and hidden windows?

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. Because Command-Tab switches applications, and macOS treats a minimized window as parked in the Dock rather than as part of the app's visible set. Switching to the app therefore leaves it parked. Hold Option as you release Command and one minimized window is restored. Hidden apps behave differently: they come back normally, because hiding is a property of the app rather than the window.

## Minimized and hidden are not the same thing

This confuses almost everyone, and the distinction explains the behaviour.
Hiding an app with Command and H hides the application. Command-Tab brings it back with every window where it was. Nothing is lost, and this is why many people use hiding instead of minimizing.
Minimizing a window with Command and M is a property of that window, not the app. The window goes to the right side of the Dock and macOS considers it parked. Switching to the app does not unpark it.
So Command-Tab does not skip hidden apps. It skips minimized windows, and only those.

## The Option trick

- Hold Command and press Tab until the app is selected.

- While still holding Command, press and hold Option.

- Release Command with Option still held.

One minimized window is restored. You cannot choose which, and there is no way to cycle through them from the switcher.

## Why it works this way

macOS is application-centric. The Dock lists applications, Command-Tab switches applications, and Force Quit quits applications. A window is something an app owns, not something the system tracks on your behalf.
Minimizing deliberately removes a window from the app's active set and puts it somewhere visible instead, which is the Dock. From that point of view the behaviour is consistent, even though it is not what you wanted.

## What to do instead

The simplest change is to stop minimizing. Hide the app with Command and H, and Command-Tab brings everything back the way you left it. For a lot of people that single habit change removes the problem entirely.
If you want minimized windows visible in a switcher, you need one that lists windows rather than apps. AltTab is free and open source and does this, showing minimized windows dimmed so their state is obvious. For most people that is the whole answer and no further tool is needed.

## Frequently asked questions

### What is the difference between hiding and minimizing?

Hiding applies to the whole app and Command-Tab restores it normally. Minimizing applies to one window, which macOS then parks in the Dock and does not restore on app switch.

### Can I restore all minimized windows of an app at once?

Not with a native shortcut. The Window menu lists them individually and you restore them one at a time.

### Why does Command-Tab sometimes seem to do nothing?

Because every window of the app is minimized or hidden. The app becomes frontmost with nothing to show. Option on release brings one window back.

### Should I stop minimizing altogether?

Many people do, in favour of Command and H. It avoids this problem and keeps the right side of the Dock clear.

