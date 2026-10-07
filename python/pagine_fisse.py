"""Pagine fisse del sito: home, laboratorio (una per strumento), organizzazione.

Le due lingue si generano dallo stesso file, così non divergono mai.
Uso: python3 python/pagine_fisse.py   e   LINGUA=en python3 python/pagine_fisse.py
"""
from capitoli import CARTELLA_ES, DOCS, EN, PARTI, REPO, SITO

LAB = "lab" if EN else "laboratorio"

# (file, titolo IT, titolo EN, strumento, sottotitolo IT, sottotitolo EN, capitoli)
STRUMENTI = [
    ("gauss", "Metodo di Gauss", "Gaussian elimination", "gauss",
     "Porta una matrice in forma a scala (o ridotta) mostrando ogni operazione elementare.",
     "Bring a matrix to row echelon (or reduced) form showing every elementary operation.", "4.2, 6"),
    ("rango" if not EN else "rank", "Rango", "Rank", "rango",
     "Il rango come numero di pivot della forma a scala.",
     "The rank as the number of pivots of the row echelon form.", "4.1"),
    ("determinante" if not EN else "determinant", "Determinante", "Determinant", "det",
     "Sviluppo di Laplace, regola di Sarrus o eliminazione di Gauss, a scelta.",
     "Laplace expansion, Sarrus rule or Gaussian elimination, your choice.", "4.1, 4.2"),
    ("inversa" if not EN else "inverse", "Matrice inversa", "Inverse matrix", "inversa",
     "Gauss–Jordan su \\((\\boldsymbol A \\mid \\boldsymbol I)\\) oppure la formula con i cofattori.",
     "Gauss–Jordan on \\((\\boldsymbol A \\mid \\boldsymbol I)\\) or the cofactor formula.", "4.3"),
    ("lu", "Fattorizzazione LU", "LU factorization", "lu",
     "I moltiplicatori che riempiono \\(\\boldsymbol L\\), gli scambi che riempiono \\(\\boldsymbol P\\).",
     "The multipliers that fill \\(\\boldsymbol L\\), the swaps that fill \\(\\boldsymbol P\\).", "4.4"),
    ("sistemi" if not EN else "systems", "Sistemi lineari", "Linear systems", "sistema",
     "Gauss e sostituzione all'indietro, Rouché–Capelli, Cramer, oppure la fattorizzazione LU.",
     "Gauss and back substitution, Rouché–Capelli, Cramer, or the LU factorization.", "6"),
    ("autovalori" if not EN else "eigenvalues", "Autovalori e definitezza", "Eigenvalues and definiteness", "autovalori",
     "Polinomio caratteristico, autovettori e criterio di Sylvester.",
     "Characteristic polynomial, eigenvectors and Sylvester's criterion.", "4.5"),
    ("prodotto" if not EN else "product", "Prodotto di matrici", "Matrix product", "prodotto",
     "Riga per colonna, un elemento alla volta.",
     "Row by column, one entry at a time.", "4.1"),
    ("somme" if not EN else "sums", "Somme e produttorie", "Sums and products", "somme",
     "Espande \\(\\sum\\) e \\(\\prod\\) e li confronta con le formule chiuse delle dispense.",
     "Expands \\(\\sum\\) and \\(\\prod\\) and compares them with the closed formulas of the notes.", "1, 2"),
    ("norme" if not EN else "norms", "Norme", "Norms", "norme",
     "Le norme \\(\\ell_1\\), \\(\\ell_2\\), \\(\\ell_\\infty\\) e quella generalizzata da \\(\\boldsymbol Q\\).",
     "The \\(\\ell_1\\), \\(\\ell_2\\), \\(\\ell_\\infty\\) norms and the one generalized by \\(\\boldsymbol Q\\).", "5"),
    ("pivoting", "Perché serve il pivoting", "Why partial pivoting", "pivoting",
     "Lo stesso sistema con e senza pivoting parziale, in virgola mobile.",
     "The same system with and without partial pivoting, in floating point.", "4.2"),
]


def scrivi(rel, testo):
    p = DOCS / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(testo.lstrip() + "\n", encoding="utf-8")


