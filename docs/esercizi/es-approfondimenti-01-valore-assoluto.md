---
title: "Valore assoluto"
---

# Valore assoluto

<div class="info-capitolo" markdown>

**Esercizi · Approfondimenti** · capitolo [A.1 · Valore assoluto](../approfondimenti/01-valore-assoluto.md) · con le soluzioni svolte · [:material-file-pdf-box: PDF](../pdf/es-approfondimenti-01-valore-assoluto.pdf)

</div>

<a id="box-exe_abs_compute-1"></a>

!!! esercizio "Esercizio 1"

    Usando la definizione di valore assoluto, calcolare:

    $$
    {\rm a)}~ |-3| + |2-7| - |-4| \; \left|\frac{1}{2}\right|, \qquad {\rm b)}~ |3 - \pi|, \qquad {\rm c)}~ \left| \frac{1}{3} - \frac{1}{2}\right|
    $$

??? soluzione "Soluzione"

    - **a)** Poiché $-3<0$, $2-7=-5<0$, $-4<0$ e $\frac{1}{2} \ge 0$:

        $$
        |-3| + |2-7| - |-4| \; \left|\frac{1}{2}\right| = 3 + 5 - 4 \cdot \frac{1}{2} = 6
        $$

    - **b)** Poiché $\pi > 3$, si ha $3 - \pi < 0$ e quindi $|3-\pi| = -(3-\pi) = \pi - 3$.

    - **c)** Poiché $\frac{1}{3} - \frac{1}{2} = -\frac{1}{6} < 0$, si ha $\left| \frac{1}{3} - \frac{1}{2}\right| = \frac{1}{6}$.

<a id="box-exe_abs_basic_properties-2"></a>

!!! esercizio "Esercizio 2"

    Dimostrare che per ogni numero reale $b$ si ha:

    $$
    {\rm a)}~ |b| \ge 0 {\rm ~~e~~} |b| = 0 \Longleftrightarrow b = 0, \qquad {\rm b)}~ -|b| \le b \le |b|, \qquad {\rm c)}~ |b|^2 = b^2
    $$

??? soluzione "Soluzione"

    Distinguiamo i due casi della definizione di valore assoluto.

    - Se $b \ge 0$, allora $|b| = b \ge 0$; inoltre $|b|=0$ se e solo se $b=0$; si ha $-|b| = -b \le 0 \le b = |b|$; infine $|b|^2 = b^2$.

    - Se $b < 0$, allora $|b| = -b > 0$ (in particolare $|b| \neq 0$); si ha $-|b| = b < 0 < -b = |b|$; infine $|b|^2 = (-b)^2 = b^2$.

    In entrambi i casi valgono a), b) e c).

<a id="box-exe_abs_inequalities-3"></a>

!!! esercizio "Esercizio 3"

    Trovare tutti i numeri reali $x$ tali che:

    $$
    {\rm a)}~ |x-2| < 3, \qquad {\rm b)}~ |2\:x+1| \le 5, \qquad {\rm c)}~ |x - 4| \ge 1
    $$

??? soluzione "Soluzione"

    - **a)** Da $|a| < \varepsilon \Longleftrightarrow -\varepsilon < a < \varepsilon$ con $a = x-2$ e $\varepsilon = 3$:

        $$
        -3 < x - 2 < 3 \Longleftrightarrow -1 < x < 5
        $$

    - **b)** Da $|a| \le \varepsilon \Longleftrightarrow -\varepsilon \le a \le \varepsilon$ con $a = 2\:x+1$ e $\varepsilon = 5$:

        $$
        -5 \le 2\:x + 1 \le 5 \Longleftrightarrow -6 \le 2\:x \le 4 \Longleftrightarrow -3 \le x \le 2
        $$

    - **c)** La disuguaglianza $|x-4| \ge 1$ è falsa esattamente quando $|x - 4| < 1$, cioè quando $-1 < x-4 < 1$, ossia $3 < x < 5$. Quindi le soluzioni sono:

        $$
        x \le 3 {\rm ~~~oppure~~~} x \ge 5
        $$

<a id="box-exe_abs_equation_two-4"></a>

!!! esercizio "Esercizio 4"

    Trovare tutti i numeri reali $x$ tali che $|x-1| = |x+3|$.

