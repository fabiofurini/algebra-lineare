"""Dalle note in capitoli separati alla dispensa nel formato della collana.

Le note di Fabio sono documenti `article` autonomi (uno per argomento) che
caricano il suo decla.tex. Le dispense della collana (Laboratorio di Ricerca
Operativa, Modellazione MIP) sono invece un libro: `main.tex`, `preambolo.tex`,
frontespizio, parti, capitoli in `capitoli/`, box didattici della collana ed
esercizi in fondo ai capitoli. Questo script produce il libro dalle note,
senza toccare la matematica:

- il corpo di ogni nota (dopo l'indice) diventa un capitolo, oppure una
  sezione di un capitolo che ne raccoglie più d'una (i livelli scendono di uno);
- i box delle note restano: Definition/Observation/... (blu e rossi, come nelle
  note e nelle slide), i riquadri verdi diventano il box verde della collana,
  gli esempi il box `esempio`, gli esercizi `esercizio` + `soluzione`;
- le etichette ricevono il prefisso della nota (nel libro non devono collidere);
- le figure incluse si copiano in figure/<nota>/.

La configurazione (volumi, parti, capitoli, testi del frontespizio) è nel file
dispense_config.py accanto a questo. Uso:

    python3 python/genera_dispensa.py            # italiano
    LINGUA=en python3 python/genera_dispensa.py  # inglese
    ... --compila                                # e compila i PDF
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))
import dispense_config as CFG  # noqa: E402

LINGUA = os.environ.get("LINGUA", "it")
EN = LINGUA == "en"

TEOREMI = ("Definition", "Theorem", "Corollary", "Proposition", "Observation", "Lemma",
           "Definizione", "Teorema", "Corollario", "Proposizione", "Osservazione")


# ---------------------------------------------------------------- utilità LaTeX
def maschera_commenti(s: str) -> str:
    """Toglie il testo dei commenti ma lascia il %: la semantica TeX non cambia
    (il % continua a unire le righe) e i \\begin commentati non disturbano."""
    out = []
    for riga in s.split("\n"):
        m = re.search(r"(?<!\\)%", riga)
        if m:
            prima = riga[:m.start()]
            if prima.strip() == "":
                continue            # riga interamente commentata
            riga = prima + "%"
        out.append(riga)
    return "\n".join(out)


def chiusa(s: str, i: int, a="{", b="}") -> int:
    d = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == a:
            d += 1
        elif c == b:
            d -= 1
            if d == 0:
                return j
        j += 1
    raise ValueError("parentesi non chiusa: " + s[i:i + 60])


def gruppo(s: str, i: int):
    while i < len(s) and s[i] in " \t\n":
        i += 1
    if i >= len(s) or s[i] != "{":
        return None, i
    j = chiusa(s, i)
    return s[i + 1:j], j + 1


def opzionale(s: str, i: int):
    k = i
    while k < len(s) and s[k] in " \t\n":
        k += 1
    if k < len(s) and s[k] == "[":
        j = chiusa(s, k, "[", "]")
        return s[k + 1:j], j + 1
    return None, i


def fine_ambiente(s: str, nome: str, da: int):
    pat = re.compile(r"\\(begin|end)\{" + re.escape(nome) + r"\}")
    d = 1
    for m in pat.finditer(s, da):
        d += 1 if m.group(1) == "begin" else -1
        if d == 0:
            return m.start(), m.end()
    raise ValueError("ambiente non chiuso: " + nome)


# ---------------------------------------------------------------- una nota → corpo
def corpo_nota(tex: str) -> str:
    tex = maschera_commenti(tex)
    _, _, resto = tex.partition("\\begin{document}")
    corpo, _, _ = resto.partition("\\end{document}")
    k = corpo.find("\\tableofcontents")
    if k >= 0:
        corpo = corpo[k + len("\\tableofcontents"):]
    else:   # fogli di esercizi: dal primo esercizio o dalla prima sezione
        cand = [x for x in (corpo.find("\\section"), corpo.find("\\begin{texercise}"), corpo.find("\\clearpage")) if x >= 0]
        corpo = corpo[min(cand):] if cand else corpo
    return corpo


def titolo_nota(tex: str) -> str:
    m = re.search(r"\{\s*\\huge\s*\\bf(.*?)\}\s*\\vspace", tex, re.S)
    t = m.group(1) if m else ""
    t = re.sub(r"\\\\(\[[^\]]*\])?", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def converti_corpo(corpo: str, sid: str, scendi: int, cartella: Path, figure_out: Path) -> str:
    """Trasforma il corpo di una nota nel formato della dispensa."""
    s = corpo
    # 1. niente salti pagina degli article: l'impaginazione è del libro
    s = re.sub(r"\\(newpage|clearpage)\b", "", s)
    s = re.sub(r"\\renewcommand\{\\proofname\}\{[^}]*\}", "", s)
    s = re.sub(r"\\pagestyle\{[^}]*\}|\\setcounter\{page\}\{\d+\}", "", s)
    # 2. i livelli delle sezioni scendono di `scendi`
    if scendi:
        livelli = ["section", "subsection", "subsubsection", "paragraph", "subparagraph"]
        def giu(m):
            nome, stella = m.group(1), m.group(2) or ""
            i = livelli.index(nome)
            return "\\" + livelli[min(i + scendi, len(livelli) - 1)] + stella
        s = re.sub(r"\\(section|subsection|subsubsection|paragraph)(\*?)(?=[\s\[{])", giu, s)
    # 3. le \newcommand interne possono ripetersi fra note: \DeclareRobustCommand ridefinisce
    s = re.sub(r"\\newcommand(\*?)(?=\s*\{?\\)", r"\\DeclareRobustCommand\1", s)
    # 4. ambienti
    s = ambienti(s, sid)
    # 4b. le tabelle larghe non devono uscire dal testo né dai box: la pagina della
    #     collana è più stretta di quella delle note. Si riducono solo se servono.
    s = tabelle_adattate(s)
    # 5. etichette con il prefisso della nota
    s = re.sub(r"\\label\{([^}]*)\}", lambda m: "\\label{" + sid + ":" + m.group(1) + "}", s)
    s = re.sub(r"\\(ref|eqref|pageref|autoref|cref|Cref)\{([^}]*)\}",
               lambda m: "\\" + m.group(1) + "{" + ",".join(rif(x.strip(), sid) for x in m.group(2).split(",")) + "}", s)
    # 6. figure: copiate in figure/<nota>/
    def fig(m):
        opt, percorso = m.group(1) or "", m.group(2)
        src = (cartella / percorso)
        if not src.suffix:
            for ext in (".pdf", ".png", ".jpg", ".jpeg", ".eps"):
                if src.with_suffix(ext).exists():
                    src = src.with_suffix(ext)
                    break
        if not src.exists():
            print(f"   ! figura mancante: {percorso} ({sid})")
            return m.group(0)
        dest = figure_out / sid / src.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
        return f"\\includegraphics{opt}{{figure/{sid}/{src.name}}}"
    s = re.sub(r"\\includegraphics(\[[^\]]*\])?\{([^}]*)\}", fig, s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip() + "\n"


MATEMATICA = re.compile(r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?|displaymath|math)\}|"
                        r"\\end\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?|displaymath|math)\}|"
                        r"\\\[|\\\]|\$\$")


def in_matematica(s: str, pos: int) -> bool:
    """La posizione pos è dentro una formula a blocco?"""
    d = 0
    dollari = False
    for m in MATEMATICA.finditer(s, 0, pos):
        t = m.group(0)
        if t == "$$":
            dollari = not dollari
        elif t.startswith("\\begin") or t == "\\[":
            d += 1
        else:
            d = max(0, d - 1)
    return d > 0 or dollari


def tabelle_adattate(s: str) -> str:
    out, i = [], 0
    pat = re.compile(r"\\begin\{(tabular|tabularx|tabular\*)\}")
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            break
        e0, e1 = fine_ambiente(s, m.group(1), m.end())
        out.append(s[i:m.start()])
        blocco = s[m.start():e1]
        if in_matematica(s, m.start()):
            out.append(blocco)
        else:
            out.append("\\begin{adjustbox}{max width=\\linewidth}" + blocco + "\\end{adjustbox}")
        i = e1
    return "".join(out)


def rif(x: str, sid: str) -> str:
    # \ref{mytheorem:lab} dei box (prefisso di tcbtheorem) → mytheorem:<nota>-lab
    m = re.match(r"^(mytheorem|def|theo|cor|prop|obs|lem|def_ita|theo_ita|cor_ita|prop_ita|obs_ita):(.*)$", x)
    if m:
        return f"mytheorem:{sid}-{m.group(2)}"
    return f"{sid}:{x}"


def ambienti(s: str, sid: str) -> str:
    out, i = [], 0
    pat = re.compile(r"\\begin\{(tcolorbox|texercise|" + "|".join(TEOREMI) + r")\}")
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            break
        out.append(s[i:m.start()])
        nome = m.group(1)
        a = m.end()
        e0, e1 = fine_ambiente(s, nome, a)
        dentro = s[a:e0]
        if nome in TEOREMI:
            tit, k = gruppo(dentro, 0)
            lab, k = gruppo(dentro, k)
            env = {"Definizione": "Definition", "Teorema": "Theorem", "Corollario": "Corollary",
                   "Proposizione": "Proposition", "Osservazione": "Observation"}.get(nome, nome)
            lab2 = f"{sid}-{lab.strip()}" if lab and lab.strip() else f"{sid}-x{len(out)}"
            out.append(f"\\begin{{{env}}}{{{tit or ''}}}{{{lab2}}}" + ambienti(dentro[k:], sid) + f"\\end{{{env}}}")
        elif nome == "texercise":
            opt, k = opzionale(dentro, 0)
            lab, k = gruppo(dentro, k)
            etich = f"\\label{{exe:{lab.strip()}}}" if lab else ""
            out.append("\\begin{esercizio}" + etich + ambienti(dentro[k:], sid) + "\\end{esercizio}")
        else:  # tcolorbox
            opt, k = opzionale(dentro, 0)
            opt = opt or ""
            corpo = ambienti(dentro[k:], sid)
            me = re.search(r"example=\{", opt)
            if me:
                tit, fine = gruppo(opt, me.end() - 1)
                lab, _ = gruppo(opt, fine)
                out.append(f"\\begin{{esempion}}{{{tit}}}{{{sid}:{(lab or '').strip()}}}" + corpo + "\\end{esempion}")
            elif "green" in opt:
                out.append("\\begin{riquadro}" + corpo + "\\end{riquadro}")
            elif "blue" in opt and "colback=blue" in opt.replace(" ", ""):
                out.append("\\begin{soluzione}" + corpo + "\\end{soluzione}")
            else:
                pulita = re.sub(r",?\s*text width=[^,\]]*", "", opt).strip(", ")
                out.append(f"\\begin{{tcolorbox}}[{pulita}]" + corpo + "\\end{tcolorbox}")
        i = e1
    r = "".join(out)
    # un box che era centrato con center: il center non serve più
    r = re.sub(r"\\begin\{center\}\s*(\\begin\{(riquadro|soluzione)\}.*?\\end\{\2\})\s*\\end\{center\}", r"\1", r, flags=re.S)
    return r


# ---------------------------------------------------------------- un volume
def genera_volume(vol: dict, radice: Path, compila: bool):
    radice.mkdir(parents=True, exist_ok=True)
    (radice / "capitoli").mkdir(exist_ok=True)
    figure = radice / "figure"
    figure.mkdir(exist_ok=True)
    shutil.copy(CFG.LOGO, figure / "sapienza.jpeg")
    (radice / "preambolo.tex").write_text(CFG.preambolo(EN, vol), encoding="utf-8")
    (radice / "frontespizio.tex").write_text(CFG.frontespizio(EN, vol), encoding="utf-8")
    sorgente = CFG.sorgente(EN)
    righe_main = []
    ncap = 0
    for parte in vol["parti"]:
        if parte.get("appendice"):
            righe_main.append("\\appendix")
        elif parte.get("titolo"):
            righe_main.append(f"\\part{{{parte['titolo'][1 if EN else 0]}}}")
        for cap in parte["capitoli"]:
            ncap += 1
            nome_file = cap["file"]
            pezzi = []
            if "sezioni" in cap:      # un capitolo che raccoglie più note
                titolo = cap["titolo"][1 if EN else 0]
                pezzi.append(f"\\chapter{{{titolo}}}\\label{{cap:{cap['id']}}}\n")
                if cap.get("intro"):
                    pezzi.append(cap["intro"][1 if EN else 0] + "\n")
                for sez in cap["sezioni"]:
                    pezzi.append(blocco(sez, sorgente, 1, figure, sez["titolo"][1 if EN else 0], "section"))
            else:
                pezzi.append(blocco(cap, sorgente, 0, figure, None, "chapter"))
            (radice / "capitoli" / f"{nome_file}.tex").write_text("\n".join(pezzi), encoding="utf-8")
            righe_main.append(f"\\include{{capitoli/{nome_file}}}")
    main = (f"\\documentclass[11pt,a4paper,oneside]{{book}}\n\\input{{preambolo}}\n\n"
            f"\\title{{{vol['titolo'][1 if EN else 0]}}}\n\\author{{Fabio Furini}}\n\n"
            "\\begin{document}\n\\input{frontespizio}\n\\tableofcontents\n\n" +
            "\n".join(righe_main) + "\n\n\\end{document}\n")
    (radice / "main.tex").write_text(main, encoding="utf-8")
    print(f"[{LINGUA}] {vol['file']}: {ncap} capitoli → {radice}")
    if compila:
        return compila_volume(radice)
    return None


def blocco(voce: dict, sorgente: Path, scendi: int, figure: Path, titolo_forzato, livello: str) -> str:
    f = sorgente / voce["note"]
    tex = f.read_text(encoding="utf-8", errors="replace")
    titolo = titolo_forzato or titolo_nota(tex)
    sid = voce["id"]
    testa = f"\\{livello}{{{titolo}}}\\label{{{'cap' if livello == 'chapter' else 'sec'}:{sid}}}\n\n"
    corpo = converti_corpo(corpo_nota(tex), sid, scendi, f.parent, figure)
    # gli esercizi della nota, in fondo
    for es in voce.get("esercizi", []):
        fe = sorgente / es
        if not fe.exists():
            print(f"   ! esercizi mancanti: {es}")
            continue
        te = fe.read_text(encoding="utf-8", errors="replace")
        liv = "\\section" if scendi == 0 else "\\subsection"
        corpo += f"\n{liv}{{{'Exercises' if EN else 'Esercizi'}}}\\label{{es:{sid}}}\n\n"
        corpo += converti_corpo(corpo_nota(te), sid + "-es", scendi, fe.parent, figure)
    return testa + corpo


def compila_volume(radice: Path):
    for _ in range(3):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=radice,
                           capture_output=True, text=True, errors="replace", timeout=1800)
    log = (radice / "main.log").read_text(errors="replace")
    errori = re.findall(r"^! .*", log, re.M)
    indef = len(re.findall(r"Reference `[^']*' on page \d+ undefined", log))
    multiple = len(re.findall(r"multiply defined", log))
    pdf = radice / "main.pdf"
    pagine = None
    if pdf.exists():
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        m = re.search(r"Pages:\s+(\d+)", info)
        pagine = int(m.group(1)) if m else None
    print(f"   pdflatex: {len(errori)} errori, {indef} riferimenti indefiniti, {multiple} etichette doppie, {pagine} pagine")
    for e in errori[:8]:
        print("     ", e)
    for est in ("aux", "log", "out", "toc", "fls", "fdb_latexmk"):
        pass
    return {"errori": len(errori), "indefiniti": indef, "doppie": multiple, "pagine": pagine, "pdf": pdf}


if __name__ == "__main__":
    compila = "--compila" in sys.argv
    filtro = [a for a in sys.argv[1:] if not a.startswith("--")]
    esiti = {}
    for vol in CFG.VOLUMI:
        if filtro and not any(vol["file"].startswith(f) for f in filtro):
            continue
        radice = CFG.cartella(EN, vol)
        esiti[vol["file"]] = genera_volume(vol, radice, compila)
        if compila and esiti[vol["file"]] and esiti[vol["file"]]["pdf"].exists():
            dest = CFG.pdf_sito(EN, vol)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(esiti[vol["file"]]["pdf"], dest)
            print(f"   → {dest}")
