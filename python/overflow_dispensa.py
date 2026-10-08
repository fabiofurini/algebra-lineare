"""Elenca gli overflow (Overfull \\hbox) di una dispensa compilata, con il
capitolo, la riga e il testo LaTeX che li produce.

Uso: python3 python/overflow_dispensa.py <cartella della dispensa> [soglia_pt]
"""
import re
import sys
from pathlib import Path

radice = Path(sys.argv[1])
soglia = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
logs = [p for p in radice.glob("*.log")]
if not logs:
    sys.exit("nessun log")
log = max(logs, key=lambda p: p.stat().st_mtime).read_text(errors="replace")

eventi = []
for m in re.finditer(r"\(\./capitoli/([\w-]+)\.tex|Overfull \\hbox \(([0-9.]+)pt too wide\) (?:in paragraph at lines (\d+)--(\d+)|detected at line (\d+))", log):
    eventi.append(m)
corrente = None
trovati = []
for m in eventi:
    if m.group(1):
        corrente = m.group(1)
        continue
    pt = float(m.group(2))
    if pt < soglia or not corrente:
        continue
    a = int(m.group(3) or m.group(5))
    b = int(m.group(4) or m.group(5))
    trovati.append((corrente, a, b, pt))

for cap, a, b, pt in trovati:
    righe = (radice / "capitoli" / f"{cap}.tex").read_text(errors="replace").split("\n")
    estratto = " ⏎ ".join(r.strip() for r in righe[max(0, a - 3):b] if r.strip())[:300]
    print(f"{cap}:{a}-{b}  {pt:.1f}pt  {estratto}")
print(f"TOTALE overflow > {soglia}pt: {len(trovati)}")
