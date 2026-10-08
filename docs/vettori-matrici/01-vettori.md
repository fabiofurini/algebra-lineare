---
title: "Vettori"
---

# Vettori

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 3** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/vettori-matrici-01-vettori.pdf)

</div>

## 1. Definizione e trasposto

<a id="box-defVector-1"></a>

!!! definizione "Definizione 1: Vettore"

    Un <strong>vettore</strong> è una colonna di numeri reali con \(n\) righe.

Dato un vettore \(\boldsymbol{a}\in\R^{n}\), scriviamo:

$$
\boldsymbol{a}=
\begin{pmatrix}
[\boldsymbol a]_{1}\\
[\boldsymbol a]_{2}\\
\vdots \\
[\boldsymbol a]_{n}
\end{pmatrix}
\qquad 
\text{oppure, per brevità,}
\qquad
\boldsymbol{a}=
\begin{pmatrix}
a_{1}\\
a_{2}\\
\vdots \\
a_{n}
\end{pmatrix}.
$$

- L'intero \(n\) è la <strong>dimensione</strong> del vettore (il numero di righe).

- La quantità \([\boldsymbol a]_i\) (o \(a_i\)) denota l'<strong>\(i\)-esimo elemento</strong> (o <strong>\(i\)-esima componente</strong>) di \(\boldsymbol{a}\), per \(i\in\{1,2,\dots,n\}\).

<a id="box-exVector-2"></a>

!!! esempio "Esempio 1: Vettore"

    Il vettore

    $$
    \boldsymbol a = 
    \begin{pmatrix}
    2 \\
    -5 \\
    3 \\
    1
    \end{pmatrix}
    \in \R^{4}
    $$

    è un vettore colonna con \(n=4\) righe, dove \(a_1 = 2\), \(a_2 = -5\), \(a_3 = 3\) e \(a_4 = 1\).

<a id="box-defTransposeVector-3"></a>

