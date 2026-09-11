<!-- Markdown twin of https://superdock.app/answers/shortcut-toggle-windows-same-app.html -->

# Shortcut to toggle between windows of the same app

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. Press Command and backtick, the key above Tab, to cycle the windows of the app you are in. Shift and the same combination goes backwards. It genuinely works, and it has three limits: it skips minimized windows, it shows no preview, and the backtick key moves on non-US keyboards. Where it fails hardest is several windows of one app with identical titles.

## The shortcut, and what it does

Command and backtick cycles forward through the windows of the frontmost application. Command, Shift and backtick cycles backwards. Both are enabled by default and both are listed in System Settings under Keyboard Shortcuts as Move focus to next window.
If nothing happens when you press it, check that shortcut is enabled, and check the app is not a full screen game or remote desktop session capturing the keyboard.

## Three genuine limits

- It skips minimized windows. A window you tucked away is invisible to the cycle. The Window menu lists it, and holding Option while releasing Command-Tab restores one.

- There is no preview. You cycle blind. With four similar documents open you are pressing the shortcut repeatedly and watching what appears.

- The key moves. On a UK, German or French layout the backtick is not above Tab, which makes a one-handed shortcut a two-handed one.

## The case that defeats it

The shortcut assumes you can tell the windows apart once you see them. That assumption fails with several browser windows signed into different accounts. A question on Ask Different from 2015 puts it plainly, and opens with the author explaining they had two Chrome windows open because they were using multiple Gmail accounts. It is still the top result for this search, and no product has answered it.
The same applies to several terminal windows in different directories, or several documents from one template.

## What helps

If the windows are visually distinct, the native shortcut is enough and you should not install anything.
If they are not, you need something that labels them. AltTab is free and open source and shows every window as a thumbnail with its title, and for most people that is the complete answer.
Superdock labels Chrome windows with the profile they belong to, which is the narrower case where even a thumbnail does not help because the pages look similar. That is the only thing it adds here.

## Frequently asked questions

### What is the backtick key?

On a US layout it is above Tab, sharing a key with the tilde. On other layouts it sits elsewhere, which is one reason this shortcut is unpopular outside the US.

### Why does the shortcut skip some windows?

It cycles only unminimized windows of the frontmost app. Minimized windows are excluded by design, and the Window menu is where you find them.

### Can I change this shortcut?

Yes. System Settings, Keyboard, Keyboard Shortcuts, then Keyboard. Look for Move focus to next window.

### Is there a shortcut that includes other apps?

Command-Tab switches applications rather than windows. For every window from every app in one list you need a window switcher such as AltTab.

