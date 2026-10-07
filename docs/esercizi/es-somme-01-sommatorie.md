---
title: "Sommatorie"
---

# Sommatorie

<div class="info-capitolo" markdown>

**Esercizi · Somme e produttorie** · con le soluzioni svolte · [:material-file-pdf-box: PDF](../pdf/es-somme-01-sommatorie.pdf)

</div>

<a id="box-exe_sum_squares_proof-1"></a>

!!! esercizio "Esercizio 1"

    Dimostrare, usando le proprietà delle sommatorie, che per ogni numero naturale $n \ge 1$ si ha:

    \begin{equation}
    \label{EXSQ}
    \sum_{k=1}^{n} k^2 = \underbrace{\frac{2\;n^3 + 3\;n^2 + n}{6}}_{
    =\frac{n\:(n+1)\:(2\:n+1)}{6}}
    \end{equation}

    (somma dei quadrati dei primi $n$ numeri naturali, zero escluso).

??? soluzione "Soluzione"

    Cominciamo scrivendo $\sum_{k=0}^n (k+1)^3$ in due modi diversi:

    \begin{align*}
    1)~~~\sum_{k=0}^n (k+1)^3 &=\sum_{k=0}^n(k^3+3\:k^2+3\:k+1)\\[2ex]
    &= \left( \sum_{k=1}^n k^3 + 3\: \sum_{k=1}^n k^2 + 3\: \sum_{k=1}^n k + \sum_{k=1}^n 1 \right)  +1 \\[2ex]
    &=\sum_{k=1}^n k^3 + 3\: \sum_{k=1}^n k^2 + \frac{3\;(n^2+n)}{2} +n +1\\[5ex]
    2)~~~ \sum_{k=0}^n (k+1)^3&=\sum_{k=1}^{n+1} k^3=\sum_{k=1}^n k^3 + (n+1)^3
    \end{align*}

    (in 1) il termine con $k=0$, uguale a $1$, è stato separato dagli altri). Uguagliando le due espressioni e semplificando la sommatoria con $k^3$ otteniamo:

    $$
    3\: \sum_{k=1}^n k^2 + \frac{3\:(n^2+n)}{2} +n +1=   (n+1)^3
    $$

    Isolando la sommatoria con $k^2$ otteniamo:

    \begin{align*}
    3\: \sum_{k=1}^n k^2 &= (n+1)^3 - \frac{3\:(n^2+n)}{2} -n -1 \\[2ex]
     &= n^3 + 3n^2 +3n+1 - \frac{3n^2+3n}{2} -n -1\\[2ex]
       &= \frac{2n^3 + 3n^2 + n}{2}
    \end{align*}

    Quindi si ha:

    \begin{align*}
    \sum_{k=1}^n k^2 &= \frac{2n^3 + 3n^2 + n}{6}
    \end{align*}

<a id="box-exe_sum_squares_numbers-2"></a>

!!! esercizio "Esercizio 2"

    Calcolare la somma dei quadrati dei primi $10$, $100$ e $1000$ numeri naturali (zero escluso).

??? soluzione "Soluzione"

    Usando la formula \(\eqref{EXSQ}\), la somma dei quadrati dei primi 10 numeri naturali (zero escluso) è:

    $$
    \sum_{k=1}^{10} k^2  = \frac{2\cdot 10^3 + 3\cdot 10^2 + 10}{6} = 385
    $$

    La somma dei quadrati dei primi 100 numeri naturali (zero escluso) è:

    $$
    \sum_{k=1}^{100} k^2  = \frac{2\cdot 100^3 + 3\cdot 100^2 + 100}{6} = 338.350
    $$

    La somma dei quadrati dei primi 1000 numeri naturali (zero escluso) è:

    $$
    \sum_{k=1}^{1000} k^2  = \frac{2\cdot 1000^3 + 3\cdot 1000^2 + 1000}{6} = 333.833.500
    $$

<a id="box-exe_sum_cubes_proof-3"></a>

