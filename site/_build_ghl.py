# -*- coding: utf-8 -*-
"""Turns the verified static pages into self-contained GHL custom-code blocks.
Run AFTER _build.py.  Output lands in ../ghl/ , one paste-ready file per page."""
import re, os, html

SITE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SITE)
OUT  = os.path.join(ROOT, "ghl")
KIT  = os.path.join(ROOT, "logo-kit")
os.makedirs(OUT, exist_ok=True)

# GHL page slugs, edit here if you name the pages differently in GHL
SLUG = {"index.html":"/", "services.html":"/services", "first-visit.html":"/first-visit",
        "about.html":"/about", "academy.html":"/academy", "contact.html":"/contact"}

CSS = open(os.path.join(SITE,"method.css")).read()
JS  = open(os.path.join(SITE,"site.js")).read()

FONTS = ("@import url('https://fonts.googleapis.com/css2?"
         "family=Prata&family=Jost:wght@300;400;500&display=swap');\n")

# scope everything to a wrapper so GHL's own styles cannot bleed in or out
SCOPE = "mw"

def inline_svg(path, cls, style):
    s = open(path).read()
    s = re.sub(r'<\?xml.*?\?>', '', s, flags=re.S)
    s = re.sub(r'<!DOCTYPE.*?>', '', s, flags=re.S)
    s = s.strip()
    s = s.replace('<svg ', f'<svg class="{cls}" style="{style}" aria-hidden="true" ', 1)
    return s

LOGOS = {
 f'../logo-kit/05-icon-and-submark/method-submark-black.svg':
   (os.path.join(KIT,"05-icon-and-submark","method-submark-black.svg"), "mark", "height:38px;width:auto"),
 f'../logo-kit/04-wordmark/method-wordmark-black.svg':
   (os.path.join(KIT,"04-wordmark","method-wordmark-black.svg"), "word", "height:15px;width:auto;margin-top:2px"),
 f'../logo-kit/01-primary-logo/method-primary-white.svg':
   (os.path.join(KIT,"01-primary-logo","method-primary-white.svg"), "foot-mark", "height:clamp(120px,16vw,164px);width:auto"),
}