!!! definizione "Definizione 2: Trasposto di un vettore"

    Dato un vettore colonna \(\boldsymbol a \in \R^{n}\), il <strong>trasposto</strong> di \(\boldsymbol a\), denotato con \(\boldsymbol a'\), è il vettore riga:

    \begin{equation}
    \boldsymbol a' = 
    \begin{pmatrix}
    a_1 & a_2 & \dots & a_n
    \end{pmatrix}
    \in \R^{1 \times n}.
    \end{equation}

<a id="box-exTransposeVector-4"></a>

!!! esempio "Esempio 2: Trasposto di un vettore"

    Dato il vettore colonna

    $$
    \boldsymbol a = 
    \begin{pmatrix}
    2 \\
    -5 \\
    3 \\
    1
    \end{pmatrix}
    \in \R^{4},
    $$

    il suo trasposto è il vettore riga

    $$
    \boldsymbol a' = 
    \begin{pmatrix}
    2 & -5 & 3 & 1
    \end{pmatrix}
    \in \R^{1 \times 4}.
    $$

## 2. Somma di vettori e prodotto per uno scalare

!!! chiave ""

    Dati due vettori colonna

    $$
    \underbrace{
    \begin{pmatrix}
    p_1 \\
    p_2 \\
    \vdots \\
    p_n
    \end{pmatrix}
    }_{\boldsymbol p} \in \R^{n}
    \quad \text{e} \quad 
    \underbrace{
    \begin{pmatrix}
    w_1 \\
    w_2 \\
    \vdots \\
    w_n
    \end{pmatrix}
    }_{\boldsymbol w} \in \R^{n}
    $$

    la loro <strong>somma</strong> è il vettore

    \begin{equation}
    \boldsymbol p + \boldsymbol w
    =
    \begin{pmatrix}
    p_1+w_1\\
    p_2+w_2\\
    \vdots\\
    p_n+w_n
    \end{pmatrix}
    \in \R^{n}
    \label{vecSUM}
    \end{equation}

!!! chiave ""

    Dati uno scalare \(\lambda\in\R\) e un vettore colonna

    $$
    \underbrace{
    \begin{pmatrix}
    p_1 \\
    p_2 \\
    \vdots \\
    p_n
    \end{pmatrix}
    }_{\boldsymbol p} \in \R^{n}
    $$

    il <strong>prodotto</strong> di \(\boldsymbol p\) <strong>per lo scalare</strong> \(\lambda\) è il vettore

    \begin{equation}
    \lambda \boldsymbol p
    =
    \begin{pmatrix}
    \lambda p_1\\
    \lambda p_2\\
    \vdots\\
    \lambda p_n
    \end{pmatrix}
    \in \R^{n}
    \label{vecScalPROD}
    \end{equation}

<a id="box-exSumScalarVector-5"></a>

!!! esempio "Esempio 3: Somma di vettori e prodotto per uno scalare"

    Consideriamo i seguenti due vettori e uno scalare:

    $$
    \boldsymbol p=\begin{pmatrix}1\\4\end{pmatrix}\in\R^2,
    \qquad
    \boldsymbol w=\begin{pmatrix}4\\1\end{pmatrix}\in\R^2,
    \qquad
    \lambda=2.
    $$

    Allora:

    $$
    \boldsymbol p+\boldsymbol w
    =
    \begin{pmatrix}
    1+4\\
    4+1
    \end{pmatrix}
    =
    \begin{pmatrix}
    5\\
    5
    \end{pmatrix},
    \qquad
    \lambda \boldsymbol p
    =
    2\begin{pmatrix}1\\4\end{pmatrix}
    =
    \begin{pmatrix}
    2\\
    8
    \end{pmatrix}.
    $$

### 2.1 Proprietà

!!! chiave ""

    Le proprietà della somma di vettori e del prodotto per uno scalare sono:

    \begin{equation}
    \boldsymbol p + \boldsymbol w = \boldsymbol w + \boldsymbol p,
    \quad \forall \boldsymbol p, \boldsymbol w \in \R^{n}
    \label{vecsum_1}
    \end{equation}

    \begin{equation}
    (\boldsymbol p + \boldsymbol w) + \boldsymbol u = \boldsymbol p + (\boldsymbol w + \boldsymbol u),
    \quad \forall \boldsymbol p, \boldsymbol w, \boldsymbol u \in \R^{n}
    \label{vecsum_2}
    \end{equation}

    \begin{equation}
    \lambda (\boldsymbol p + \boldsymbol w) = \lambda \boldsymbol p + \lambda \boldsymbol w,
    \quad \forall \lambda \in \R,\; \boldsymbol p, \boldsymbol w \in \R^{n}
    \label{vecsum_3}
    \end{equation}

    \begin{equation}
    (\lambda+\mu)\boldsymbol p = \lambda \boldsymbol p + \mu \boldsymbol p,
    \quad \forall \lambda,\mu \in \R,\; \boldsymbol p \in \R^{n}
    \label{vecsum_4}
    \end{equation}

    \begin{equation}
    \lambda(\mu \boldsymbol p) = (\lambda\mu)\boldsymbol p,
    \quad \forall \lambda,\mu \in \R,\; \boldsymbol p \in \R^{n}
    \label{vecsum_5}
    \end{equation}

    \begin{equation}
    1\cdot \boldsymbol p = \boldsymbol p,
    \quad \forall \boldsymbol p \in \R^{n}.
    \label{vecsum_6}
    \end{equation}

## 3. Prodotto scalare

!!! chiave ""

    Dati due vettori colonna

    $$
    \underbrace{
    \begin{pmatrix}
    p_1 \\
    p_2 \\
    \vdots \\
    p_n
    \end{pmatrix}
    }_{\boldsymbol p} \in \R^{n}
    \quad \text{e} \quad 
    \underbrace{
    \begin{pmatrix}
    w_1 \\
    w_2 \\
    \vdots \\
    w_n
    \end{pmatrix}
    }_{\boldsymbol w} \in \R^{n}
    $$

    l'espressione

    \begin{equation}
    \boldsymbol p' \, \boldsymbol w = \sum_{j=1}^n p_j w_j
    \end{equation}

    è detta <strong>prodotto scalare</strong> di \( \boldsymbol p \) e \( \boldsymbol w \).

<a id="box-exScalarProduct-6"></a>

!!! esempio "Esempio 4: Prodotto scalare"

    Consideriamo i due vettori \(\begin{pmatrix} 1 \\ 4 \end{pmatrix}\in\R^2\) e \(\begin{pmatrix} 4 \\ 1 \end{pmatrix}\in\R^2\). Il loro prodotto scalare è:

    $$
    \begin{pmatrix} 1 & 4 \end{pmatrix}\,\begin{pmatrix} 4 \\ 1 \end{pmatrix}
    = 1 \cdot 4 + 4 \cdot 1 = 4 + 4 = 8.
    $$

### 3.1 Proprietà

!!! chiave ""

    Le proprietà del prodotto scalare sono:

    \begin{equation}
    \boldsymbol p' \, \boldsymbol w = \boldsymbol w' \, \boldsymbol p, 
    \quad \forall \boldsymbol p, \boldsymbol w \in \R^{n}
    \label{scalar_1}
    \end{equation}

    \begin{equation}
    \boldsymbol p' \, (\boldsymbol w + \boldsymbol u) = \boldsymbol p' \, \boldsymbol w + \boldsymbol p' \, \boldsymbol u, 
    \quad \forall \boldsymbol p, \boldsymbol w, \boldsymbol u \in \R^{n}
    \label{scalar_2}
    \end{equation}

    \begin{equation}
    \lambda \, (\boldsymbol p' \, \boldsymbol w) = (\lambda \, \boldsymbol p)' \, \boldsymbol w, 
    \quad \forall \lambda \in \R,\; \boldsymbol p, \boldsymbol w \in \R^{n}
    \label{scalar_3}
    \end{equation}

    Dalla definizione si ha:

    \begin{equation}
    \boldsymbol p' \, \boldsymbol p \ge 0, 
    \quad \forall \boldsymbol p \in \R^{n} 
    \quad \text{e} \quad 
    \boldsymbol p' \, \boldsymbol p = 0 \Longleftrightarrow \boldsymbol p = \boldsymbol 0
    \label{scalar_4_bis}
    \end{equation}

## 4. Combinazioni lineari e indipendenza lineare

<a id="box-defLinearCombination-7"></a>

!!! definizione "Definizione 3: Combinazione lineare"

    Dati \(k\) vettori \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\in\R^{n}\) e \(k\) scalari \(\lambda_1,\lambda_2,\dots,\lambda_k\in\R\), il vettore

    \begin{equation}
    \lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2+\dots+\lambda_k\boldsymbol v_k=\sum_{i=1}^{k}\lambda_i\boldsymbol v_i\in\R^{n}
    \label{vecLinComb}
    \end{equation}

    è detto <strong>combinazione lineare</strong> di \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\) con <strong>coefficienti</strong> \(\lambda_1,\lambda_2,\dots,\lambda_k\).

