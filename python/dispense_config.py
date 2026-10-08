"""Configurazione della dispensa di Algebra Lineare (formato della collana).

Una sola dispensa: le parti come sul sito, i capitoli con i numeri delle note
(1, 2, 3, 4 con le sezioni 4.1-4.5, 5, 6, appendice A). Il preambolo è quello
comune delle dispense della collana (Laboratorio di Ricerca Operativa,
Modellazione MIP) più le aggiunte di questo corso: i box delle note
(Definition/Observation… blu e rossi, come nelle note e nelle slide) e quello
che serve alle figure e alle macro delle note.
"""
from pathlib import Path

QUI = Path(__file__).resolve().parent
MODULO = QUI.parents[1]
LOGO = MODULO / "materiale_sorgente" / "NOTES_EN" / "FIGURES" / "sapienza.jpeg"


def sorgente(en: bool) -> Path:
    return MODULO / "materiale_sorgente" / ("NOTES_EN" if en else "NOTES_IT") / "1_PRELIMINARIES" / "1_LINEAR_ALGEBRA"


def cartella(en: bool, vol: dict) -> Path:
    # come nel Laboratorio: it/dispensa, en/notes (cartelle private, non pubblicate)
    return MODULO / ("en/notes" if en else "it/dispensa")


def pdf_sito(en: bool, vol: dict) -> Path:
    return MODULO / ("en" if en else "it") / "docs" / "pdf" / (vol["pdf_en"] if en else vol["pdf_it"])


def es(cart: str, nome: str) -> str:
    return f"{cart}/EXSERCISES/EXERCISES_{nome.upper()}/Exercises{nome}.tex"


VOLUMI = [{
    "file": "algebra-lineare",
    "pdf_it": "dispense-algebra-lineare.pdf",
    "pdf_en": "lecture-notes-linear-algebra.pdf",
    "titolo": ("Algebra Lineare", "Linear Algebra"),
    "sottotitolo": ("Vettori, matrici, norme e sistemi lineari", "Vectors, matrices, norms and linear systems"),
    "descrizione": (
        "Dispensa didattica con definizioni, risultati e dimostrazioni, esempi svolti passo per passo "
        "ed esercizi con le soluzioni in fondo a ogni capitolo. Sommatorie e produttorie; vettori e "
        "indipendenza lineare; matrici, determinanti e rango; operazioni elementari ed eliminazione di "
        "Gauss; matrice inversa, fattorizzazione LU, autovalori; norme; sistemi lineari.",
        "Lecture notes with definitions, results and proofs, examples worked out step by step and "
        "exercises with solutions at the end of each chapter. Sums and products; vectors and linear "
        "independence; matrices, determinants and rank; elementary operations and Gaussian elimination; "
        "inverse matrix, LU factorization, eigenvalues; norms; linear systems."),
    "parti": [
        {"titolo": ("Somme e produttorie", "Sums and products"), "capitoli": [
            {"file": "cap01_sommatorie", "id": "somme", "note": "1_SUMS/Sums.tex", "esercizi": [es("1_SUMS", "Sums")]},
            {"file": "cap02_produttorie", "id": "prodotti", "note": "2_PRODUCTS/Products.tex", "esercizi": [es("2_PRODUCTS", "Products")]},
        ]},
        {"titolo": ("Vettori e matrici", "Vectors and matrices"), "capitoli": [
            {"file": "cap03_vettori", "id": "vettori", "note": "3_VECTORS/Vectors.tex", "esercizi": [es("3_VECTORS", "Vectors")]},
            {"file": "cap04_matrici", "id": "matrici", "titolo": ("Matrici", "Matrices"), "sezioni": [
                {"id": "matrici-def", "titolo": ("Definizione e proprietà", "Definition and properties"),
                 "note": "4_MATRICES/1_DEFINITION_AND_PROPERTIES/Matrices.tex",
                 "esercizi": [es("4_MATRICES/1_DEFINITION_AND_PROPERTIES", "Matrices")]},
                {"id": "operazioni", "titolo": ("Operazioni sulle matrici", "Matrix operations"),
                 "note": "4_MATRICES/2_MATRIX_OPERATIONS/Operations.tex",
                 "esercizi": [es("4_MATRICES/2_MATRIX_OPERATIONS", "Operations")]},
                {"id": "inversa", "titolo": ("Inversione di matrici", "Inversion of matrices"),
                 "note": "4_MATRICES/3_MATRIX_INVERSION/Inversion.tex",
                 "esercizi": [es("4_MATRICES/3_MATRIX_INVERSION", "Inversion")]},
                {"id": "lu", "titolo": ("Fattorizzazione di matrici", "Factorization of matrices"),
                 "note": "4_MATRICES/4_FACTORIZATION/Factorization.tex",
                 "esercizi": [es("4_MATRICES/4_FACTORIZATION", "Factorization")]},
                {"id": "autovalori", "titolo": ("Autovalori e autovettori", "Eigenvalues and eigenvectors"),
                 "note": "4_MATRICES/5_EIGENVALUES/Eigenvalues.tex",
                 "esercizi": [es("4_MATRICES/5_EIGENVALUES", "Eigenvalues")]},
            ]},
        ]},
        {"titolo": ("Norme", "Norms"), "capitoli": [
            {"file": "cap05_norme", "id": "norme", "note": "5_NORMS/Norms.tex", "esercizi": [es("5_NORMS", "Norms")]},
        ]},
        {"titolo": ("Sistemi lineari", "Linear systems"), "capitoli": [
            {"file": "cap06_sistemi", "id": "sistemi", "note": "6_SYSTEM_OF_LINEAR_EQUATIONS/SystemOfLinearEquations.tex",
             "esercizi": [es("6_SYSTEM_OF_LINEAR_EQUATIONS", "Systems")]},
        ]},
        {"appendice": True, "capitoli": [
            {"file": "capA_approfondimenti", "id": "approfondimenti", "titolo": ("Approfondimenti", "Further topics"), "sezioni": [
                {"id": "valoreassoluto", "titolo": ("Valore assoluto", "Absolute value"),
                 "note": "100_OTHERS/1_ABSOLUTE_VALUE/AbsoluteValues.tex",
                 "esercizi": ["100_OTHERS/1_ABSOLUTE_VALUE/EXSERCISES/EXERCISES_ABSOLUTE_VALUE/ExercisesAbsoluteValue.tex"]},
                {"id": "modulare", "titolo": ("Aritmetica modulare", "Modular arithmetic"),
                 "note": "100_OTHERS/2_MODULAR_ARITHMETIC/ModularArithmetic.tex",
                 "esercizi": ["100_OTHERS/2_MODULAR_ARITHMETIC/EXSERCISES/EXERCISES_MODULAR_ARITHMETIC/ExercisesModularArithmetic.tex"]},
            ]},
        ]},
    ],
}]

