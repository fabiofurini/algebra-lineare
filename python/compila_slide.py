"""Compila le slide dei capitoli (beamer) e le copia fra i PDF del sito.

Le slide stanno in slides/ del repository della lingua (it/slides, en/slides),
come in MIP e nel Laboratorio: una cartella per capitolo, slides/<nome>/ con
<nome>.tex e il suo PDF (nome come il PDF del sito: slide-03-vettori,
slides-03-vectors); in slides/ ci sono anche decla_slide.tex e FIGURES/.
La cartella non va su GitHub; sul sito va solo il PDF, in docs/pdf/.

Uso: python3 python/compila_slide.py      (LINGUA=en per l'inglese)
"""
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from capitoli import DOCS, EN, IT
from pagine_fisse import SLIDE

SLIDES = IT / "slides"


def compila(nomi):
    nome = nomi[1] if EN else nomi[0]
    tex = SLIDES / nome / f"{nome}.tex"
    if not tex.exists():
        return f"ERRORE manca {nome}/{nome}.tex"
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", tex.name], cwd=tex.parent,
                       capture_output=True, timeout=900)
    log = tex.with_suffix(".log").read_text(errors="replace")
    errori = log.count("\n! ")
    pdf = tex.with_suffix(".pdf")
    if not pdf.exists():
        return f"ERRORE {nome}: nessun PDF"
    shutil.copy(pdf, DOCS / "pdf" / pdf.name)
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    pagine = next((l.split()[-1] for l in info.splitlines() if l.startswith("Pages")), "?")
    return f"{'ok' if not errori else 'ERRORI ' + str(errori)}  {pdf.name}  ({pagine} slide)"


if __name__ == "__main__":
    (DOCS / "pdf").mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(6) as ex:
        esiti = list(ex.map(compila, SLIDE))
    for e in esiti:
        print(e)
    sys.exit(1 if any(not e.startswith("ok") for e in esiti) else 0)