- Denotiamo con \(\boldsymbol 0\in\R^{n}\) il <strong>vettore nullo</strong>, cioè il vettore i cui elementi sono tutti uguali a \(0\).

- Scegliendo \(\lambda_1=\lambda_2=\dots=\lambda_k=0\) si ottiene sempre \(\boldsymbol 0\): questa è detta combinazione lineare <strong>banale</strong>.

<a id="box-exLinearCombination-8"></a>

!!! esempio "Esempio 5: Combinazione lineare"

    Consideriamo i vettori

    $$
    \boldsymbol v_1=\begin{pmatrix}1\\2\\0\end{pmatrix},
    \qquad
    \boldsymbol v_2=\begin{pmatrix}0\\1\\-1\end{pmatrix}\in\R^{3},
    $$

    e i coefficienti \(\lambda_1=2\) e \(\lambda_2=-3\). La corrispondente combinazione lineare è

    $$
    2\boldsymbol v_1-3\boldsymbol v_2
    =
    \begin{pmatrix}2\\4\\0\end{pmatrix}
    +
    \begin{pmatrix}0\\-3\\3\end{pmatrix}
    =
    \begin{pmatrix}2\\1\\3\end{pmatrix}.
    $$

<a id="box-defLinIndependence-9"></a>

!!! definizione "Definizione 4: Vettori linearmente indipendenti"

    The vectors \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\in\R^{n}\) sono <strong>linearmente indipendenti</strong> se l'unica combinazione lineare uguale al vettore nullo è quella banale, cioè

    \begin{equation}
    \lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2+\dots+\lambda_k\boldsymbol v_k=\boldsymbol 0
    \quad\Longrightarrow\quad
    \lambda_1=\lambda_2=\dots=\lambda_k=0.
    \label{vecLinIndep}
    \end{equation}

    Altrimenti, cioè se esistono coefficienti \(\lambda_1,\lambda_2,\dots,\lambda_k\), <strong>non tutti nulli</strong>, tali che \(\lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2+\dots+\lambda_k\boldsymbol v_k=\boldsymbol 0\), i vettori sono <strong>linearmente dipendenti</strong>.

