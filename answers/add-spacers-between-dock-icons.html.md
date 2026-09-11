<!-- Markdown twin of https://superdock.app/answers/add-spacers-between-dock-icons.html -->

# How to add spacers between Dock icons

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. Run defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}' then killall Dock. A blank gap appears at the end of the Dock and you drag it where you want. Repeat for more. To remove one, drag it out of the Dock like any icon. Use small-spacer-tile for a narrower gap.

## The command

Open Terminal and run these two lines together:
defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}'
killall Dock
A blank space appears at the right end of the application section. Drag it to wherever you want the gap. Run the command again for each additional spacer.

## What each part does

- defaults write changes a preference value.

- com.apple.dock is the Dock's preference domain.

- persistent-apps is the list of items in the left section, the pinned applications.

- -array-add appends to that list rather than replacing it, which is the important part. Without it you would wipe your Dock.

- killall Dock restarts the Dock so it reloads its preferences. Your windows and apps are unaffected.

Worth knowing what you are pasting. A command that writes to persistent-apps without -array-add will replace every pinned app you have.

## Variants

A narrower gap: use small-spacer-tile instead of spacer-tile.
A gap in the right section, where folders and the Trash live, uses persistent-others in place of persistent-apps.
defaults write com.apple.dock persistent-others -array-add '{"tile-type"="spacer-tile";}'
killall Dock

## Removing a spacer

Drag it out of the Dock and hold until Remove appears, exactly as you would with an app icon. There is no separate command needed.

## What this does not give you

Apple's Dock has no visible divider, only blank space. There is no line, no colour, and no way to label a group. The spacer is also invisible, so it can be fiddly to grab when you want to move it later.
A dock replacement that draws its own tiles can offer real dividers, fixed-width spacers and flexible spacers that push groups apart, configured in a settings window rather than in Terminal. That is a reason to replace the Dock, not a reason to avoid the command above, which is free and works today.

## Frequently asked questions

### Will this break my Dock?

No, as long as you include -array-add. That appends a spacer rather than replacing the list. Without it, the command overwrites every pinned app.

### Do spacers survive a restart?

Yes. They are stored in the Dock's preferences like any other item.

### Why can I not see the spacer I just added?

It is transparent, and it lands at the right end of the applications section. Look for a gap before the divider line, then drag from there.

### Is there a way to do this without Terminal?

Not with Apple's Dock. Several dock replacements offer spacers and dividers in their settings, which is the only way to avoid the command line here.

