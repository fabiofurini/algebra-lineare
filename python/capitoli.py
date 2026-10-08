"""Registro dei capitoli: da dove viene ogni pagina del sito.

Ogni capitolo è una dispensa di `materiale_sorgente/NOTES_IT` (italiano) o
`NOTES_EN` (inglese): copie delle note originali, che restano intatte in
`01_TOPICS/1_PRELIMINARIES/1_LINEAR_ALGEBRA/`.

Lingua: LINGUA=en python3 python/... produce il sito inglese in ../en/
"""
import os
from pathlib import Path

LINGUA = os.environ.get("LINGUA", "it")
EN = LINGUA == "en"
MODULO = Path(__file__).resolve().parents[2]
NOTE = MODULO / "materiale_sorgente" / ("NOTES_EN" if EN else "NOTES_IT")
SORGENTE = NOTE / "1_PRELIMINARIES" / "1_LINEAR_ALGEBRA"
SORGENTE_ES = SORGENTE
IT = MODULO / LINGUA          # radice del repository della lingua (it/ o en/)
DOCS = IT / "docs"

REPO = "https://github.com/fabiofurini/" + ("linear-algebra" if EN else "algebra-lineare")
SITO = "https://fabiofurini.github.io/" + ("linear-algebra/" if EN else "algebra-lineare/")

# (cartella del sito, titolo della parte, icona, descrizione breve, capitoli delle note)
PARTI = [
    ("somme", "Somme e produttorie", "material/sigma",
     "Il simbolo di sommatoria e di produttoria, le loro proprietà, le somme notevoli, il fattoriale.", "1–2"),
    ("vettori-matrici", "Vettori e matrici", "material/matrix",
     "Vettori e indipendenza lineare, matrici, determinanti e rango; operazioni elementari ed eliminazione di Gauss, matrice inversa, fattorizzazione LU, autovalori e criterio di Sylvester.", "3–4"),
    ("norme", "Norme", "material/vector-line",
     "Le norme ℓ₁, ℓ₂, ℓ∞ e ℓ₂ generalizzata, la disuguaglianza di Cauchy–Schwarz e la disuguaglianza triangolare.", "5"),
    ("sistemi", "Sistemi lineari", "material/equal-box",
     "Esistenza e unicità delle soluzioni, teorema di Rouché–Capelli, eliminazione di Gauss, sistemi omogenei, metodo LU, regola di Cramer.", "6"),
    ("approfondimenti", "Approfondimenti", "material/plus-circle-outline",
     "Valore assoluto e aritmetica modulare.", "A"),
]

# (parte, numero, slug, file sorgente relativo a SORGENTE, numero del capitolo nelle note)
CAPITOLI = [
    ("somme", 1, "sommatorie", "1_SUMS/Sums.tex", "1"),
    ("somme", 2, "produttorie", "2_PRODUCTS/Products.tex", "2"),
    ("vettori-matrici", 1, "vettori", "3_VECTORS/Vectors.tex", "3"),
    ("vettori-matrici", 2, "matrici", "4_MATRICES/1_DEFINITION_AND_PROPERTIES/Matrices.tex", "4.1"),
    ("vettori-matrici", 3, "operazioni-elementari", "4_MATRICES/2_MATRIX_OPERATIONS/Operations.tex", "4.2"),
    ("vettori-matrici", 4, "matrice-inversa", "4_MATRICES/3_MATRIX_INVERSION/Inversion.tex", "4.3"),
    ("vettori-matrici", 5, "fattorizzazione-lu", "4_MATRICES/4_FACTORIZATION/Factorization.tex", "4.4"),
    ("vettori-matrici", 6, "autovalori", "4_MATRICES/5_EIGENVALUES/Eigenvalues.tex", "4.5"),
    ("norme", 1, "norme", "5_NORMS/Norms.tex", "5"),
    ("sistemi", 1, "sistemi-lineari", "6_SYSTEM_OF_LINEAR_EQUATIONS/SystemOfLinearEquations.tex", "6"),
    ("approfondimenti", 1, "valore-assoluto", "100_OTHERS/1_ABSOLUTE_VALUE/AbsoluteValues.tex", "A.1"),
    ("approfondimenti", 2, "aritmetica-modulare", "100_OTHERS/2_MODULAR_ARITHMETIC/ModularArithmetic.tex", "A.2"),
]

