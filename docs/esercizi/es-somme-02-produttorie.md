---
title: "Produttorie"
---

# Produttorie

<div class="info-capitolo" markdown>

**Esercizi · Somme e produttorie** · con le soluzioni svolte · [:material-file-pdf-box: PDF](../pdf/es-somme-02-produttorie.pdf)

</div>

<a id="box-exe_prod_factorials-1"></a>

!!! esercizio "Esercizio 1"

    Calcolare:

    $$
    {\rm a)}~ 5!, \qquad {\rm b)}~ \frac{7!}{5!}, \qquad {\rm c)}~ \frac{10!}{7!}, \qquad {\rm d)}~ \frac{10!}{7!\;3!}
    $$

??? soluzione "Soluzione"

    - **a)** $5! = \prod_{j=1}^{5} j = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120$.

    - **b)** Usando la formula $\frac{n!}{(n-k)!} = \prod_{j=1}^{k} (n-j+1)$ con $n=7$ e $k=2$: $\frac{7!}{5!} = 7 \cdot 6 = 42$.

    - **c)** Con $n=10$ e $k=3$: $\frac{10!}{7!} = 10 \cdot 9 \cdot 8 = 720$.

    - **d)** Da c): $\frac{10!}{7!\;3!} = \frac{720}{3!} = \frac{720}{6} = 120$.

<a id="box-exe_prod_even-2"></a>

!!! esercizio "Esercizio 2"

    Dimostrare che per ogni numero naturale $n \ge 1$ il prodotto dei primi $n$ numeri pari positivi è:

    $$
    \prod_{j=1}^{n} 2\:j = 2^n \; n!
    $$

    e calcolarne il valore per $n=5$.

??? soluzione "Soluzione"

    Usando il prodotto per una costante (con $c=2$ e $a_j = j$) si ha:

    $$
    \prod_{j=1}^{n} 2\:j = 2^n \; \prod_{j=1}^{n} j = 2^n \; n!
    $$

    Per $n=5$: $\prod_{j=1}^{5} 2\:j = 2 \cdot 4 \cdot 6 \cdot 8 \cdot 10 = 2^5 \cdot 5! = 32 \cdot 120 = 3840$.

<a id="box-exe_prod_odd-3"></a>

!!! esercizio "Esercizio 3"

    Dimostrare che per ogni numero naturale $n \ge 1$ il prodotto dei primi $n$ numeri dispari è:

    $$
    \prod_{j=1}^{n} (2\:j-1) = \frac{(2n)!}{2^n \; n!}
    $$

    e calcolarne il valore per $n=4$.

??? soluzione "Soluzione"

    I fattori di $(2n)! = \prod_{j=1}^{2n} j$ sono gli $n$ numeri pari $2, 4, \dots, 2n$ e gli $n$ numeri dispari $1, 3, \dots, 2n-1$. Riordinando i fattori e usando l'Esercizio [Esercizio 2](#box-exe_prod_even-2), si ha:

    $$
    (2n)! = \prod_{j=1}^{n} 2\:j \; \prod_{j=1}^{n} (2\:j-1) = 2^n \; n! \; \prod_{j=1}^{n} (2\:j-1)
    $$

    e quindi

    $$
    \prod_{j=1}^{n} (2\:j-1) = \frac{(2n)!}{2^n \; n!}
    $$

    Per $n=4$: $1 \cdot 3 \cdot 5 \cdot 7 = 105$ e infatti $\frac{8!}{2^4 \cdot 4!} = \frac{40320}{16 \cdot 24} = \frac{40320}{384} = 105$.

<a id="box-exe_prod_telescoping-4"></a>

!!! esercizio "Esercizio 4"

    - **a)** Dimostrare che per ogni successione di numeri reali non nulli $a_1, a_2, \dots, a_{n+1}$ si ha (<strong>prodotto telescopico</strong>):

        $$
        \prod_{j=1}^{n} \frac{a_{j+1}}{a_j} = \frac{a_{n+1}}{a_1}
        $$

    - **b)** Usando a), calcolare $\displaystyle \prod_{j=1}^{n} \frac{j+1}{j}$.

