<!-- Markdown twin of https://superdock.app/answers/alt-tab-not-working-on-mac.html -->

# Why is Alt-Tab not working on my Mac?

By Mahad Kazmi, developer of Superdock. Updated 10 September 2026.

Short answer. Because on a Mac the switching shortcut is Command-Tab, not Alt-Tab. The Alt key is labelled Option, and Option-Tab is not bound to anything by macOS, so pressing it appears to do nothing. Command-Tab also switches between apps rather than windows, which is why it still feels wrong to anyone coming from Windows. A window switcher gives you the Windows behaviour on Option-Tab.

## The key is called Option

On an Apple keyboard the key in the Alt position is Option, often printed with the symbol next to the word alt. Pressing Option and Tab together does nothing on a stock Mac, because macOS binds app switching to Command-Tab instead.

## What each shortcut actually does

- Command-Tab cycles applications, one entry per app, icons only. Two Chrome windows are one entry.

- Command-Backtick cycles the windows of the frontmost app only.

- Option-Tab is unbound by default, which is why it looks broken.

- Control-Up opens Mission Control, which shows everything but does not cycle.

## If Command-Tab is also not working

- Check the app is not full screen. Some full screen apps and games capture the keyboard.

- Check Keyboard Shortcuts. In Settings, Keyboard, Keyboard Shortcuts, Keyboard, confirm "Move focus to next window" and the app switcher entries are enabled.

- Check for a remapping tool. Karabiner Elements and similar utilities can capture Command-Tab.

- Restart the Dock. The app switcher is drawn by the Dock process; log out and back in if it stops responding.

## Getting real Alt-Tab behaviour

- Turn on the window switcher in Superdock, from the menu bar icon or Settings, Behavior. It is off until you enable it.

- Hold Option and press Tab. Every window from every app appears as a thumbnail with its title, most recent first, minimized windows included.

- Release Option to bring the selected window forward.

Tab moves forward, Shift-Tab back, arrow keys work and Escape cancels. If you would rather it took over Command-Tab, that is a setting.

## Frequently asked questions

### Is there an Alt key on a Mac keyboard?

Yes, it is the Option key. On most Apple keyboards it is printed with both the Option symbol and the word alt.

### Why does Command-Tab not show my minimized windows?

Because it activates an app rather than a window, and macOS treats a minimized window as parked in the Dock. Holding Option as you release Command restores one.

### Can I remap Alt-Tab to the app switcher?

macOS has no built-in way to rebind the app switcher to Option-Tab. A window switcher that registers its own shortcut is the practical route.

### Does the switcher need any permissions?

Accessibility, to see the window list. Screen Recording is optional and only used for live thumbnails.

