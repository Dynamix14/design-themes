#!/usr/bin/env python3
"""Generate the theme gallery: one full sample page per theme + an index.

Run:  python build.py
Output: index.html, themes/<slug>.html, themes.json, README.md
Edit themes_data.py, not the generated HTML.
"""
import html
import json
import os
import re

from themes_data import THEMES, FALLBACK

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "themes")

# Google Fonts only ships specific weights for some families; asking for a
# weight that does not exist makes the whole stylesheet 400 and kills every
# font on the page, so keep these explicit.
WEIGHTS = {
    "Instrument Serif": "400",
    "Bebas Neue": "400",
    "Press Start 2P": "400",
    "VT323": "400",
    "Libre Baskerville": "400;700",
    "Cormorant Garamond": "300;400;500;600;700",
}
DEFAULT_WEIGHTS = "400;500;600;700"
# How much larger/smaller a face renders at the same px size. Pixel and wide
# display faces need a much lower cap or the hero overflows at 72px.
TYPE_SCALE = {
    "Press Start 2P": 0.42,
    "Orbitron": 0.72,
    "Bebas Neue": 0.92,
    "Syne": 0.86,
    "Caveat": 1.1,
    "Cormorant Garamond": 1.12,
    "Instrument Serif": 1.0,
    "Playfair Display": 1.0,
}
SYSTEM_FAMILIES = {"-apple-system"}


# ------------------------------------------------------------------ helpers
def lum(hexcolor):
    h = hexcolor.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def on_color(hexcolor):
    return "#0B0B0C" if lum(hexcolor) > 0.45 else "#FFFFFF"


def split_font(spec):
    family, kind = spec.split("|")
    if family in SYSTEM_FAMILIES:
        stack = ('-apple-system, BlinkMacSystemFont, "SF Pro Display", '
                 '"Segoe UI", system-ui, sans-serif')
    else:
        stack = f"'{family}', {FALLBACK[kind]}"
    return family, stack


def google_link(themes):
    fams = []
    for t in themes:
        for spec in (t["fh"], t["fb"]):
            fam = spec.split("|")[0]
            if fam in SYSTEM_FAMILIES or fam in fams:
                continue
            fams.append(fam)
    if not fams:
        return ""
    parts = []
    for fam in fams:
        w = WEIGHTS.get(fam, DEFAULT_WEIGHTS)
        parts.append("family=" + fam.replace(" ", "+") + ":wght@" + w)
    url = "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=swap"
    return f'<link rel="preconnect" href="https://fonts.googleapis.com">\n' \
           f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n' \
           f'<link href="{url}" rel="stylesheet">'


def esc(s):
    return html.escape(s, quote=True)


