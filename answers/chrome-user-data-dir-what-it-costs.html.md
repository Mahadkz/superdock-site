<!-- Markdown twin of https://superdock.app/answers/chrome-user-data-dir-what-it-costs.html -->

# What separate Chrome instances actually cost you

By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.

Short answer. About 2.8 times the memory, plus a sign-in to every account again, plus broken automatic updates. We measured one Chrome with three profiles and roughly 35 tabs at 1.67 GB across 11 processes, and the same three profiles as separate instances at about 4.6 GB across 33 processes. Separate instances do genuinely produce real Dock icons, which is why people put up with all of that.

A disclosure, because this measurement favours the product I make. I build Superdock, which separates Chrome profiles without separate instances, so I had an interest in the answer. The method is below so you can repeat it and disagree.

## What people are actually doing

macOS gives one Dock icon per running process, and every Chrome profile runs inside one process. So a popular workaround is to launch Chrome with its own data folder using the --user-data-dir flag, usually wrapped in an Automator app or a shell script.
macOS then sees a genuinely separate application, and you get a genuinely separate Dock icon. It works. The question is what it costs.

## The measurement

Method. One Mac, one set of three signed-in Google profiles, the same extensions installed in each, and about 35 tabs spread across them. Memory read from Activity Monitor as the total for all Chrome processes, measured twice: once with the three profiles running inside a single Chrome, and once with three instances each launched with its own --user-data-dir.

SetupMemoryProcesses
One Chrome, three profiles1.67 GB11
Three separate instancesabout 4.6 GBabout 33

That is a ratio of roughly 2.8 to 1. Your figure will differ with extensions, tab count and what those tabs contain. The direction will not, and the reason is structural.

## Why it costs that much

A Chrome profile is a set of preferences bound to a set of windows inside one running browser. The browser process, the GPU process, the network service and the extension host are shared across every profile.
A separate instance duplicates all of it. Each one is a whole browser: its own browser process, its own GPU process, its own network service, its own copy of every extension. The process count tells the story more clearly than the memory figure does, at 11 against 33.

## The two costs nobody mentions

You sign in again, everywhere. A separate data directory means separate cookies, so every account in every instance needs a fresh sign-in, including two-factor. People describe this as the part that made them give up.
Updates break. Chrome's updater is tied to the application bundle. Tools that duplicate Chrome.app to get a separate icon often have to disable or remove the update mechanism, which means a browser that stops receiving security updates. That is a real risk, not a theoretical one.

## What separate instances are genuinely good at

Being fair, because this matters. Separate instances give you true isolation. Different cookie jars, different storage, no possibility of one identity leaking into another through a shared browser state. If you are testing a site as two users at once, or you need certainty that two accounts cannot see each other, that isolation is the feature and the memory is the price.
They also produce a real system Dock icon with no third-party software at all, which no other approach does.

## The alternative

If what you actually want is to tell your profiles apart and click straight into the right one, you do not need a second browser. Superdock draws its own dock, so it can show one tile per profile with that profile's avatar while Chrome keeps running as a single process. Your memory, your logins and your updater are untouched.
That is the narrow claim. It does not give you isolation, and if isolation is what you need then separate instances remain the correct tool despite the cost.

## Frequently asked questions

### Is the 2.8 times figure reliable?

It is one measurement on one machine with three profiles and about 35 tabs, and I have given the method so it can be repeated. Treat it as an indication of scale rather than a constant. The process count of 11 against 33 is the more stable signal.

### Does Chrome's Memory Saver change this?

It helps within an instance by discarding idle tabs. It does not remove the duplicated browser, GPU and network processes, which is where the structural cost sits.

### Do separate instances share extensions?

No. Each instance has its own extension host and its own copies, which is part of the memory cost and means configuring each extension repeatedly.

### Is there any way to get a separate Dock icon without a separate instance?

Not from Apple's Dock, because it allocates one tile per process. A dock replacement that draws its own tiles can do it, which is the approach Superdock takes.

