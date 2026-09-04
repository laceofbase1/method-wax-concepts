# -*- coding: utf-8 -*-
"""Builds the METHOD static site. Re-run after editing content here."""
import os

BOOK = "https://na2.meevo.com/customerportal/advanced/ob?tenantId=502504"   # Meevo online booking (new experience, no login wall)
LOGO = "../logo-kit"

NAV = [("services.html","The Menu"), ("first-visit.html","First Visit"),
       ("about.html","About"), ("academy.html","The Academy"), ("contact.html","Contact")]

MENU = [
 ("Face", [("Full Face","64",0),("Eyebrow","24",1),("Cheek","16",0),("Chin","14",0),
           ("Hairline","14",0),("Neck","17",0),("Nose","15",0),("Sideburn","17",0),("Ears","17",0)]),
 ("Lip", [("Upper Lip","14",0),("Lower Lip","14",0)]),
 ("Bikini", [("Brazilian","64",1),("Full Bikini","56",0),("Bikini Line","48",0)]),
 ("Legs", [("Full Leg","79",0),("Upper Leg","57",0),("Lower Leg","51",0),
           ("Inner Thigh","19",0),("Knee","17",0),("Toes","19",0)]),
 ("Arms", [("Full Arm","51",0),("Half Arm","44",0),("Underarm","25",1),
           ("Shoulder","31",0),("Hand","19",0)]),
 ("Back", [("Full Back","74",0),("Upper Back","31",0),("Mid Back","31",0),("Lower Back","27",0)]),
 ("Chest", [("Full Chest","39",0),("Chest Strip","27",0),("Nipple","17",0)]),
 ("Stomach", [("Full Stomach","39",0),("Stomach Strip","16",0)]),
 ("Butt", [("Full Butt","33",0),("Butt Strip","21",0)]),
]

def rows(items):
    out=[]
    for n,p,star in items:
        out.append(f'      <div class="row{" star" if star else ""}"><span class="s">{n}</span>'
                   f'<span class="d"></span><span class="p">${p}</span></div>')
    return "\n".join(out)

def full_menu():
    out=[]
    for i,(cat,items) in enumerate(MENU,1):
        out.append(f'''    <div class="cat">
      <div class="ch"><span class="n">{i:02d}</span><h3>{cat}</h3></div>
{rows(items)}
    </div>''')
    return "\n".join(out)

SET_CARDS = '''      <div class="set">
        <span class="k">The Set</span>
        <h3>Buy nine, get three free.</h3>
        <p>Nine of any single service, then three of the same on us. New guests get four free
        instead of three, because your first year is the one that builds the habit.</p>
        <div class="fine">New guests: buy 9, get 4 &nbsp;&#183;&nbsp; Returning: buy 9, get 3</div>
      </div>
      <div class="set">
        <span class="k">The Year</span>
        <h3>Unlimited, for a year and then some.</h3>
        <p>Thirteen months of unlimited waxing for returning guests, fourteen for new. Pay upfront
        or split it into payments. No expiration, and no scramble to use it up.</p>
        <div class="fine">Pricing in studio <span class="tbc">confirm</span></div>
      </div>'''