SITO = ("https://fabiofurini.github.io/algebra-lineare/", "https://fabiofurini.github.io/linear-algebra/")
REPO = ("https://github.com/fabiofurini/algebra-lineare", "https://github.com/fabiofurini/linear-algebra")


def preambolo(en: bool, vol: dict) -> str:
    """Il preambolo comune della collana (quello del Laboratorio) con i dati di
    questo corso, più le aggiunte del corso in fondo (come fa MIP)."""
    s = (QUI / ("dispensa_preambolo_en.tex" if en else "dispensa_preambolo_it.tex")).read_text(encoding="utf-8")
    t = vol["titolo"][1 if en else 0]
    sost = [
        ("% Preambolo comune della dispensa del Laboratorio di RO", "% Preambolo comune delle dispense della collana (Laboratorio di RO, Modellazione MIP)"),
        ("\\graphicspath{{./}{../dispensa/}}", "\\graphicspath{{./}{figure/}}"),
        ("\\graphicspath{{./}{../notes/}}", "\\graphicspath{{./}{figure/}}"),
        ("pdftitle={Laboratorio di Ricerca Operativa}", f"pdftitle={{{t}}}"),
        ("pdftitle={Operations Research Lab}", f"pdftitle={{{t}}}"),
        ("pdfsubject={Modelli continui di ottimizzazione}", f"pdfsubject={{{vol['sottotitolo'][0]}}}"),
        ("pdfsubject={Continuous optimization models}", f"pdfsubject={{{vol['sottotitolo'][1]}}}"),
        ("pdfkeywords={ricerca operativa, ottimizzazione, programmazione lineare, Gurobi, Python}",
         "pdfkeywords={algebra lineare, vettori, matrici, determinanti, sistemi lineari, norme}"),
        ("pdfkeywords={operations research, optimization, linear programming, Gurobi, Python}",
         "pdfkeywords={linear algebra, vectors, matrices, determinants, linear systems, norms}"),
        ("\\href{https://github.com/fabiofurini/laboratorio-ricerca-operativa}{\\textbf{Laboratorio di Ricerca Operativa}}",
         f"\\href{{{REPO[0]}}}{{\\textbf{{{t}}}}}"),
        ("\\href{https://github.com/fabiofurini/operations-research-lab}{\\textbf{Operations Research Lab}}",
         f"\\href{{{REPO[1]}}}{{\\textbf{{{t}}}}}"),
    ]
    for a, b in sost:
        s = s.replace(a, b)
    # i link ai dati del laboratorio non servono qui
    s = "\n".join(r for r in s.split("\n") if "RepoDati" not in r and "\\dato}" not in r)
    return s.rstrip() + "\n\n" + AGGIUNTE(en)


