#!/usr/bin/env python3
"""Build index.html, sitemap.xml, robots.txt from src/config.json. Change "brand" there and rerun."""
import json,html,datetime,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
C=json.load(open('src/config.json'))
work=[('aarna-jewellery','Aarna Handcrafts — jewellery sale post'),('shanti-yoga','Shanti Flow Studio — yoga offer'),('maa-achaar','Maa Ke Haath Ka Achaar — festive post'),('before-after','Before / after — same product, new design'),('diwali-bakery','Diwali post — home bakery'),('diwali-boutique','Diwali post — boutique'),('diwali-skincare','Diwali post — skincare'),('diwali-cafe','Diwali post — café')]
W='\n'.join(f'<figure class="r"><img src="assets/img/{f}.webp" alt="Sample design for a fictional brand: {html.escape(t)}" width="720" height="900" loading="lazy" decoding="async"><figcaption>{html.escape(t)} · <i>sample, fictional brand</i></figcaption></figure>' for f,t in work)
V='\n'.join(f'<div class="r"><div class="vid"><video data-src="{v["src"]}" poster="{v["poster"]}" controls muted playsinline preload="none"></video></div><p class="vt">{html.escape(v["title"])}</p></div>' for v in C['localVideos'])
B=C['brand'];U=C['siteUrl']
ld={"@context":"https://schema.org","@type":["ProfessionalService","LocalBusiness"],"name":B,"url":U+"/","image":U+"/assets/img/og.jpg","founder":{"@type":"Person","name":C['owner']},"email":C['email'],"telephone":"+"+C['whatsapp'],"areaServed":{"@type":"Country","name":"India"},"address":{"@type":"PostalAddress","addressCountry":"IN"},"priceRange":"₹600–₹2,000+","paymentAccepted":"UPI","sameAs":["https://instagram.com/"+C['instagram']],
"hasOfferCatalog":{"@type":"OfferCatalog","name":"Services","itemListElement":[{"@type":"Offer","name":"Landing page","description":"Mobile-first one-page website, 3–5 day delivery","priceSpecification":{"@type":"PriceSpecification","minPrice":2000,"priceCurrency":"INR"}},{"@type":"Offer","name":"Diwali Post Pack","description":"3 festive posts in 48 hours","price":600,"priceCurrency":"INR"},{"@type":"Offer","name":"Premium landing page","description":"Custom animations, more sections — price on request"}]}}
ctx={k:html.escape(str(v)) for k,v in C.items() if isinstance(v,str)}
ctx.update(work=W,videos=V,jsonld=json.dumps(ld,ensure_ascii=False).replace('</','<\\/'),cfgjs=json.dumps({"youtubeIds":C['youtubeIds']}))
t=open('src/template.html').read()
for k,v in ctx.items(): t=t.replace('{{'+k+'}}',v)
assert '{{' not in t
open('index.html','w').write(t)
d=datetime.date.today().isoformat()
open('sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{U}/</loc><lastmod>{d}</lastmod></url></urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {U}/sitemap.xml\n')
print('built',B)
