---
title: "Produttorie"
---

# Produttorie

<div class="info-capitolo" markdown>

**Somme e produttorie · Capitolo 2** · dalle dispense di Fabio Furini · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf) · [:material-presentation: Slide (PDF)](../pdf/slide-02-produttorie.pdf)

</div>

## 1. Definizione

<a id="box-def_product-1"></a>

!!! definizione "Definizione 1: produttoria"

    Dati $n$ valori $a_j \in \R$ con $j \in \{1,2,\dots,n\}$, il <strong>prodotto</strong>

    $$
    a_1 \; a_2 \; {\rm \dots} \; a_n
    $$

    può essere indicato in forma compatta con il simbolo di produttoria:

    $$
    \prod_{j=1}^n a_j
    $$

    che si legge: “produttoria per $j$ da $1$ a $n$ di $a_j$”. Il simbolo $j$ è detto <strong>indice di produttoria</strong>.

- Il simbolo di produttoria è quindi molto utile quando i termini $a_j$ sono definiti esplicitamente in funzione dell'indice di produttoria $j$.

<a id="box-ex_products-2"></a>

!!! esempio "Esempio 1: produttorie"

    \begin{align*}
    \prod_{j=1}^{10} \frac{1}{j} &~~=~~ 1 \; \frac{1}{2} \; \frac{1}{3} \; \frac{1}{4} \; \frac{1}{5} \; \frac{1}{6} \; \frac{1}{7} \; \frac{1}{8} \; \frac{1}{9} \; \frac{1}{10} \\[2ex]
     \prod_{j=3}^{n} j^2 &~~=~~ 3^2 \; 4^2 \; 5^2 \; {\rm \dots} \; n^2
    \end{align*}

## 2. Proprietà

<a id="box-obs_prod-constant-term-3"></a>

!!! teorema "Osservazione 1: produttoria di un termine costante"

    Per ogni numero naturale $n\ge 1$ e ogni numero reale $c$, si ha:

    \begin{equation}
    \label{P2}
    \prod_{j=1}^n c  = c^n
    \end{equation}

??? dimostrazione "Dimostrazione"

    Si ha:

    $$
    \underbrace{c\:  \; c  \; {\rm \dots} \; c\:}_{=\prod_{j=1}^n c, {\rm ~~~} c {\rm ~moltiplicato~} n {\rm ~volte}} =  c^n
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_prod-product-constant-4"></a>

!!! teorema "Osservazione 2: prodotto per una costante"

    Per ogni produttoria $\prod_{j=1}^n a_j$ e ogni numero reale $c$, si ha:

    \begin{equation}
    \label{P1}
    \prod_{j=1}^n (c \; a_j) = c^n \: \prod_{j=1}^n a_j
    \end{equation}

??? dimostrazione "Dimostrazione"

    Per le proprietà commutativa e associativa del prodotto, si ha:

    $$
    \underbrace{c\: a_1 \; c\: a_2 \; {\rm \dots} \; c\: a_n}_{=\prod_{j=1}^n (c \; a_j)} = \underbrace{\underbrace{(c\:  \; c  \; {\rm \dots} \; c)\:}_{=\prod_{j=1}^n c, {\rm ~~~} c {\rm ~moltiplicato~} n {\rm ~volte}} \; (a_1 \; a_2 \; {\rm \dots} \; a_n)}_{= c^n \: \prod_{j=1}^n a_j}
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_prod-of-products-5"></a>

!!! teorema "Osservazione 3: prodotto di produttorie"

    Per ogni coppia di produttorie $\prod_{j=1}^n a_j$ e $\prod_{j=1}^n b_j$, si ha:

    \begin{equation}
    \label{P3}
    \prod_{j=1}^n a_j  \; \prod_{j=1}^n b_j = \prod_{j=1}^n (a_j \; b_j)
    \end{equation}

??? dimostrazione "Dimostrazione"

    Si ha:

    $$
    \underbrace{a_1 \;  a_2 \; {\rm \dots} \; a_n \;  b_1 \;  b_2 \; {\rm \dots} \;  b_n}_{=\prod_{j=1}^n a_j  \; \prod_{j=1}^n b_j} = \underbrace{a_1 \; b_1 \; a_2 \;  b_2 \; {\rm \dots} \; a_n \; b_n}_{=\prod_{j=1}^n (a_j \; b_j) }
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-obs_prod-decomposition-6"></a>

