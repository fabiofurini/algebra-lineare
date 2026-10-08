"""PDF del sito: la dispensa nel formato della collana (un solo libro).

I PDF dei singoli capitoli nel formato delle note non si pubblicano più: il
PDF è la dispensa prodotta da genera_dispensa.py (sorgenti in it/dispensa e
en/notes, privati). Questo script resta per comodità: genera e compila la
dispensa e la copia in docs/pdf/.

Uso: python3 python/compila_pdf.py      (LINGUA=en per l'inglese)
"""
import os
import subprocess
import sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
if __name__ == "__main__":
    r = subprocess.run([sys.executable, str(QUI / "genera_dispensa.py"), "--compila"], env=dict(os.environ))
    sys.exit(r.returncode)