def AGGIUNTE(en: bool) -> str:
    nomi = (("Definition", "Theorem", "Corollary", "Proposition", "Observation", "Lemma", "Example")
            if en else ("Definizione", "Teorema", "Corollario", "Proposizione", "Osservazione", "Lemma", "Esempio"))
    return r"""
% ---------- aggiunte del corso di Algebra Lineare ----------
% Le note di algebra lineare usano gli stessi box delle note e delle slide di
% Fabio: definizioni in blu, risultati (osservazioni, proposizioni, teoremi) in
% rosso, numerati per capitolo con un unico contatore. I riquadri verdi delle
% note sono il box verde della collana (gli stessi colori di «modello»).
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{2}
\tcbset{
  defstyle/.style={enhanced, breakable, fonttitle=\bfseries\upshape, fontupper=\slshape,
    colback=blue!5, colframe=blue!55!black, boxrule=0.8pt, arc=1.5mm},
  theostyle/.style={enhanced, breakable, fonttitle=\bfseries\upshape, fontupper=\slshape,
    colback=red!10, colframe=red!75!black, boxrule=0.8pt, arc=1.5mm},
}
\newtcbtheorem[number within=chapter]{Definition}{""" + nomi[0] + r"""}{defstyle}{mytheorem}
\newtcbtheorem[use counter from=Definition]{Theorem}{""" + nomi[1] + r"""}{theostyle}{mytheorem}
\newtcbtheorem[use counter from=Definition]{Corollary}{""" + nomi[2] + r"""}{theostyle}{mytheorem}
\newtcbtheorem[use counter from=Definition]{Proposition}{""" + nomi[3] + r"""}{theostyle}{mytheorem}
\newtcbtheorem[use counter from=Definition]{Observation}{""" + nomi[4] + r"""}{theostyle}{mytheorem}
\newtcbtheorem[use counter from=Definition]{Lemma}{""" + nomi[5] + r"""}{theostyle}{mytheorem}
% esempi numerati per capitolo nel box «esempio» della collana
\newcounter{esempion}[chapter]
\renewcommand{\theesempion}{\thechapter.\arabic{esempion}}
\newenvironment{esempion}[2]{\refstepcounter{esempion}\label{#2}%
  \begin{esempio}[""" + nomi[6] + r""" \theesempion\ifstrempty{#1}{}{: #1}]}{\end{esempio}}
% riquadro verde senza titolo (le regole e i metodi delle note)
\newtcolorbox{riquadro}{enhanced, breakable, colback=green!7!white, colframe=green!55!black,
  boxrule=0.8pt, arc=1.5mm, left=2mm, right=2mm, top=1.5mm, bottom=1.5mm}
% soluzione degli esercizi (come in Modellazione MIP)
\newtcolorbox{soluzione}[1][""" + ("Solution" if en else "Soluzione") + r"""]{%
  enhanced, breakable, colback=teal!6!white, colframe=teal,
  title={#1}, fonttitle=\bfseries, boxrule=0.8pt, arc=1.5mm, left=2mm, right=2mm}

% ---------- quello che serve alle note (dal decla.tex di Fabio) ----------
\usepackage{empheq}
\usepackage{mathrsfs}
\usepackage{colortbl}
\usepackage{subcaption}
\usepackage{adjustbox}
\usepackage{float}
\usepackage{tkz-graph}
\usepackage{forest}
\usepackage{fancybox}
\usepackage{array}
\usetikzlibrary{shapes,arrows,positioning,decorations,automata,backgrounds,petri,bending,
  shapes.multipart,arrows.meta,bbox,calc,angles,quotes,fit,patterns}
\newcolumntype{C}[1]{>{\centering\arraybackslash}m{#1}}
\makeatletter
\newcommand{\tpmod}[1]{{\@displayfalse\pmod{#1}}}
\makeatother
\providecommand{\N}{\mathbb{N}}
\providecommand{\C}{\mathbb{C}}
\providecommand{\F}{\mathbb{F}}
\DeclareMathOperator{\sgn}{sgn}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\Ima}{Im}
\DeclareMathOperator*{\argsup}{arg\,sup}
\DeclareMathOperator*{\arginf}{arg\,inf}
\newcommand{\rr}{\rightarrow}
\newcommand{\mt}{\mapsto}
\newcommand{\ip}{+\infty}
\newcommand{\im}{-\infty}
\DeclareRobustCommand{\brkbinom}{\genfrac[]{0pt}{}}
\definecolor{airforceblue}{rgb}{0.36, 0.54, 0.66}
\definecolor{munsell}{rgb}{0.94, 0.8, 0.0}
\definecolor{viridian}{rgb}{0.25, 0.51, 0.43}
\definecolor{myblue}{rgb}{.8, .8, 1}
\newcommand{\blue}[1]{{\color{blue} #1}}
\newcommand{\red}[1]{{\color{red} #1}}
\newcommand{\green}[1]{{\color{green} #1}}
\newcommand{\yellow}[1]{{\color{yellow} #1}}
\newcommand{\violet}[1]{{\color{violet} #1}}
\newcommand{\orange}[1]{{\color{orange} #1}}
\newcommand\bbb{\cellcolor{blue!40}}
\newcommand\rrr{\cellcolor{red!40}}
\newcommand*\mybluebox[1]{\colorbox{myblue}{\hspace{1em}#1\hspace{1em}}}
"""


