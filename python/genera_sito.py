"""Genera la struttura del sito dal registro dei capitoli.

Scrive:
  - mkdocs.yml (con la nav completa)
  - docs/<parte>/index.md: la pagina della parte, una card per capitolo
  - docs/indice.md: l'indice completo
I titoli dei capitoli vengono dalle pagine già convertite (front matter).
"""
from __future__ import annotations

import re

from pathlib import Path

from capitoli import CAPITOLI, DOCS, IT, LINGUA, PARTI, REPO, SITO, etichetta, pagina

EN = LINGUA == "en"



def titolo(parte, num, slug):
    p = DOCS / pagina(parte, num, slug)
    if not p.exists():
        return None
    m = re.search(r'^title: "(.*)"$', p.read_text(), re.M)
    return m.group(1) if m else slug


def sommario(parte, num, slug, max_voci=4):
    """Le prime sezioni del capitolo, per la card."""
    p = DOCS / pagina(parte, num, slug)
    sez = re.findall(r"^## \d+\. (.+)$", p.read_text(), re.M)
    sez = [re.sub(r"\$[^$]*\$", "…", s) for s in sez]
    testo = " · ".join(sez[:max_voci])
    return testo + (" · …" if len(sez) > max_voci else "")


def esercizi():
    """Pagina indice degli esercizi e voce di menu."""
    from capitoli import CARTELLA_ES, ESERCIZI, PARTI_ES, ident_es
    righe = ["# " + ("Exercises" if EN else "Esercizi"), "",
             ("Exercise sheets with **worked solutions**, organized as the parts of the notes. "
              "Try each exercise on your own first: the solution opens with a click." if EN else
              "Fogli di esercizi con le **soluzioni svolte**, divisi come le parti delle dispense. "
              "Prova prima da solo: la soluzione si apre con un clic."), "",
             '<div class="grid cards" markdown>', ""]
    voci = ["  - " + ("Exercises" if EN else "Esercizi") + ":", f"      - {CARTELLA_ES}/index.md"]
    for key, (nit, nen, cen) in PARTI_ES.items():
        fogli = [e for e in ESERCIZI if e[0] in (key, cen)]
        fogli = [e for e in fogli if (DOCS / CARTELLA_ES / f"{ident_es(*e[:3])}.md").exists()]
        if not fogli:
            continue
        nome = nen if EN else nit
        voci.append(f"      - {nome}:")
        righe += [f"-   **{nome}**", "", "    ---", ""]
        for e in fogli:
            cid = ident_es(*e[:3])
            testo = (DOCS / CARTELLA_ES / f"{cid}.md").read_text()
            t = re.search(r'^title: "(.*)"$', testo, re.M).group(1)
            n = len(re.findall(r'^!!! esercizio ', testo, re.M))
            lab = etichetta(e[0], e[1])   # lo stesso numero del capitolo
            voci.append(f'          - "{lab}. {t}": {CARTELLA_ES}/{cid}.md')
            righe.append(f"    - **{lab}.** [{t}]({cid}.md) · {n} " + ("exercises" if EN else "esercizi"))
        righe.append("")
    righe += ["</div>", ""]
    if len(voci) == 2:
        return None  # nessun foglio di esercizi (ancora) in questa lingua
    (DOCS / CARTELLA_ES / "index.md").write_text("\n".join(righe))
    return "\n".join(voci)


def versiona(yml: str) -> str:
    """Aggiunge ?v=<impronta del file> a css e js del sito: quando un file cambia
    cambia anche il suo indirizzo, e il browser non usa la copia vecchia."""
    import hashlib
    import re as _re

    def sost(m):
        rel = m.group(2)
        f = DOCS / rel
        if not f.exists():
            return m.group(0)
        v = hashlib.sha1(f.read_bytes()).hexdigest()[:10]
        return f"{m.group(1)}{rel}?v={v}"
    return _re.sub(r"^(  - )((?:javascripts|stylesheets)/[\w.-]+\.(?:js|css))$", sost, yml, flags=_re.M)


