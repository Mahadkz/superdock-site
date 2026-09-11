import html, json, sys, os

TPL = '''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-MPHGSB98');</script>
<!-- End Google Tag Manager -->
<title>{title}</title>
<meta name="description" content="{desc_attr}">
<link rel="canonical" href="https://superdock.app/answers/{slug}.html">
<link rel="alternate" type="text/markdown" href="https://superdock.app/answers/{slug}.html.md">
<link rel="describedby" href="https://superdock.app/llms.txt">
<meta property="og:type" content="article"><meta property="og:url" content="https://superdock.app/answers/{slug}.html"><meta property="og:site_name" content="Superdock"><meta property="og:title" content="{title_attr}"><meta property="og:description" content="{desc_attr}"><meta property="og:image" content="https://superdock.app/assets/icon-1024.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title_attr}"><meta name="twitter:description" content="{desc_attr}"><meta name="twitter:image" content="https://superdock.app/assets/icon-1024.png">

<link rel="preload" href="../assets/fonts/GeneralSans-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/GeneralSans-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/style.css">
<script type="application/ld+json">{ldjson}</script>
<link rel="icon" type="image/png" sizes="32x32" href="../assets/mark.png">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="../assets/icon-256.png">
</head><body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MPHGSB98"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<header class="nav"><div class="wrap"><a class="brand" href="/"><img src="../assets/mark.png" alt="">Superdock</a><div class="links"><a href="/answers/">Answers</a><a href="/compare/">Compare</a><a href="/#pricing">Pricing</a><a href="/blog/">Blog</a></div><a class="navcta" href="../Superdock-1.0.3.dmg">Download free</a></div></header>
<main><article class="wrap doc post">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Superdock</a> / <a href="./">Answers</a></nav>
<h1>{h1}</h1>
<p class="byline">By Mahad Kazmi, developer of Superdock. Updated 12 September 2026.</p>
<div class="answer"><img src="../assets/icon-256.png" width="72" height="72" alt="Superdock icon"><div><p class="short"><strong>Short answer.</strong> {short}</p></div></div>

{body}

<h2>Frequently asked questions</h2>
{faq_html}
<div class="cta"><img src="../assets/icon-256.png" width="56" height="56" alt=""><div><p><a class="btn primary" href="../Superdock-1.0.3.dmg">Download free</a> <span class="muted">Superdock is free to download. The dock, window previews, the switcher and multi-display support are all free. Chrome profile icons: 14 days free, then $7.99 once. macOS 14 or later.</span></p></div></div>
<h2>Continue reading</h2>
<ul class="related">{related}</ul>
<div class="authorbox">
  <img src="../assets/mahad-112.jpg" width="56" height="56" alt="Mahad Kazmi" loading="lazy">
  <div>
    <p class="name"><a href="../author/mahad-kazmi.html">Mahad Kazmi</a></p>
    <p>Independent macOS developer and the author of Superdock. I switched to a Mac from Windows, lost the per profile taskbar buttons I relied on, and built the dock I wanted instead. I write these guides from daily use of the apps in them, and I answer the support email myself.</p>
    <p class="profiles"><a href="https://github.com/Mahadkz" rel="me noopener" target="_blank">GitHub</a> &middot; <a href="https://www.linkedin.com/in/syed-mahad-kazmi/" rel="me noopener" target="_blank">LinkedIn</a> &middot; <a href="../about.html">About</a> &middot; hello@superdock.app</p>
  </div>
</div>
</article></main>
<footer><div class="wrap"><div class="row"><div>Copyright 2026 Superdock. All rights reserved.</div><div class="links"><a href="../about.html">About</a> <a href="../terms.html">Terms</a> <a href="../privacy.html">Privacy</a> <a href="../refund.html">Refunds</a> <a href="../affiliates.html">Affiliates</a></div></div></div></footer>
</body></html>
'''

def build(p):
    slug=p['slug']
    faq_html=''.join('<details class="qa"><summary><h3>%s</h3></summary><p>%s</p></details>'%(html.escape(q),html.escape(a)) for q,a in p['faq'])
    ld={"@context":"https://schema.org","@graph":[
      {"@type":"WebPage","@id":f"https://superdock.app/answers/{slug}.html","url":f"https://superdock.app/answers/{slug}.html","name":p['h1'],"description":p['desc'],"datePublished":"2026-09-12","dateModified":"2026-09-12","isPartOf":{"@id":"https://superdock.app/#site"},"about":{"@id":"https://superdock.app/#app"},"author":{"@id":"https://superdock.app/#mahad"},"publisher":{"@id":"https://superdock.app/#org"},"primaryImageOfPage":"https://superdock.app/assets/icon-1024.png"},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Superdock","item":"https://superdock.app/"},
        {"@type":"ListItem","position":2,"name":"Answers","item":"https://superdock.app/answers/"},
        {"@type":"ListItem","position":3,"name":p['h1'],"item":f"https://superdock.app/answers/{slug}.html"}]},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p['faq']]},
      {"@type":"Person","@id":"https://superdock.app/#mahad","name":"Mahad Kazmi","url":"https://superdock.app/author/mahad-kazmi.html","email":"hello@superdock.app","jobTitle":"Independent software developer","description":"Independent macOS developer and the author of Superdock.","sameAs":["https://github.com/Mahadkz","https://www.linkedin.com/in/syed-mahad-kazmi/"]}]}
    rel=''.join('<li><a href="%s">%s</a></li>'%(u,html.escape(t)) for t,u in p['related'])
    out=TPL.format(title=html.escape(p['title']),title_attr=html.escape(p['title'],quote=True),
        desc_attr=html.escape(p['desc'],quote=True).replace("'","&#x27;"),slug=slug,
        ldjson=json.dumps(ld),h1=html.escape(p['h1']),short=p['short'],body=p['body'],
        faq_html=faq_html,related=rel)
    open(f"answers/{slug}.html","w").write(out)
    # markdown twin
    import re
    md=f"<!-- Markdown twin of https://superdock.app/answers/{slug}.html -->\n\n# {p['h1']}\n\nBy Mahad Kazmi, developer of Superdock. Updated 12 September 2026.\n\nShort answer. {re.sub('<[^>]*>','',p['short'])}\n\n"
    b=p['body']
    b=re.sub(r'<h2>(.*?)</h2>',r'\n## \1\n',b)
    b=re.sub(r'<li>(.*?)</li>',r'- \1\n',b,flags=re.S)
    b=re.sub(r'<[^>]*>','',b)
    md+=re.sub(r'\n{3,}','\n\n',b).strip()+"\n\n## Frequently asked questions\n\n"
    for q,a in p['faq']: md+=f"### {q}\n\n{a}\n\n"
    open(f"answers/{slug}.html.md","w").write(md)
    print("wrote", slug)

pages=json.load(open(sys.argv[1]))
for p in pages: build(p)
