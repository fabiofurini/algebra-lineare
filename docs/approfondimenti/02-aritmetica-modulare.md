---
title: "Aritmetica modulare"
---

# Aritmetica modulare

<div class="info-capitolo" markdown>

**Approfondimenti · Capitolo A.2** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/approfondimenti-02-aritmetica-modulare.pdf)

</div>

## 1. Divisione euclidea

<a id="box-lem_euclid-division-1"></a>

!!! teorema "Lemma 1: divisione euclidea (o divisione con resto)"

    Per ogni coppia di numeri interi $n$ e $m$, con $m \neq 0$, esistono e sono unici due numeri interi $q$ e $r$ tali che

    \begin{equation}
    \label{DIVISION}
    n = q \; m  + r ~~~~~\text{e}~~~~~ 0 \le r <  |m|
    \end{equation}

- Il valore $n$ è detto <strong>dividendo</strong>, il valore $m$ è detto <strong>divisore</strong>, il valore $q$ è detto <strong>quoziente</strong> e il valore $r$ è detto <strong>resto</strong>.

- La convenzione standard prevede che il resto sia non negativo, ma esistono altre convenzioni in cui il resto $r$ può essere negativo.

??? dimostrazione "Dimostrazione"

    - Per dimostrare l'<em>esistenza</em>, consideriamo l'insieme

        $$
        S = \big\{~~ n - k m:~~ k \in \mathbb{Z} ~~\text{e}~~ n - k m \geq 0 ~~\big\}
        $$

        L'insieme \( S \) è non vuoto, poiché per \( k = -|n|\, m \) si ha \( n - k m = n + |n|\, m^2 \geq n + |n| \geq 0 \). Poiché \( S \) è un sottoinsieme non vuoto degli interi non negativi, il principio del buon ordinamento garantisce che esiste un elemento minimo \( r \in S \), cioè esiste un intero \( q \) tale che

        $$
        r = n - q m, \quad \text{con } r \geq 0
        $$

        Per costruzione, deve essere \( r < |m| \): infatti, se fosse \( r \geq |m| \), potremmo scrivere

        $$
        r' = r - |m| = n - \Big(q+\frac{|m|}{m}\Big)\,m \geq 0
        $$

        e quindi \( r' \in S \), contro la minimalità di \( r \).

    - Per dimostrare l'<em>unicità</em>, supponiamo che esistano due coppie \( (q_1, r_1) \) e \( (q_2, r_2) \) tali che

        $$
        n = q_1 m + r_1 = q_2 m + r_2
        $$

        con \( 0 \leq r_1, r_2 < |m| \). Sottraendo le due equazioni, si ha

        $$
        (q_1 - q_2) m = r_2 - r_1
        $$

        Poiché \( |r_2 - r_1| < |m| \) e \( m \) divide \( r_2 - r_1 \) (che è uguale al membro sinistro), l'unica possibilità è \( r_1 = r_2 \), da cui \( q_1 = q_2 \), il che garantisce l'unicità.

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-def_multiple-2"></a>

!!! definizione "Definizione 1: multiplo"

    Un numero intero \( n  \) è un <strong>multiplo</strong> di un numero intero \( m \) se esiste un numero intero \( q  \) tale che

    \begin{equation}
    n = q \cdot m
    \end{equation}

<a id="box-def_factor-3"></a>

!!! definizione "Definizione 2: divisore"

    Un numero intero \( m  \) è un <strong>divisore</strong> (o <strong>fattore</strong>) di un numero intero \( n \) se esiste un numero intero \( q  \) tale che

    \begin{equation}
    n = q \cdot m
    \end{equation}

- Un numero intero ${n}$ è <strong>divisibile</strong> per un numero intero ${m}$ se ${m}$ è un divisore di ${n}$.

## 2. Modulo e congruenza modulo $m$

!!! chiave ""

    Dati due numeri interi $n$ e $m$, con $m \neq 0$, $n$ <strong>modulo</strong> $m$ (abbreviato in ${n} \text{~mod~} {m}$) è il <strong>resto</strong> $r$ della divisione euclidea (o divisione con resto) di $n$ per $m$, dove $n$ è il <strong>dividendo</strong> e $m$ è il <strong>divisore</strong>.

- Dalla definizione segue che:

    $$
    0 \le {n} \text{~mod~} {m}  < |m|  \qquad \forall n,m \in \Z,~m \neq 0
    $$

!!! chiave ""

    Due numeri naturali $n$ e $k$ sono <strong>congruenti</strong> modulo un numero naturale $m \ge 1$ se

    $$
    {n} \text{~mod~} {m} = {k} \text{~mod~} {m}
    $$

    e si scrive

    \begin{equation*}
    {n} \equiv {k} \tpmod{ {m}}
    \end{equation*}

- Le parentesi indicano che (mod m) si applica all'intera relazione e non solo al membro destro (qui, $k$).

- Equivalentemente, si ha ${n} \equiv {k} \tpmod{ {m}}$

    1. se ${n}$ e ${k}$ hanno lo stesso resto nella divisione per ${m}$;

    2. se ${m}$ è un divisore di $|n - k|$, cioè se esiste un numero naturale \( q  \) tale che \(|n - k| = q \cdot m \) o, equivalentemente, se esiste un numero intero \( q  \) tale che \(n - k = q \cdot m \).

<a id="box-ex_congruence-mod-5-4"></a>

!!! esempio "Esempio 1: congruenza modulo $5$"

    Per esempio, $23$ e $13$ sono congruenti modulo $5$ e si ha $23 \equiv 13 \tpmod{5}$