<a id="box-exLinIndepR2-10"></a>

!!! esempio "Esempio 6: Vettori linearmente indipendenti in \(\R^2\)"

    Consideriamo i vettori \( \boldsymbol v_1=\begin{pmatrix}1\\2\end{pmatrix} \) e \( \boldsymbol v_2=\begin{pmatrix}3\\1\end{pmatrix}\in\R^{2}. \) La condizione \(\lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2=\boldsymbol 0\) si scrive

    $$
    \begin{cases}
    \lambda_1+3\lambda_2=0\\
    2\lambda_1+\lambda_2=0
    \end{cases}
    $$

    Dalla prima equazione \(\lambda_1=-3\lambda_2\); sostituendo nella seconda si ottiene \(-6\lambda_2+\lambda_2=-5\lambda_2=0\), quindi \(\lambda_2=0\) e \(\lambda_1=0\). Pertanto, \(\boldsymbol v_1\) e \(\boldsymbol v_2\) sono linearmente indipendenti.

<a id="box-exLinDepR2-11"></a>

!!! esempio "Esempio 7: Vettori linearmente dipendenti in \(\R^2\)"

    Consideriamo i vettori

    $$
    \boldsymbol v_1=\begin{pmatrix}1\\2\end{pmatrix},
    \qquad
    \boldsymbol v_2=\begin{pmatrix}3\\1\end{pmatrix},
    \qquad
    \boldsymbol v_3=\begin{pmatrix}4\\3\end{pmatrix}\in\R^{2}.
    $$

    Con i coefficienti \(\lambda_1=1\), \(\lambda_2=1\), \(\lambda_3=-1\) (non tutti nulli) si ottiene

    $$
    \boldsymbol v_1+\boldsymbol v_2-\boldsymbol v_3
    =
    \begin{pmatrix}1+3-4\\2+1-3\end{pmatrix}
    =
    \begin{pmatrix}0\\0\end{pmatrix}.
    $$

    Pertanto, \(\boldsymbol v_1\), \(\boldsymbol v_2\) e \(\boldsymbol v_3\) sono linearmente dipendenti.

<a id="box-exLinIndepR3-12"></a>

