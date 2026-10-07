"""Ricompila i PDF dei capitoli dalla copia corretta delle note.

La copia `materiale_sorgente/DISPENSE/` viene duplicata in build/tex/ e lì si
compila (due passate di pdflatex); i PDF finiscono in docs/pdf/<id>.pdf.
Né le note originali né la copia ricevono file ausiliari.

Uso: python3 python/compila_pdf.py [prefisso]
"""
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from capitoli import CAPITOLI, DOCS, ESERCIZI, IT, LINGUA, NOTE, SORGENTE, ident, ident_es

# si compila su una copia dell'intero albero delle note (serve anche decla.tex)
RADICE = IT / "build" / "tex"
BUILD = RADICE / SORGENTE.relative_to(NOTE)
BUILD_ES = BUILD


def compila(cap, esercizi=False):
    cid = ident_es(*cap[:3]) if esercizi else ident(*cap[:3])
    tex = (BUILD_ES if esercizi else BUILD) / cap[3]
    if not tex.exists():
        return f"manca {cid}"
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", tex.name], cwd=tex.parent,
                       capture_output=True, timeout=600)
    pdf = tex.with_suffix(".pdf")
    if not pdf.exists():
        return f"ERRORE {cid}"
    shutil.copy(pdf, DOCS / "pdf" / f"{cid}.pdf")
    return f"ok {cid}"


if __name__ == "__main__":
    filtri = sys.argv[1:] or [""]
    if RADICE.exists():
        shutil.rmtree(RADICE)
    shutil.copytree(NOTE, RADICE, ignore=shutil.ignore_patterns("*.pdf", "*.aux", "*.log", "SLIDES"))
    (DOCS / "pdf").mkdir(parents=True, exist_ok=True)
    caps = [c for c in CAPITOLI if any(ident(*c[:3]).startswith(f) for f in filtri)]
    es = [c for c in ESERCIZI if any(ident_es(*c[:3]).startswith(f) for f in filtri)]
    with ThreadPoolExecutor(6) as ex:
        ris = list(ex.map(compila, caps)) + list(ex.map(lambda c: compila(c, True), es))
    for r in ris:
        if not r.startswith("ok"):
            print(r)
    print(f"{len(caps)} capitoli e {len(es)} fogli di esercizi compilati")
    caps = [c for c in caps if (DOCS / "pdf" / f"{ident(*c[:3])}.pdf").exists()]
    if caps:
        # il PDF unico di tutte le dispense, nell'ordine dei capitoli
        unico = DOCS / "pdf" / ("dispense-algebra-lineare.pdf" if LINGUA == "it" else "lecture-notes-linear-algebra.pdf")
        subprocess.run(["pdfunite", *[str(DOCS / "pdf" / f"{ident(*c[:3])}.pdf") for c in CAPITOLI], str(unico)], check=True)
        print("PDF unico:", unico.name)