??? soluzione "Soluzione"

    Due numeri reali hanno lo stesso valore assoluto se e solo se sono uguali oppure opposti. Quindi:

    - $x - 1 = x + 3$ dà $-1 = 3$, che è impossibile;

    - $x - 1 = -(x+3)$ dà $2\:x = -2$, cioè $x = -1$.

    L'unica soluzione è $x=-1$. Verifica: $|-1-1| = 2 = |-1+3|$.

<a id="box-exe_abs_equation_sum-5"></a>

!!! esercizio "Esercizio 5"

    Trovare tutti i numeri reali $x$ tali che $|x| + |x-2| = 4$.

??? soluzione "Soluzione"

    I segni di $x$ e di $x-2$ cambiano in $x=0$ e in $x=2$, quindi distinguiamo tre casi:

    - $x < 0$: $|x| = -x$ e $|x-2| = 2-x$, quindi $-2\:x + 2 = 4$, cioè $x = -1$, che soddisfa $x<0$;

    - $0 \le x < 2$: $|x| = x$ e $|x-2| = 2-x$, quindi $x + 2 - x = 2 = 4$, che è impossibile;

    - $x \ge 2$: $|x| = x$ e $|x-2| = x-2$, quindi $2\:x - 2 = 4$, cioè $x = 3$, che soddisfa $x \ge 2$.

    Le soluzioni sono $x=-1$ e $x=3$.

<a id="box-exe_abs_triangle_equality-6"></a>

!!! esercizio "Esercizio 6"

    Dimostrare che per ogni coppia di numeri reali $b$ e $c$:

    $$
    |b+c| = |b| + |c| \Longleftrightarrow b\:c \ge 0
    $$

??? soluzione "Soluzione"

    Sia $|b+c|$ sia $|b|+|c|$ sono non negativi, e due numeri non negativi sono uguali se e solo se i loro quadrati sono uguali. Usando l'Esercizio [Esercizio 2](#box-exe_abs_basic_properties-2) c) e $|b\:c| = |b|\:|c|$, si ha:

    $$
    |b+c|^2 = (b+c)^2 = b^2 + 2\:b\:c + c^2, \qquad \big(|b| + |c|\big)^2 = b^2 + 2\:|b\:c| + c^2
    $$

    Quindi $|b+c| = |b| + |c|$ se e solo se $b\:c = |b\:c|$, cioè (per la definizione di valore assoluto) se e solo se $b\:c \ge 0$.

<a id="box-exe_abs_triangle_check-7"></a>

!!! esercizio "Esercizio 7"

    Verificare la disuguaglianza triangolare $|b+c| \le |b| + |c|$ e la disuguaglianza triangolare inversa $\big|\,|b| - |c|\,\big| \le |b - c|$ per $b = 5$ e $c = -3$.

??? soluzione "Soluzione"

    Si ha $|b| = 5$ e $|c| = 3$.

    - Disuguaglianza triangolare: $|b+c| = |5-3| = 2 \le 8 = |b| + |c|$.

    - Disuguaglianza triangolare inversa: $\big|\,|b| - |c|\,\big| = |5 - 3| = 2 \le 8 = |5-(-3)| = |b-c|$.

    La disuguaglianza triangolare vale con il segno di disuguaglianza stretta, in accordo con l'Esercizio [Esercizio 6](#box-exe_abs_triangle_equality-6), poiché $b\:c = -15 < 0$.

<a id="box-exe_abs_bound-8"></a>

!!! esercizio "Esercizio 8"

    Sia $x$ un numero reale tale che $|x - 3| \le 1$. Dimostrare che:

    $$
    {\rm a)}~ |x| \le 4, \qquad {\rm b)}~ |x^2 - 9| \le 7
    $$

    e mostrare che la stima in b) non può essere migliorata.

??? soluzione "Soluzione"

    - **a)** Dalla forma $|g| \le |g-h| + |h|$ della disuguaglianza triangolare, con $g = x$ e $h = 3$:

        $$
        |x| \le |x-3| + |3| \le 1 + 3 = 4
        $$

    - **b)** Si ha $x^2 - 9 = (x-3)\:(x+3)$ e quindi $|x^2 - 9| = |x-3| \; |x+3|$. Dalla disuguaglianza triangolare:

        $$
        |x+3| = |(x-3) + 6| \le |x-3| + 6 \le 7
        $$

        e pertanto $|x^2-9| = |x-3|\; |x+3| \le 1 \cdot 7 = 7$.

    La stima non può essere migliorata: per $x=4$ (che soddisfa $|4-3| = 1$) si ha $|16 - 9| = 7$.