!!! teorema "Osservazione 4: scomposizione"

    Per ogni produttoria $\prod_{j=1}^{n+m} a_j$, si ha:

    \begin{align}
    \label{P4}
    \prod_{j=1}^{n+m} a_j   &= \prod_{j=1}^n a_j \; \prod_{j=n+1}^{n+m} a_j
    \end{align}

<a id="box-obs_prod-index-translation-7"></a>

!!! teorema "Osservazione 5: traslazione dell'indice"

    Per ogni produttoria $\prod_{j=1}^{n} a_j$ e ogni numero naturale $m \ge 1$, si ha:

    \begin{align}
    \label{P5}
    \prod_{j=1}^n a_j   &= \prod_{j=1+m}^{n+m} a_{j-m} =  \prod_{j=1-m}^{n-m} a_{j+m}
    \end{align}

<a id="box-obs_prod-index-reflection-8"></a>

!!! teorema "Osservazione 6: riflessione dell'indice"

    Per ogni produttoria $\prod_{j=1}^{n} a_j$, si ha:

    \begin{align}
    \label{P6}
    \prod_{j=1}^n a_j   &= \prod_{j=1}^n a_{n-j+1} = \prod_{j=0}^{n-1} a_{n-j}
    \end{align}

??? dimostrazione "Dimostrazione"

    Le tre proprietà sono semplicemente notazioni diverse e/o riordinamenti dei fattori delle produttorie. <span class="qed">□</span>

## 3. Fattoriale

<a id="box-def_factorial-9"></a>

!!! definizione "Definizione 2: fattoriale"

    Il <strong>fattoriale</strong> di un numero naturale \( n \), indicato con \( n! \), è il prodotto dei primi \( n \) numeri naturali positivi. Per convenzione, il fattoriale di 0 è definito uguale a \( 1 \).

- Formalmente, il fattoriale è definito come segue:

    \begin{equation}
    n! =
    \begin{cases}
    1 & \text{se~~} n = 0, \\[2ex]
    \prod_{j=1}^n j & \text{se~~} n \geq 1.
    \end{cases}
    \end{equation}

- Non è nota una formula chiusa per il fattoriale, ma la formula di Stirling ne fornisce un'approssimazione asintotica.

<a id="box-obs_factorial-ratio-10"></a>

!!! teorema "Osservazione 7"

    Per ogni coppia di numeri naturali $n \ge 0$ e $k \in \{0,1,\dots, n\}$, si ha:

    \begin{equation}
    \label{MM}
    \frac{n!}{(n-k)!}  =  \prod_{j=1}^{k} (n-j+1) =  \prod_{j=n-k+1}^{n} j
    \end{equation}

- La formula \(\eqref{MM}\) è il prodotto di $k$ fattori, a partire da $n$ e decrescendo di un'unità alla volta.

- Per convenzione, una produttoria senza fattori (cioè con indice superiore minore dell'indice inferiore, come $\prod_{j=1}^{0} a_j$) è uguale a $1$. Questa convenzione è coerente con $0!=1$ e rende la formula \(\eqref{MM}\) valida anche per $k=0$ e $k=n$.

??? dimostrazione "Dimostrazione"

    Si ha:

    $$
    \frac{n!}{(n-k)!}
    =
    \frac{\prod_{j=1}^n j}{\prod_{j=1}^{n-k} j}
    =
    \frac{\prod_{j=1}^{n-k} j \; \prod_{j=n-k+1}^{n} j }{\prod_{j=1}^{n-k} j}
    = \prod_{j=n-k+1}^{n} j
    =  \prod_{j=1}^{k} (n-j+1)
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-ex_factorial-ratio-11"></a>

!!! esempio "Esempio 2: uso dell'osservazione"

    $$
    \frac{100!}{98!}= \frac{100!}{(100-2)!}=\prod_{j=1}^{2} (100-j+1)=100 \cdot 99  = 9.900
    $$

!!! interattivo "Provalo nel laboratorio"

    lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi.

<div class="la-tool" data-tool="somme" data-f="k" data-tipo="prod"></div>

## Esercizi e laboratorio

- :material-pencil-box-multiple: **Esercizi** · [il foglio di esercizi di questo capitolo: 9 esercizi con le soluzioni svolte](../esercizi/es-somme-02-produttorie.md)
- :material-calculator-variant: **Laboratorio** · [Somme e produttorie](../laboratorio/somme.md) — scegli «Produttoria Π»: per esempio \(\prod_{k=1}^{n} k = n!\)

