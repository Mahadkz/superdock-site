<!-- Markdown twin of https://superdock.app/answers/mac-app-switcher-with-thumbnails.html -->

# Can the Mac app switcher show window thumbnails?

By Mahad Kazmi, developer of Superdock. Updated 10 September 2026.

Short answer. Not Apple's. Command-Tab shows one large icon per app and no window thumbnails, so two Chrome windows are a single entry you cannot tell apart. Mission Control shows real thumbnails but does not let you cycle with the keyboard. A window switcher combines the two: hold Option, press Tab, and every window appears as a live thumbnail you can step through.

## What Apple gives you

- Command-Tab shows application icons, one per app, at a fixed size. No thumbnails, no window titles, no per window entries.

- Mission Control (Control-Up) shows live thumbnails of every window, but it is a mouse driven overview rather than a keyboard cycle.

- App Expos&eacute; (Control-Down) shows thumbnails for the front app only.

There is no setting anywhere in macOS that adds thumbnails to Command-Tab. It has looked the same for many releases.

## Why icons are not enough

An icon identifies an app, not a window. If you have three Finder windows, two Chrome profiles and four documents in the same editor, Command-Tab shows three icons and you are guessing. The moment your work is spread across windows rather than apps, the switcher stops matching how you actually think about it.

## Adding thumbnails

- Enable the window switcher in Superdock, in Settings, Behavior. It is off by default.

- Hold Option and press Tab. A centred panel shows every open window as a thumbnail with its title and app icon, most recent first.

- Grant Screen Recording if you want live thumbnails. Without it the switcher still works and shows the app icon and window title instead.

Minimized windows appear in the list, dimmed, and are restored when you pick one. That alone covers the most common complaint about Command-Tab.

## Hover previews on the dock

If you would rather stay on the mouse, dock hover previews solve the same problem from the other direction: point at a dock tile and its windows appear as thumbnails, the way the Windows taskbar does. That is free in Superdock, and DockDoor adds it to Apple's own Dock.

## Frequently asked questions

### Can I add thumbnails to Command-Tab with a setting?

No. macOS has no option for it, and the app switcher has worked this way for many releases.

### Do live thumbnails need a permission?

Yes, Screen Recording, and it is optional. Without it you still get the window list with app icons and titles.

### Do thumbnails slow the Mac down?

No. They are captured when the switcher opens rather than continuously.

### Is there a free way to get this?

Yes. AltTab is free and open source and does window switching with thumbnails. Superdock's switcher is also free.