!!! esercizio "Esercizio 3"

    Dimostrare, usando le proprietà delle sommatorie, che per ogni numero naturale $n \ge 1$ si ha:

    \begin{equation}
    \label{EXCU}
    \sum_{k=1}^{n} k^3 = \underbrace{\frac{n^4 + 2\;n^3 + n^2}{4}}_{
    =\frac{n^2\:(n+1)^2}{4}=\frac{(n^2+n)^2}{4}}
    \end{equation}

    (somma dei cubi dei primi $n$ numeri naturali, zero escluso).

??? soluzione "Soluzione"

    Cominciamo scrivendo $\sum_{k=0}^n (k+1)^4$ in due modi diversi, usando la formula \(\eqref{EXSQ}\) per la somma dei quadrati:

    \begin{align*}
    1)~~~\sum_{k=0}^n (k+1)^4 &=\sum_{k=0}^n(k^4+4\:k^3+6\:k^2+4\:k+1)\\[2ex]
    &= \left( \sum_{k=1}^n k^4 + 4\: \sum_{k=1}^n k^3 + 6\: \sum_{k=1}^n k^2 + 4\: \sum_{k=1}^n k + \sum_{k=1}^n 1 \right) +1 \\[2ex]
    &=\sum_{k=1}^n k^4 + 4\: \sum_{k=1}^n k^3 + 2n^3 + 3n^2 + n + 2\:n^2 +2\:n +n +1\\[2ex]
    &=\sum_{k=1}^n k^4 + 4\: \sum_{k=1}^n k^3 + 2n^3 + 5n^2 +4n +1\\[2ex]
    2)~~~  \sum_{k=0}^n (k+1)^4&=\sum_{k=1}^{n+1} k^4=\sum_{k=1}^n k^4 + (n+1)^4
    \end{align*}

    Uguagliando le due espressioni e semplificando la sommatoria con $k^4$ otteniamo:

    $$
    4\: \sum_{k=1}^n k^3 +
    2n^3 + 5 n^2 +4n +1  =   (n+1)^4
    $$

    Isolando la sommatoria con $k^3$ otteniamo:

    \begin{align*}
    4\: \sum_{k=1}^n k^3 &= n^4 + 4n^3 +6n^2 + 4n +1  -
    2n^3 - 5 n^2 -4n -1 =  n^4 + 2n^3 +  n^2
    \end{align*}

    Quindi si ha:

    \begin{align*}
    \sum_{k=1}^n k^3 & = \frac{n^4 + 2n^3 +  n^2}{4}
    \end{align*}

<a id="box-exe_sum_cubes_numbers-4"></a>

!!! esercizio "Esercizio 4"

    Calcolare la somma dei cubi dei primi $10$, $100$ e $1000$ numeri naturali (zero escluso).

??? soluzione "Soluzione"

    Usando la formula \(\eqref{EXCU}\), la somma dei cubi dei primi 10 numeri naturali (zero escluso) è:

    $$
    \sum_{k=1}^{10} k^3  =  \frac{ 10^4 + 2 \cdot 10^3 + 10^2}{4} = 3025
    $$

    La somma dei cubi dei primi 100 numeri naturali (zero escluso) è:

    $$
    \sum_{k=1}^{100} k^3  =  \frac{ 100^4 + 2 \cdot 100^3 + 100^2}{4} = 25.502.500
    $$

    La somma dei cubi dei primi 1000 numeri naturali (zero escluso) è:

    $$
    \sum_{k=1}^{1000} k^3  =  \frac{ 1000^4 + 2 \cdot 1000^3 + 1000^2}{4} = 250.500.250.000
    $$

<a id="box-exe_sum_cubes_square-5"></a>

!!! esercizio "Esercizio 5"

    Dimostrare che la somma dei cubi dei primi $n$ numeri naturali (zero escluso) è uguale al quadrato della somma dei primi $n$ numeri naturali (zero escluso):

    $$
    \sum_{k=1}^{n} k^3 = \left(\sum_{k=1}^{n} k \right)^2
    $$

