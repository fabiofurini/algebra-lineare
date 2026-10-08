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


def parti_del_corso():
    """Le schede delle parti: titolo con i numeri dei capitoli, descrizione e link.
    Vengono dal registro dei capitoli, così home, menu e indice non divergono."""
    from capitoli import CAPITOLI, pagina
    righe = ['<div class="grid cards" markdown>', ""]
    for key, nome, icona, descr, np in PARTI:
        icona_md = ":" + icona.replace("/", "-") + ":"
        caps = [c for c in CAPITOLI if c[0] == key]
        # una parte con un solo capitolo porta direttamente al capitolo
        if len(caps) == 1:
            link, testo = pagina(*caps[0][:3]), ("The chapter" if EN else "Il capitolo")
        else:
            link, testo = f"{key}/index.md", ("The chapters" if EN else "I capitoli")
        righe += [f"-   {icona_md} **{np} · {nome}**", "", "    ---", "", f"    {descr}", "",
                  f"    [:octicons-arrow-right-24: {testo}]({link})", ""]
    righe += ["</div>", ""]
    return "\n".join(righe)


def legenda():
    """Come si leggono le dispense: i box che compaiono davvero nei capitoli,
    con le classi (e quindi i colori) che usa il sito."""
    if EN:
        return """## How each chapter is organized

Each chapter is one of the course notes, with the same numbers and the same
colours as the PDF: on the website and on paper you find everything in the
same place.

<div class="grid" markdown>

!!! definizione "Definition"
    The precise meaning of a new concept.

!!! teorema "Observation, Proposition, Theorem"
    A result to remember, with its hypotheses. In these notes most results are
    **Observations**: they share the theorems' red box and often come with a proof.

!!! esempio "Example"
    A computation worked out in full, one step at a time.

!!! chiave ""
    **In green** the key point to take away: rules, methods, summaries.

</div>

??? dimostrazione "Proof — opens with a click"
    All proofs are there, but folded: first read the statement, then open the
    proof when you want to study it.

!!! interattivo "Try it in the lab"
    In the chapters with computations, the same example can be redone step by
    step in the lab: change the matrix and watch the steps change.
"""
    return """## Come è fatto ogni capitolo

Ogni capitolo è una delle dispense del corso, con gli stessi numeri e gli stessi
colori del PDF: così sul sito e sulla carta si ritrova tutto nello stesso posto.

<div class="grid" markdown>

!!! definizione "Definizione"
    Il significato preciso di un concetto nuovo.

!!! teorema "Osservazione, Proposizione, Teorema"
    Un risultato da ricordare, con le sue ipotesi. In queste dispense la
    maggior parte dei risultati sono **Osservazioni**: hanno lo stesso box rosso
    dei teoremi e spesso la loro dimostrazione.

!!! esempio "Esempio"
    Un calcolo svolto per intero, un passaggio alla volta.

!!! chiave ""
    **In verde** il punto chiave da portarsi via: regole, metodi, riepiloghi.

</div>

??? dimostrazione "Dimostrazione — si apre con un clic"
    Le dimostrazioni sono tutte presenti, ma chiuse: prima si legge
    l'enunciato, poi si apre la dimostrazione quando la si vuole studiare.

!!! interattivo "Provalo nel laboratorio"
    Nei capitoli con i calcoli, lo stesso esempio si rifà passo per passo nel
    laboratorio: cambia la matrice e guarda come cambiano i passaggi.
"""


def home():
    pdf = "pdf/lecture-notes-linear-algebra.pdf" if EN else "pdf/dispense-algebra-lineare.pdf"
    assert (DOCS / pdf).exists(), f"manca {pdf}: niente link a file inesistenti"
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