def home():
    if EN:
        testo = f"""
---
title: Linear Algebra
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Linear Algebra

Teaching material designed and developed by **[Fabio Furini](https://sites.google.com/view/fabiofurini/home-page)**, associate
professor at [DIAG](https://www.diag.uniroma1.it/), Sapienza University of Rome.

**The course lecture notes, online**: definitions, worked examples, exercises
with full solutions, and a **computation lab** that shows every step —
Gaussian elimination, determinants, inverses, linear systems, LU factorization —
with the same notation as the notes.

[Start with sums :material-arrow-right:](sums-products/index.md){{ .md-button .md-button--primary }}
[Try the lab](lab/index.md){{ .md-button }}

</div>

## Try it right now

Type a matrix and watch every row operation, in exact fractions.

<div class="la-tool" data-tool="gauss" data-matrix="0,2,1;1,-1,0;2,1,3"></div>

## What you will find here

<div class="grid cards" markdown>

-   **The lecture notes**

    ---

    Every chapter of the course, with the same boxes and the same numbers as
    the PDF: definitions, observations, proofs you can unfold, worked examples.

-   **The computation lab**

    ---

    Eleven tools that do not only give the answer: they show the steps, the way
    you would write them by hand.

-   **Exercises with solutions**

    ---

    One sheet per chapter, with the full solution one click away, plus endless
    generated exercises in the lab's *Practice* tab.

-   **It is a propaedeutic course**

    ---

    Everything here is used in the [Operations Research Lab](https://fabiofurini.github.io/operations-research-lab/)
    and in [MIP Modelling](https://fabiofurini.github.io/mip-modelling/).

</div>
"""
    else:
        testo = f"""
---
title: Algebra Lineare
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Algebra Lineare

Materiale didattico ideato e sviluppato da **[Fabio Furini](https://sites.google.com/view/fabiofurini/home-page)**, professore
associato al [DIAG](https://www.diag.uniroma1.it/), Sapienza Università di Roma.

**Le dispense del corso, online**: definizioni, esempi svolti, esercizi con le
soluzioni e un **laboratorio di calcolo** che mostra tutti i passaggi —
eliminazione di Gauss, determinanti, inverse, sistemi lineari, fattorizzazione
LU — con la stessa notazione delle dispense.

[Inizia dalle somme :material-arrow-right:](somme/index.md){{ .md-button .md-button--primary }}
[Prova il laboratorio](laboratorio/index.md){{ .md-button }}

</div>

## Provalo subito

Scrivi una matrice e guarda ogni operazione di riga, in frazioni esatte.

<div class="la-tool" data-tool="gauss" data-matrix="0,2,1;1,-1,0;2,1,3"></div>

## Che cosa trovi qui

<div class="grid cards" markdown>

-   **Le dispense**

    ---

    Tutti i capitoli del corso, con gli stessi box e gli stessi numeri del PDF:
    definizioni, osservazioni, dimostrazioni che si aprono con un clic, esempi
    svolti.

-   **Il laboratorio di calcolo**

    ---

    Undici strumenti che non danno solo il risultato: mostrano i passaggi, come
    li scriveresti a mano.

-   **Esercizi con le soluzioni**

    ---

    Un foglio per capitolo, con lo svolgimento a un clic di distanza, più gli
    esercizi generati all'infinito nella scheda *Esercitati* del laboratorio.

-   **È un corso propedeutico**

    ---

    Tutto quello che c'è qui serve nel [Laboratorio di Ricerca Operativa](https://fabiofurini.github.io/laboratorio-ricerca-operativa/)
    e in [Modellazione MIP](https://fabiofurini.github.io/modellazione-mip/).

</div>
"""
    scrivi("index.md", testo)


def laboratorio():
    titolo = "The computation lab" if EN else "Il laboratorio di calcolo"
    intro = ("""Here you do not only get the answer: you see **every step**, written the way
you would write it by hand, with the notation of the lecture notes
(\\(R_2 \\leftarrow R_2 - 2R_1\\)). The arithmetic is **exact**: fractions, never
rounded decimals.

Each tool has three tabs: **Compute** (the full solution), **Practice**
(exercises generated for you, with a check), and — for Gaussian elimination —
**Do it yourself**, where you choose each row operation and the lab checks it.

Everything runs in your browser: nothing to install, no account, and it works on
a phone.""" if EN else """Qui non trovi solo il risultato: vedi **tutti i passaggi**, scritti come li
scriveresti a mano, con la notazione delle dispense
(\\(R_2 \\leftarrow R_2 - 2R_1\\)). I conti sono **esatti**: frazioni, mai decimali
arrotondati.

Ogni strumento ha tre schede: **Calcola** (lo svolgimento completo),
**Esercitati** (esercizi generati per te, con la correzione) e — per il metodo
di Gauss — **Fallo tu**, dove scegli tu ogni operazione di riga e il laboratorio
la controlla.

Tutto gira nel browser: niente da installare, nessun account, e funziona anche
dal telefono.""")
    card = []
    for rel, tit_it, tit_en, tool, sub_it, sub_en, caps in STRUMENTI:
        card += [f"-   **{tit_en if EN else tit_it}**", "", "    ---", "",
                 f"    {sub_en if EN else sub_it}", "",
                 f"    [:octicons-arrow-right-24: {'Open the tool' if EN else 'Apri lo strumento'}]({rel}.md)", ""]
    scrivi(f"{LAB}/index.md", f"""
---
title: {"Lab" if EN else "Laboratorio"}
---

# {titolo}

{intro}

<div class="grid cards" markdown>

{chr(10).join(card)}
</div>
""")
    for rel, tit_it, tit_en, tool, sub_it, sub_en, caps in STRUMENTI:
        tit = tit_en if EN else tit_it
        sub = sub_en if EN else sub_it
        rif = (f"From the lecture notes, chapter {caps}." if EN else f"Dalle dispense, capitolo {caps}.")
        scrivi(f"{LAB}/{rel}.md", f"""
---
title: "{tit}"
---

# {tit}

{sub} *{rif}*

<div class="la-tool" data-tool="{tool}"></div>
""")