!!! esempio "Esempio 8: Vettori linearmente indipendenti in \(\R^3\)"

    Consideriamo i vettori

    $$
    \boldsymbol v_1=\begin{pmatrix}1\\0\\1\end{pmatrix},
    \qquad
    \boldsymbol v_2=\begin{pmatrix}0\\1\\1\end{pmatrix},
    \qquad
    \boldsymbol v_3=\begin{pmatrix}1\\1\\0\end{pmatrix}\in\R^{3}.
    $$

    La condizione \(\lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2+\lambda_3\boldsymbol v_3=\boldsymbol 0\) si scrive

    $$
    \begin{cases}
    \lambda_1+\lambda_3=0\\
    \lambda_2+\lambda_3=0\\
    \lambda_1+\lambda_2=0
    \end{cases}
    $$

    Dalle prime due equazioni \(\lambda_1=-\lambda_3\) e \(\lambda_2=-\lambda_3\); sostituendo nella terza si ottiene \(-2\lambda_3=0\). Quindi \(\lambda_1=\lambda_2=\lambda_3=0\) e i tre vettori sono linearmente indipendenti.

<a id="box-exLinDepR3-13"></a>

!!! esempio "Esempio 9: Vettori linearmente dipendenti in \(\R^3\)"

    Consideriamo i vettori

    $$
    \boldsymbol v_1=\begin{pmatrix}1\\2\\3\end{pmatrix},
    \qquad
    \boldsymbol v_2=\begin{pmatrix}4\\5\\6\end{pmatrix},
    \qquad
    \boldsymbol v_3=\begin{pmatrix}7\\8\\9\end{pmatrix}\in\R^{3}.
    $$

    Con i coefficienti \(\lambda_1=1\), \(\lambda_2=-2\), \(\lambda_3=1\) si ottiene

    $$
    \boldsymbol v_1-2\boldsymbol v_2+\boldsymbol v_3
    =
    \begin{pmatrix}1-8+7\\2-10+8\\3-12+9\end{pmatrix}
    =
    \begin{pmatrix}0\\0\\0\end{pmatrix}.
    $$

    Pertanto, i tre vettori sono linearmente dipendenti. Equivalentemente, \(\boldsymbol v_3=2\boldsymbol v_2-\boldsymbol v_1\) è combinazione lineare di \(\boldsymbol v_1\) e \(\boldsymbol v_2\).

<a id="box-obsZeroDependent-14"></a>

!!! teorema "Osservazione 1: Insiemi contenenti il vettore nullo"

    Ogni insieme di vettori \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\in\R^{n}\) contenente il vettore nullo \(\boldsymbol 0\) è linearmente dipendente.

??? dimostrazione "Dimostrazione"

    Supponiamo, senza perdita di generalità, che \(\boldsymbol v_1=\boldsymbol 0\). Scegliendo \(\lambda_1=1\) e \(\lambda_2=\dots=\lambda_k=0\) si ottiene \(1\cdot\boldsymbol 0+0\cdot\boldsymbol v_2+\dots+0\cdot\boldsymbol v_k=\boldsymbol 0\), che è una combinazione lineare uguale a \(\boldsymbol 0\) con coefficienti non tutti nulli. <span class="qed">□</span>

<a id="box-obsDependentCombination-15"></a>

!!! teorema "Osservazione 2: Caratterizzazione della dipendenza lineare"

    Sia \(k\ge 2\). I vettori \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\in\R^{n}\) sono linearmente dipendenti se e solo se almeno uno di essi è combinazione lineare degli altri.

??? dimostrazione "Dimostrazione"

    (\(\Rightarrow\)) Se i vettori sono linearmente dipendenti, esistono coefficienti, non tutti nulli, tali che \(\sum_{i=1}^{k}\lambda_i\boldsymbol v_i=\boldsymbol 0\). Sia \(j\) un indice con \(\lambda_j\neq 0\). Allora

    $$
    \boldsymbol v_j=\sum_{i\neq j}\left(-\frac{\lambda_i}{\lambda_j}\right)\boldsymbol v_i,
    $$

    cioè \(\boldsymbol v_j\) è combinazione lineare degli altri.

    (\(\Leftarrow\)) Se \(\boldsymbol v_j=\sum_{i\neq j}\mu_i\boldsymbol v_i\) per opportuni scalari \(\mu_i\), allora \(\sum_{i\neq j}\mu_i\boldsymbol v_i+(-1)\,\boldsymbol v_j=\boldsymbol 0\), che è una combinazione lineare uguale a \(\boldsymbol 0\) in cui il coefficiente di \(\boldsymbol v_j\) è \(-1\neq 0\). <span class="qed">□</span>