# ------------------------------------------------------------------ page CSS
PAGE_CSS = """
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--fb);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;
  text-rendering:optimizeLegibility}
img,svg{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
::selection{background:var(--accent);color:var(--on-accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}

.wrap{width:100%;max-width:var(--max);margin:0 auto;padding:0 28px}
.muted{color:var(--muted)}
.accent{color:var(--accent)}
h1,h2,h3,h4{font-family:var(--fh);font-weight:600;margin:0;color:var(--text)}
h1{font-size:var(--h1);line-height:1.02;letter-spacing:var(--track-h)}
h2{font-size:clamp(28px,3.1vw,40px);line-height:1.1;letter-spacing:var(--track-h)}
h3{font-size:19px;line-height:1.3;letter-spacing:var(--track-h)}
p{margin:0}
.mono{font-family:var(--fmono)}

/* ---- chrome ---- */
.gallerybar{background:var(--surface-2);border-bottom:1px solid var(--line);
  font-size:12px;color:var(--muted)}
.gallerybar .wrap{display:flex;justify-content:space-between;gap:16px;align-items:center;
  height:38px;letter-spacing:.02em}
.gallerybar a{color:var(--text);font-weight:600}
.gallerybar a:hover{color:var(--accent)}
.gallerybar .tag{text-transform:uppercase;letter-spacing:.12em;font-size:10.5px;
  font-weight:700;opacity:.8}

nav.top{position:sticky;top:0;z-index:40;background:var(--nav-bg);
  backdrop-filter:blur(14px) saturate(140%);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;gap:34px;height:70px}
.brand{display:flex;align-items:center;gap:10px;font-family:var(--fh);
  font-weight:700;font-size:19px;letter-spacing:var(--track-h)}
.mark{width:26px;height:26px;border-radius:var(--r-mark);background:var(--accent);
  display:grid;place-items:center;color:var(--on-accent);font-size:13px;
  font-weight:800;flex:none}
.nav-links{display:flex;gap:26px;margin-left:8px;font-size:14.5px;color:var(--muted)}
.nav-links a:hover{color:var(--text)}
.nav-cta{margin-left:auto;display:flex;gap:10px;align-items:center}

.btn{display:inline-flex;align-items:center;gap:8px;font-family:var(--fb);
  font-size:14.5px;font-weight:600;padding:11px 18px;border-radius:var(--r-btn);
  border:1px solid transparent;cursor:pointer;transition:transform .14s ease,
  background .14s ease,box-shadow .14s ease;letter-spacing:var(--track-b)}
.btn-primary{background:var(--accent);color:var(--on-accent)}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 10px 26px -14px var(--accent)}
.btn-ghost{background:transparent;color:var(--text);border-color:var(--line)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent)}
.btn-lg{padding:14px 24px;font-size:15.5px}

/* ---- hero ---- */
.hero{padding:76px 0 12px;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1.06fr .94fr;gap:56px;align-items:center}
.hero-grid h1{font-size:var(--h1-split);line-height:1.04}
.hero-center{text-align:center;max-width:820px;margin:0 auto}
.hero-center .lede{margin-left:auto;margin-right:auto}
.hero-center .hero-actions{justify-content:center}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:11px;
  font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
  border:1px solid var(--line);border-radius:999px;padding:6px 12px;
  background:var(--surface);margin-bottom:22px}
.dot{width:6px;height:6px;border-radius:50%;background:var(--accent)}
.lede{font-size:clamp(16px,1.25vw,18.5px);color:var(--muted);max-width:56ch;
  margin-top:22px;line-height:1.65}
.hero-actions{display:flex;gap:12px;margin-top:30px;flex-wrap:wrap}
.hero-meta{display:flex;gap:26px;margin-top:30px;flex-wrap:wrap;font-size:13px;
  color:var(--muted)}
.hero-meta span{display:flex;align-items:center;gap:7px}
.grad-text{background:linear-gradient(100deg,var(--accent),var(--accent-2) 62%,var(--accent));
  -webkit-background-clip:text;background-clip:text;color:transparent}

/* ---- product panel ---- */
.panel{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);
  box-shadow:var(--shadow);overflow:hidden}
.panel-bar{display:flex;align-items:center;gap:7px;padding:11px 14px;
  border-bottom:1px solid var(--line);background:var(--surface-2)}
.panel-bar i{width:9px;height:9px;border-radius:50%;background:var(--line);display:block}
.panel-bar .tag{margin-left:auto;font-size:10.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--muted);font-weight:700}
.panel-body{padding:18px}
.chart{display:flex;align-items:flex-end;gap:7px;height:132px;margin:14px 0 4px}
.chart b{flex:1;background:var(--accent);border-radius:var(--r-bar);opacity:.32;
  display:block;transition:opacity .2s}
.chart b:nth-child(3n){opacity:.85}
.chart b:nth-child(4n+1){opacity:.55;background:var(--accent-2)}
.kpis{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.kpi{border:1px solid var(--line);border-radius:calc(var(--r) * .7);padding:11px 13px;
  background:var(--surface-2)}
.kpi small{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);font-weight:700;margin-bottom:4px}
.kpi strong{font-family:var(--fh);font-size:22px;letter-spacing:var(--track-h)}

/* ---- sections ---- */
section{padding:64px 0}
.sec-head{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;
  margin-bottom:34px;flex-wrap:wrap}
.sec-head p{color:var(--muted);max-width:52ch;margin-top:10px;font-size:15px}
.rule{height:1px;background:var(--line);border:0;margin:0}

.logos{display:flex;flex-wrap:wrap;gap:38px;align-items:center;justify-content:space-between;
  padding:26px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);
  color:var(--muted);font-weight:700;letter-spacing:.1em;font-size:13px;
  text-transform:uppercase}
.logos span{opacity:.6}

.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);
  padding:24px;box-shadow:var(--shadow-soft);transition:transform .16s ease,border-color .16s ease}
.card:hover{transform:translateY(-2px);border-color:var(--accent)}
.card .ico{width:38px;height:38px;border-radius:calc(var(--r) * .6);display:grid;
  place-items:center;background:var(--accent-soft);color:var(--accent);margin-bottom:16px;
  font-size:16px;font-weight:800}
.card p{color:var(--muted);font-size:14.5px;margin-top:8px}

.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line)}
.stat{padding:26px 24px 0;border-left:1px solid var(--line)}
.stat:first-child{border-left:0;padding-left:0}
.stat strong{display:block;font-family:var(--fh);font-size:40px;line-height:1;
  letter-spacing:var(--track-h)}
.stat small{display:block;color:var(--muted);font-size:13px;margin-top:8px}

.price-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.price{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);
  padding:26px;display:flex;flex-direction:column;gap:14px;box-shadow:var(--shadow-soft)}
.price.hot{border-color:var(--accent);box-shadow:var(--shadow)}
.price .amt{font-family:var(--fh);font-size:42px;line-height:1;letter-spacing:var(--track-h)}
.price .amt span{font-size:14px;color:var(--muted);font-family:var(--fb);letter-spacing:0}
.price ul{list-style:none;margin:0;padding:0;display:grid;gap:9px;font-size:14px;color:var(--muted)}
.price li{display:flex;gap:9px;align-items:flex-start}
.tick{color:var(--accent);font-weight:800;flex:none}
.price .btn{margin-top:auto;justify-content:center}

.cta{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);
  padding:46px;display:flex;align-items:center;justify-content:space-between;gap:30px;
  box-shadow:var(--shadow);flex-wrap:wrap}
.cta h2{max-width:22ch}
.cta p{color:var(--muted);margin-top:12px;max-width:44ch}

footer{border-top:1px solid var(--line);padding:44px 0 60px;color:var(--muted);font-size:13.5px}
.foot-grid{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:30px}
.foot-grid h4{font-size:12px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--text);margin-bottom:10px;font-family:var(--fb);font-weight:700}
.foot-grid ul{list-style:none;margin:0;padding:0;display:grid;gap:7px}
.foot-bottom{display:flex;justify-content:space-between;gap:16px;margin-top:34px;
  padding-top:20px;border-top:1px solid var(--line);flex-wrap:wrap;font-size:12.5px}

/* ---- flavour flags ---- */
.f-caps .nav-links,.f-caps .eyebrow,.f-caps .logos,.f-caps .foot-grid h4{
  text-transform:uppercase;letter-spacing:.16em;font-size:12px}
.f-tight h1,.f-tight h2{letter-spacing:-.04em}
.f-wide h1{letter-spacing:-.015em}
body>*{position:relative;z-index:1}
.f-grid::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
  background-image:linear-gradient(var(--line) 1px,transparent 1px),
  linear-gradient(90deg,var(--line) 1px,transparent 1px);
  background-size:64px 64px;opacity:.35}
.f-grain::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:50;
  opacity:.05;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='120' height='120' filter='url(%23n)'/%3E%3C/svg%3E")}
.f-glow .panel{box-shadow:0 40px 90px -40px var(--accent),var(--shadow)}
.f-blur .panel,.f-blur .kpi,.f-blur .card{background:var(--glass);backdrop-filter:blur(18px)}
body.f-mono{font-family:var(--fmono);font-size:15px}
body.f-mono .lede,body.f-mono .card p,body.f-mono .price p{font-family:var(--fmono)}
.f-hard .card,.f-hard .price,.f-hard .panel,.f-hard .cta,.f-hard .btn{
  border-width:2px;border-color:var(--text);box-shadow:5px 5px 0 var(--text)}
.f-hard .btn-primary{box-shadow:4px 4px 0 var(--text)}
.f-hard .card:hover,.f-hard .price.hot{transform:translate(-1px,-1px);box-shadow:7px 7px 0 var(--text)}

@media (max-width:960px){
  .btn{white-space:nowrap}
  .nav-in{gap:14px;height:62px}
  .nav-cta .btn-ghost{display:none}
  .nav-cta .btn{padding:10px 14px;font-size:14px}
  .gallerybar .wrap{height:auto;padding:7px 0;flex-wrap:wrap;gap:2px;
    align-items:flex-start;font-size:11px}
  .gallerybar .tag{font-size:9.5px;letter-spacing:.09em}
  .hero{padding:44px 0 8px}
  .lede{margin-top:18px}
  .hero-actions{margin-top:24px}
  .hero-grid{grid-template-columns:1fr;gap:36px}
  .grid3,.price-grid,.stats{grid-template-columns:1fr}
  .stat{border-left:0;border-top:1px solid var(--line);padding:20px 0 0}
  .stat:first-child{border-top:0}
  .foot-grid{grid-template-columns:1fr 1fr}
  .nav-links{display:none}
  .cta{padding:30px}
  h1{font-size:calc(var(--h1) * .84)}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""


def page(t, all_themes):
    fh_family, fh_stack = split_font(t["fh"])
    fb_family, fb_stack = split_font(t["fb"])
    flags = set(t["flags"])
    cls = [f"treat-{t['treat']}"] + [f"f-{f}" for f in flags]
    if t["treat"] == "hard":
        cls.append("f-hard")
    acc, acc2 = t["accent"], t["accent2"]
    vars_css = f"""
  --bg:{t['bg']};
  --surface:{t['surface']};
  --line:{t['line']};
  --text:{t['text']};
  --muted:{t['muted']};
  --accent:{acc};
  --accent-2:{acc2};
  --on-accent:{on_color(acc)};
  --surface-2:{'color-mix(in srgb, ' + t['surface'] + ' 88%, ' + t['text'] + ')'};
  --accent-soft:{'color-mix(in srgb, ' + acc + ' 14%, transparent)'};
  --glass:{'color-mix(in srgb, ' + t['surface'] + ' 62%, transparent)'};
  --nav-bg:{'color-mix(in srgb, ' + t['bg'] + ' 82%, transparent)'};
  --r:{t['radius']}px;
  --r-btn:{max(2, round(t['radius'] * 0.55))}px;
  --r-mark:{max(2, round(t['radius'] * 0.5))}px;
  --r-bar:{max(0, round(t['radius'] * 0.3))}px;
  --max:1140px;
  --fh:{fh_stack};
  --fb:{fb_stack};
  --fmono:'JetBrains Mono', {FALLBACK['mono']};
  --track-h:{'-0.045em' if 'tight' in flags else ('0.01em' if 'wide' in flags else '-0.02em')};
  --track-b:0em;
  --h1:clamp({round(42 * _sc(t))}px,{round(5.4 * _sc(t), 2)}vw,{round(72 * _sc(t))}px);
  --h1-split:clamp({round(34 * _sc(t))}px,{round(3.9 * _sc(t), 2)}vw,{round(56 * _sc(t))}px);
  --shadow:{_shadow(t)};
  --shadow-soft:{_shadow(t, soft=True)};