Teaching material designed and developed by **[Fabio Furini](https://fabiofurini.github.io/)**, associate
professor at [DIAG](https://www.diag.uniroma1.it/), Sapienza University of Rome.

**The course lecture notes, online**: definitions, worked examples, exercises
with full solutions, and a **computation lab** that shows every step —
Gaussian elimination, determinants, inverses, linear systems, LU factorization —
with the same notation as the notes.

[Start with sums :material-arrow-right:](sums-products/index.md){{ .md-button .md-button--primary }}
[Try the lab](lab/index.md){{ .md-button }}
[:material-download: Download all the lecture notes (PDF)]({pdf}){{ .md-button }}

</div>

## Matrices, step by step

Watch how a matrix becomes upper triangular with simple row operations: press
«Next step» and the zeros appear below the diagonal, one step at a time (or ▶
to let it run by itself).

<div class="la-tool" data-tool="demo" data-matrix="2,4,2;4,10,6;2,6,8"></div>

## The parts of the course

{parti_del_corso()}
{legenda()}
## Don't miss

<div class="grid cards" markdown>

-   :material-calculator-variant: **The computation lab**

    ---

    Eleven tools that show the steps, the way you would write them by hand,
    with exercises generated for you.

    [:octicons-arrow-right-24: The tools](lab/index.md)

-   :material-pencil-box-multiple: **Exercises with solutions**

    ---

    One sheet per chapter, with the full solution one click away.

    [:octicons-arrow-right-24: The exercises](exercises/index.md)

-   :material-school: **The course**

    ---

    How to use the site, where these topics come back in the Operations
    Research courses, the full index of the chapters.

    [:octicons-arrow-right-24: Organization](organization.md) · [Full index](index-full.md)

</div>

---

Teaching material by **[Fabio Furini](https://fabiofurini.github.io/)** —
[DIAG](https://www.diag.uniroma1.it/), Sapienza University of Rome. Part of the same
series as the [Operations Research Lab](https://fabiofurini.github.io/operations-research-lab/),
[MIP Modelling](https://fabiofurini.github.io/mip-modelling/) and
[Mathematical Analysis 1](https://fabiofurini.github.io/mathematical-analysis-1/).

*Questo sito è disponibile anche in [italiano](https://fabiofurini.github.io/algebra-lineare/).*
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

Materiale didattico ideato e sviluppato da **[Fabio Furini](https://fabiofurini.github.io/)**, professore
associato al [DIAG](https://www.diag.uniroma1.it/), Sapienza Università di Roma.

**Le dispense del corso, online**: definizioni, esempi svolti, esercizi con le
soluzioni e un **laboratorio di calcolo** che mostra tutti i passaggi —
eliminazione di Gauss, determinanti, inverse, sistemi lineari, fattorizzazione
LU — con la stessa notazione delle dispense.

[Inizia dalle somme :material-arrow-right:](somme/index.md){{ .md-button .md-button--primary }}
[Prova il laboratorio](laboratorio/index.md){{ .md-button }}
[:material-download: Scarica tutte le dispense (PDF)]({pdf}){{ .md-button }}

</div>

## Le matrici, passo dopo passo

Guarda come una matrice diventa triangolare superiore con semplici operazioni
sulle righe: premi «Passo successivo» e gli zeri compaiono sotto la diagonale,
un passo alla volta (oppure ▶ per vederla scorrere da sola).

<div class="la-tool" data-tool="demo" data-matrix="2,4,2;4,10,6;2,6,8"></div>

## Le parti del corso

{parti_del_corso()}
{legenda()}
## Da non perdere

<div class="grid cards" markdown>

-   :material-calculator-variant: **Il laboratorio di calcolo**

    ---

    Undici strumenti che mostrano i passaggi, come li scriveresti a mano, con
    gli esercizi generati per te.

    [:octicons-arrow-right-24: Gli strumenti](laboratorio/index.md)

-   :material-pencil-box-multiple: **Esercizi con le soluzioni**

    ---

    Un foglio per capitolo, con lo svolgimento a un clic di distanza.

    [:octicons-arrow-right-24: Gli esercizi](esercizi/index.md)

-   :material-school: **Il corso**

    ---

    Come usare il sito, dove questi argomenti tornano nei corsi di Ricerca
    Operativa, l'indice completo dei capitoli.

    [:octicons-arrow-right-24: Organizzazione](organizzazione.md) · [Indice completo](indice.md)

</div>

---

Materiale didattico di **[Fabio Furini](https://fabiofurini.github.io/)** —
[DIAG](https://www.diag.uniroma1.it/), Sapienza Università di Roma. Fa parte della
stessa collana del [Laboratorio di Ricerca Operativa](https://fabiofurini.github.io/laboratorio-ricerca-operativa/),
di [Modellazione MIP](https://fabiofurini.github.io/modellazione-mip/) e di
[Analisi Matematica 1](https://fabiofurini.github.io/analisi-matematica-1/).

*This website is also available in [English](https://fabiofurini.github.io/linear-algebra/).*
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

<div class="la-tool" data-tool="{tool}" data-url="1"></div>
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


# slide dei capitoli: file nel sito e titolo (IT, EN); compaiono solo se il PDF esiste
SLIDE = [
    ("slide-01-sommatorie", "slides-01-sums", "1. Sommatorie", "1. Sums"),
    ("slide-02-produttorie", "slides-02-products", "2. Produttorie", "2. Products"),
    ("slide-03-vettori", "slides-03-vectors", "3. Vettori", "3. Vectors"),
    ("slide-04-1-matrici", "slides-04-1-matrices", "4.1 Matrici", "4.1 Matrices"),
    ("slide-04-2-operazioni", "slides-04-2-operations", "4.2 Operazioni sulle matrici", "4.2 Matrix operations"),
    ("slide-04-3-inversa", "slides-04-3-inverse", "4.3 Inversione di matrici", "4.3 Inversion of matrices"),
    ("slide-04-4-fattorizzazione", "slides-04-4-factorization", "4.4 Fattorizzazione di matrici", "4.4 Factorization of matrices"),
    ("slide-04-5-autovalori", "slides-04-5-eigenvalues", "4.5 Autovalori e autovettori", "4.5 Eigenvalues and eigenvectors"),
    ("slide-05-norme", "slides-05-norms", "5. Norme", "5. Norms"),
    ("slide-06-sistemi", "slides-06-systems", "6. Sistemi lineari", "6. Linear systems"),
    ("slide-A1-valore-assoluto", "slides-A1-absolute-value", "A.1 Valore assoluto", "A.1 Absolute value"),
    ("slide-A2-aritmetica-modulare", "slides-A2-modular-arithmetic", "A.2 Aritmetica modulare", "A.2 Modular arithmetic"),
]


def materiale():
    from dispense_config import VOLUMI
    vol = VOLUMI[0]
    pdf = vol["pdf_en"] if EN else vol["pdf_it"]
    assert (DOCS / "pdf" / pdf).exists(), f"manca {pdf}"
    slide = [(f"{(s_en if EN else s_it)}.pdf", t_en if EN else t_it) for s_it, s_en, t_it, t_en in SLIDE
             if (DOCS / "pdf" / f"{s_en if EN else s_it}.pdf").exists()]
    if EN:
        testo = f"""
---
title: Downloads
---

# Downloads

All the course material as PDF, updated at every publication of the site.
Text and figures are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en).

## The lecture notes

<div class="grid cards" markdown>

-   :material-book-open-variant: **{vol['titolo'][1]}** — {vol['sottotitolo'][1]}

    ---

    {vol['descrizione'][1]}

    [:octicons-download-24: {pdf}](pdf/{pdf})

</div>
"""
        if slide:
            testo += "\n## The slides\n\nOne deck per chapter, with the same numbering as the lecture notes.\n\n"
            testo += "\n".join(f"- [:octicons-download-24: {t}](pdf/{f})" for f, t in slide) + "\n"
        scrivi("downloads.md", testo)
    else:
        testo = f"""
---
title: Materiale scaricabile
---

# Materiale scaricabile

Tutto il materiale del corso, in PDF, aggiornato a ogni pubblicazione del sito.
Testi e figure sono sotto licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it).

## La dispensa

<div class="grid cards" markdown>

-   :material-book-open-variant: **{vol['titolo'][0]}** — {vol['sottotitolo'][0]}

    ---

    {vol['descrizione'][0]}

    [:octicons-download-24: {pdf}](pdf/{pdf})

</div>
"""
        if slide:
            testo += "\n## Le slide\n\nUna presentazione per capitolo, con la stessa numerazione della dispensa.\n\n"
            testo += "\n".join(f"- [:octicons-download-24: {t}](pdf/{f})" for f, t in slide) + "\n"
        scrivi("materiale.md", testo)


if __name__ == "__main__":
    home()
    laboratorio()
    organizzazione()
    materiale()
    print(f"[{'en' if EN else 'it'}] home, {len(STRUMENTI)} pagine del laboratorio, organizzazione")