<a id="box-obsMoreThanN-16"></a>

!!! teorema "Osservazione 3: Più di \(n\) vettori di \(\R^n\)"

    Comunque si scelgano \(k>n\) vettori di \(\R^{n}\), essi sono linearmente dipendenti.

- Enunciamo questo risultato senza dimostrazione. Ad esempio, tre vettori qualsiasi di \(\R^2\) sono linearmente dipendenti (si veda l'Esempio [Esempio 7](#box-exLinDepR2-11)).

### 4.1 Span e base

<a id="box-defSpan-17"></a>

!!! definizione "Definizione 5: Span (sottospazio generato)"

    Lo <strong>span</strong> (o <strong>sottospazio generato</strong>) dei vettori \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\in\R^{n}\) è l'insieme di tutte le loro combinazioni lineari:

    \begin{equation}
    \mathrm{span}(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k)
    =
    \Bigl\{\lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2+\dots+\lambda_k\boldsymbol v_k \;:\; \lambda_1,\lambda_2,\dots,\lambda_k\in\R\Bigr\}.
    \label{vecSpan}
    \end{equation}

<a id="box-defBasis-18"></a>

!!! definizione "Definizione 6: Base di \(\R^n\)"

    The vectors \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\in\R^{n}\) formano una <strong>base</strong> di \(\R^{n}\) se

    - sono linearmente indipendenti, e

    - \(\mathrm{span}(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k)=\R^{n}\), cioè ogni vettore di \(\R^{n}\) è loro combinazione lineare.

<a id="box-obsUniqueCoordinates-19"></a>

!!! teorema "Osservazione 4: Coordinate rispetto a una base"

    Se \(\boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k\) formano una base di \(\R^{n}\), allora ogni vettore \(\boldsymbol x\in\R^{n}\) si scrive in modo <strong>unico</strong> come \(\boldsymbol x=\lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2+\dots+\lambda_k\boldsymbol v_k\). I coefficienti \(\lambda_1,\lambda_2,\dots,\lambda_k\) sono detti <strong>coordinate</strong> di \(\boldsymbol x\) rispetto alla base.

??? dimostrazione "Dimostrazione"

    Tali coefficienti esistono perché lo span della base è \(\R^{n}\). Se \(\boldsymbol x=\sum_{i=1}^{k}\lambda_i\boldsymbol v_i=\sum_{i=1}^{k}\mu_i\boldsymbol v_i\), sottraendo le due espressioni si ottiene \(\sum_{i=1}^{k}(\lambda_i-\mu_i)\boldsymbol v_i=\boldsymbol 0\). Poiché i vettori sono linearmente indipendenti, \(\lambda_i-\mu_i=0\) per ogni \(i\in\{1,2,\dots,k\}\). <span class="qed">□</span>

<a id="box-defCanonicalBasis-20"></a>

!!! definizione "Definizione 7: Base canonica"

    Per \(i\in\{1,2,\dots,n\}\), denotiamo con \(\boldsymbol e_i\in\R^{n}\) il vettore il cui \(i\)-esimo elemento è uguale a \(1\) e tutti gli altri elementi sono uguali a \(0\):

    $$
    \boldsymbol e_1=\begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},
    \qquad
    \boldsymbol e_2=\begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix},
    \qquad
    \dots,
    \qquad
    \boldsymbol e_n=\begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}.
    $$

    I vettori \(\boldsymbol e_1,\boldsymbol e_2,\dots,\boldsymbol e_n\) formano la <strong>base canonica</strong> di \(\R^{n}\).