"""

    hero_tag = "The theme gallery / %s" % t["name"]
    hero_inner = f"""
      <div class="eyebrow"><span class="dot"></span>{esc(_short(t))}</div>
      <h1>{_headline(t)}</h1>
      <p class="lede">{_lede(t)}</p>
      <div class="hero-actions">
        <a class="btn btn-primary btn-lg" href="#pricing">Start free trial</a>
        <a class="btn btn-ghost btn-lg" href="#features">See how it works</a>
      </div>
      <div class="hero-meta">
        <span>◆ No credit card</span><span>◆ SOC 2 Type II</span><span>◆ 4.9/5 on G2</span>
      </div>"""

    if t["hero"] == "center":
        hero = f'<div class="wrap"><div class="hero-center">{hero_inner}</div>' \
               f'<div style="margin-top:48px">{_panel()}</div></div>'
    elif t["hero"] == "stack":
        hero = f'<div class="wrap">{hero_inner}<div style="margin-top:44px">{_panel()}</div></div>'
    else:
        hero = f'<div class="wrap"><div class="hero-grid"><div>{hero_inner}</div>' \
               f'<div>{_panel()}</div></div></div>'

    page_html = HTML_PAGE
    page_html = page_html.replace("<!--HEAD-->", google_link(all_themes) if False else google_link([t]))
    page_html = page_html.replace("<!--VARS-->", vars_css)
    page_html = page_html.replace("<!--BODYCLASS-->", " ".join(cls))
    page_html = page_html.replace("<!--TITLE-->", esc(t["name"]) + " — Aperture sample")
    page_html = page_html.replace("<!--THEMENAME-->", esc(t["name"]))
    page_html = page_html.replace("<!--NAVLABEL-->", esc(t["name"]))
    page_html = page_html.replace("<!--COUNT-->", str(len(THEMES)))
    page_html = page_html.replace(
        "<!--THEMEMETA-->",
        esc(t["name"]) + " · " + t["mode"] + " · " + esc(t["cat"]))
    page_html = page_html.replace("<!--BODY-->", _body(t, flags, hero))
    return page_html


def _shadow(t, soft=False):
    if t["treat"] == "hard":
        return "5px 5px 0 var(--text)"
    if t["treat"] == "flat":
        return "none" if soft else "none"
    if t["treat"] == "glow":
        base = "0 24px 70px -34px rgba(0,0,0,.75), 0 0 0 1px color-mix(in srgb, var(--accent) 12%, transparent)"
        return "0 10px 24px -18px rgba(0,0,0,.5)" if soft else base
    return ("0 2px 6px -2px rgba(0,0,0,.12)" if soft
            else "0 1px 2px rgba(0,0,0,.06), 0 18px 44px -26px rgba(0,0,0,.35)")


def _sc(t):
    return TYPE_SCALE.get(t["fh"].split("|")[0], 1.0)


def _short(t):
    """Short label for the eyebrow chip: 'Claude / Anthropic warm editorial' -> 'Claude'."""
    return t["name"].split(" / ")[0]


def _headline(t):
    grad = "grad" in t["flags"]
    tail = 'class="grad-text"' if grad else ""
    return f'Know exactly where<br>your product <span {tail}>loses people</span>.' if grad else \
           'Know exactly where<br>your product loses people.'


def _lede(t):
    base = ("Aperture is the visual analytics layer for product teams — session replay, "
            "funnel truth, and alerts that fire before your users complain.")
    return esc(base if not t["note"] else base)


def _panel():
    heights = [38, 62, 48, 84, 56, 96, 72, 88, 44, 68, 92, 58, 78, 40]
    bars = "".join(f'<b style="height:{h}%"></b>' for h in heights)
    return f"""
    <div class="panel">
      <div class="panel-bar"><i></i><i></i><i></i><span class="tag">live · 14d</span></div>
      <div class="panel-body">
        <div style="display:flex;justify-content:space-between;align-items:baseline">
          <div style="font-family:var(--fh);font-size:15px;letter-spacing:var(--track-h)">Active sessions</div>
          <div class="mono" style="font-size:12px;color:var(--accent)">+18.4%</div>
        </div>
        <div class="chart">{bars}</div>
        <div class="kpis">
          <div class="kpi"><small>Sessions</small><strong>24,918</strong></div>
          <div class="kpi"><small>Conversion</small><strong>6.2%</strong></div>
        </div>
      </div>
    </div>"""


def _body(t, flags, hero):
    features = [
        ("01", "Session replay", "Scrub any session at 10x speed and jump straight to the moment intent breaks."),
        ("02", "Funnel truth", "Compare cohorts without waiting on a data team or a Monday sync."),
        ("03", "Signal alerts", "Thresholds that page you only when a real user path regresses."),
    ]
    cards = "".join(
        f'<article class="card"><div class="ico">{n}</div><h3>{h}</h3><p>{p}</p></article>'
        for n, h, p in features)
    plans = [
        ("Starter", "0", "For solo builders shipping their first flow.", "Get started", False),
        ("Team", "29", "For product teams that argue with data, not opinions.", "Start trial", True),
        ("Scale", "89", "For orgs with audit, SSO, and a lot of stakeholders.", "Talk to sales", False),
    ]
    pricing = "".join(f"""
      <div class="price{' hot' if hot else ''}">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <h3>{name}</h3>{'<span class="eyebrow" style="margin:0">Popular</span>' if hot else ''}
        </div>
        <div class="amt">${amt}<span> /month</span></div>
        <p class="muted" style="font-size:14px">{desc}</p>
        <ul><li><span class="tick">✓</span>Unlimited events</li>
            <li><span class="tick">✓</span>Session replay retention</li>
            <li><span class="tick">✓</span>Slack + webhook alerts</li></ul>
        <a class="btn {'btn-primary' if hot else 'btn-ghost'}" href="#">{cta}</a>
      </div>""" for name, amt, desc, cta, hot in plans)

    return f"""
  <div class="hero">{hero}</div>

  <div class="wrap"><div class="logos">
    <span>Northwind</span><span>Vercel</span><span>Ramp</span><span>Linear</span><span>Supabase</span>
  </div></div>

  <section id="features"><div class="wrap">
    <div class="sec-head">
      <div><h2>Everything you need to see<br>where the product leaks</h2>
      <p>One tool for the three questions every launch raises: who got stuck, where, and what changed.</p></div>
      <a class="btn btn-ghost" href="#">Browse docs →</a>
    </div>
    <div class="grid3">{cards}</div>
    <div class="stats" style="margin-top:38px">
      <div class="stat"><strong>2.4M</strong><small>Sessions analysed per day</small></div>
      <div class="stat"><strong>180ms</strong><small>Median query latency</small></div>
      <div class="stat"><strong>99.98%</strong><small>Ingest uptime, trailing 90 days</small></div>
    </div>
  </div></section>

  <section id="pricing" style="padding-top:12px"><div class="wrap">
    <div class="sec-head"><div><h2>Simple pricing</h2>
      <p>Every plan includes the full event pipeline. Pay for seats and retention.</p></div></div>
    <div class="price-grid">{pricing}</div>
  </div></section>

  <section style="padding-top:8px"><div class="wrap">
    <div class="cta">
      <div><h2>Try this theme on your own copy</h2>
        <p>Edit the tokens in <span class="mono">themes_data.py</span> and re-run the build — every colour, radius and type choice here is data.</p>
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a class="btn btn-primary btn-lg" href="../index.html">Back to gallery</a>
      </div>
    </div>
  </div></section>

  <footer><div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="brand" style="margin-bottom:10px"><span class="mark">A</span>Aperture</div>
        <p style="max-width:32ch">Sample page generated for the theme gallery. Content is placeholder.</p>
      </div>
      <div><h4>Product</h4><ul><li>Replay</li><li>Funnels</li><li>Alerts</li></ul></div>
      <div><h4>Company</h4><ul><li>About</li><li>Careers</li><li>Press</li></ul></div>
      <div><h4>Legal</h4><ul><li>Privacy</li><li>Terms</li><li>DPA</li></ul></div>
    </div>
    <div class="foot-bottom"><span>© 2026 Aperture Labs</span><span class="mono">{esc(t['slug'])}.html · {t['mode']} · {esc(t['cat'])}</span></div>
  </div></footer>
