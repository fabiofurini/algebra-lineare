<h3 align="center">Materiale didattico di
<a href="https://sites.google.com/view/fabiofurini/home-page">Fabio Furini</a></h3>
<p align="center">
  Professore associato di Ricerca Operativa ·
  <a href="https://www.diag.uniroma1.it/">DIAG</a>, Sapienza Università di Roma ·
  <a href="https://sites.google.com/view/fabiofurini/home-page">sito personale</a>
</p>

# Algebra Lineare

Il materiale preliminare di algebra lineare per i corsi di Ricerca Operativa:
somme e produttorie, vettori, matrici e determinanti, operazioni elementari,
matrice inversa, fattorizzazione LU, autovalori, norme e sistemi lineari.

**📖 Dispensa online: [fabiofurini.github.io/algebra-lineare](https://fabiofurini.github.io/algebra-lineare/)**

**🧮 Laboratorio di calcolo: [gli strumenti](https://fabiofurini.github.io/algebra-lineare/laboratorio/)** — scrivi una
matrice e guarda **tutti i passaggi**: eliminazione di Gauss, determinante
(Laplace, Sarrus, eliminazione), matrice inversa con Gauss–Jordan, rango,
fattorizzazione LU/PLU, sistemi lineari (Gauss, Rouché–Capelli, Cramer),
autovalori e criterio di Sylvester. Conti **esatti con le frazioni**, con la
stessa notazione delle dispense. Gira nel browser, anche da telefono.

**⬇️ Tutte le dispense in PDF: [dispense-algebra-lineare.pdf](https://fabiofurini.github.io/algebra-lineare/pdf/dispense-algebra-lineare.pdf)**

## Esercizi

Un foglio per capitolo, con le soluzioni svolte; nella scheda *Esercitati* del
laboratorio gli esercizi si generano all'infinito, con la correzione.

## Il motore di calcolo

Il laboratorio è in [`docs/javascripts/algebra.js`](docs/javascripts/algebra.js)
(aritmetica esatta con frazioni) e [`docs/javascripts/laboratorio.js`](docs/javascripts/laboratorio.js).
I risultati e **ogni passo intermedio** sono verificati contro SymPy:

```bash
python3 test/genera_casi.py     # i casi attesi, calcolati con SymPy
node test/test_algebra.js       # oltre 46 000 controlli
```

## Licenza

- **Testi, figure e dati** (`docs/`): [CC BY 4.0](LICENSE).
- **Codice** (`docs/javascripts/`, `python/`, `test/`): [MIT](LICENSE-CODE).

Per citare il materiale c'è [`CITATION.cff`](CITATION.cff).

## English version

The whole course is also available in English:
**[fabiofurini.github.io/linear-algebra](https://fabiofurini.github.io/linear-algebra/)**
([repository](https://github.com/fabiofurini/linear-algebra)).

## Della stessa collana

- [Laboratorio di Ricerca Operativa](https://fabiofurini.github.io/laboratorio-ricerca-operativa/)
- [Modellazione MIP](https://fabiofurini.github.io/modellazione-mip/)
- [Analisi Matematica 1](https://fabiofurini.github.io/analisi-matematica-1/)

---

Materiale didattico di **[Fabio Furini](https://sites.google.com/view/fabiofurini/home-page)** — [DIAG](https://www.diag.uniroma1.it/), Sapienza Università di Roma.