def shell(slug, title, desc, body, hero=""):
    CUR = ' aria-current="page"'
    links = "\n".join(
        '      <a href="%s"%s>%s</a>' % (h, CUR if h == slug else "", t) for h, t in NAV)
    drawer = "\n".join(f'  <a href="{h}">{t}</a>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{LOGO}/07-website-and-social/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Prata&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="method.css">
</head>
<body>

<div class="announce">
  Now booking &#183; First appointments October 5, 2026
  <span>&#183;</span> Naples, Florida
</div>

<header>
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="METHOD, luxury waxing and professional training">
      <img class="mark" src="{LOGO}/05-icon-and-submark/method-submark-black.svg" alt="">
      <img class="word" src="{LOGO}/04-wordmark/method-wordmark-black.svg" alt="METHOD.">
    </a>
    <nav class="nav-links">
{links}
    </nav>
    <button class="burger" aria-label="Menu"><i></i><i></i><i></i></button>
    <!-- BOOK NOW: replace href with the Meevo online booking link -->
    <a class="btn btn-solid" href="{BOOK}">Book Now</a>
  </div>
  <nav class="drawer">
{drawer}
  </nav>
</header>
{hero}
{body}

<footer>
  <div class="wrap">
    <img class="foot-mark" src="{LOGO}/01-primary-logo/method-primary-white.svg"
         alt="METHOD, luxury waxing and professional training">
    <div class="foot-links">
      <a href="services.html">The Menu</a>
      <a href="first-visit.html">First Visit</a>
      <a href="about.html">About</a>
      <a href="academy.html">The Academy</a>
      <a href="contact.html">Contact</a>
      <!-- BOOK NOW: replace href with the Meevo online booking link -->
      <a href="{BOOK}">Book Now</a>
    </div>
    <div class="foot-fine">
      1410 Pine Ridge Road, Suite 22, Naples, FL 34108 &nbsp;&#183;&nbsp; (239) 529-5441<br>
      &copy; 2026 Method Luxury Waxing and Professional Training
    </div>
  </div>
</footer>
<script src="site.js"></script>
</body>
</html>
'''

def phead(eyebrow, h1, lede):
    return f'''<section class="phead wrap rv">
  <span class="u-label">{eyebrow}</span>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
</section>
'''

CTA = f'''<section class="band band-emerald cta rv">
  <div class="wrap">
    <h2>Ready when you are.</h2>
    <p>Booking takes about a minute. No card, no deposit, and you pay in studio when you are done.</p>
    <!-- BOOK NOW: replace href with the Meevo online booking link -->
    <a class="btn btn-light" href="{BOOK}">Book an appointment</a>
  </div>
</section>
'''

IMG = "https://images.unsplash.com/photo-"
def u(pid,w=1200):
    assert "-" in pid and len(pid.split("-")[1]) == 12, \
        "Unsplash id must be <13 digits>-<12 char hash>, got %r" % pid
    return f"{IMG}{pid}?auto=format&fit=crop&w={w}&q=80"

# ---------------------------------------------------------------- HOME
HOME_HERO = f'''
<section class="hero" id="top">
  <img src="{u('1763750759240-a1398573772a',2000)}" alt="The warm, softly lit arched treatment studio">
  <div class="hero-cap">
    <span class="k">Luxury Waxing &#183; Naples, Florida</span>
    <h1>Where the wax is the whole point.</h1>
    <div class="hero-cta">
      <!-- BOOK NOW: replace href with the Meevo online booking link -->
      <a class="btn btn-light" href="{BOOK}">Book an appointment</a>
      <a class="hero-link" href="services.html">See the menu</a>
    </div>
  </div>
</section>
'''

SIGNATURE = [("Brazilian","64"),("Full Bikini","56"),("Eyebrow","24"),
             ("Underarm","25"),("Full Leg","79"),("Full Face","64")]

HOME = f'''
<section class="statement wrap rv" style="text-align:center;padding-block:clamp(4rem,9vw,7.5rem) clamp(2.5rem,5vw,4rem)">
  <span class="label">A Naples Waxing Studio</span>
  <h2 style="font-size:clamp(2rem,5.2vw,4.4rem);max-width:17ch;margin:1.7rem auto 0">The art of the
  <span class="g">wax</span>, done <em>with intention.</em></h2>
  <p class="lede" style="margin:2rem auto 0;max-width:56ch">We came from the corporate wax world,
  where the schedule mattered more than the person on the table. Method is the correction. Honest
  pricing, unhurried appointments, and technique held to the standard we teach other professionals.</p>
</section>

<section class="split wrap rv">
  <div class="split-media"><img src="{u('1648285191822-1b02b816cd78')}"
       alt="A warm copper toned arched niche with travertine and a trailing plant"></div>
  <div class="split-copy">
    <span class="u-label">01 &#183; The Studio</span>
    <h2>Care you can feel in the room.</h2>
    <p>Two estheticians, two treatment rooms, and nobody rushing you out the door. We will tell you
    the truth about your skin, explain the why behind every step, and never sell you something you
    did not come in for.</p>
    <ul class="credo">
      <li>Fair pricing, published openly, with no upsell at the table</li>
      <li>The science explained, not just the technique performed</li>
      <li>Appointments paced for comfort, not for volume</li>
      <li>The same standard we hold our students to</li>
    </ul>
    <p style="margin-top:1.7rem"><a class="link" href="about.html">Meet the studio</a></p>
  </div>
</section>

<section class="band band-paper rv">
  <div class="wrap">
    <div class="band-head">
      <span class="u-label">The Menu</span>
      <h2>What people book most.</h2>
      <p>Thirty six services, every price in the open. These are the six we are asked about
      before anything else.</p>
    </div>
    <div style="max-width:640px;margin-inline:auto">
{rows([(n,p,0) for n,p in SIGNATURE])}
    </div>
    <p style="text-align:center;margin-top:2.4rem">
      <a class="btn btn-ghost" href="services.html">See the full menu</a></p>
  </div>
</section>

<section class="band band-mauve rv" id="sets">
  <div class="wrap">
    <div class="band-head">
      <span class="u-label">The Method Set</span>
      <h2>Waxing is a habit, not a one time thing.</h2>
      <p>Hair grows on a cycle, so results compound when you keep a rhythm. Our sets are built to
      reward that, and they never expire.</p>
    </div>
    <div class="set-grid">
{SET_CARDS}
    </div>
    <p style="text-align:center;color:var(--muted);font-size:.9rem;margin:2rem auto 0;max-width:48ch">
      Sets can be shared with your children under 22, because the whole family should not need
      four separate memberships.</p>
  </div>
</section>

<section class="quote wrap rv">
  <p><span class="g">Intentional</span> care is not a tagline. It is the <em>method.</em></p>
  <div class="cite">Sophia, Tori and Rachel</div>
</section>

<section class="band band-emerald rv" id="visit">
  <div class="wrap">
    <span class="u-label">Visit</span>
    <h2>Find us in Naples.</h2>
    <div style="display:grid;grid-template-columns:1.15fr 1fr;gap:clamp(2rem,5vw,4.5rem);margin-top:2.6rem"
         class="visit-grid">
      <div>
        <div class="hours">
          <div><span>Monday to Thursday</span><span>8am to 8pm</span></div>
          <div><span>Friday</span><span>8am to 6pm</span></div>
          <div><span>Saturday</span><span>9am to 3pm</span></div>
          <div><span>Sunday</span><span>10am to 5pm</span></div>
        </div>
      </div>
      <div>
        <p class="addr">1410 Pine Ridge Road, Suite 22<br>Naples, FL 34108<br><br>
          <a href="tel:+12395295441">(239) 529-5441</a><br>
          <a href="mailto:Info@MethodWaxPro.Com">Info@MethodWaxPro.Com</a></p>
        <p style="margin-top:1.8rem"><a class="btn btn-light" href="contact.html">Get in touch</a></p>
      </div>
    </div>
  </div>
</section>

<section class="split rev wrap rv">
  <div class="split-media"><img src="{u('1690994065552-6a35a0455ea2')}"
       alt="An olive branch in a soft sunlit still life"></div>
  <div class="split-copy">
    <span class="u-label">Coming Next</span>
    <h2>The Academy.</h2>
    <p>Method is a training academy as much as a studio. Professional waxing certification, taught
    online and finished by hand in this room, is in development now.</p>
    <p style="margin-top:-.4rem">If you are an esthetician, tell us and we will let you know the
    moment enrollment opens.</p>
    <a class="link" href="academy.html">About the academy</a>
  </div>
</section>
'''

# ---------------------------------------------------------------- SERVICES
SERVICES = f'''
<section class="wrap rv" style="padding-block:clamp(2.5rem,5vw,4rem)">
  <div class="menu-cols">
{full_menu()}
  </div>
  <div class="menu-note">
    <p><strong>Services for men.</strong> Most of the menu is available to all guests. Full Face,
    Full Butt, Butt Strip, and bikini services are offered to women only.</p>
    <p><strong>Guests under 18.</strong> Welcome with a parent's consent and a signed waiver.
    Brazilian and Full Bikini are available from age 16 with the same consent.</p>
    <p><strong>Paying.</strong> No card and no deposit to book. You pay in studio at the end of
    your appointment.</p>
  </div>
</section>

<section class="band band-mauve rv" id="sets">
  <div class="wrap">
    <div class="band-head">
      <span class="u-label">The Method Set</span>
      <h2>The regulars pay less.</h2>
      <p>Hair grows on a cycle, so results compound when you keep a rhythm. Our sets reward that,
      and they never expire.</p>
    </div>
    <div class="set-grid">
{SET_CARDS}
    </div>
    <p style="text-align:center;color:var(--muted);font-size:.9rem;margin:2rem auto 0;max-width:48ch">
      Sets can be shared with your children under 22, because the whole family should not need
      four separate memberships.</p>
  </div>
</section>

<section class="band wrap rv">
  <div class="narrow" style="text-align:center">
    <span class="u-label">Not Sure What To Book</span>
    <h2 style="font-size:clamp(1.8rem,3.8vw,2.7rem);margin:1.1rem 0 1.2rem">Ask us. Really.</h2>
    <p class="lede" style="margin-inline:auto">If you are new to waxing, or coming back after a long
    gap, call and describe what you want. We will tell you which service fits and roughly how long
    it takes, with no pressure to book anything bigger.</p>
    <p style="margin-top:1.8rem"><a class="btn btn-ghost" href="tel:+12395295441">(239) 529-5441</a></p>
  </div>
</section>
''' + CTA

# ---------------------------------------------------------------- FIRST VISIT
FIRST = f'''
<section class="split wrap rv">
  <div class="split-media"><img src="{u('1706795033855-eee02f726868')}" alt="Rolled spa towels in soft warm light"></div>
  <div class="split-copy">
    <span class="u-label">Before You Come</span>
    <h2>Let it grow, and keep it simple.</h2>
    <p>The single thing that decides whether a wax goes well is hair length. About a quarter of an
    inch, roughly the length of a grain of rice, gives the wax something to hold. If you have been
    shaving, give it two to three weeks.</p>
    <ul class="credo">
      <li>Exfoliate gently a day or two before, not the morning of</li>
      <li>Skip lotion, oil, and deodorant on the area being waxed</li>
      <li>Avoid sun, tanning, and hot tubs for a day or two beforehand</li>
      <li>Pause retinol and strong actives on the area for five to seven days</li>
      <li>Come in clean and dry, and wear something loose to go home in</li>
    </ul>
  </div>
</section>

<section class="band band-paper rv">
  <div class="wrap">
    <div class="band-head">
      <span class="u-label">In The Room</span>
      <h2>What actually happens.</h2>
      <p>Nobody tells you this part, so here it is. The whole thing is shorter and less dramatic
      than the internet suggests.</p>
    </div>
    <div class="steps narrow">
      <div class="step"><div class="n">1</div><div>
        <h3>We talk first</h3>
        <p>A quick conversation about what you are booking, anything on your skin, medications, and
        whether you have been waxed before. Tell us if you are nervous. It changes how we work.</p></div></div>
      <div class="step"><div class="n">2</div><div>
        <h3>You get a minute alone</h3>
        <p>We step out, you undress from the waist down for bikini services, and get on the table
        with the drape provided. Nobody walks in until you say you are ready.</p></div></div>
      <div class="step"><div class="n">3</div><div>
        <h3>The wax itself</h3>
        <p>We work in small sections and tell you before each one. A Brazilian takes about twenty
        minutes. It stings for a second and then it is done. You can ask us to pause at any point.</p></div></div>
      <div class="step"><div class="n">4</div><div>
        <h3>We finish and soothe</h3>
        <p>Stray hairs tweezed, a calming product applied, and a straight answer about when to come
        back. Then you dress and pay at the front. That is the whole appointment.</p></div></div>
    </div>
  </div>
</section>

<section class="split rev wrap rv">
  <div class="split-media"><img src="{u('1630595271375-5073a6c0638b')}" alt="A calm moment of warm self care"></div>
  <div class="split-copy">
    <span class="u-label">Afterward</span>
    <h2>The next twenty four hours.</h2>
    <p>Your skin has just had a lot done to it. Keep it cool and clean for a day and it settles
    quickly.</p>
    <ul class="credo">
      <li>No gym, hot tubs, pools, saunas, or sun for twenty four hours</li>
      <li>Loose clothing, and skip heavy lotions and fragrance on the area</li>
      <li>Start gentle exfoliation again after three or four days to prevent ingrowns</li>
      <li>Come back every four to six weeks to stay on the growth cycle</li>
    </ul>
    <p style="margin-top:1.6rem;font-size:.9rem">Some redness and small bumps for a few hours is
    normal. Anything that worries you, call us.</p>
  </div>
</section>

<section class="band band-emerald rv">
  <div class="wrap narrow">
    <span class="u-label">The Fine Print</span>
    <h2>Our policies, in plain words.</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem 3rem;margin-top:2.4rem" class="pol">
      <div><h3 style="font-size:1.2rem;margin-bottom:.5rem">Running late</h3>
        <p style="color:#C9D6CD;font-size:.94rem">Arriving more than ten minutes late may mean we
        have to reschedule, so the guest after you is not kept waiting.
        <span class="tbc">5 or 10 min, confirm</span></p></div>
      <div><h3 style="font-size:1.2rem;margin-bottom:.5rem">Cancelling</h3>
        <p style="color:#C9D6CD;font-size:.94rem">Just call us. There is no fee. We only ask that
        you let us know so we can offer the time to someone else.</p></div>
      <div><h3 style="font-size:1.2rem;margin-bottom:.5rem">Paying</h3>
        <p style="color:#C9D6CD;font-size:.94rem">No card and no deposit to book. You pay in studio
        at the end of your appointment.</p></div>
      <div><h3 style="font-size:1.2rem;margin-bottom:.5rem">Under 18</h3>
        <p style="color:#C9D6CD;font-size:.94rem">Welcome with a parent's consent and a signed
        waiver. Brazilian and Full Bikini from age 16 with the same consent.</p></div>
    </div>
  </div>
</section>

<section class="band wrap rv">
  <div class="band-head"><span class="u-label">Questions</span>
    <h2>The ones we get asked.</h2></div>
  <div class="narrow">
    <details open><summary>Does it hurt?</summary>
      <p>The first time is the most uncomfortable, and it is over quickly. It gets noticeably easier
      by the third appointment, because regular waxing weakens the hair and your skin gets used to
      it. Tell us if you are nervous and we will talk you through every section.</p></details>
    <details><summary>How long should my hair be?</summary>
      <p>About a quarter of an inch, roughly the length of a grain of rice. Too short and the wax
      has nothing to grip. If you have been shaving, give it two to three weeks.</p></details>
    <details><summary>What if I am on Accutane or using retinol?</summary>
      <p>Tell us before you book. Accutane means waiting six months after your last dose. Retinol
      and strong actives mean pausing for five to seven days on the area being waxed.</p></details>
    <details><summary>Can I get waxed on my period?</summary>
      <p>Yes, as long as you are wearing a tampon or a cup. Skin can be a little more sensitive
      around that week, so bear that in mind if it is your first time.</p></details>
    <details><summary>How often should I come back?</summary>
      <p>Every four to six weeks keeps you on the growth cycle, which means less hair, finer
      regrowth, and a more comfortable wax every time.</p></details>
    <details><summary>Do you wax men?</summary>
      <p>Yes, for most of the menu. Full Face, Full Butt, Butt Strip, and bikini services are
      offered to women only.</p></details>
    <details><summary>Can I bring my daughter?</summary>
      <p>Yes. Guests under 18 need a parent's consent and a signed waiver. For Brazilian and Full
      Bikini the youngest we accept is 16, with the same consent.</p></details>
  </div>
  <p style="text-align:center;margin-top:2rem">
    <span class="tbc">Draft answers, please review and correct these in your own words</span></p>
</section>
''' + CTA

# ---------------------------------------------------------------- ABOUT
def person(name, role, bio):
    return f'''      <div class="person">
        <figure style="display:grid;place-items:center;background:#EFE6D8;border:1px solid var(--line)">
          <img src="{LOGO}/05-icon-and-submark/method-submark-black.svg" alt=""
               style="width:38%;height:auto;object-fit:contain;opacity:.32">
        </figure>
        <div class="role">{role}</div>
        <h3>{name}</h3>
        <p>{bio}</p>
        <p style="margin-top:.6rem"><span class="tbc">photo + bio in her words</span></p>
      </div>'''

ABOUT = f'''
<section class="split wrap rv">
  <div class="split-media"><img src="{u('1687293233752-ec42de2050db')}"
       alt="An esthetician in the warm treatment room"></div>
  <div class="split-copy">
    <span class="u-label">Why We Opened</span>
    <h2>We left, and then we built this.</h2>
    <p>Between us we spent years in the corporate wax world. It taught us the technique and it
    taught us what we never wanted to do again: run people through on a clock, sell them something
    at the table, and call it service.</p>
    <p>Method is small on purpose. Two estheticians, two rooms, appointments paced so nobody is
    hurried. Prices published so nobody is surprised. And the honest answer every time, even when
    the honest answer is that you do not need what you came in asking for.</p>
    <p style="margin-top:-.3rem">We are also a training academy, which changes how we work. When you
    teach the why behind a technique, you cannot cut corners on it yourself.</p>
  </div>
</section>

<section class="band band-paper rv">
  <div class="wrap">
    <div class="band-head">
      <span class="u-label">What We Stand For</span>
      <h2>Four promises, kept quietly.</h2>
    </div>
    <div class="steps narrow">
      <div class="step"><div class="n">1</div><div>
        <h3>Fair pricing, in the open</h3>
        <p>Every price is on this website. No packages you have to ask about, no quiet increase
        because you booked with the busier person.</p></div></div>
      <div class="step"><div class="n">2</div><div>
        <h3>The why, not just the how</h3>
        <p>We will explain what your skin is doing and why we are treating it this way. You should
        leave knowing more than you came in with.</p></div></div>
      <div class="step"><div class="n">3</div><div>
        <h3>No selling at the table</h3>
        <p>You are half undressed and lying down. That is not a moment for a sales pitch, and we
        will never use it as one.</p></div></div>
      <div class="step"><div class="n">4</div><div>
        <h3>Time, not volume</h3>
        <p>We would rather see fewer people properly than more people quickly. It is the entire
        reason we opened our own room.</p></div></div>
    </div>
  </div>
</section>

<section class="band wrap rv">
  <div class="band-head">
    <span class="u-label">The Founders</span>
    <h2>Three of us, one standard.</h2>
    <p>Sophia and Tori are taking guests from opening day. Rachel runs everything behind the
    front desk that makes a studio feel calm.</p>
  </div>
  <div class="people">
{person("Sophia Vega","Founder &#183; Esthetician","Creative, direct, and the one who will tell you exactly what your skin is doing. Skincare, waxing, and training.")}
{person("Tori Foresta","Founder &#183; Esthetician","The business mind of the three, and a technician who can explain the science behind every step. Skincare, waxing, and training.")}
{person("Rachel Scott","Founder &#183; Studio Management","More than a decade in spa management and guest care. If the studio runs calmly, that is Rachel.")}
  </div>
</section>

<section class="quote wrap rv">
  <p>We were told to move faster. We <em>opened our own room</em> instead.</p>
  <div class="cite">The Method Founders</div>
</section>
''' + CTA

# ---------------------------------------------------------------- ACADEMY
ACADEMY = f'''
<section class="split wrap rv">
  <div class="split-media"><img src="{u('1690994065552-6a35a0455ea2')}"
       alt="An olive branch in a soft sunlit still life"></div>
  <div class="split-copy">
    <span class="u-label">In Development</span>
    <h2>Certification, taught the way we wish we had been taught.</h2>
    <p>Method was always meant to be a training academy as much as a studio. The plan is online
    coursework you complete at your own pace, finished with a hands-on intensive in our Naples
    studio, taught by two instructors with different styles and the same fundamentals.</p>
    <p>We are pursuing state continuing education provider approval now. Nothing is open for
    enrollment yet, and we will not pretend otherwise.</p>
  </div>
</section>

<section class="band band-paper rv">
  <div class="wrap">
    <div class="band-head">
      <span class="u-label">The Plan</span>
      <h2>What it will look like.</h2>
    </div>
    <div class="steps narrow">
      <div class="step"><div class="n">1</div><div><h3>Learn online, at your pace</h3>
        <p>Video modules covering skin science, product chemistry, contraindications, and technique,
        which you can revisit as often as you need.</p></div></div>
      <div class="step"><div class="n">2</div><div><h3>Come in for the hands-on day</h3>
        <p>The part you cannot learn from a screen. Small groups, real models, and two instructors
        correcting your hands in the room.</p></div></div>
      <div class="step"><div class="n">3</div><div><h3>Get certified</h3>
        <p>Assessment, certificate, and continuing education hours logged, once our provider
        approval is in place. <span class="tbc">accreditation in progress</span></p></div></div>
      <div class="step"><div class="n">4</div><div><h3>Stay connected</h3>
        <p>Graduates keep access to us. Questions after you are certified are the ones that
        actually matter, and most programs disappear right when they start.</p></div></div>
    </div>
  </div>
</section>

<section class="band band-paper rv">
  <div class="wrap narrow" style="text-align:center">
    <span class="u-label">Interest List</span>
    <h2 style="font-size:clamp(1.9rem,4vw,2.9rem);margin-top:1rem">Be first to know.</h2>
    <p style="color:var(--muted);max-width:46ch;margin:1.1rem auto 2.2rem">No commitment and no
    deposit. We will email you once, when enrollment opens.</p>
    <!-- FORM: wire submissions to Info@MethodWaxPro.Com -->
    <form onsubmit="return false" style="max-width:560px;margin-inline:auto;text-align:left">
      <div class="f2">
        <div class="field"><label for="an">Name</label><input id="an" type="text"></div>
        <div class="field"><label for="ae">Email</label><input id="ae" type="email"></div>
      </div>
      <div class="field"><label for="al">Florida esthetician license number, if you have one</label>
        <input id="al" type="text"></div>
      <button class="btn btn-solid" type="submit">Join the list</button>
    </form>
  </div>
</section>

<section class="band wrap rv">
  <div class="narrow" style="text-align:center">
    <h2 style="font-size:clamp(1.7rem,3.6vw,2.5rem);margin-bottom:1.1rem">In the meantime, the studio is open.</h2>
    <p class="lede" style="margin-inline:auto">Come and see how we work. It is the fastest way to
    understand what we will be teaching.</p>
    <p style="margin-top:1.8rem"><a class="btn btn-ghost" href="services.html">See the menu</a></p>
  </div>
</section>
'''

# ---------------------------------------------------------------- CONTACT
CONTACT = f'''
<section class="band wrap rv">
  <div style="display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(2rem,5vw,5rem);align-items:start"
       class="contact-grid plain">
    <div>
      <h2 style="font-size:clamp(1.6rem,3.2vw,2.2rem);margin-bottom:1.4rem">The studio</h2>
      <p class="addr">1410 Pine Ridge Road, Suite 22<br>Naples, FL 34108<br><br>
        <a href="tel:+12395295441">(239) 529-5441</a><br>
        <a href="mailto:Info@MethodWaxPro.Com">Info@MethodWaxPro.Com</a></p>
      <div class="hours" style="margin-top:2rem">
        <div><span>Monday to Thursday</span><span>8am to 8pm</span></div>
        <div><span>Friday</span><span>8am to 6pm</span></div>
        <div><span>Saturday</span><span>9am to 3pm</span></div>
        <div><span>Sunday</span><span>10am to 5pm</span></div>
      </div>
      <p style="margin-top:1.8rem;color:var(--muted);font-size:.9rem">Parking and how to find
      Suite 22 <span class="tbc">details needed</span></p>
    </div>
    <!-- CONTACT FORM: wire submissions to Info@MethodWaxPro.Com -->
    <form onsubmit="return false">
      <div class="f2">
        <div class="field"><label for="fn">First name</label><input id="fn" type="text" autocomplete="given-name"></div>
        <div class="field"><label for="ln">Last name</label><input id="ln" type="text" autocomplete="family-name"></div>
      </div>
      <div class="f2">
        <div class="field"><label for="em">Email</label><input id="em" type="email" autocomplete="email"></div>
        <div class="field"><label for="ph">Phone</label><input id="ph" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="tp">What is this about</label>
        <select id="tp">
          <option>A waxing service</option>
          <option>The Method Set</option>
          <option>Professional training and the academy</option>
          <option>Something else</option>
        </select></div>
      <div class="field"><label for="ms">Message</label><textarea id="ms"></textarea></div>
      <button class="btn btn-solid" type="submit">Send message</button>
    </form>
  </div>
</section>

<section class="band band-paper rv">
  <div class="wrap" style="text-align:center">
    <div style="background:#EFE6D8;border:1px solid var(--line);height:clamp(220px,32vw,380px);
                display:grid;place-items:center;color:var(--muted);font-size:.72rem;
                letter-spacing:.24em;text-transform:uppercase">
      Google map embed <span class="tbc">add at build</span>
    </div>
  </div>
</section>
''' + CTA

# ---------------------------------------------------------------- EMIT
PAGES = [
 ("index.html", "METHOD &#183; Luxury Waxing &#183; Naples, Florida",
  "Luxury waxing in Naples, Florida. Fair pricing, real care, technique held to the standard we teach professionals. Now booking for October 5.",
  HOME, HOME_HERO),
 ("services.html", "Services and Pricing &#183; METHOD Luxury Waxing &#183; Naples",
  "The full METHOD waxing menu and prices. Brazilian $64, Full Bikini $56, Eyebrow $24. Every price published openly. Naples, Florida.",
  SERVICES, phead("The Menu","Services and pricing.",
   "Thirty six services, every price in the open. Book any of them online, and if you are not sure what to choose, call and we will talk it through.")),
 ("first-visit.html", "Your First Visit &#183; METHOD Luxury Waxing &#183; Naples",
  "How to prepare for your first wax, what happens in the room, aftercare, and our policies. METHOD Luxury Waxing, Naples, Florida.",
  FIRST, phead("Your First Visit","What to know before you come in.",
   "Nobody explains this part properly, so we will. How to prepare, what actually happens in the room, and how to look after your skin afterward.")),
 ("about.html", "About &#183; METHOD Luxury Waxing &#183; Naples, Florida",
  "Method is a Naples waxing studio and training academy founded by three estheticians who left the corporate wax world. Fair pricing, real care.",
  ABOUT, phead("About","A training academy that happens to have the best room in town.",
   "Three estheticians who left the production line and built the studio they wanted to work in.")),
 ("academy.html", "The Academy &#183; METHOD Professional Waxing Training &#183; Naples",
  "Professional waxing certification from METHOD in Naples, Florida. Online coursework plus a hands-on studio intensive. In development, join the interest list.",
  ACADEMY, phead("The Academy","Professional training, coming soon.",
   "Waxing certification for estheticians, taught online and finished by hand in our Naples studio. In development now.")),
 ("contact.html", "Contact &#183; METHOD Luxury Waxing &#183; Naples, Florida",
  "Call (239) 529-5441 or visit METHOD Luxury Waxing at 1410 Pine Ridge Road, Suite 22, Naples, FL 34108. Hours, directions and contact form.",
  CONTACT, phead("Contact","Say hello.",
   "Questions about a service, a set, or the academy. We answer every message ourselves.")),
]

for slug, title, desc, body, hero in PAGES:
    page = shell(slug, title, desc, body, hero)
    # booking leaves the site, so open it in a new tab and keep ours behind
    page = page.replace('href="%s"' % BOOK,
                        'href="%s" target="_blank" rel="noopener"' % BOOK)
    open(slug,"w").write(page)
    print("built", slug)