def organizzazione():
    if EN:
        testo = f"""
---
title: The course
---

# The course

This is the **preliminary** material on linear algebra for the Operations
Research courses: the notation, the computations and the results that the other
modules take for granted.

## How to use this site

1. Read the chapter: definitions and observations are in coloured boxes, exactly
   as in the PDF; proofs and solutions open with a click.
2. Try the examples in the [lab](lab/index.md): every tool has a button that
   loads the matrices used in the notes.
3. Do the exercises at the end of each chapter, then switch to the lab's
   *Practice* tab for as many new ones as you like.

## Where you will use it

| Topic | Where it comes back |
|---|---|
| Linear systems, rank, bases | the simplex method — [Operations Research Lab](https://fabiofurini.github.io/operations-research-lab/) |
| Definite matrices, generalized \\(\\ell_2\\) norm | quadratic models, Markowitz portfolios |
| \\(\\ell_1\\) and \\(\\ell_\\infty\\) norms | robust and quantile regression |
| Determinants, LU | solving systems efficiently inside a solver |

## Material

The lecture notes are by **Fabio Furini**. Text, figures and data are released
under [CC BY 4.0]({REPO}/blob/main/LICENSE); the code of the lab under
[MIT]({REPO}/blob/main/LICENSE-CODE). To cite the material see
[`CITATION.cff`]({REPO}/blob/main/CITATION.cff).

## Of the same series

- [Operations Research Lab](https://fabiofurini.github.io/operations-research-lab/)
- [MIP Modelling](https://fabiofurini.github.io/mip-modelling/)
- [Mathematical Analysis 1](https://fabiofurini.github.io/mathematical-analysis-1/)
"""
        scrivi("organization.md", testo)
    else:
        testo = f"""
---
title: Il corso
---

# Il corso

Questo è il materiale **preliminare** di algebra lineare per i corsi di Ricerca
Operativa: la notazione, i calcoli e i risultati che gli altri moduli danno per
noti.

## Come si usa il sito

1. Leggi il capitolo: definizioni e osservazioni sono nei box colorati, come nel
   PDF; dimostrazioni e soluzioni si aprono con un clic.
2. Rifai gli esempi nel [laboratorio](laboratorio/index.md): ogni strumento ha un
   pulsante che carica le matrici usate nelle dispense.
3. Fai gli esercizi in fondo a ogni capitolo, poi passa alla scheda *Esercitati*
   del laboratorio per averne quanti ne vuoi.

## Dove lo ritroverai

| Argomento | Dove torna |
|---|---|
| Sistemi lineari, rango, basi | il metodo del simplesso — [Laboratorio di Ricerca Operativa](https://fabiofurini.github.io/laboratorio-ricerca-operativa/) |
| Matrici definite, norma \\(\\ell_2\\) generalizzata | modelli quadratici, portafogli di Markowitz |
| Norme \\(\\ell_1\\) e \\(\\ell_\\infty\\) | regressione robusta e quantile |
| Determinanti, LU | risolvere sistemi in modo efficiente dentro un solver |

## Il materiale

Le dispense sono di **Fabio Furini**. Testi, figure e dati hanno licenza
[CC BY 4.0]({REPO}/blob/main/LICENSE); il codice del laboratorio licenza
[MIT]({REPO}/blob/main/LICENSE-CODE). Per citare il materiale c'è
[`CITATION.cff`]({REPO}/blob/main/CITATION.cff).

## Della stessa collana

- [Laboratorio di Ricerca Operativa](https://fabiofurini.github.io/laboratorio-ricerca-operativa/)
- [Modellazione MIP](https://fabiofurini.github.io/modellazione-mip/)
- [Analisi Matematica 1](https://fabiofurini.github.io/analisi-matematica-1/)
"""
        scrivi("organizzazione.md", testo)


if __name__ == "__main__":
    home()
    laboratorio()
    organizzazione()
    print(f"[{'en' if EN else 'it'}] home, {len(STRUMENTI)} pagine del laboratorio, organizzazione")
