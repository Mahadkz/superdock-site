#!/usr/bin/env node
// Fetch official app icons for listicle pages.
// Usage: node tools/fetch-icons.mjs
// Writes assets/apps/<slug>.png. Skips any file that already exists.
import { writeFile, access } from 'node:fs/promises';
import { createHash } from 'node:crypto';

// Each entry: official source only. Never a competitor's copy of the icon.
const APPS = [
  { slug: 'alttab',      name: 'AltTab',      site: 'https://alt-tab-macos.netlify.app/', icon: 'https://raw.githubusercontent.com/lwouis/alt-tab-macos/master/resources/icons/app/app.iconset/icon_128x128.png' },
  { slug: 'rectangle',   name: 'Rectangle',   site: 'https://rectangleapp.com/',          icon: 'https://rectangleapp.com/assets/images/AppIcon-macOS-Default-512x512@1x.png' },
  { slug: 'raycast',     name: 'Raycast',     site: 'https://www.raycast.com/',           icon: 'https://www.raycast.com/favicon-production.png' },
  { slug: 'maccy',       name: 'Maccy',       site: 'https://maccy.app/',                 icon: 'https://maccy.app/img/maccy/Logo.png' },
  { slug: 'ice',         name: 'Ice',         site: 'https://icemenubar.app/',            icon: 'https://icemenubar.app/gallery/Ice%20Cube.png' },
  { slug: 'linearmouse', name: 'LinearMouse', site: 'https://linearmouse.app/',           icon: 'https://raw.githubusercontent.com/linearmouse/linearmouse/main/LinearMouse/Assets.xcassets/AppIcon.appiconset/Icon-256.png' },
  { slug: 'dockdoor',    name: 'DockDoor',    site: 'https://dockdoor.net/',              icon: 'https://dockdoor.net/Assets/Assets.xcassets/AppIcon.appiconset/AppIcon-iOS-Default-512x512@1x.png' },
];

const exists = async p => { try { await access(p); return true; } catch { return false; } };

let ok = 0, skipped = 0, failed = [];
for (const app of APPS) {
  const out = `assets/apps/${app.slug}.png`;
  if (await exists(out)) { console.log(`skip   ${app.slug} (already present)`); skipped++; continue; }
  try {
    const r = await fetch(app.icon, { redirect: 'follow', headers: { 'User-Agent': 'superdock.app icon fetcher' } });
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    const buf = Buffer.from(await r.arrayBuffer());
    const sig = buf.subarray(0, 8).toString('hex');
    if (!sig.startsWith('89504e47')) throw new Error(`not a PNG (sig ${sig.slice(0,8)})`);
    if (buf.length < 500) throw new Error(`suspiciously small (${buf.length}b)`);
    await writeFile(out, buf);
    console.log(`ok     ${app.slug}  ${(buf.length/1024).toFixed(0)}kb  ${createHash('sha1').update(buf).digest('hex').slice(0,8)}`);
    ok++;
  } catch (e) {
    console.log(`FAIL   ${app.slug}: ${e.message}`);
    failed.push(app.slug);
  }
}
console.log(`\n${ok} fetched, ${skipped} skipped, ${failed.length} failed${failed.length ? ': ' + failed.join(', ') : ''}`);
if (failed.length) console.log('Fetch failures need a manual icon URL; do not substitute a screenshot.');
