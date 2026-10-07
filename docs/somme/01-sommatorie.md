---
title: "Sommatorie"
---

# Sommatorie

<div class="info-capitolo" markdown>

**Somme e produttorie · Capitolo 1** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/somme-01-sommatorie.pdf)

</div>

## 1. Definizione

<a id="box-def_sum-1"></a>

!!! definizione "Definizione 1: sommatoria"

    Dati $n$ valori $a_j \in \R$ con $j \in \{1,2,\dots,n\}$, la <strong>somma</strong>

    $$
    a_1 + a_2 + {\rm \dots} + a_n
    $$

    può essere indicata in forma compatta con il simbolo di sommatoria:

    $$
    \sum_{j=1}^n a_j
    $$

    che si legge: “sommatoria per $j$ da $1$ a $n$ di $a_j$”. Il simbolo $j$ è detto <strong>indice di sommatoria</strong>.

- Il simbolo di sommatoria è quindi molto utile quando i termini $a_j$ sono definiti esplicitamente in funzione dell'indice di sommatoria $j$.

<a id="box-ex_sums-2"></a>

!!! esempio "Esempio 1: sommatorie"

    \begin{align*}
    \sum_{j=1}^{10} \frac{1}{j} &~~=~~ 1 +\frac{1}{2} +\frac{1}{3} +\frac{1}{4} +\frac{1}{5} +\frac{1}{6} +\frac{1}{7} +\frac{1}{8} +\frac{1}{9} +\frac{1}{10} \\[2ex]
     \sum_{j=3}^{n} j^2 &~~=~~ 3^2 +4^2 +5^2 + {\rm \dots} +n^2
    \end{align*}

- L'indice di sommatoria è un <strong>indice muto</strong>. Ciò significa che, se $j$ viene sostituito con $i$, $k$ o qualsiasi altro indice in tutte le sue occorrenze, il valore della sommatoria non cambia.

<a id="box-ex_dummy-index-3"></a>

!!! esempio "Esempio 2: indice muto"

    Si ha:

    $$
    \sum_{j=1}^n j^2 ~~=~~  \sum_{i=1}^n i^2 ~~=~~   \sum_{k=1}^{n} k^2
    $$

    poiché i simboli indicano tutti la somma dei quadrati dei primi $n$ numeri naturali (zero escluso). Al contrario, si ha:

    $$
    \sum_{j=1}^n j^2 ~~\neq~~   \sum_{j=1}^{m} j^2
    $$

    poiché i due simboli indicano la somma, rispettivamente, dei primi $n$ e dei primi $m$ quadrati dei numeri naturali (zero escluso). Chiaramente, se $n \neq m$, il risultato è diverso.

## 2. Proprietà

<a id="box-obs_sum-constant-term-4"></a>

!!! teorema "Osservazione 1: sommatoria di un termine costante"

    Per ogni numero naturale $n\ge 1$ e ogni numero reale $c$, si ha:

    \begin{equation}
    \label{P2}
    \sum_{j=1}^n c  = n  \; c
    \end{equation}

??? dimostrazione "Dimostrazione"

    Si ha:

    $$
    \underbrace{c\:  + c  + {\rm \dots} + c\:}_{=\sum_{j=1}^n c, {\rm ~~~} c {\rm ~sommato~} n {\rm ~volte}} = n \: c
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_sum-product-constant-5"></a>

!!! teorema "Osservazione 2: prodotto per una costante"

    Per ogni sommatoria $\sum_{j=1}^n a_j$ e ogni numero reale $c$, si ha:

    \begin{equation}
    \label{P1}
    \sum_{j=1}^n (c \; a_j) = c \: \sum_{j=1}^n a_j
    \end{equation}

??? dimostrazione "Dimostrazione"

    Per la proprietà distributiva, si ha:

    $$
    \underbrace{c\: a_1 + c\: a_2 + {\rm \dots} + c\: a_n}_{=\sum_{j=1}^n (c \; a_j)} = \underbrace{c \: (a_1+a_2+{\rm \dots}+a_n)}_{= c \: \sum_{j=1}^n a_j}
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_sum-union-6"></a>

!!! teorema "Osservazione 3: unione di sommatorie"

    Per ogni coppia di sommatorie $\sum_{j=1}^n a_j$ e $\sum_{j=1}^n b_j$, si ha:

    \begin{equation}
    \label{P3}
    \sum_{j=1}^n a_j  + \sum_{j=1}^n b_j = \sum_{j=1}^n (a_j + b_j)
    \end{equation}

??? dimostrazione "Dimostrazione"

    Si ha:

    $$
    \underbrace{a_1 +  a_2 + {\rm \dots} + a_n +  b_1 +  b_2 + {\rm \dots} +  b_n}_{=\sum_{j=1}^n a_j  + \sum_{j=1}^n b_j} = \underbrace{a_1 + b_1 +a_2 + b_2+{\rm \dots}+a_n + b_n}_{=\sum_{j=1}^n (a_j + b_j) }
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_sum-decomposition-7"></a>