??? soluzione "Soluzione"

    - **a)** Usando il prodotto di produttorie, la traslazione dell'indice e la scomposizione, si ha:

        \begin{align*}
        \prod_{j=1}^{n} \frac{a_{j+1}}{a_j} &= \frac{\prod_{j=1}^{n} a_{j+1}}{\prod_{j=1}^{n} a_j} = \frac{\prod_{j=2}^{n+1} a_{j}}{\prod_{j=1}^{n} a_j}
        = \frac{ \left(\prod_{j=2}^{n} a_{j}\right) \; a_{n+1}}{a_1 \; \prod_{j=2}^{n} a_j} = \frac{a_{n+1}}{a_1}
        \end{align*}

    - **b)** Applicando a) con $a_j = j$:

        $$
        \prod_{j=1}^{n} \frac{j+1}{j} = \frac{n+1}{1} = n+1
        $$

<a id="box-exe_prod_one_minus-5"></a>

!!! esercizio "Esercizio 5"

    Dimostrare che per ogni numero naturale $n \ge 2$ si ha:

    $$
    \prod_{j=2}^{n} \left( 1 - \frac{1}{j^2} \right) = \frac{n+1}{2\:n}
    $$

    e calcolarne il valore per $n=10$.

??? soluzione "Soluzione"

    Poiché

    $$
    1 - \frac{1}{j^2} = \frac{j^2-1}{j^2} = \frac{(j-1)\:(j+1)}{j^2} = \frac{j-1}{j} \; \frac{j+1}{j}
    $$

    per il prodotto di produttorie si ha:

    $$
    \prod_{j=2}^{n} \left( 1 - \frac{1}{j^2} \right) = \prod_{j=2}^{n} \frac{j-1}{j} \; \prod_{j=2}^{n} \frac{j+1}{j}
    $$

    Entrambe le produttorie sono telescopiche (Esercizio [Esercizio 4](#box-exe_prod_telescoping-4), con l'indice che parte da $2$): con $a_j = \frac{1}{j}$ si ha $\frac{a_{j}}{a_{j-1}} = \frac{j-1}{j}$, e con $a_j = j$ si ha $\frac{a_{j+1}}{a_j} = \frac{j+1}{j}$. Quindi:

    $$
    \prod_{j=2}^{n} \frac{j-1}{j} = \frac{1}{2} \cdot \frac{2}{3} \cdots \frac{n-1}{n} = \frac{1}{n}, \qquad \prod_{j=2}^{n} \frac{j+1}{j} = \frac{3}{2} \cdot \frac{4}{3} \cdots \frac{n+1}{n} = \frac{n+1}{2}
    $$

    e pertanto

    $$
    \prod_{j=2}^{n} \left( 1 - \frac{1}{j^2} \right) = \frac{1}{n} \; \frac{n+1}{2} = \frac{n+1}{2\:n}
    $$

    Per $n=10$ si ottiene $\frac{11}{20}$.

<a id="box-exe_prod_index_shift-6"></a>

!!! esercizio "Esercizio 6"

    Usando la traslazione e la riflessione dell'indice, dimostrare che:

    $$
    {\rm a)}~ \prod_{j=3}^{n} (j-2) = (n-2)! \quad (n \ge 3), \qquad {\rm b)}~ \prod_{j=0}^{n-1} (n-j) = n! \quad (n \ge 1)
    $$

    e calcolare la produttoria in a) per $n=8$.

