"""Compila le slide dei capitoli (beamer) e le copia fra i PDF del sito.

Le slide sono nelle cartelle SLIDES/ delle note (materiale_sorgente/NOTES_IT e
NOTES_EN). Si compila su una copia dell'albero delle note in build/ (né le note
né la copia ricevono file ausiliari); sul sito va solo il PDF.

Uso: python3 python/compila_slide.py      (LINGUA=en per l'inglese)
"""
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from capitoli import DOCS, EN, IT, NOTE
from pagine_fisse import SLIDE

# presentazione di ogni capitolo, nello stesso ordine di SLIDE
DECK = [
    "1_SUMS/SLIDES/Sums_Slides.tex",
    "2_PRODUCTS/SLIDES/Products_Slides.tex",
    "3_VECTORS/SLIDES/Vectors_Slides.tex",
    "4_MATRICES/1_DEFINITION_AND_PROPERTIES/SLIDES/Matrices_Slides.tex",
    "4_MATRICES/2_MATRIX_OPERATIONS/SLIDES/Operations_Slides.tex",
    "4_MATRICES/3_MATRIX_INVERSION/SLIDES/Inversion_Slides.tex",
    "4_MATRICES/4_FACTORIZATION/SLIDES/Factorization_Slides.tex",
    "4_MATRICES/5_EIGENVALUES/SLIDES/Eigenvalues_Slides.tex",
    "5_NORMS/SLIDES/Norms_Slides.tex",
    "6_SYSTEM_OF_LINEAR_EQUATIONS/SLIDES/SystemOfLinearEquations_Slides.tex",
    "100_OTHERS/1_ABSOLUTE_VALUE/SLIDES/AbsoluteValues_Slides.tex",
    "100_OTHERS/2_MODULAR_ARITHMETIC/SLIDES/ModularArithmetic_Slides.tex",
]
assert len(DECK) == len(SLIDE)

ALBERO = IT / "build" / "slides_tree"
BASE = ALBERO / "1_PRELIMINARIES" / "1_LINEAR_ALGEBRA"


def compila(i):
    rel = DECK[i]
    nome = (SLIDE[i][1] if EN else SLIDE[i][0]) + ".pdf"
    tex = BASE / rel
    if not tex.exists():
        return f"manca {rel}"
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", tex.name], cwd=tex.parent,
                       capture_output=True, timeout=900)
    log = tex.with_suffix(".log").read_text(errors="replace")
    errori = log.count("\n! ")
    pdf = tex.with_suffix(".pdf")
    if not pdf.exists():
        return f"ERRORE {rel}: nessun PDF"
    shutil.copy(pdf, DOCS / "pdf" / nome)
    pagine = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    pagine = next((l.split()[-1] for l in pagine.splitlines() if l.startswith("Pages")), "?")
    return f"{'ok' if not errori else 'ERRORI ' + str(errori)}  {nome}  ({pagine} slide)"


if __name__ == "__main__":
    if ALBERO.exists():
        shutil.rmtree(ALBERO)
    shutil.copytree(NOTE, ALBERO, ignore=shutil.ignore_patterns("*.aux", "*.log", "*.nav", "*.snm", "*.toc", "*.out", "*.vrb", "*.pdf"))
    (DOCS / "pdf").mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(6) as ex:
        esiti = list(ex.map(compila, range(len(DECK))))
    for e in esiti:
        print(e)
    sys.exit(1 if any(e.startswith("ERRORE") for e in esiti) else 0)
