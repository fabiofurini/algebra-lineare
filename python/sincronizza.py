"""Copia in en/ ciò che è identico nelle due lingue: fogli di stile, motore di
calcolo, laboratorio, MathJax, licenze. Si lancia dopo ogni modifica a questi file.

Uso: python3 python/sincronizza.py
"""
import shutil
from pathlib import Path

IT = Path(__file__).resolve().parents[1]
EN = IT.parent / "en"

CONDIVISI = [
    "docs/stylesheets/extra.css", "docs/stylesheets/laboratorio.css",
    "docs/javascripts/cloudflare-analytics.js", "docs/javascripts/mathjax.js", "docs/javascripts/algebra.js", "docs/javascripts/laboratorio.js",
    "LICENSE", "LICENSE-CODE", ".gitignore",
    # il workflow NON si copia: in en/ si chiama publish.yml ed è in inglese
    # (due workflow uguali si annullerebbero a vicenda sulla stessa concorrenza)
]

if __name__ == "__main__":
    for rel in CONDIVISI:
        src, dst = IT / rel, EN / rel
        if not src.exists():
            print("manca:", rel)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dst)
    print(f"{len(CONDIVISI)} file condivisi copiati in en/")