??? soluzione "Soluzione"

    - **a)** Con la traslazione dell'indice di $m=2$ (ponendo $i = j-2$, quando $j$ va da $3$ a $n$, $i$ va da $1$ a $n-2$):

        $$
        \prod_{j=3}^{n} (j-2) = \prod_{i=1}^{n-2} i = (n-2)!
        $$

        Per $n=8$: $\prod_{j=3}^{8} (j-2) = 6! = 720$.

    - **b)** Con la riflessione dell'indice (con $a_j = j$, così che $a_{n-j} = n-j$):

        $$
        \prod_{j=0}^{n-1} (n-j) = \prod_{j=0}^{n-1} a_{n-j} = \prod_{j=1}^{n} a_j = \prod_{j=1}^{n} j = n!
        $$

<a id="box-exe_prod_powers-7"></a>

!!! esercizio "Esercizio 7"

    Dimostrare che per ogni numero naturale $n \ge 1$ si ha:

    $$
    \prod_{j=1}^{n} 2^j = 2^{\frac{n^2+n}{2}}
    $$

    e calcolarne il valore per $n=4$.

??? soluzione "Soluzione"

    Poiché il prodotto di potenze con la stessa base è la potenza con esponente la somma degli esponenti ($2^a \; 2^b = 2^{a+b}$), si ha:

    $$
    \prod_{j=1}^{n} 2^j = 2^1 \; 2^2 \; {\rm \dots} \; 2^n = 2^{1+2+{\rm \dots}+n} = 2^{\sum_{j=1}^{n} j} = 2^{\frac{n^2+n}{2}}
    $$

    Per $n=4$: $2^1 \cdot 2^2 \cdot 2^3 \cdot 2^4 = 2^{10} = 1024$.

<a id="box-exe_prod_bounds-8"></a>

!!! esercizio "Esercizio 8"

    Dimostrare che per ogni numero naturale $n \ge 1$ si ha:

    $$
    2^{n-1} \le n! \le n^n
    $$

??? soluzione "Soluzione"

    Usiamo il fatto che, se $0 \le a_j \le b_j$ per ogni $j \in \{1, \dots, n\}$, allora $\prod_{j=1}^{n} a_j \le \prod_{j=1}^{n} b_j$ (le disuguaglianze tra numeri non negativi si possono moltiplicare membro a membro).

    - Maggiorazione: poiché $j \le n$ per ogni $j \in \{1,\dots,n\}$, usando la produttoria di un termine costante si ha:

        $$
        n! = \prod_{j=1}^{n} j \le \prod_{j=1}^{n} n = n^n
        $$

    - Minorazione: per $n=1$ si ha $2^0 = 1 = 1!$. Per $n \ge 2$, usando la scomposizione e poiché $j \ge 2$ per ogni $j \in \{2,\dots,n\}$, si ha:

        $$
        n! = 1 \cdot \prod_{j=2}^{n} j \ge \prod_{j=2}^{n} 2 = 2^{n-1}
        $$

<a id="box-exe_prod_factorial_simplify-9"></a>

!!! esercizio "Esercizio 9"

    Dimostrare che $(n+1)! = (n+1)\; n!$ per ogni numero naturale $n \ge 0$, e usarlo per semplificare, per $n \ge 1$, l'espressione

    $$
    \frac{(n+1)! - n!}{(n-1)!}
    $$

    Calcolarne poi il valore per $n=6$.

??? soluzione "Soluzione"

    Per $n=0$ si ha $1! = 1 = 1 \cdot 0!$. Per $n \ge 1$, dalla scomposizione:

    $$
    (n+1)! = \prod_{j=1}^{n+1} j = \left(\prod_{j=1}^{n} j\right) \; (n+1) = (n+1) \; n!
    $$

    Quindi, usandolo due volte ($n! = n \; (n-1)!$ vale per $n \ge 1$):

    $$
    \frac{(n+1)! - n!}{(n-1)!} = \frac{(n+1)\; n! - n!}{(n-1)!} = \frac{n \; n!}{(n-1)!} = \frac{n \; n \; (n-1)!}{(n-1)!} = n^2
    $$

    Per $n=6$: $\frac{7! - 6!}{5!} = \frac{5040 - 720}{120} = \frac{4320}{120} = 36 = 6^2$.