??? soluzione "Soluzione"

    Usando la formula \(\eqref{EXCU}\) e la formula $\sum_{k=1}^{n} k = \frac{n\:(n+1)}{2}$, si ha:

    $$
    \sum_{k=1}^{n} k^3 = 	\frac{n^4 + 2n^3 +  n^2}{4}  = 	\frac{n^2 \; (n^2 + 2n +  1)}{4}  = \frac{n^2\:(n+1)^2}{4}= \left(\frac{n\:(n+1)}{2}\right)^2= \left(\sum_{k=1}^{n} k \right)^2
    $$

<a id="box-exe_sum_index_shift-6"></a>

!!! esercizio "Esercizio 6"

    Usando la traslazione dell'indice, riscrivere le seguenti sommatorie in modo che l'indice di sommatoria parta da $1$, e calcolarle:

    $$
    {\rm a)}~ \sum_{j=3}^{12} (j-2)^2, \qquad {\rm b)}~ \sum_{j=0}^{n-1} (j+1), \qquad {\rm c)}~ \sum_{j=0}^{49} (2\:j+1)
    $$

??? soluzione "Soluzione"

    - **a)** Con la traslazione dell'indice di $m=2$ (ponendo $i=j-2$, quando $j$ va da $3$ a $12$, $i$ va da $1$ a $10$) e la formula \(\eqref{EXSQ}\):

        $$
        \sum_{j=3}^{12} (j-2)^2 = \sum_{i=1}^{10} i^2 = \frac{2\cdot 10^3 + 3 \cdot 10^2 + 10}{6} = 385
        $$

    - **b)** Con la traslazione dell'indice di $m=1$ (ponendo $i=j+1$):

        $$
        \sum_{j=0}^{n-1} (j+1) = \sum_{i=1}^{n} i = \frac{n^2+n}{2}
        $$

    - **c)** Con la traslazione dell'indice di $m=1$ (ponendo $i=j+1$, così che $2\:j+1 = 2\:i-1$), si tratta della somma dei primi $50$ numeri dispari:

        $$
        \sum_{j=0}^{49} (2\:j+1) = \sum_{i=1}^{50} (2\:i-1) = 50^2 = 2500
        $$

<a id="box-exe_sum_linearity-7"></a>

!!! esercizio "Esercizio 7"

    Trovare una formula chiusa per la sommatoria

    $$
    \sum_{j=1}^{n} \big(3\:j^2 - 2\:j + 5\big)
    $$

    e usarla per calcolarne il valore per $n=10$.

??? soluzione "Soluzione"

    Usando l'unione di sommatorie, il prodotto per una costante e la sommatoria di un termine costante, si ha:

    \begin{align*}
    \sum_{j=1}^{n} \big(3\:j^2 - 2\:j + 5\big) &= 3\: \sum_{j=1}^{n} j^2 - 2\: \sum_{j=1}^{n} j + \sum_{j=1}^{n} 5 \\[2ex]
    &= 3 \: \frac{2n^3 + 3n^2 + n}{6} - 2\: \frac{n^2+n}{2} + 5\:n \\[2ex]
    &= n^3 + \frac{3}{2}\: n^2 + \frac{1}{2}\: n - n^2 - n + 5\:n
    = \frac{2n^3 + n^2 + 9n}{2}
    \end{align*}

    Per $n=10$ si ottiene:

    $$
    \sum_{j=1}^{10} \big(3\:j^2 - 2\:j + 5\big) = \frac{2000 + 100 + 90}{2} = 1095
    $$

    Verifica: $3 \cdot 385 - 2 \cdot 55 + 5 \cdot 10 = 1155 - 110 + 50 = 1095$.

<a id="box-exe_sum_decomposition-8"></a>

!!! esercizio "Esercizio 8"

    Usando la proprietà di scomposizione, calcolare:

    $$
    {\rm a)}~ \sum_{j=11}^{20} j^2, \qquad {\rm b)}~ \sum_{j=n+1}^{2n} j \quad (n \ge 1)
    $$