"""


HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><!--TITLE--></title>
<meta name="description" content="Sample page for the <!--TITLE--> frontend theme.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><rect width='16' height='16' rx='4' fill='%23111'/><text x='8' y='12' font-size='10' fill='white' text-anchor='middle' font-family='sans-serif'>A</text></svg>">
<!--HEAD-->
<style>
:root{<!--VARS-->}
""" + PAGE_CSS + """
</style>
</head>
<body class="<!--BODYCLASS-->">
<div class="gallerybar"><div class="wrap">
  <a href="../index.html">← All <!--COUNT--> themes</a>
  <span class="tag"><!--THEMEMETA--></span>
</div></div>
<nav class="top"><div class="wrap nav-in">
  <a class="brand" href="../index.html"><span class="mark">A</span>Aperture</a>
  <div class="nav-links"><a href="#features">Product</a><a href="#features">Docs</a>
    <a href="#pricing">Pricing</a><a href="#pricing">Customers</a></div>
  <div class="nav-cta"><a class="btn btn-ghost" href="#">Sign in</a>
    <a class="btn btn-primary" href="#pricing">Get started</a></div>
</div></nav>
<!--BODY-->
</body>
</html>
"""


# ------------------------------------------------------------------ index
INDEX_CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --bg:#08080A;--card:#101013;--card-2:#151519;--line:#232329;--text:#F4F4F6;
  --muted:#8D8D98;--accent:#C6F24E;--r:14px;
}
body{margin:0;background:var(--bg);color:var(--text);
  font:15px/1.55 'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
h1,h2,h3{margin:0;line-height:1.05;letter-spacing:-.03em}
.wrap{max-width:1460px;margin:0 auto;padding:0 30px}
header.top{padding:56px 0 30px;border-bottom:1px solid var(--line)}
.kicker{display:inline-flex;align-items:center;gap:9px;font-size:11px;font-weight:700;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);
  border:1px solid var(--line);border-radius:999px;padding:7px 13px;margin-bottom:22px}