def frontespizio(en: bool, vol: dict) -> str:
    i = 1 if en else 0
    sito, repo = SITO[i], REPO[i]
    return r"""% Frontespizio della dispensa (stesso modello del Laboratorio di Ricerca Operativa
% e di Modellazione MIP)
\begin{titlepage}
  \centering
  \vspace*{0.4cm}
  \href{https://www.diag.uniroma1.it/}{%
    \includegraphics[width=0.46\textwidth]{figure/sapienza.jpeg}}\\[1.0cm]
  {\color{blunotte}\rule{\textwidth}{2pt}}\\[1.2cm]
  {\Huge\bfseries\color{blunotte} """ + vol["titolo"][i] + r"""\par}
  \vspace{0.9cm}
  {\Large\color{teal} """ + vol["sottotitolo"][i] + r"""\par}
  \vspace{0.6cm}
  {\color{blunotte}\rule{\textwidth}{2pt}}\\[1.4cm]
  \begin{tcolorbox}[colback=tealchiaro,colframe=teal,width=0.86\textwidth,arc=2mm]
    \small """ + vol["descrizione"][i] + r"""
  \end{tcolorbox}
  \vfill
  {\Large\bfseries \href{https://sites.google.com/view/fabiofurini/home-page}{Fabio Furini}\par}
  \vspace{0.15cm}
  {\footnotesize \href{https://sites.google.com/view/fabiofurini/home-page}%
   {sites.google.com/view/fabiofurini}\par}
  \vspace{0.15cm}
  {\small \href{https://www.diag.uniroma1.it/}{""" + (
        "Department of Computer, Control and Management Engineering} --- Sapienza University of Rome\\par}"
        if en else "Dipartimento di Ingegneria informatica,\n   automatica e gestionale} --- Sapienza Università di Roma\\par}") + r"""
  \vspace{0.45cm}
  {\footnotesize """ + ("Online version and downloadable material:" if en else "Versione online e materiale scaricabile:") + r"""\\
   \href{""" + sito + "}{" + sito.replace("https://", "") + r"""}\\
   \href{""" + repo + "}{" + repo.replace("https://", "") + r"""}\par}
  \vspace{0.4cm}
  {\small """ + ("Academic year 2026--2027" if en else "Anno accademico 2026--2027") + r"""\par}
\end{titlepage}
"""
