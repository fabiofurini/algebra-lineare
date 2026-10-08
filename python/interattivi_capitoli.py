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


# ---------------------------------------------------------------- fine del capitolo
# Alla fine di ogni capitolo: il foglio di esercizi di QUEL capitolo e gli
# strumenti del laboratorio pertinenti, ciascuno con l'indicazione di cosa farci.
# (strumento, nota IT, nota EN); nota None = il sottotitolo dello strumento.
FINE = {
    "somme-01-sommatorie": [("somme", "scrivi il termine generale e confronta con le somme notevoli di questo capitolo",
                             "type the general term and compare with the closed-form sums of this chapter")],
    "somme-02-produttorie": [("somme", "scegli «Produttoria Π»: per esempio \\(\\prod_{k=1}^{n} k = n!\\)",
                              "choose «Product Π»: for example \\(\\prod_{k=1}^{n} k = n!\\)")],
    "vettori-matrici-01-vettori": [],
    "vettori-matrici-02-matrici": [
        ("prodotto", None, None),
        ("det", "sviluppo di Laplace lungo la riga o colonna che scegli, oppure regola di Sarrus",
                "Laplace expansion along the row or column you choose, or the Sarrus rule"),
        ("rango", None, None)],
    "vettori-matrici-03-operazioni-elementari": [
        ("gauss", None, None),
        ("det", "scegli il metodo «Eliminazione di Gauss»: l'effetto di ogni operazione elementare sul determinante",
                "choose the «Gaussian elimination» method: the effect of each elementary operation on the determinant"),
        ("pivoting", None, None)],
    "vettori-matrici-04-matrice-inversa": [("inversa", None, None)],
    "vettori-matrici-05-fattorizzazione-lu": [
        ("lu", None, None),
        ("sistema", "scegli «Con la fattorizzazione LU»: sostituzione in avanti e all'indietro",
                    "choose «With the LU factorization»: forward and back substitution")],
    "vettori-matrici-06-autovalori": [("autovalori", None, None)],
    "norme-01-norme": [("norme", None, None)],
    "sistemi-01-sistemi-lineari": [
        ("sistema", None, None),
        ("rango", "il rango di \\(\\boldsymbol A\\) e della matrice completa \\((\\boldsymbol A\\mid\\boldsymbol b)\\) per Rouché–Capelli",
                  "the rank of \\(\\boldsymbol A\\) and of the augmented matrix \\((\\boldsymbol A\\mid\\boldsymbol b)\\) for Rouché–Capelli")],
    "approfondimenti-01-valore-assoluto": [],
    "approfondimenti-02-aritmetica-modulare": [],
}


def fine_capitolo(cid_it: str, parte: str, num: int, en: bool = False) -> str:
    import re
    from capitoli import CARTELLA_ES, ESERCIZI, SORGENTE_ES, ident_es
    from pagine_fisse import LAB, STRUMENTI
    righe = ["## " + ("Exercises and lab" if en else "Esercizi e laboratorio"), ""]
    foglio = next((e for e in ESERCIZI if e[0] == parte and e[1] == num), None)
    if foglio and (SORGENTE_ES / foglio[3]).exists():
        n = len(re.findall(r"\\begin\{texercise\}", (SORGENTE_ES / foglio[3]).read_text(errors="replace")))
        cid = ident_es(*foglio[:3])
        testo = (f"the exercise sheet of this chapter: {n} exercises with worked solutions" if en
                 else f"il foglio di esercizi di questo capitolo: {n} esercizi con le soluzioni svolte")
        righe.append(f"- :material-pencil-box-multiple: **{'Exercises' if en else 'Esercizi'}** · "
                     f"[{testo}](../{CARTELLA_ES}/{cid}.md)")
    strumenti = {t[3]: t for t in STRUMENTI}
    for tool, nota_it, nota_en in FINE.get(cid_it, []):
        rel, tit_it, tit_en, _, sub_it, sub_en, _ = strumenti[tool]
        nota = (nota_en if en else nota_it) or (sub_en if en else sub_it)
        righe.append(f"- :material-calculator-variant: **{'Lab' if en else 'Laboratorio'}** · "
                     f"[{tit_en if en else tit_it}](../{LAB}/{rel}.md) — {nota}")
    return "\n".join(righe) + "\n" if len(righe) > 2 else ""