def rinvio(key, nome, num, slug):
    """Il vecchio indirizzo della parte (/norme/) rimanda al suo unico capitolo:
    i link già salvati non si rompono. La pagina non è nel menu né nella ricerca."""
    dest = f"{num:02d}-{slug}/"
    testo = (f"This part of the course has a single chapter: you are being taken there." if EN
             else f"Questa parte del corso ha un solo capitolo: ti stiamo portando lì.")
    (DOCS / key / "index.md").write_text(f"""---
title: "{nome}"
search:
  exclude: true
---

<meta http-equiv="refresh" content="0; url={dest}">
<script>location.replace("{dest}" + location.hash);</script>

# {nome}

{testo}

[:octicons-arrow-right-24: {etichetta(key, num)}. {titolo(key, num, slug)}]({num:02d}-{slug}.md){{ .md-button .md-button--primary }}
""")


def main():
    nav_parti = []
    indice = ["# Full index" if EN else "# Indice completo", ""]
    for key, nome, icona, descr, np in PARTI:
        caps = [c for c in CAPITOLI if c[0] == key and titolo(*c[:3])]
        if not caps:
            continue
        if len(caps) == 1:
            # una parte con un solo capitolo (Norme, Sistemi lineari): niente pagina
            # di passaggio, la scheda del menu apre direttamente il capitolo
            parte, num, slug, *_ = caps[0]
            t, rel = titolo(parte, num, slug), pagina(parte, num, slug)
            nav_parti.append(f"  - {nome}: {rel}")
            indice += [f"## [{nome}]({rel})", "", f"- **{etichetta(parte, num)}.** [{t}]({rel})", ""]
            rinvio(key, nome, num, slug)
            continue
        voci = [f"      - {key}/index.md"]
        card = [f"# {nome}", "", (f"*Chapters {np} of the lecture notes.* " if EN else f"*Capitoli {np} delle dispense.* ") + descr, "",
                '<div class="grid cards" markdown>', ""]
        indice.append(f"## [{nome}]({key}/index.md)")
        indice.append("")
        for parte, num, slug, *_ in caps:
            t = titolo(parte, num, slug)
            rel = pagina(parte, num, slug)
            voci.append(f'      - "{etichetta(parte, num)}. {t}": {rel}')
            card += [f"-   **{etichetta(parte, num)}. {t}**", "", "    ---", "",
                     f"    {sommario(parte, num, slug)}", "",
                     f"    [:octicons-arrow-right-24: {'Read the chapter' if EN else 'Leggi il capitolo'}]({num:02d}-{slug}.md)", ""]
            # elenco puntato con il numero scritto: un elenco numerato di Markdown
            # ripartirebbe da 1 in ogni parte (3. Vettori diventerebbe 1.)
            indice.append(f"- **{etichetta(parte, num)}.** [{t}]({rel})")
        card += ["</div>", ""]
        indice.append("")
        (DOCS / key / "index.md").write_text("\n".join(card))
        nav_parti.append(f"  - {nome}:\n" + "\n".join(voci))
    (DOCS / ("index-full.md" if EN else "indice.md")).write_text("\n".join(indice))
    voce_es = esercizi()
    if voce_es:
        nav_parti.append(voce_es)

    yml = (Path(__file__).parent / ("mkdocs_modello_en.yml" if EN else "mkdocs_modello.yml")).read_text()
    yml = yml.replace("  # NAV_PARTI", "\n".join(nav_parti))
    yml = versiona(yml)
    (IT / "mkdocs.yml").write_text(yml)
    (DOCS / "img").mkdir(exist_ok=True)
    print(f"[{LINGUA}] mkdocs.yml, indice e pagine delle parti aggiornati")


if __name__ == "__main__":
    main()
