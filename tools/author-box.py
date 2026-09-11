#!/usr/bin/env python3
"""Insert the EEAT author box into every answer, blog and compare page.

Idempotent: skips a page that already has one. Run from splitdock-releases/.
"""
import glob, re, sys

BOX = '''<div class="authorbox">
  <img src="{up}assets/mark.png" width="56" height="56" alt="">
  <div>
    <p class="name">Mahad Kazmi</p>
    <p>Independent macOS developer and the author of Superdock. I switched to a Mac from Windows, lost the per profile taskbar buttons I relied on, and built the dock I wanted instead. I write these guides from daily use of the apps in them, and I answer the support email myself.</p>
    <p class="profiles"><a href="https://github.com/Mahadkz" rel="me noopener" target="_blank">GitHub</a> · <a href="https://www.linkedin.com/in/syed-mahad-kazmi/" rel="me noopener" target="_blank">LinkedIn</a> · <a href="{up}about.html">About</a> · hello@superdock.app</p>
  </div>
</div>
'''

def main():
    targets = sorted(set(glob.glob("answers/*.html") + glob.glob("blog/*.html") + glob.glob("compare/*.html")))
    done = skipped = 0
    for p in targets:
        if p.endswith("index.html"):
            skipped += 1; continue
        s = open(p).read()
        if 'class="authorbox"' in s:
            skipped += 1; continue
        # insert just before the closing </article>
        m = s.rfind("</article>")
        if m == -1:
            print(f"  NO </article>: {p}"); skipped += 1; continue
        s = s[:m] + BOX.format(up="../") + s[m:]
        open(p, "w").write(s)
        done += 1
    print(f"author box added to {done} pages, {skipped} skipped")
    return 0

if __name__ == "__main__":
    sys.exit(main())
