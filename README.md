# Site FEED4FOOD România

Site static (HTML + CSS), publicat pe GitHub Pages.

## Structura

| Ce | Unde |
|---|---|
| Conținutul fiecărei pagini | `_src/*.html` |
| Meniul, subsolul, logo-urile de finanțare | `build.py` (șablonul comun) |
| Design (culori, fonturi, aranjare) | `assets/style.css` |
| Imagini | `img/` (echipa, parteneri, galerie) |
| Paginile finale, publicate | `*.html` din acest folder (generate, nu le edita direct) |

## Cum modifici ceva

1. Editezi fișierul din `_src/` (de exemplu `_src/noutati.html` pentru o știre nouă).
2. Rulezi `python build.py`.
3. Verifici local: `python -m http.server 8765`, apoi deschizi http://localhost:8765
4. Faci commit și push. GitHub Pages actualizează site-ul în 1–2 minute.

## Publicare pe GitHub Pages (o singură dată)

1. Creezi un repository nou pe github.com (de exemplu `feed4food-romania`), public.
2. Din acest folder:
   ```
   git remote add origin https://github.com/<utilizator>/feed4food-romania.git
   git push -u origin main
   ```
3. Pe GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
4. Site-ul apare la `https://<utilizator>.github.io/feed4food-romania/`.
5. Opțional, adresă proprie: în **Settings → Pages → Custom domain** scrii domeniul (de exemplu `feed4food.ro`) și urmezi instrucțiunile DNS.