??? soluzione "Soluzione"

    - **a)** Dalla scomposizione $\sum_{j=1}^{20} j^2 = \sum_{j=1}^{10} j^2 + \sum_{j=11}^{20} j^2$ e dalla formula \(\eqref{EXSQ}\):

        $$
        \sum_{j=11}^{20} j^2 = \sum_{j=1}^{20} j^2 - \sum_{j=1}^{10} j^2 = \frac{2\cdot 20^3 + 3 \cdot 20^2 + 20}{6} - 385 = 2870 - 385 = 2485
        $$

    - **b)** Dalla scomposizione $\sum_{j=1}^{2n} j = \sum_{j=1}^{n} j + \sum_{j=n+1}^{2n} j$:

        $$
        \sum_{j=n+1}^{2n} j = \frac{(2n)^2 + 2n}{2} - \frac{n^2+n}{2} = \frac{4n^2 + 2n - n^2 - n}{2} = \frac{3n^2+n}{2}
        $$

<a id="box-exe_sum_telescoping-9"></a>

!!! esercizio "Esercizio 9"

    - **a)** Dimostrare che per ogni successione di numeri reali $a_1, a_2, \dots, a_{n+1}$ si ha (<strong>somma telescopica</strong>):

        $$
        \sum_{j=1}^{n} \big( a_{j+1} - a_j \big) = a_{n+1} - a_1
        $$

    - **b)** Usando a), calcolare $\displaystyle \sum_{j=1}^{n} \frac{1}{j\:(j+1)}$ e il suo valore per $n=99$.

??? soluzione "Soluzione"

    - **a)** Usando l'unione di sommatorie, la traslazione dell'indice e la scomposizione, si ha:

        \begin{align*}
        \sum_{j=1}^{n} \big( a_{j+1} - a_j \big) &= \sum_{j=1}^{n} a_{j+1} - \sum_{j=1}^{n} a_j = \sum_{j=2}^{n+1} a_{j} - \sum_{j=1}^{n} a_j\\[2ex]
        &= \left(\sum_{j=2}^{n} a_{j} + a_{n+1}\right) - \left( a_1 + \sum_{j=2}^{n} a_j \right) = a_{n+1} - a_1
        \end{align*}

    - **b)** Poiché

        $$
        \frac{1}{j\:(j+1)} = \frac{(j+1) - j}{j\:(j+1)} = \frac{1}{j} - \frac{1}{j+1}
        $$

        possiamo applicare a) con $a_j = -\frac{1}{j}$:

        $$
        \sum_{j=1}^{n} \frac{1}{j\:(j+1)} = \sum_{j=1}^{n} \left( -\frac{1}{j+1} - \Big(-\frac{1}{j}\Big)\right) = -\frac{1}{n+1} + 1 = \frac{n}{n+1}
        $$

        Per $n=99$ si ottiene $\frac{99}{100}$.

<a id="box-exe_sum_telescoping_naturals-10"></a>

!!! esercizio "Esercizio 10"

    Calcolare $\displaystyle \sum_{j=1}^{n} \big( (j+1)^2 - j^2 \big)$ in due modi diversi e ricavare nuovamente la formula

    $$
    \sum_{j=1}^n j = \frac{n^2+n}{2}
    $$