SCHEMA = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"HealthAndBeautyBusiness",
"name":"Method Luxury Waxing and Professional Training",
"image":"https://laceofbase1.github.io/method-wax-concepts/logo-kit/07-website-and-social/og-share-image-1200x630.png",
"url":"https://methodwaxpro.com",
"telephone":"+1-239-529-5441",
"email":"Info@MethodWaxPro.Com",
"priceRange":"$$",
"address":{"@type":"PostalAddress","streetAddress":"1410 Pine Ridge Road, Suite 22",
"addressLocality":"Naples","addressRegion":"FL","postalCode":"34108","addressCountry":"US"},
"openingHoursSpecification":[
{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"08:00","closes":"20:00"},
{"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"08:00","closes":"18:00"},
{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"15:00"},
{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"10:00","closes":"17:00"}],
"areaServed":"Naples, Florida"}
</script>'''

def scope_css(css):
    """prefix every selector so the block is isolated inside GHL"""
    out=[]
    for chunk in re.split(r'(@media[^{]+\{|@import[^;]+;|\})', css):
        out.append(chunk)
    css = css.replace(":root{", f".{SCOPE}{{")
    lines=[]
    for line in css.split("\n"):
        m = re.match(r'^(\s*)([^@\s/][^{]*?)\{', line)
        if m and not line.strip().startswith(("@","/*","}")):
            sels = m.group(2)
            new = ", ".join(
                (s.strip() if s.strip().startswith(f".{SCOPE}") else f".{SCOPE} {s.strip()}")
                for s in sels.split(","))
            line = f"{m.group(1)}{new}{{" + line[m.end():]
        lines.append(line)
    css = "\n".join(lines)
    css = css.replace(f".{SCOPE} .{SCOPE}{{", f".{SCOPE}{{")
    css = css.replace(f".{SCOPE} body{{", f".{SCOPE}{{")
    css = css.replace(f".{SCOPE} html{{", f".{SCOPE}{{")
    css = css.replace(f".{SCOPE} *{{", f".{SCOPE} *, .{SCOPE}{{")
    return css


# a host page (GHL, or a theme) can use !important and win on our headings and images.
# this armour re-asserts only the properties that actually get hijacked in practice.
ARMOUR = f"""
/* --- isolation armour, keep last --- */
.{SCOPE} h1, .{SCOPE} h2, .{SCOPE} h3 {{
  font-family:'Prata',Georgia,serif !important; color:inherit !important;
  text-transform:none !important; text-decoration:none !important; }}
.{SCOPE} .hero-cap h1 {{ color:var(--ivory) !important; }}
.{SCOPE} img, .{SCOPE} svg {{ border:0 !important; box-shadow:none !important;
  border-radius:0 !important; }}
.{SCOPE} a {{ text-decoration:none !important; }}
.{SCOPE} .u-label, .{SCOPE} .label, .{SCOPE} .nav-links a, .{SCOPE} .btn,
.{SCOPE} .announce, .{SCOPE} .foot-links a, .{SCOPE} .foot-fine, .{SCOPE} .cap,
.{SCOPE} .field label, .{SCOPE} .set .k, .{SCOPE} .person .role, .{SCOPE} .link {{
  font-family:'Jost',system-ui,sans-serif !important; text-transform:uppercase !important; }}
.{SCOPE} .row .s, .{SCOPE} .split-copy p, .{SCOPE} .lede, .{SCOPE} details p,
.{SCOPE} .step p, .{SCOPE} .set p, .{SCOPE} .person p, .{SCOPE} .addr {{
  font-family:'Jost',system-ui,sans-serif !important; text-transform:none !important; }}
.{SCOPE} .row .p, .{SCOPE} .hours div span:last-child, .{SCOPE} summary, .{SCOPE} .quote p {{
  font-family:'Prata',Georgia,serif !important; }}
.{SCOPE} button, .{SCOPE} input, .{SCOPE} select, .{SCOPE} textarea {{
  font-family:'Jost',system-ui,sans-serif !important; }}
.{SCOPE} p {{ margin:0; }}

/* --- full-bleed breakout ---------------------------------------------
   GHL wraps page content in a fixed max-width row. These blocks are
   designed edge to edge (hero, emerald bands, footer), so we escape the
   container regardless of the builder's width setting. */
.{SCOPE} {{
  width:100vw !important; max-width:100vw !important;
  margin-left:calc(50% - 50vw) !important;
  margin-right:calc(50% - 50vw) !important;
}}
html, body {{ overflow-x:clip !important; max-width:100% !important; }}
/* sticky must not be trapped by an overflow ancestor */
.{SCOPE} {{ overflow:visible !important; }}
.{SCOPE} header {{ position:sticky !important; top:0 !important; z-index:60 !important; }}

/* --- content must never depend on JS to be visible --------------------
   The scroll-reveal never fires inside GHL's builder, which left every
   section at opacity 0 and the pages effectively blank. Content is now
   visible unconditionally; the reveal is gone rather than fragile. */
.{SCOPE} .rv {{ opacity:1 !important; transform:none !important; }}

/* --- GHL native form, styled into the brand --------------------------
   GHL renders no <form> element, so these target its own classes.
   Deliberately global: the form sits outside .{SCOPE}. */
[class*="cform-"] {{ max-width:600px !important; margin-inline:auto !important;
  text-align:left !important; }}
.form-builder--item {{ margin-bottom:1.15rem !important; }}
.field-label, .label-alignment {{
  font-family:'Jost',system-ui,sans-serif !important; font-weight:400 !important;
  font-size:.63rem !important; letter-spacing:.2em !important;
  text-transform:uppercase !important; color:#7A7064 !important;
  margin-bottom:.45rem !important; display:block !important; }}
.form-control, .multiselect__tags {{
  width:100% !important; background:transparent !important;
  border:0 !important; border-bottom:1px solid #DFD5C4 !important;
  border-radius:0 !important; box-shadow:none !important;
  padding:.6rem 0 !important; min-height:0 !important; height:auto !important;
  font-family:'Jost',system-ui,sans-serif !important; font-weight:300 !important;
  font-size:1rem !important; color:#2A2620 !important; }}
.form-control.text-area-element {{ min-height:104px !important; resize:vertical !important; }}
.form-control:focus, .multiselect--active .multiselect__tags {{
  outline:none !important; border-bottom-color:#A56B41 !important; }}
.form-control::placeholder {{ color:#B4A897 !important; }}
.phone-input, .phone-input.flex, .email-input {{
  border:0 !important; background:transparent !important; padding:0 !important; }}
.multiselect, .multi_select_form {{ background:transparent !important; }}
.multiselect__single, .multiselect__placeholder, .multiselect__input {{
  font-family:'Jost',system-ui,sans-serif !important; font-weight:300 !important;
  font-size:1rem !important; color:#2A2620 !important;
  background:transparent !important; padding:0 !important; margin:0 !important; }}
.multiselect__content-wrapper {{ border:1px solid #DFD5C4 !important;
  border-radius:0 !important; background:#FBF7EF !important; }}
.multiselect__option {{ font-family:'Jost',system-ui,sans-serif !important;
  font-weight:300 !important; font-size:.95rem !important; }}
.multiselect__option--highlight {{ background:#EFE6D8 !important; color:#2A2620 !important; }}
.checkbox-container, .checkbox-container * {{
  font-family:'Jost',system-ui,sans-serif !important; font-weight:300 !important;
  font-size:.76rem !important; line-height:1.55 !important; color:#7A7064 !important; }}
.checkbox-container {{ margin-top:.5rem !important; }}
.button-element, .btn.btn-dark {{
  background:#1D392F !important; color:#F5EFE4 !important; border:0 !important;
  border-radius:100px !important; padding:.85rem 1.9rem !important;
  font-family:'Jost',system-ui,sans-serif !important; font-weight:400 !important;
  font-size:.7rem !important; letter-spacing:.18em !important;
  text-transform:uppercase !important; width:auto !important;
  box-shadow:none !important; transition:background .3s !important; }}
.button-element:hover, .btn.btn-dark:hover {{ background:#2C5344 !important; }}
"""

SCOPED = FONTS + scope_css(CSS) + ARMOUR

def build(page):
    src = open(os.path.join(SITE, page)).read()
    body = re.search(r'<body>(.*?)<script src="site\.js">', src, re.S).group(1)
    for rel,(path,cls,style) in LOGOS.items():
        body = re.sub(r'<img class="%s" src="%s"[^>]*>' % (cls, re.escape(rel)),
                      inline_svg(path, cls, style), body)
    for f,slug in SLUG.items():
        body = body.replace('href="%s"' % f, 'href="%s"' % slug)
    body = body.replace('href="../logo-kit/07-website-and-social/favicon.ico"','')
    out = (f'<!-- METHOD {page}  |  paste this whole thing into ONE GHL custom code element -->\n'
           f'<style>\n{SCOPED}\n</style>\n{SCHEMA}\n<div class="{SCOPE}">\n{body}\n</div>\n'
           f'<script>\n(function(){{\n{JS}\n}})();\n</script>\n')
    dest = os.path.join(OUT, page)
    open(dest,"w").write(out)
    return dest, len(out)

for p in SLUG:
    d,n = build(p)
    print("  %-18s %6.1f KB" % (os.path.basename(d), n/1024))
print("GHL blocks written to", OUT)

# ---- split the two form pages so a NATIVE GHL form can sit in the middle -------
# a hand-coded <form> cannot reach the CRM; GHL's own form element must do that job.
import io
SPLITS = {"contact.html":"contact", "academy.html":"academy"}
for page, name in SPLITS.items():
    txt = open(os.path.join(OUT, page)).read()
    m = re.search(r'<!-- (?:CONTACT )?FORM:.*?-->\s*<form.*?</form>', txt, re.S)
    if not m:
        print("  ! no form found in", page); continue
    before, after = txt[:m.start()], txt[m.end():]
    # `after` opens with closing tags belonging to elements block 1 already
    # closed. Left in, they close block 2's wrapper immediately and every
    # section below it falls outside the scoped styles.
    after = re.sub(r'^(?:\s*</(?:div|section)>)+', '', after)
    marker = ('\n<!-- ================================================================\n'
              '     STOP. End of block 1.\n'
              '     In GHL, drop a native FORM element here, then paste block 2 below it.\n'
              '     The form must be a GHL form so submissions reach the CRM.\n'
              '     ================================================================ -->\n')
    open(os.path.join(OUT, f"{name}-block-1.html"),"w").write(before + marker + "</div>\n")
    # GHL isolates each custom-code element, so block 2 must carry its own
    # stylesheet. Without it the footer renders as raw unstyled HTML.
    open(os.path.join(OUT, f"{name}-block-2.html"),"w").write(
        f'<!-- METHOD {name}, block 2. Paste BELOW the GHL form element. -->\n'
        f'<style>\n{SCOPED}\n</style>\n'
        f'<div class="{SCOPE}">\n' + after)
    print("  split %-14s -> %s-block-1.html + %s-block-2.html" % (page, name, name))

# ---- CSS to make a native GHL form match the rest of the design ---------------
FORMCSS = f""".{SCOPE}-form, .{SCOPE}-form * {{ box-sizing:border-box; }}
.{SCOPE}-form label {{ font-family:'Jost',sans-serif !important; font-size:.62rem !important;
  letter-spacing:.22em !important; text-transform:uppercase !important; color:#7A7064 !important;
  margin-bottom:.5rem !important; display:block !important; }}
.{SCOPE}-form input, .{SCOPE}-form select, .{SCOPE}-form textarea {{
  width:100% !important; background:transparent !important; border:0 !important;
  border-bottom:1px solid #DFD5C4 !important; border-radius:0 !important;
  padding:.6rem 0 !important; font-family:'Jost',sans-serif !important; font-weight:300 !important;
  font-size:1rem !important; color:#2A2620 !important; box-shadow:none !important; }}
.{SCOPE}-form input:focus, .{SCOPE}-form select:focus, .{SCOPE}-form textarea:focus {{
  outline:none !important; border-bottom-color:#A56B41 !important; }}
.{SCOPE}-form button, .{SCOPE}-form .btn {{
  background:#1D392F !important; color:#F5EFE4 !important; border:0 !important;
  border-radius:100px !important; padding:.8rem 1.6rem !important;
  font-family:'Jost',sans-serif !important; font-size:.7rem !important;
  letter-spacing:.18em !important; text-transform:uppercase !important; width:auto !important; }}
.{SCOPE}-form button:hover {{ background:#2C5344 !important; }}
"""
open(os.path.join(OUT,"ghl-form-styling.css"),"w").write(
 "/* Paste into GHL > Sites > your form > Styles > Custom CSS,\n"
 "   or into the page's custom CSS. Wrap the form in a container\n"
 f"   with class \"{SCOPE}-form\" so this only touches Method forms. */\n\n" + FORMCSS)
print("  wrote ghl-form-styling.css")