!!! teorema "Osservazione 4: scomposizione"

    Per ogni sommatoria $\sum_{j=1}^{n+m} a_j$, si ha:

    \begin{align}
    \label{P4}
    \sum_{j=1}^{n+m} a_j   &= \sum_{j=1}^n a_j + \sum_{j=n+1}^{n+m} a_j
    \end{align}

<a id="box-obs_sum-index-translation-8"></a>

!!! teorema "Osservazione 5: traslazione dell'indice"

    Per ogni sommatoria $\sum_{j=1}^{n} a_j$ e ogni numero naturale $m \ge 1$, si ha:

    \begin{align}
    \label{P5}
    \sum_{j=1}^n a_j   &= \sum_{j=1+m}^{n+m} a_{j-m} =  \sum_{j=1-m}^{n-m} a_{j+m}
    \end{align}

<a id="box-obs_sum-index-reflection-9"></a>

!!! teorema "Osservazione 6: riflessione dell'indice"

    Per ogni sommatoria $\sum_{j=1}^{n} a_j$, si ha:

    \begin{align}
    \label{P6}
    \sum_{j=1}^n a_j   &= \sum_{j=1}^n a_{n-j+1} = \sum_{j=0}^{n-1} a_{n-j}
    \end{align}

??? dimostrazione "Dimostrazione"

    Le tre proprietà sono semplicemente notazioni diverse e/o riordinamenti dei termini delle sommatorie. <span class="qed">□</span>

## 3. Alcune sommatorie importanti

<a id="box-obs_sum-first-n-naturals-10"></a>

!!! teorema "Osservazione 7: somma dei primi $n$ numeri naturali positivi"

    Per ogni numero naturale $n \ge 1$, si ha:

    \begin{equation}
    \sum_{j=1}^n j  = \frac{n^2 +n}{2}
    \end{equation}

??? dimostrazione "Dimostrazione"

    Si ha:

    \begin{align*}
    \sum_{j=1}^n j &= \frac{1}{2} \left( \sum_{j=1}^n j + \sum_{j=1}^n j \right)\\[2ex]
    & = \frac{1}{2} \left( \sum_{j=1}^n j + \sum_{j=1}^n \big( n-j+1 \big) \right)\\[2ex]
     & = \frac{1}{2}  \; \sum_{j=1}^n  \big(j+ n-j+1 \big)\\[2ex]
      &= \frac{1}{2} \; \sum_{j=1}^n  \big(n +1  \big)
      = \frac{n \: (n+1)}{2} = \frac{n^2 +n}{2}
    \end{align*}

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_sum-first-n-even-11"></a>

!!! teorema "Osservazione 8: somma dei primi $n$ numeri pari positivi"

    Per ogni numero naturale $n \ge 1$, si ha:

    \begin{equation}
    \sum_{j=1}^n 2\:j = n^2 + n
    \end{equation}

??? dimostrazione "Dimostrazione"

    Si ha:

    \begin{align*}
    \sum_{j=1}^n 2\:j &= 2\:\sum_{j=1}^n j = 2 \left(\frac{n^2 + n}{2} \right) =  n^2 + n
    \end{align*}

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_sum-first-n-odd-12"></a>

!!! teorema "Osservazione 9: somma dei primi $n$ numeri dispari"

    Per ogni numero naturale $n \ge 1$, si ha:

    $$
    \sum_{j=0}^{n-1} (2\:j+1) = n^2 \quad {\rm ~~o~~~equivalentemente~~} \quad \sum_{j=1}^n (2\:j-1) = n^2
    $$

??? dimostrazione "Dimostrazione"

    Si ha:

    \begin{align*}
    \sum_{j=0}^{n-1} (2\: j+1) &= 2\:\sum_{j=0}^{n-1} j + {\sum_{j=0}^{n-1} 1} = 2\:\sum_{j=1}^{n} (j-1) + {\sum_{j=1}^{n} 1}\\[2ex]
     &  = 2\:\left(\sum_{j=1}^n j - \sum_{j=1}^n 1 \right)+ n \\[2ex]
        & = 2\:\left( \frac{n^2 + n}{2} - n \right)+ n
         =  n^2 + n - 2\:n + n
         =  n^2 \\[5ex]
          \sum_{j=1}^n (2\:j-1) &= 2\:\sum_{j=1}^n j - {\sum_{j=1}^n 1}\\[2ex]
        & = 2\:\left( \frac{n^2 + n}{2}  \right)- n
         =  n^2 + n -n
         =  n^2
    \end{align*}

    <p class="qed-riga"><span class="qed">□</span></p>

!!! interattivo "Provalo nel laboratorio"

    lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi.

<div class="la-tool" data-tool="somme" data-f="k^2" data-tipo="sum"></div>