??? soluzione "Soluzione"

    Primo modo: si tratta di una somma telescopica (Esercizio [Esercizio 9](#box-exe_sum_telescoping-9)) con $a_j = j^2$, quindi:

    $$
    \sum_{j=1}^{n} \big( (j+1)^2 - j^2 \big) = (n+1)^2 - 1 = n^2 + 2\:n
    $$

    Secondo modo: poiché $(j+1)^2 - j^2 = 2\:j + 1$, si ha:

    $$
    \sum_{j=1}^{n} \big( (j+1)^2 - j^2 \big) = \sum_{j=1}^{n} (2\:j+1) = 2 \: \sum_{j=1}^{n} j + n
    $$

    Uguagliando le due espressioni:

    $$
    2 \: \sum_{j=1}^{n} j + n = n^2 + 2\:n \text{~~~~cioè~~~~} \sum_{j=1}^{n} j = \frac{n^2 + n}{2}
    $$

<a id="box-exe_sum_double-11"></a>

!!! esercizio "Esercizio 11"

    Una <strong>sommatoria doppia</strong> $\sum_{i=1}^{n} \sum_{j=1}^{m} a_{ij}$ è la sommatoria per $i$ da $1$ a $n$ delle sommatorie interne $\sum_{j=1}^{m} a_{ij}$. Calcolare, per ogni coppia di numeri naturali $n,m \ge 1$:

    $$
    {\rm a)}~ \sum_{i=1}^{n} \sum_{j=1}^{m} (i+j), \qquad {\rm b)}~ \sum_{i=1}^{n} \sum_{j=1}^{n} i\:j
    $$

    e il valore di a) per $n=3$ e $m=4$.

??? soluzione "Soluzione"

    - **a)** Per la sommatoria interna ($i$ è costante rispetto a $j$):

        $$
        \sum_{j=1}^{m} (i+j) = \sum_{j=1}^{m} i + \sum_{j=1}^{m} j = m\: i + \frac{m^2+m}{2}
        $$

        quindi

        \begin{align*}
        \sum_{i=1}^{n} \sum_{j=1}^{m} (i+j) &= \sum_{i=1}^{n} \left( m\: i + \frac{m^2+m}{2}\right) = m \: \frac{n^2+n}{2} + n \: \frac{m^2+m}{2} \\[2ex]
        &= \frac{n\:m\:(n+1) + n\:m\:(m+1)}{2} = \frac{n\:m\:(n+m+2)}{2}
        \end{align*}

        Per $n=3$ e $m=4$ si ottiene $\frac{3 \cdot 4 \cdot 9}{2} = 54$.

    - **b)** Usando due volte il prodotto per una costante:

        $$
        \sum_{i=1}^{n} \sum_{j=1}^{n} i\:j = \sum_{i=1}^{n} \left( i \: \sum_{j=1}^{n} j \right) = \left(\sum_{j=1}^{n} j \right) \: \sum_{i=1}^{n} i = \left( \frac{n^2+n}{2} \right)^2
        $$

<a id="box-exe_sum_double_dependent-12"></a>

!!! esercizio "Esercizio 12"

    Calcolare, per ogni numero naturale $n \ge 1$, le seguenti sommatorie doppie, in cui l'indice superiore della sommatoria interna dipende da $i$:

    $$
    {\rm a)}~ \sum_{i=1}^{n} \sum_{j=1}^{i} 1, \qquad {\rm b)}~ \sum_{i=1}^{n} \sum_{j=1}^{i} j
    $$

    e il valore di b) per $n=10$.

??? soluzione "Soluzione"

    - **a)** Poiché $\sum_{j=1}^{i} 1 = i$, si ha:

        $$
        \sum_{i=1}^{n} \sum_{j=1}^{i} 1 = \sum_{i=1}^{n} i = \frac{n^2+n}{2}
        $$

    - **b)** Poiché $\sum_{j=1}^{i} j = \frac{i^2+i}{2}$, usando la formula \(\eqref{EXSQ}\) si ha:

        \begin{align*}
        \sum_{i=1}^{n} \sum_{j=1}^{i} j &= \sum_{i=1}^{n} \frac{i^2+i}{2} = \frac{1}{2} \left( \sum_{i=1}^{n} i^2 + \sum_{i=1}^{n} i \right) = \frac{1}{2} \left( \frac{2n^3 + 3n^2 + n}{6} + \frac{n^2+n}{2} \right) \\[2ex]
        &= \frac{2n^3 + 6n^2 + 4n}{12} = \frac{n\:(n+1)\:(n+2)}{6}
        \end{align*}

        Per $n=10$ si ottiene $\frac{10 \cdot 11 \cdot 12}{6} = 220$.
