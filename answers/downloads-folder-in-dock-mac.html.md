<!-- Markdown twin of https://superdock.app/answers/downloads-folder-in-dock-mac.html -->

# How to get the Downloads folder back in your Mac's Dock

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. Open Finder, press Command-Shift-H for your Home folder, and drag Downloads onto the Dock to the right of the thin divider line. Anything dropped to the left of it becomes an app shortcut instead, which is the usual reason this does not work the first time. Then right-click it and set Sort by: Date Added and View content as: Grid, so the file you just saved is the first one you see.

## Why it vanished

The Dock has two halves, split by a thin divider. Apps live on the left, folders and the Trash on the right. Dragging any item out of the Dock removes it, and a folder dragged away is gone from the Dock but untouched on disk. Nothing was deleted. Your files are still in ~/Downloads.

## Putting it back

- Open your Home folder. In Finder, press Command-Shift-H.

- Drag Downloads onto the Dock, to the right of the divider, near the Trash.

- Right-click it and choose Sort by Date Added, Display as Folder, and View content as Grid.

The order matters more than it looks. Sorted by Name, the file you just downloaded could land anywhere in the list. Sorted by Date Added, it is always first.

## Fan, Grid or List

Apple gives three ways to show a stack, and they suit different folders.

- Grid shows icons with names, scrolls, and previews images. Best for Downloads.

- List is compact text with submenus for nested folders. Best for a deep folder like Documents.

- Fan curves a few items upward. It looks nice and stops being readable past about ten files.

## What Superdock changes

Superdock draws its own dock, so folders work the same way but without the setup. Downloads is already there on first launch if your Dock has no folders, sorted newest first, opening as a grid or list. Click a file to open it, or open the whole folder in Finder.
The difference you will notice is that the stack stays put while you use it, and folders come before files so a folder of screenshots does not get buried under the screenshots.

## If it still will not stay

Two things undo this. Dropping the folder to the left of the divider makes an app shortcut that opens Finder rather than a stack. And if the Dock is set to auto-hide, a slow drag can release over the desktop instead of the Dock, which looks like the folder refusing to stick. Turn auto-hide off while you do it, then back on.

## Frequently asked questions

### Did removing it from the Dock delete my downloads?

No. The Dock holds a shortcut, not the folder. Your files are still in your Home folder under Downloads, and you can reach them in Finder with Command-Shift-H or from the Finder sidebar.

### Why does my Downloads folder open a Finder window instead of a stack?

It was dropped on the left of the Dock's divider, where apps live, or Display as is set to Folder with View content as set to Automatic. Right-click it and choose View content as Grid or List.

### How do I make the newest file appear first?

Right-click the folder in the Dock and choose Sort by Date Added. Sorting by Name is the default and puts the newest file wherever the alphabet puts it.

### Can I put other folders in the Dock too?

Yes, any folder, as long as it goes to the right of the divider. Screenshots, a current project, or a client folder are common ones. Superdock treats them the same way and keeps folders above files inside the stack.

### Does Superdock need setting up for this?

No. If your Dock has no folders when Superdock first runs, it adds Downloads for you, sorted newest first. You can remove it, and it will not come back.

