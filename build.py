"""Construiește site-ul FEED4FOOD România.

Fiecare pagină are conținutul în _src/<nume>.html. Prima linie din fișier este
un comentariu cu titlul și descrierea paginii, de forma:
    <!-- {"title": "Despre proiect", "desc": "...", "nav": "despre"} -->

Rulează:  python build.py
Rezultatul: fișierele .html din acest folder (cele publicate pe GitHub Pages).
Modifici meniul sau subsolul o singură dată, aici, și se schimbă pe toate paginile.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "_src"
SITE_NAME = "FEED4FOOD România"

NAV = [
    ("index", "index.html", "Acasă"),
    ("despre", "despre.html", "Despre proiect"),
    ("laborator", "laborator-bucuresti.html", "Laboratorul București"),
    ("consortiu", "consortiu.html", "Consorțiu și echipă"),
    ("rezultate", "rezultate.html", "Rezultate"),
    ("noutati", "noutati.html", "Noutăți"),
    ("contact", "contact.html", "Contact"),
]

TEMPLATE = """<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="img/hero.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Sari la conținut</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/logo-alb.png" alt=""><span>FEED4FOOD<small>România · Universitatea din București</small></span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Meniu</button>
    <nav class="nav" id="nav" aria-label="Meniu principal">
{nav}
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4>FEED4FOOD România</h4>
        <p>Comunități vulnerabile care stimulează inovarea și guvernanța sistemelor alimentare durabile în orașele europene.</p>
        <p>Universitatea din București<br>Strada Panduri 90, 050663 București<br><a href="mailto:daniel.diaconu@unibuc.ro">daniel.diaconu@unibuc.ro</a></p>
      </div>
      <div>
        <h4>Pagini</h4>
        <ul>
{footnav}
        </ul>
      </div>
      <div>
        <h4>Urmărește-ne</h4>
        <ul>
          <li><a href="https://www.facebook.com/profile.php?id=61557230353816" rel="noopener">Facebook FEED4FOOD România</a></li>
          <li><a href="https://www.linkedin.com/company/feed4foodromaniaresearch/" rel="noopener">LinkedIn</a></li>
          <li><a href="https://feed4food.eu/" rel="noopener">feed4food.eu (proiectul european)</a></li>
          <li><a href="https://www.facebook.com/feed4foodeu" rel="noopener">Facebook FEED4FOOD EU</a></li>
        </ul>
      </div>
    </div>
    <div class="funding">
      <img src="img/finantare.png" alt="Driving Urban Transitions · Co-funded by the European Union" width="900" height="150">
      <div>
        <p>Proiect finanțat prin PN4, Programul 5.8. Cooperare europeană și internațională, Subprogramul 5.8.1. Orizont Europa (COFUND), contract nr. 50/2024. Autoritate contractantă: Unitatea Executivă pentru Finanțarea Învățământului Superior, a Cercetării, Dezvoltării și Inovării (UEFISCDI).</p>
        <p>FEED4FOOD, Grant Agreement nr. 101069506, este finanțat în cadrul parteneriatului Driving Urban Transitions, cofinanțat de Uniunea Europeană. Opiniile exprimate aparțin exclusiv autorilor și nu reflectă neapărat pe cele ale Uniunii Europene.</p>
      </div>
    </div>
  </div>
</footer>
<script src="assets/site.js" defer></script>
</body>
</html>
"""


def nav_html(active, indent="      "):
    out = []
    for key, href, label in NAV:
        cur = ' aria-current="page"' if key == active else ""
        out.append(f'{indent}<a href="{href}"{cur}>{label}</a>')
    return "\n".join(out)


def build_page(src_file: Path):
    text = src_file.read_text(encoding="utf-8")
    m = re.match(r"\s*<!--\s*(\{.*?\})\s*-->\s*", text, re.S)
    meta = json.loads(m.group(1))
    body = text[m.end():]
    title = meta["title"] if meta.get("nav") == "index" else f'{meta["title"]} · {SITE_NAME}'
    page = TEMPLATE.format(
        title=html.escape(title),
        desc=html.escape(meta.get("desc", "")),
        nav=nav_html(meta.get("nav")),
        footnav="\n".join(f'          <li><a href="{h}">{l}</a></li>' for _, h, l in NAV),
        body=body.rstrip(),
    )
    out = ROOT / (src_file.stem + ".html")
    out.write_text(page, encoding="utf-8", newline="\n")
    print("scris", out.name)


if __name__ == "__main__":
    for f in sorted(SRC.glob("*.html")):
        build_page(f)