PARTI_EN = {
    "somme": ("sums-products", "Sums and products",
              "Summation and product notation, their properties, closed-form sums, the factorial."),
    "vettori-matrici": ("vectors-matrices", "Vectors and matrices",
                        "Vectors and linear independence, matrices, determinants and rank; elementary operations and Gaussian elimination, inverse matrix, LU factorization, eigenvalues and Sylvester's criterion."),
    "norme": ("norms", "Norms",
              "The ℓ₁, ℓ₂, ℓ∞ and generalized ℓ₂ norms, the Cauchy–Schwarz inequality and the triangle inequality."),
    "sistemi": ("systems", "Linear systems",
                "Existence and uniqueness of solutions, the Rouché–Capelli theorem, Gaussian elimination, homogeneous systems, the LU method, Cramer's rule."),
    "approfondimenti": ("extras", "Further topics", "Absolute value and modular arithmetic."),
}
SLUG_EN = {
    "sommatorie": "sums", "produttorie": "products", "vettori": "vectors", "matrici": "matrices",
    "operazioni-elementari": "elementary-operations", "matrice-inversa": "inverse-matrix",
    "fattorizzazione-lu": "lu-factorization", "autovalori": "eigenvalues", "norme": "norms",
    "sistemi-lineari": "linear-systems", "valore-assoluto": "absolute-value", "aritmetica-modulare": "modular-arithmetic",
}
CAPITOLI_IT = list(CAPITOLI)
_PARTI_IT = list(PARTI)
if EN:
    PARTI = [(PARTI_EN[k][0], PARTI_EN[k][1], icona, PARTI_EN[k][2], np) for k, _, icona, _, np in PARTI]
    _cartella = {k: v[0] for k, v in PARTI_EN.items()}
    CAPITOLI = [(_cartella[p], n, SLUG_EN[s], rel, lab) for p, n, s, rel, lab in CAPITOLI]


def ident(parte, num, slug, *_):
    """Identificativo stabile del capitolo (nomi delle figure, dei PDF)."""
    return f"{parte}-{num:02d}-{slug}"


def ident_it(cid):
    """Identificativo italiano corrispondente (per le tabelle condivise fra le lingue)."""
    for c, ci in zip(CAPITOLI, CAPITOLI_IT):
        if ident(*c[:3]) == cid:
            return ident(*ci[:3])
    return cid


def pagina(parte, num, slug, *_):
    """Percorso della pagina Markdown relativo a docs/."""
    return f"{parte}/{num:02d}-{slug}.md"


def etichetta(parte, num):
    """Numero del capitolo nelle note (1, 4.2, A.1…)."""
    for c in CAPITOLI:
        if c[0] == parte and c[1] == num:
            return c[4]
    return str(num)


# ---------------------------------------------------------------- esercizi
CARTELLA_ES = "exercises" if EN else "esercizi"   # cartella del sito

# un foglio per capitolo: (parte, numero, slug, file relativo a SORGENTE_ES)
ESERCIZI = [
    ("somme", 1, "sommatorie", "1_SUMS/EXSERCISES/EXERCISES_SUMS/ExercisesSums.tex"),
    ("somme", 2, "produttorie", "2_PRODUCTS/EXSERCISES/EXERCISES_PRODUCTS/ExercisesProducts.tex"),
    ("vettori-matrici", 1, "vettori", "3_VECTORS/EXSERCISES/EXERCISES_VECTORS/ExercisesVectors.tex"),
    ("vettori-matrici", 2, "matrici", "4_MATRICES/1_DEFINITION_AND_PROPERTIES/EXSERCISES/EXERCISES_MATRICES/ExercisesMatrices.tex"),
    ("vettori-matrici", 3, "operazioni-elementari", "4_MATRICES/2_MATRIX_OPERATIONS/EXSERCISES/EXERCISES_OPERATIONS/ExercisesOperations.tex"),
    ("vettori-matrici", 4, "matrice-inversa", "4_MATRICES/3_MATRIX_INVERSION/EXSERCISES/EXERCISES_INVERSION/ExercisesInversion.tex"),
    ("vettori-matrici", 5, "fattorizzazione-lu", "4_MATRICES/4_FACTORIZATION/EXSERCISES/EXERCISES_FACTORIZATION/ExercisesFactorization.tex"),
    ("vettori-matrici", 6, "autovalori", "4_MATRICES/5_EIGENVALUES/EXSERCISES/EXERCISES_EIGENVALUES/ExercisesEigenvalues.tex"),
    ("norme", 1, "norme", "5_NORMS/EXSERCISES/EXERCISES_NORMS/ExercisesNorms.tex"),
    ("sistemi", 1, "sistemi-lineari", "6_SYSTEM_OF_LINEAR_EQUATIONS/EXSERCISES/EXERCISES_SYSTEMS/ExercisesSystems.tex"),
    ("approfondimenti", 1, "valore-assoluto", "100_OTHERS/1_ABSOLUTE_VALUE/EXSERCISES/EXERCISES_ABSOLUTE_VALUE/ExercisesAbsoluteValue.tex"),
    ("approfondimenti", 2, "aritmetica-modulare", "100_OTHERS/2_MODULAR_ARITHMETIC/EXSERCISES/EXERCISES_MODULAR_ARITHMETIC/ExercisesModularArithmetic.tex"),
]
PARTI_ES = {p[0]: (p[1], PARTI_EN[p[0]][1], PARTI_EN[p[0]][0]) for p in _PARTI_IT}
ESERCIZI_IT = list(ESERCIZI)
if EN:
    ESERCIZI = [(PARTI_ES[p][2], n, SLUG_EN[s], rel) for p, n, s, rel in ESERCIZI]


def ident_es(parte, num, slug, *_):
    return f"es-{parte}-{num:02d}-{slug}"


def ident_es_it(cid):
    for c, ci in zip(ESERCIZI, ESERCIZI_IT):
        if ident_es(*c[:3]) == cid:
            return ident_es(*ci[:3])
    return cid
