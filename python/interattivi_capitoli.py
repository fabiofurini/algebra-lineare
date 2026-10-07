"""Dove va, nei capitoli, il richiamo al laboratorio di calcolo.

Per ogni capitolo (identificativo italiano) una lista di inserti:
(numero della sezione, strumento, matrice iniziale o None, attributi in più).
Il blocco va alla FINE della sezione indicata: prima la teoria e gli esempi
delle dispense, poi lo stesso calcolo rifatto passo per passo nel laboratorio.
Le matrici sono quelle degli esempi del capitolo.
"""

# cid -> [(numero di sezione, strumento, matrice, extra)]
INSERTI = {
    "somme-01-sommatorie": [(3, "somme", None, {"f": "k^2", "tipo": "sum"})],
    "somme-02-produttorie": [(3, "produttorie", None, {"f": "k", "tipo": "prod"})],
    "vettori-matrici-02-matrici": [
        (3, "prodotto", "1,2,0;-1,3,1", {"b": "2,1;0,-1;4,3"}),
        (5, "det", "1,2,0;3,1,4;2,-1,1", {}),
        (6, "rango", "1,2,3;2,4,6", {}),
    ],
    "vettori-matrici-03-operazioni-elementari": [
        (3, "gauss", "0,2,1;1,-1,0;2,1,3", {}),
        (4, "pivoting", None, {}),
    ],
    "vettori-matrici-04-matrice-inversa": [(2, "inversa", "2,1;1,1", {})],
    "vettori-matrici-05-fattorizzazione-lu": [(1, "lu", "2,1,1;4,3,3;8,7,9", {})],
    "vettori-matrici-06-autovalori": [(4, "autovalori", "2,-1;-1,2", {})],
    "norme-01-norme": [(6, "norme", None, {"x": "3,-4,12"})],
    "sistemi-01-sistemi-lineari": [
        (3, "sistema", "1,1,1;2,-1,1;1,2,-1", {"b": "6,3,2"}),
        (6, "sistema", "-1,1;8,2", {"b": "2,19"}),
    ],
}

TESTO = {
    "it": ("Provalo nel laboratorio", "lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi."),
    "en": ("Try it in the lab", "the same computation step by step: change the matrix and watch the steps change."),
}
# gli strumenti hanno nomi diversi nelle due lingue solo nelle pagine, non nel codice
ALIAS = {"produttorie": "somme"}


def inserisci(cid: str, md: str, en: bool = False) -> str:
    inserti = INSERTI.get(cid)
    if not inserti:
        return md
    titolo, invito = TESTO["en" if en else "it"]
    righe = md.split("\n")
    # dal numero di sezione alla riga del titolo (le sezioni sono «## N. …»)
    for num, strumento, matrice, extra in sorted(inserti, key=lambda x: -x[0]):
        pref = f"## {num}. "
        idx = next((i for i, r in enumerate(righe) if r.startswith(pref)), None)
        if idx is None:
            raise ValueError(f"{cid}: sezione «{pref}» non trovata")
        fine = next((j for j in range(idx + 1, len(righe))
                     if righe[j].startswith("## ")), len(righe))
        attr = f' data-tool="{ALIAS.get(strumento, strumento)}"'
        if matrice:
            attr += f' data-matrix="{matrice}"'
        for k, v in extra.items():
            attr += f' data-{k}="{v}"'
        righe[fine:fine] = ["", f'!!! interattivo "{titolo}"', "",
                            f"    {invito}", "",
                            f'<div class="la-tool"{attr}></div>', ""]
    return "\n".join(righe)