<a id="box-obsCanonicalBasis-21"></a>

!!! teorema "Osservazione 5: La base canonica è una base"

    I vettori \(\boldsymbol e_1,\boldsymbol e_2,\dots,\boldsymbol e_n\) formano una base di \(\R^{n}\), e ogni \(\boldsymbol x\in\R^{n}\) soddisfa

    \begin{equation}
    \boldsymbol x=x_1\boldsymbol e_1+x_2\boldsymbol e_2+\dots+x_n\boldsymbol e_n.
    \label{vecCanonical}
    \end{equation}

??? dimostrazione "Dimostrazione"

    Per qualsiasi scelta degli scalari \(\lambda_1,\dots,\lambda_n\) si ha \(\lambda_1\boldsymbol e_1+\dots+\lambda_n\boldsymbol e_n=\begin{pmatrix}\lambda_1 & \lambda_2 & \dots & \lambda_n\end{pmatrix}'\). Questo vettore è uguale a \(\boldsymbol 0\) solo se \(\lambda_1=\dots=\lambda_n=0\), quindi i vettori sono linearmente indipendenti; scegliendo \(\lambda_i=x_i\) si ottiene \(\eqref{vecCanonical}\), quindi il loro span è \(\R^{n}\). <span class="qed">□</span>

- Si può dimostrare che ogni base di \(\R^{n}\) è formata esattamente da \(n\) vettori.

<a id="box-exCanonicalBasis-22"></a>

!!! esempio "Esempio 10: Base canonica di \(\R^3\)"

    Il vettore \(\boldsymbol x=\begin{pmatrix}2 & -5 & 3\end{pmatrix}'\in\R^{3}\) si può scrivere come

    $$
    \boldsymbol x
    =
    2\begin{pmatrix}1\\0\\0\end{pmatrix}
    -5\begin{pmatrix}0\\1\\0\end{pmatrix}
    +3\begin{pmatrix}0\\0\\1\end{pmatrix}
    =
    2\boldsymbol e_1-5\boldsymbol e_2+3\boldsymbol e_3.
    $$

<a id="box-exCoordinatesR2-23"></a>

!!! esempio "Esempio 11: Coordinate rispetto a una base di \(\R^2\)"

    Consideriamo i vettori \( \boldsymbol v_1=\begin{pmatrix}1\\1\end{pmatrix} \) e \( \boldsymbol v_2=\begin{pmatrix}1\\-1\end{pmatrix}. \)

    - Sono linearmente indipendenti: \(\lambda_1+\lambda_2=0\) e \(\lambda_1-\lambda_2=0\) danno \(\lambda_1=\lambda_2=0\).

    - Il loro span è \(\R^{2}\): per ogni \(\begin{pmatrix}a & b\end{pmatrix}'\in\R^{2}\),

        $$
        \begin{pmatrix}a\\b\end{pmatrix}
        =
        \frac{a+b}{2}\begin{pmatrix}1\\1\end{pmatrix}
        +
        \frac{a-b}{2}\begin{pmatrix}1\\-1\end{pmatrix}.
        $$

    Quindi \(\boldsymbol v_1,\boldsymbol v_2\) formano una base di \(\R^2\). Ad esempio, le coordinate di \(\boldsymbol x=\begin{pmatrix}3 & 1\end{pmatrix}'\) sono \(\lambda_1=\frac{3+1}{2}=2\) e \(\lambda_2=\frac{3-1}{2}=1\):

    $$
    \begin{pmatrix}3\\1\end{pmatrix}
    =
    2\begin{pmatrix}1\\1\end{pmatrix}
    +
    1\begin{pmatrix}1\\-1\end{pmatrix}.
    $$

## Esercizi e laboratorio

- :material-pencil-box-multiple: **Esercizi** · [il foglio di esercizi di questo capitolo: 10 esercizi con le soluzioni svolte](../esercizi/es-vettori-matrici-01-vettori.md)