.kicker b{color:var(--accent)}
h1{font-size:clamp(38px,4.6vw,66px);font-weight:650}
h1 em{font-style:normal;color:var(--accent)}
.sub{color:var(--muted);max-width:62ch;margin-top:18px;font-size:16.5px}
.controls{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-top:34px}
.search{flex:1 1 300px;display:flex;align-items:center;gap:10px;background:var(--card);
  border:1px solid var(--line);border-radius:10px;padding:11px 14px}
.search input{flex:1;background:none;border:0;outline:0;color:var(--text);font-size:14.5px;
  font-family:inherit}
.search svg{opacity:.5;flex:none}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{background:var(--card);border:1px solid var(--line);color:var(--muted);
  border-radius:999px;padding:9px 15px;font:600 13px/1 inherit;cursor:pointer;
  transition:.15s}
.chip:hover{color:var(--text);border-color:#3A3A44}
.chip[aria-pressed="true"]{background:var(--accent);color:#0A0A0C;border-color:var(--accent)}
.toolbar{display:flex;justify-content:space-between;align-items:baseline;
  padding:26px 0 16px;color:var(--muted);font-size:13px;gap:16px;flex-wrap:wrap}
.toolbar b{color:var(--text)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(370px,1fr));gap:24px;
  padding-bottom:70px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:var(--r);
  overflow:hidden;transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease;
  display:flex;flex-direction:column}
.tile:hover{transform:translateY(-3px);border-color:#3C3C48;
  box-shadow:0 26px 60px -34px rgba(0,0,0,.9)}
.shot{position:relative;aspect-ratio:16/10;overflow:hidden;background:#fff;
  border-bottom:1px solid var(--line);container-type:inline-size;
  display:block;color:inherit}
.mini{position:absolute;inset:0;display:flex;flex-direction:column;
  padding:4.4cqw 5cqw;background:var(--m-bg);color:var(--m-text);
  font-family:var(--m-fb);overflow:hidden}
.m-nav{display:flex;align-items:center;gap:2.2cqw;font-size:2.2cqw;
  color:var(--m-muted);flex:none}
.m-mark{width:3.1cqw;height:3.1cqw;background:var(--m-accent);flex:none;
  border-radius:calc(var(--m-r) * .45)}
.m-nav u{width:6.4cqw;height:1.05cqw;background:currentColor;opacity:.45;
  border-radius:1px;text-decoration:none}
.m-nav i{margin-left:auto;width:12.5cqw;height:4.3cqw;background:var(--m-accent);
  border-radius:calc(var(--m-r) * .5)}
.m-h{font-family:var(--m-fh);font-weight:600;font-size:5.2cqw;line-height:1.06;
  letter-spacing:-.022em;margin:4.2cqw 0 0;max-width:82%}
.m-sub{font-size:2.6cqw;color:var(--m-muted);margin:2cqw 0 0;max-width:74%;
  line-height:1.45}
.m-cta{margin-top:2.6cqw;align-self:flex-start;background:var(--m-accent);
  color:var(--m-on);font-size:2.4cqw;font-weight:600;padding:1.4cqw 3cqw;
  border-radius:calc(var(--m-r) * .5)}
.m-panel{margin-top:auto;background:var(--m-surface);border:1px solid var(--m-line);
  border-radius:var(--m-r);padding:2.4cqw 2.8cqw;height:26%;display:flex;
  flex-direction:column;gap:1.6cqw}
.m-panel em{display:flex;justify-content:space-between;font-size:2cqw;
  color:var(--m-muted);font-style:normal}
.m-bars{display:flex;align-items:flex-end;gap:1.1cqw;flex:1;min-height:0}
.m-bars b{flex:1;background:var(--m-accent);opacity:.32;border-radius:1px;
  display:block;min-height:2px}
.m-bars b:nth-child(3n){opacity:.9}
.m-bars b:nth-child(4n+1){opacity:.6;background:var(--m-accent2)}
.shot .overlay{position:absolute;inset:0;display:flex;align-items:flex-end;
  justify-content:flex-end;padding:12px;opacity:0;transition:opacity .18s;
  background:linear-gradient(to top,rgba(0,0,0,.5),transparent 45%)}
.tile:hover .overlay{opacity:1}
.open{background:rgba(10,10,12,.86);border:1px solid rgba(255,255,255,.18);color:#fff;
  font:600 12px/1 inherit;padding:9px 13px;border-radius:8px;backdrop-filter:blur(6px)}
.meta{position:relative;padding:15px 16px 17px;display:flex;gap:12px;align-items:flex-start}
.swatches{display:flex;flex-direction:column;gap:3px;padding-top:2px}
.sw{width:14px;height:14px;border-radius:4px;border:1px solid rgba(255,255,255,.14)}
.meta .txt{min-width:0;flex:1}
.meta h3{font-size:15px;font-weight:600;letter-spacing:-.01em;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
.meta p{margin:4px 0 0;color:var(--muted);font-size:12.5px;
  display:flex;gap:7px;align-items:center;flex-wrap:wrap}
.pill{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  border:1px solid var(--line);border-radius:5px;padding:3px 6px;color:var(--muted)}
.pill.dark{color:#B9B9C6}
.pill.light{color:#F0E3B4;border-color:#3A3524}
.star{position:absolute;left:10px;top:10px;z-index:2;width:30px;height:30px;
  border-radius:8px;background:rgba(10,10,12,.6);border:1px solid rgba(255,255,255,.16);
  color:#fff;font-size:15px;line-height:1;cursor:pointer;display:grid;place-items:center;
  backdrop-filter:blur(6px);opacity:0;transition:.15s}
.tile:hover .star,.star.on{opacity:1}
.star.on{color:#C6F24E;border-color:rgba(198,242,78,.5)}
.copy{position:absolute;right:14px;top:12px;background:#191920;border:1px solid var(--line);
  color:var(--muted);border-radius:6px;font:600 11px/1 inherit;padding:6px 8px;
  cursor:pointer;opacity:0;transition:.15s}
.tile:hover .copy{opacity:1}
.copy:hover{color:var(--text);border-color:#3C3C48;background:#202028}
.toast{position:fixed;left:50%;bottom:26px;transform:translate(-50%,14px);z-index:99;
  background:#C6F24E;color:#0A0A0C;font:700 13px/1 inherit;padding:11px 18px;
  border-radius:9px;opacity:0;pointer-events:none;transition:.2s}
.toast.on{opacity:1;transform:translate(-50%,0)}
.empty{display:none;padding:80px 0;text-align:center;color:var(--muted)}
.empty h2{font-size:22px;color:var(--text);margin-bottom:8px}
footer{border-top:1px solid var(--line);padding:34px 0 60px;color:var(--muted);font-size:13px;
  display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
footer a{color:var(--text);border-bottom:1px solid var(--line)}
.note{background:var(--card);border:1px solid var(--line);border-radius:var(--r);
  padding:24px 26px;margin:0 0 40px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.note h3{font-size:15px;margin-bottom:8px}
.note p{color:var(--muted);font-size:13.5px;margin:0}
.note code{background:#1B1B21;border-radius:4px;padding:1px 5px;font-size:12px}
@media(max-width:820px){.note{grid-template-columns:1fr}.grid{grid-template-columns:1fr}
  .copy,.star{opacity:.62}
  .tile:hover .copy,.tile:hover .star{opacity:1}}
"""

INDEX_JS = """
const tiles=[...document.querySelectorAll('.tile')];
const toast=document.getElementById('toast');
let toastTimer;
function flash(msg){toast.textContent=msg;toast.classList.add('on');
  clearTimeout(toastTimer);toastTimer=setTimeout(()=>toast.classList.remove('on'),1600);}
document.addEventListener('click',e=>{
  const b=e.target.closest('.copy'); if(!b) return;
  e.preventDefault(); e.stopPropagation();
  const css=TOKENS[b.dataset.slug]||'';
  const done=()=>{b.textContent='✓ copied';flash('CSS tokens copied');
    setTimeout(()=>b.textContent='⧉ tokens',1500);};
  const fallback=()=>{
    const ta=document.createElement('textarea');ta.value=css;
    ta.style.cssText='position:fixed;top:0;left:-9999px';
    document.body.appendChild(ta);ta.select();
    try{document.execCommand('copy')?done():flash('Copy blocked — open a theme and view source');}
    catch(e){flash('Copy blocked — open a theme and view source');}
    document.body.removeChild(ta);
  };
  if(navigator.clipboard&&window.isSecureContext){
    navigator.clipboard.writeText(css).then(done).catch(fallback);
  } else { fallback(); }
});
const grid=document.getElementById('grid'), empty=document.getElementById('empty');
const count=document.getElementById('count'), q=document.getElementById('q');
const chips=[...document.querySelectorAll('.chip')];
let filter='all';
const FAV_KEY='design-themes-fav';
let favs=new Set();
try{ favs=new Set(JSON.parse(localStorage.getItem(FAV_KEY)||'[]')); }catch(e){}
function paintFavs(){
  document.querySelectorAll('.star').forEach(b=>{
    const on=favs.has(b.dataset.slug);
    b.classList.toggle('on',on);
    b.textContent=on?'★':'☆';
  });
  const fc=document.getElementById('favcount');
  if(fc) fc.textContent=favs.size? '('+favs.size+')' : '';
}
document.addEventListener('click',e=>{
  const s=e.target.closest('.star'); if(!s) return;
  e.preventDefault(); e.stopPropagation();
  const slug=s.dataset.slug;
  favs.has(slug)?favs.delete(slug):favs.add(slug);
  try{ localStorage.setItem(FAV_KEY, JSON.stringify([...favs])); }catch(e){}
  paintFavs(); apply();
});
paintFavs();

function apply(){
  const term=q.value.trim().toLowerCase();
  let shown=0;
  tiles.forEach(t=>{
    const mode=t.dataset.mode, cat=t.dataset.cat, name=t.dataset.name;
    const byMode = (filter==='dark' || filter==='light');
    const okF = filter==='all' ? true
      : filter==='fav' ? favs.has(t.dataset.slug)
      : byMode ? mode===filter : cat===filter;
    const okQ = !term || name.includes(term);
    const show = okF && okQ;
    t.style.display = show ? '' : 'none';
    if(show) shown++;
  });
  count.textContent=shown;
  empty.style.display = shown ? 'none' : 'block';
}
chips.forEach(c=>c.addEventListener('click',()=>{
  chips.forEach(x=>x.setAttribute('aria-pressed','false'));
  c.setAttribute('aria-pressed','true');
  filter=c.dataset.f; apply();
}));
q.addEventListener('input',apply);
addEventListener('resize',()=>tiles.forEach(scale));
addEventListener('load',()=>tiles.forEach(scale));
apply();
"""


def collect_tokens():
    """Read the generated :root block back out of each page so the gallery can
    hand you the exact CSS a theme uses."""
    out = {}
    for t in THEMES:
        with open(os.path.join(OUT, f"{t['slug']}.html"), encoding="utf-8") as f:
            src = f.read()
        m = re.search(r":root\{(.*?)\n\}", src, re.S)
        if m:
            out[t["slug"]] = ":root {" + m.group(1) + "\n}"
    return out


def mini(t):
    """Token-driven thumbnail: same colours/radius/type as the real page, but a
    real DOM mockup instead of a live iframe (reliable, instant, no 89 loads)."""
    bars = [34, 58, 44, 80, 52, 96, 68, 86, 40, 72, 90, 56]
    bh = "".join(f'<b style="height:{h}%"></b>' for h in bars)
    return (
        f'<span class="mini" style="--m-bg:{t["bg"]};--m-surface:{t["surface"]};'
        f'--m-line:{t["line"]};--m-text:{t["text"]};--m-muted:{t["muted"]};'
        f'--m-accent:{t["accent"]};--m-accent2:{t["accent2"]};'
        f'--m-on:{on_color(t["accent"])};--m-r:{t["radius"]}px;'
        f'--m-fh:{split_font(t["fh"])[1]};--m-fb:{split_font(t["fb"])[1]}">'
        f'<span class="m-nav"><b class="m-mark"></b><u></u><u></u><u></u><i></i></span>'
        f'<span class="m-h">Know exactly where your product loses people.</span>'
        f'<span class="m-sub">Visual analytics for product teams.</span>'
        f'<span class="m-cta">Start free trial</span>'
        f'<span class="m-panel"><em><span>Active sessions</span><span>+18.4%</span></em>'
        f'<span class="m-bars">{bh}</span></span>'
        f'</span>'
    )


def build_index(themes, tokens):
    tokens_json = json.dumps(tokens, ensure_ascii=False)
    cards = []
    for t in themes:
        cards.append(f"""
    <article class="tile" data-slug="{t['slug']}" data-mode="{t['mode']}" data-cat="{t['cat']}" data-name="{esc(t['name'].lower())}">
      <a class="shot" href="themes/{t['slug']}.html" aria-label="Open {esc(t['name'])} sample">
        {mini(t)}
        <span class="overlay"><span class="open">Open sample →</span></span>
        <button class="star" data-slug="{t['slug']}" title="Save this theme" aria-label="Save this theme">☆</button>
      </a>
      <div class="meta">
        <div class="swatches">
          <span class="sw" style="background:{t['bg']}"></span>
          <span class="sw" style="background:{t['accent']}"></span>
        </div>
        <div class="txt">
          <h3>{esc(t['name'])}</h3>
          <button class="copy" data-slug="{t['slug']}" title="Copy this theme's :root tokens">⧉ tokens</button>
          <p><span class="pill {t['mode']}">{t['mode']}</span>
             <span class="pill">{esc(t['cat'])}</span>
             <span style="opacity:.7">{esc(t['note'])}</span></p>
        </div>
      </div>
    </article>""")

    brands = sum(1 for t in themes if t["cat"] == "Brand")
    arch = len(themes) - brands
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Frontend Theme Gallery — {len(themes)} themes</title>
<meta name="description" content="A browsable gallery of {len(themes)} frontend web design themes, each rendered as a full sample page.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><rect width='16' height='16' rx='4' fill='%23C6F24E'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{INDEX_CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <div class="kicker"><b>◆</b> {len(themes)} themes · {brands} brand · {arch} archetype · full sample each</div>
  <h1>Pick a look.<br>Steal the <em>tokens</em>.</h1>
  <p class="sub">Each tile is a mockup built from that theme's real tokens. Click through for the
  full sample — nav, hero, features, pricing, footer — then take the colours and type straight into
  your next project, or hit <b style="color:#F4F4F6">⧉ tokens</b> to copy the CSS. Everything is
  generated from one <code style="font-size:13px">themes_data.py</code> file.</p>
  <div class="controls">
    <label class="search">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="Search themes — try “dark”, “serif”, “neon”, “editorial”…" autocomplete="off">
    </label>
    <div class="chips" role="group" aria-label="Filter themes">
      <button class="chip" data-f="all" aria-pressed="true">All</button>
      <button class="chip" data-f="dark" aria-pressed="false">Dark</button>
      <button class="chip" data-f="light" aria-pressed="false">Light</button>
      <button class="chip" data-f="Brand" aria-pressed="false">Brand</button>
      <button class="chip" data-f="Archetype" aria-pressed="false">Archetype</button>
      <button class="chip" data-f="fav" aria-pressed="false">★ Saved <span id="favcount"></span></button>
    </div>
  </div>
</div></header>

<div class="wrap">
  <div class="toolbar"><span><b id="count">{len(themes)}</b> themes shown</span>
    <span>Hover a tile for <b style="color:#F4F4F6">⧉ tokens</b> · click to open the full sample</span></div>

  <div class="note">
    <div><h3>How to use a theme</h3>
      <p>Hover a tile and hit <b>⧉ tokens</b> to copy its full <code>:root</code> block — colours,
      radius, font stacks. Each theme also sets a surface treatment (flat / soft / hard / glow)
      worth copying with the colours.</p></div>
    <div><h3>How to change one</h3>
      <p>Edit <code>themes_data.py</code>, run <code>python build.py</code>, and every page plus this
      index regenerates. Add a theme by appending one <code>T(...)</code> line.</p></div>
  </div>

  <div class="grid" id="grid">{''.join(cards)}
  </div>
  <div class="empty" id="empty"><h2>Nothing matches that</h2><p>Try a broader term, or clear the filter.</p></div>

  <footer><span>Built as a reference library — samples are original layouts, not clones.</span>
    <span><a href="https://github.com/Dynamix14/design-themes">Source on GitHub</a></span></footer>
</div>
<div class="toast" id="toast">Tokens copied</div>
<script>const TOKENS={tokens_json};</script>
<script>{INDEX_JS}</script>
</body>
</html>
"""


# ------------------------------------------------------------------ README
def build_readme(themes):
    rows = "\n".join(
        f"| [{t['name']}](themes/{t['slug']}.html) | {t['mode']} | {t['cat']} | {t['note']} |"
        for t in themes)
    return f"""# Frontend Theme Gallery

{len(themes)} web design themes, each rendered as a complete sample page (nav, hero,
feature cards, metrics, pricing, CTA, footer). Built to be browsed, compared, and
mined for tokens.

**Live gallery:** https://dynamix14.github.io/design-themes/

Gallery features: search, dark/light + brand/archetype filters, `★` save to a local
shortlist (persists in your browser), `⧉ tokens` to copy a theme's `:root` CSS.

## Structure

```
index.html          generated gallery + live previews
themes/<slug>.html  one full sample page per theme
themes_data.py      the only file you edit
build.py            regenerates everything (python build.py)
themes.json         machine-readable token export
```

## Using a theme

Fastest path: hover a tile in the gallery and hit **⧉ tokens** — it copies that
theme's full `:root` block to your clipboard.

Or open a sample and copy its `:root` block from the page source:

- `--bg / --surface / --line` — surfaces
- `--text / --muted` — ink
- `--accent / --accent-2` — brand pair, `--on-accent` is the contrast-safe text colour
- `--r`, `--r-btn` — radii
- `--fh / --fb` — heading / body stacks
- surface treatment: `flat` (hairlines, no shadow), `soft` (border + soft shadow),
  `hard` (2px border + offset shadow), `glow` (dark, accent bloom)

## Adding a theme

Append one line to `themes_data.py`:

```python
T("my-theme", "My Theme", "Archetype", LIGHT,
  ("#FFFFFF", "#F7F7F7", "#E5E5E5", "#111111", "#666666", "#2563EB", "#111111"),
  "Inter|sans", "Inter|sans", 12, "soft", "split", ("grad",),
  "One line about the vibe.")
```

then `python build.py`.

## Theme list

| Theme | Mode | Type | Vibe |
|---|---|---|---|
{rows}

## Notes

Layouts and copy are original; palettes approximate each product's public visual
language for reference purposes. Fonts are Google Fonts substitutes for proprietary
faces. Sample content ("Aperture") is placeholder.
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for t in THEMES:
        with open(os.path.join(OUT, f"{t['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(page(t, THEMES))
    tokens = collect_tokens()
    tokens_json = json.dumps(tokens, ensure_ascii=False)
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index(THEMES, tokens))
    with open(os.path.join(ROOT, "themes.json"), "w", encoding="utf-8") as f:
        json.dump([{k: v for k, v in t.items()} for t in THEMES], f, indent=2)
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write(build_readme(THEMES))
    print(f"built {len(THEMES)} theme pages + index.html")


if __name__ == "__main__":
    main()
