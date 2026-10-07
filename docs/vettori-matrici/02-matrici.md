---
title: "Matrici"
---

# Matrici

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.1** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/vettori-matrici-02-matrici.pdf)

</div>

## 1. Definizione e trasposta

<a id="box-defMatrix-1"></a>

!!! definizione "Definizione 1: Matrice"

    Una <strong>matrice</strong> è una tabella rettangolare di numeri reali con \(m\) righe e \(n\) colonne.

Data una matrice \(\boldsymbol{A}\in\R^{m\times n}\), scriviamo:

$$
\boldsymbol{A}=
\begin{pmatrix}
[\boldsymbol A]_{1,1} & [\boldsymbol A]_{1,2} & \cdots  & [\boldsymbol A]_{1,n}\\
[\boldsymbol A]_{2,1} & [\boldsymbol A]_{2,2} & \cdots  & [\boldsymbol A]_{2,n}\\
\vdots & \vdots & \ddots  & \vdots \\
[\boldsymbol A]_{m,1} & [\boldsymbol A]_{m,2} & \cdots  & [\boldsymbol A]_{m,n}
\end{pmatrix}
\qquad 
\text{oppure, per brevità,}
\qquad
\boldsymbol{A}=
\begin{pmatrix}
a_{11} & a_{12} & \cdots  & a_{1n}\\
a_{21} & a_{22} & \cdots  & a_{2n}\\
\vdots & \vdots & \ddots  & \vdots \\
a_{m1} & a_{m2} & \cdots  & a_{mn}
\end{pmatrix}.
$$

- Gli interi \(m\) e \(n\) sono le <strong>dimensioni</strong> della matrice: \(m\) è il numero di righe e \(n\) è il numero di colonne.

- La quantità \([\boldsymbol A]_{i,j}\) (o \(a_{ij}\)) denota l'<strong>elemento</strong> di \(\boldsymbol{A}\) di riga \(i\) e colonna \(j\), per \(i\in\{1,2,\dots,m\}\) e \(j\in\{1,2,\dots,n\}\).

<a id="box-exMatrix-2"></a>

!!! esempio "Esempio 1: Matrice"

    La matrice

    $$
    \boldsymbol A = 
    \begin{pmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6
    \end{pmatrix}
    \in \R^{2 \times 3}
    $$

    è una matrice con \(m=2\) righe e \(n=3\) colonne, dove \(a_{11} = 1\), \(a_{12} = 2\), \(a_{13} = 3\), \(a_{21} = 4\), \(a_{22} = 5\) e \(a_{23} = 6\).

<a id="box-defTransposeMatrix-3"></a>

!!! definizione "Definizione 2: Trasposta di una matrice"

    Data una matrice \(\boldsymbol A \in \R^{m \times n}\), la <strong>trasposta</strong> di \(\boldsymbol A\), denotata con \(\boldsymbol A'\), è la matrice \(n \times m\) ottenuta scambiando righe e colonne:

    \begin{equation}
    \boldsymbol A'=
    \begin{pmatrix}
    a_{11} & a_{21} & \cdots  & a_{m1}\\
    a_{12} & a_{22} & \cdots  & a_{m2}\\
    \vdots & \vdots & \ddots  & \vdots \\
    a_{1n} & a_{2n} & \cdots  & a_{mn}
    \end{pmatrix}
    \in \R^{n \times m}.
    \end{equation}

- L'elemento in posizione \((i,j)\) della matrice trasposta \(\boldsymbol A'\) è:

    $$
    a'_{ij} = a_{ji}, \quad \forall i \in \{1,2,\dots,n\},\; \forall j \in \{1,2,\dots,m\}.
    $$

<a id="box-exTransposeMatrix-4"></a>

!!! esempio "Esempio 2: Trasposta di una matrice"

    Data la matrice

    $$
    \boldsymbol A = 
    \begin{pmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6
    \end{pmatrix}
    \in \R^{2 \times 3},
    $$

    la sua trasposta è

    $$
    \boldsymbol A' = 
    \begin{pmatrix}
    1 & 4 \\
    2 & 5 \\
    3 & 6
    \end{pmatrix}
    \in \R^{3 \times 2}.
    $$

### 1.1 Righe e colonne

- La \(i\)-esima riga di una matrice \(\boldsymbol{A}\) si denota con

    $$
    R_i(\boldsymbol{A})
    \qquad \text{oppure} \qquad
    \boldsymbol{A}_i
    $$

- La \(j\)-esima colonna di una matrice \(\boldsymbol{A}\) si denota con

    $$
    C_j(\boldsymbol{A})
    \qquad \text{oppure} \qquad
    \boldsymbol{A}_j
    $$

- In entrambi i casi, possiamo usare semplicemente $R_i$ o $C_j$ quando la matrice è chiara dal contesto.

### 1.2 Sottomatrici complementari

- Sia \(\boldsymbol A\in\R^{n\times m}\) una matrice e siano \(i\in\{1,2,\dots,n\}\), \(j\in\{1,2,\dots,m\}\). Denotiamo con \(\boldsymbol A_{ij}\) la matrice \((n-1)\times(m-1)\) ottenuta da \(\boldsymbol A\) eliminando la riga \(i\) e la colonna \(j\). La matrice \(\boldsymbol A_{ij}\) è detta <strong>sottomatrice complementare</strong> dell'elemento \(a_{ij}\); il suo determinante \(\det(\boldsymbol A_{ij})\) è detto <strong>minore complementare</strong> di \(a_{ij}\).

<a id="box-exMinorMatrix-5"></a>

!!! esempio "Esempio 3: Sottomatrice complementare"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & -2 & 0 & 5\\
    3 & 4 & 7 & -1\\
    2 & 0 & -3 & 6\\
    -4 & 1 & 2 & 8
    \end{pmatrix}\in\R^{4\times 4}.
    $$

    Per \(i=2\) e \(j=3\), la sottomatrice complementare \(\boldsymbol A_{23}\in\R^{3\times 3}\) si ottiene eliminando la riga \(2\) e la colonna \(3\):

    $$
    \boldsymbol A_{23}=
    \begin{pmatrix}
    1 & -2 & 5\\
    2 & 0 & 6\\
    -4 & 1 & 8
    \end{pmatrix}.
    $$

## 2. Somma di matrici e prodotto per uno scalare

!!! chiave ""

    Date due matrici

    $$
    \underbrace{
    \begin{pmatrix}
    a_{11} & a_{12} & \cdots & a_{1n}\\
    a_{21} & a_{22} & \cdots & a_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    a_{m1} & a_{m2} & \cdots & a_{mn}
    \end{pmatrix}
    }_{\boldsymbol A}\in\R^{m\times n}
    \quad \text{e} \quad
    \underbrace{
    \begin{pmatrix}
    b_{11} & b_{12} & \cdots & b_{1n}\\
    b_{21} & b_{22} & \cdots & b_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    b_{m1} & b_{m2} & \cdots & b_{mn}
    \end{pmatrix}
    }_{\boldsymbol B}\in\R^{m\times n}
    $$

    la loro somma è la matrice

    \begin{equation}
    {\boldsymbol A} + {\boldsymbol B} =
    \begin{pmatrix}
    a_{11}+b_{11} & a_{12}+b_{12} & \cdots & a_{1n}+b_{1n}\\
    a_{21}+b_{21} & a_{22}+b_{22} & \cdots & a_{2n}+b_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    a_{m1}+b_{m1} & a_{m2}+b_{m2} & \cdots & a_{mn}+b_{mn}
    \end{pmatrix}
    \end{equation}

!!! chiave ""

    Dati uno scalare \(\lambda\in\R\) e una matrice

    $$
    \underbrace{
    \begin{pmatrix}
    a_{11} & a_{12} & \cdots & a_{1n}\\
    a_{21} & a_{22} & \cdots & a_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    a_{m1} & a_{m2} & \cdots & a_{mn}
    \end{pmatrix}
    }_{\boldsymbol A}\in\R^{m\times n}
    $$

    il <strong>prodotto</strong> di \(\boldsymbol A\) <strong>per lo scalare</strong> \(\lambda\) è la matrice

    \begin{equation}
    \lambda \boldsymbol A =
    \begin{pmatrix}
    \lambda a_{11} & \lambda a_{12} & \cdots & \lambda a_{1n}\\
    \lambda a_{21} & \lambda a_{22} & \cdots & \lambda a_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    \lambda a_{m1} & \lambda a_{m2} & \cdots & \lambda a_{mn}
    \end{pmatrix}
    \end{equation}

<a id="box-exSumScalarMatrix-6"></a>

!!! esempio "Esempio 4: Somma di matrici e prodotto per uno scalare"

    Consideriamo le matrici

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & -2\\
    3 & 0
    \end{pmatrix},
    \qquad
    \boldsymbol B=
    \begin{pmatrix}
    4 & 5\\
    -1 & 2
    \end{pmatrix}
    \in \R^{2\times 2}.
    $$

    Allora

    $$
    \boldsymbol A+\boldsymbol B=
    \begin{pmatrix}
    1+4 & -2+5\\
    3+(-1) & 0+2
    \end{pmatrix}
    =
    \begin{pmatrix}
    5 & 3\\
    2 & 2
    \end{pmatrix},
    $$

    e, per \(\lambda=-2\),

    $$
    \lambda \boldsymbol A
    =
    -2\begin{pmatrix}
    1 & -2\\
    3 & 0
    \end{pmatrix}
    =
    \begin{pmatrix}
    -2 & 4\\
    -6 & 0
    \end{pmatrix}.
    $$

### 2.1 Proprietà

!!! chiave ""

    Le principali proprietà della somma di matrici e del prodotto per uno scalare sono:

    \begin{equation}
    \boldsymbol A+\boldsymbol B=\boldsymbol B+\boldsymbol A,
    \quad \forall \boldsymbol A,\boldsymbol B\in\R^{m\times n}
    \label{mat_sum_1}
    \end{equation}

    \begin{equation}
    (\boldsymbol A+\boldsymbol B)+\boldsymbol C=\boldsymbol A+(\boldsymbol B+\boldsymbol C),
    \quad \forall \boldsymbol A,\boldsymbol B,\boldsymbol C\in\R^{m\times n}
    \label{mat_sum_2}
    \end{equation}

    \begin{equation}
    \boldsymbol A+\boldsymbol 0=\boldsymbol A,
    \quad \forall \boldsymbol A\in\R^{m\times n}
    \label{mat_sum_3}
    \end{equation}

    \begin{equation}
    \boldsymbol A+(-\boldsymbol A)=\boldsymbol 0,
    \quad \forall \boldsymbol A\in\R^{m\times n}
    \label{mat_sum_4}
    \end{equation}

    \begin{equation}
    \lambda(\boldsymbol A+\boldsymbol B)=\lambda\boldsymbol A+\lambda\boldsymbol B,
    \quad \forall \lambda\in\R,\; \forall \boldsymbol A,\boldsymbol B\in\R^{m\times n}
    \label{mat_scal_1}
    \end{equation}

    \begin{equation}
    (\lambda+\mu)\boldsymbol A=\lambda\boldsymbol A+\mu\boldsymbol A,
    \quad \forall \lambda,\mu\in\R,\; \forall \boldsymbol A\in\R^{m\times n}
    \label{mat_scal_2}
    \end{equation}

    \begin{equation}
    \lambda(\mu\boldsymbol A)=(\lambda\mu)\boldsymbol A,
    \quad \forall \lambda,\mu\in\R,\; \forall \boldsymbol A\in\R^{m\times n}
    \label{mat_scal_3}
    \end{equation}

    \begin{equation}
    1\cdot \boldsymbol A=\boldsymbol A
    \quad \text{e} \quad
    0\cdot \boldsymbol A=\boldsymbol 0,
    \quad \forall \boldsymbol A\in\R^{m\times n}.
    \label{mat_scal_4}
    \end{equation}

## 3. Prodotto di matrici

!!! chiave ""

    Date due matrici

    $$
    \underbrace{
    \begin{pmatrix}
    a_{11} & a_{12} & \cdots  & a_{1n}\\
    a_{21} & a_{22} & \cdots  & a_{2n}\\
    \vdots & \vdots & \ddots  & \vdots \\
    a_{m1} & a_{m2} & \cdots  & a_{mn}
    \end{pmatrix}
    }_{\boldsymbol A} \in \R^{m \times n}
    \quad \text{e} \quad 
    \underbrace{
    \begin{pmatrix}
    b_{11} & b_{12} & \cdots  & b_{1p}\\
    b_{21} & b_{22} & \cdots  & b_{2p}\\
    \vdots & \vdots & \ddots  & \vdots \\
    b_{n1} & b_{n2} & \cdots  & b_{np}
    \end{pmatrix}
    }_{\boldsymbol B} \in \R^{n \times p}
    $$

    il loro prodotto (righe per colonne) è la matrice

    \begin{equation}
    {\boldsymbol A} {\boldsymbol B} =
    \begin{pmatrix}
    \sum_{j=1}^{n} a_{1j} b_{j1} & \sum_{j=1}^{n} a_{1j} b_{j2} & \cdots  & \sum_{j=1}^{n} a_{1j} b_{jp}\\[2ex]
    \sum_{j=1}^{n} a_{2j} b_{j1} & \sum_{j=1}^{n} a_{2j} b_{j2} & \cdots  & \sum_{j=1}^{n} a_{2j} b_{jp}\\[2ex]
    \vdots & \vdots & \ddots  & \vdots \\[1ex]
    \sum_{j=1}^{n} a_{mj} b_{j1} & \sum_{j=1}^{n} a_{mj} b_{j2} & \cdots  & \sum_{j=1}^{n} a_{mj} b_{jp}
    \end{pmatrix}
     \in \R^{m \times p}
    \end{equation}

    dove l'elemento in posizione \((i,k)\), cioè \([\boldsymbol A\boldsymbol B]_{ik}=\sum_{j=1}^{n} a_{ij}b_{jk}\), è il prodotto scalare della \(i\)-esima riga di \(\boldsymbol A\) e della \(k\)-esima colonna di \(\boldsymbol B\).

<a id="box-exMatrixProduct2x2-7"></a>

!!! esempio "Esempio 5: Prodotto di matrici"

    Consideriamo le matrici

    $$
    \boldsymbol A = 
    \begin{pmatrix}
    1 & 2 \\
    3 & 4
    \end{pmatrix}
    \in \R^{2 \times 2}
    \qquad \text{e} \qquad
    \boldsymbol B = 
    \begin{pmatrix}
    5 & 6 \\
    7 & 8
    \end{pmatrix}
    \in \R^{2 \times 2}
    $$

    Il prodotto \(\boldsymbol A \boldsymbol B\) è:

    \begin{align*}
    \boldsymbol A \boldsymbol B 
    &= \begin{pmatrix}
    1 & 2 \\
    3 & 4
    \end{pmatrix}
    \begin{pmatrix}
    5 & 6 \\
    7 & 8
    \end{pmatrix}\\
    &= \begin{pmatrix}
    1\cdot 5 + 2\cdot 7 & 1\cdot 6 + 2\cdot 8 \\
    3\cdot 5 + 4\cdot 7 & 3\cdot 6 + 4\cdot 8
    \end{pmatrix}\\
    &= \begin{pmatrix}
    19 & 22 \\
    43 & 50
    \end{pmatrix}
    \end{align*}

    Il prodotto \(\boldsymbol B  \boldsymbol A\) è:

    \begin{align*}
    \boldsymbol B \boldsymbol A 
    &= \begin{pmatrix}
    5 & 6 \\
    7 & 8
    \end{pmatrix}
    \begin{pmatrix}
    1 & 2 \\
    3 & 4
    \end{pmatrix}\\
    &= \begin{pmatrix}
    5\cdot 1 + 6\cdot 3 & 5\cdot 2 + 6\cdot 4 \\
    7\cdot 1 + 8\cdot 3 & 7\cdot 2 + 8\cdot 4
    \end{pmatrix}\\
    &= \begin{pmatrix}
    23 & 34 \\
    31 & 46
    \end{pmatrix}
    \end{align*}

<a id="box-exMatrixProduct2x3-8"></a>

!!! esempio "Esempio 6: Prodotto di matrici"

    Consideriamo le matrici

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & -1\\
    0 & 3 & 4
    \end{pmatrix}
    \in \R^{2\times 3}
    \qquad \text{e} \qquad
    \boldsymbol B=
    \begin{pmatrix}
    2 & 1\\
    -1 & 0\\
    3 & 5
    \end{pmatrix}
    \in \R^{3\times 2}
    $$

    Il prodotto \(\boldsymbol A\boldsymbol B\) è:

    \begin{align*}
    \boldsymbol A\boldsymbol B
    &=
    \begin{pmatrix}
    1 & 2 & -1\\
    0 & 3 & 4
    \end{pmatrix}
    \begin{pmatrix}
    2 & 1\\
    -1 & 0\\
    3 & 5
    \end{pmatrix}\\
    &=
    \begin{pmatrix}
    1\cdot 2 + 2\cdot(-1) + (-1)\cdot 3 & 1\cdot 1 + 2\cdot 0 + (-1)\cdot 5\\
    0\cdot 2 + 3\cdot(-1) + 4\cdot 3 & 0\cdot 1 + 3\cdot 0 + 4\cdot 5
    \end{pmatrix}\\
    &=
    \begin{pmatrix}
    -3 & -4\\
    9 & 20
    \end{pmatrix}
    \end{align*}

    Il prodotto \(\boldsymbol B  \boldsymbol A\) è:

    \begin{align*}
    \boldsymbol B\boldsymbol A
    &=
    \begin{pmatrix}
    2 & 1\\
    -1 & 0\\
    3 & 5
    \end{pmatrix}
    \begin{pmatrix}
    1 & 2 & -1\\
    0 & 3 & 4
    \end{pmatrix}\\
    &=
    \begin{pmatrix}
    2\cdot 1 + 1\cdot 0 & 2\cdot 2 + 1\cdot 3 & 2\cdot (-1) + 1\cdot 4\\
    -1\cdot 1 + 0\cdot 0 & -1\cdot 2 + 0\cdot 3 & -1\cdot (-1) + 0\cdot 4\\
    3\cdot 1 + 5\cdot 0 & 3\cdot 2 + 5\cdot 3 & 3\cdot (-1) + 5\cdot 4
    \end{pmatrix}\\
    &=
    \begin{pmatrix}
    2 & 7 & 2\\
    -1 & -2 & 1\\
    3 & 21 & 17
    \end{pmatrix}
    \end{align*}

    In particolare, \(\boldsymbol A\boldsymbol B \neq \boldsymbol B\boldsymbol A\).

### 3.1 Proprietà

!!! chiave ""

    Le principali proprietà del prodotto di matrici (quando le dimensioni sono compatibili) sono:

    \begin{equation}
    (\boldsymbol A \boldsymbol B)\boldsymbol C = \boldsymbol A(\boldsymbol B \boldsymbol C),
    \quad \forall \boldsymbol A\in\R^{m\times n},\; \boldsymbol B\in\R^{n\times p},\; \boldsymbol C\in\R^{p\times q}
    \label{mat_prod_1}
    \end{equation}

    \begin{equation}
    \boldsymbol A(\boldsymbol B+\boldsymbol C)=\boldsymbol A\boldsymbol B+\boldsymbol A\boldsymbol C,
    \quad \forall \boldsymbol A\in\R^{m\times n},\; \boldsymbol B,\boldsymbol C\in\R^{n\times p}
    \label{mat_prod_2}
    \end{equation}

    \begin{equation}
    (\boldsymbol A+\boldsymbol B)\boldsymbol C=\boldsymbol A\boldsymbol C+\boldsymbol B\boldsymbol C,
    \quad \forall \boldsymbol A,\boldsymbol B\in\R^{m\times n},\; \boldsymbol C\in\R^{n\times p}
    \label{mat_prod_3}
    \end{equation}

    \begin{equation}
    \lambda(\boldsymbol A\boldsymbol B) = (\lambda \boldsymbol A)\boldsymbol B = \boldsymbol A(\lambda \boldsymbol B),
    \quad \forall \lambda\in\R,\; \forall \boldsymbol A\in\R^{m\times n},\; \boldsymbol B\in\R^{n\times p}
    \label{mat_prod_4}
    \end{equation}

    \begin{equation}
    \boldsymbol I_m \boldsymbol A=\boldsymbol A
    \quad \text{e} \quad
    \boldsymbol A \boldsymbol I_n=\boldsymbol A,
    \quad \forall \boldsymbol A\in\R^{m\times n}
    \label{mat_prod_5}
    \end{equation}

    In generale, il prodotto di matrici <strong>non è commutativo</strong>:

    \begin{equation}
    \boldsymbol A\boldsymbol B \neq \boldsymbol B\boldsymbol A
    \quad \text{in generale}.
    \label{mat_prod_6}
    \end{equation}

!!! interattivo "Provalo nel laboratorio"

    lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi.

<div class="la-tool" data-tool="prodotto" data-matrix="1,2,0;-1,3,1" data-b="2,1;0,-1;4,3"></div>

## 4. Matrici speciali

<a id="box-defSquareMatrix-9"></a>

!!! definizione "Definizione 3: Matrice quadrata"

    Una matrice \(\boldsymbol A\in\R^{m\times n}\) si dice <strong>matrice quadrata</strong> se ha lo stesso numero di righe e di colonne (\(m=n\)). In questo caso, \(\boldsymbol A\in\R^{n\times n}\) e ha la forma:

    \begin{equation}
    \boldsymbol A=
    \begin{pmatrix}
    a_{11} & a_{12} & \cdots & a_{1n}\\
    a_{21} & a_{22} & \cdots & a_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{pmatrix}.
    \end{equation}

<a id="box-exSquareMatrix-10"></a>

!!! esempio "Esempio 7: Matrice quadrata"

    Un esempio di matrice quadrata di ordine \(3\) è:

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & -1 & 0\\
    4 & 3 & 5\\
    1 & 0 & 7
    \end{pmatrix}
    \in\R^{3\times 3}.
    $$

<a id="box-defIdentityMatrix-11"></a>

!!! definizione "Definizione 4: Matrice identità"

    Una matrice quadrata \(\boldsymbol I_n\in\R^{n\times n}\) si dice <strong>matrice identità</strong> se ha elementi uguali a uno sulla diagonale principale e zero altrove. Ha la forma:

    \begin{equation}
    \boldsymbol I_n=
    \begin{pmatrix}
    1 & 0 & \cdots & 0\\
    0 & 1 & \cdots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \cdots & 1
    \end{pmatrix}.
    \end{equation}

- Equivalentemente, la matrice identità soddisfa

    $$
    [\boldsymbol I_n]_{ij}=
    \begin{cases}
    1, & \text{se } i=j,\\
    0, & \text{se } i\neq j,
    \end{cases}
    \qquad \forall i,j\in\{1,2,\dots,n\}.
    $$

<a id="box-exIdentityMatrix-12"></a>

!!! esempio "Esempio 8: Matrice identità"

    La matrice identità di ordine \(3\) è:

    $$
    \boldsymbol I_3=
    \begin{pmatrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1
    \end{pmatrix}
    \in\R^{3\times 3}.
    $$

- Per ogni matrice \(\boldsymbol A \in \R^{m \times n}\) si ha:

    $$
    \boldsymbol I_m \boldsymbol A = \boldsymbol A
    \qquad \text{e} \qquad
    \boldsymbol A \boldsymbol I_n = \boldsymbol A.
    $$

<a id="box-defDiagonalMatrix-13"></a>

!!! definizione "Definizione 5: Matrice diagonale"

    Una matrice quadrata \(\boldsymbol D\in\R^{n\times n}\) si dice <strong>diagonale</strong> se tutti i suoi elementi fuori dalla diagonale principale sono nulli. Ha la forma:

    \begin{equation}
    \boldsymbol D=
    \begin{pmatrix}
    d_{11} & 0      & \cdots & 0\\
    0      & d_{22} & \cdots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0      & 0      & \cdots & d_{nn}
    \end{pmatrix}.
    \end{equation}

- Equivalentemente, una matrice diagonale soddisfa

    $$
    d_{ij}=0,\qquad \forall i,j\in\{1,2,\dots,n\}\ \text{con}\ i\neq j.
    $$

<a id="box-exDiagonalMatrix-14"></a>

!!! esempio "Esempio 9: Matrice diagonale"

    La matrice

    $$
    \boldsymbol D=
    \begin{pmatrix}
    2 & 0 & 0\\
    0 & -1 & 0\\
    0 & 0 & 5
    \end{pmatrix}
    \in\R^{3\times 3}
    $$

    è diagonale.

<a id="box-defSymmetricMatrix-15"></a>

!!! definizione "Definizione 6: Matrice simmetrica"

    Una matrice quadrata \(\boldsymbol Q\in\R^{n\times n}\) si dice <strong>simmetrica</strong> se ha elementi uguali in posizioni simmetriche rispetto alla diagonale principale (cioè l'elemento in posizione \((i,j)\) è uguale all'elemento in posizione \((j,i)\)). Ha la forma:

    \begin{equation}
    \boldsymbol Q=
    \begin{pmatrix}
    q_{11} & q_{12} & \cdots & q_{1n}\\
    q_{12} & q_{22} & \cdots & q_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    q_{1n} & q_{2n} & \cdots & q_{nn}
    \end{pmatrix}.
    \end{equation}

- Equivalentemente, una matrice simmetrica soddisfa

    $$
    q_{ij}=q_{ji},\qquad \forall i,j\in\{1,2,\dots,n\}.
    $$

- In forma matriciale, la simmetria si può scrivere come

    $$
    \boldsymbol Q'=\boldsymbol Q.
    $$

<a id="box-defUpperTriangularMatrix-16"></a>

!!! definizione "Definizione 7: Matrice triangolare superiore"

    Una matrice quadrata \(\boldsymbol U\in\R^{n\times n}\) si dice <strong>triangolare superiore</strong> se tutti i suoi elementi al di sotto della diagonale principale sono nulli. Ha la forma:

    \begin{equation}
    \boldsymbol U=
    \begin{pmatrix}
    u_{11} & u_{12} & \cdots & u_{1n}\\
    0      & u_{22} & \cdots & u_{2n}\\
    \vdots & \vdots & \ddots & \vdots\\
    0      & 0      & \cdots & u_{nn}
    \end{pmatrix}.
    \end{equation}

- Equivalentemente, una matrice triangolare superiore soddisfa

    $$
    u_{ij}=0,\qquad \forall i,j\in\{1,2,\dots,n\}\ \text{con}\ i>j.
    $$

<a id="box-exUpperTriangular-17"></a>

!!! esempio "Esempio 10: Matrice triangolare superiore"

    La matrice

    $$
    \boldsymbol U=
    \begin{pmatrix}
    1 & 2 & -3\\
    0 & 4 & 5\\
    0 & 0 & -2
    \end{pmatrix}
    \in\R^{3\times 3}
    $$

    è triangolare superiore.

<a id="box-defLowerTriangularMatrix-18"></a>

!!! definizione "Definizione 8: Matrice triangolare inferiore"

    Una matrice quadrata \(\boldsymbol L\in\R^{n\times n}\) si dice <strong>triangolare inferiore</strong> se tutti i suoi elementi al di sopra della diagonale principale sono nulli. Ha la forma:

    \begin{equation}
    \boldsymbol L=
    \begin{pmatrix}
    \ell_{11} & 0        & \cdots & 0\\
    \ell_{21} & \ell_{22}& \cdots & 0\\
    \vdots    & \vdots   & \ddots & \vdots\\
    \ell_{n1} & \ell_{n2}& \cdots & \ell_{nn}
    \end{pmatrix}.
    \end{equation}

- Equivalentemente, una matrice triangolare inferiore soddisfa

    $$
    \ell_{ij}=0,\qquad \forall i,j\in\{1,2,\dots,n\}\ \text{con}\ i<j.
    $$

<a id="box-exLowerTriangular-19"></a>

!!! esempio "Esempio 11: Matrice triangolare inferiore"

    La matrice

    $$
    \boldsymbol L=
    \begin{pmatrix}
    3 & 0 & 0\\
    -1 & 2 & 0\\
    4 & 5 & 1
    \end{pmatrix}
    \in\R^{3\times 3}
    $$

    è triangolare inferiore.

### 4.1 Matrici di permutazione

- Le matrici di permutazione sono matrici quadrate ottenute permutando le righe (o, equivalentemente, le colonne) della matrice identità. Codificano permutazioni di indici e realizzano riordinamenti di righe/colonne tramite il prodotto di matrici.

!!! chiave ""

    Dato un ordinamento (permutazione) \(\pi\) di \(\{1,\dots,n\}\), denotiamo con \(\boldsymbol P_{\pi}\) la <strong>matrice di permutazione</strong> ottenuta da \(\boldsymbol I_n\) riordinandone le righe secondo \(\pi\), cioè mettendo per prima la riga \(\pi(1)\), poi la riga \(\pi(2)\), \(\dots\), e infine la riga \(\pi(n)\).

    - <strong>Riordinamento delle righe tramite moltiplicazione a sinistra.</strong> Date \(\boldsymbol A \in \R^{m \times n}\) e \(\boldsymbol P_{\pi} \in \R^{m \times m}\), la matrice

        $$
        \boldsymbol P_{\pi}\boldsymbol A
        $$

        è formata dalle righe di \(\boldsymbol A\) riordinate secondo la permutazione \(\pi\) (la riga \(\pi(1)\) diventa la prima riga, la riga \(\pi(2)\) diventa la seconda riga, ecc.).

    - <strong>Riordinamento delle colonne tramite moltiplicazione a destra.</strong> Date \(\boldsymbol A \in \R^{m \times n}\) e \(\boldsymbol P_{\pi} \in \R^{n \times n}\), la matrice

        $$
        \boldsymbol A\boldsymbol P_{\pi}'
        $$

        (si noti la trasposta: \(\boldsymbol P_{\pi}'\) si ottiene da \(\boldsymbol I_n\) riordinandone le <em>colonne</em> secondo \(\pi\)) è formata dalle colonne di \(\boldsymbol A\) riordinate secondo la permutazione \(\pi\) (la colonna \(\pi(1)\) diventa la prima colonna, la colonna \(\pi(2)\) diventa la seconda colonna, ecc.).

<a id="box-exRowPermutation-20"></a>

!!! esempio "Esempio 12: Riordinamento delle righe con una matrice di permutazione"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4\\
    5 & 6
    \end{pmatrix}
    \in \R^{3 \times 2}.
    $$

    Dato l'ordinamento desiderato delle righe \(\pi=(3,1,2)\) (cioè prima la riga \(3\), poi la riga \(1\), poi la riga \(2\)), usiamo la matrice di permutazione \(\boldsymbol P_{\pi}\) ottenuta da \(\boldsymbol I_3\) riordinandone le righe come \((3,1,2)\):

    $$
    \boldsymbol P_{\pi}=
    \begin{pmatrix}
    0 & 0 & 1\\
    1 & 0 & 0\\
    0 & 1 & 0
    \end{pmatrix}
    \in \R^{3 \times 3}.
    $$

    Allora:

    $$
    \boldsymbol P_{\pi}\boldsymbol A
    =
    \begin{pmatrix}
    0 & 0 & 1\\
    1 & 0 & 0\\
    0 & 1 & 0
    \end{pmatrix}
    \begin{pmatrix}
    1 & 2\\
    3 & 4\\
    5 & 6
    \end{pmatrix}
    =
    \begin{pmatrix}
    5 & 6\\
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    Le righe di \(\boldsymbol A\) sono state riordinate secondo \(\pi=(3,1,2)\).

<a id="box-exColumnPermutation-21"></a>

!!! esempio "Esempio 13: Riordinamento delle colonne con una matrice di permutazione"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6
    \end{pmatrix}
    \in \R^{2 \times 3}.
    $$

    Dato l'ordinamento desiderato delle colonne \(\pi=(2,3,1)\) (cioè prima la colonna \(2\), poi la colonna \(3\), poi la colonna \(1\)), usiamo la matrice di permutazione \(\boldsymbol P_{\pi}\) ottenuta da \(\boldsymbol I_3\) riordinandone le righe come \((2,3,1)\), e la sua trasposta:

    $$
    \boldsymbol P_{\pi}=
    \begin{pmatrix}
    0 & 1 & 0\\
    0 & 0 & 1\\
    1 & 0 & 0
    \end{pmatrix},
    \qquad
    \boldsymbol P_{\pi}'=
    \begin{pmatrix}
    0 & 0 & 1\\
    1 & 0 & 0\\
    0 & 1 & 0
    \end{pmatrix}
    \in \R^{3 \times 3}.
    $$

    Allora:

    $$
    \boldsymbol A\boldsymbol P_{\pi}'
    =
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6
    \end{pmatrix}
    \begin{pmatrix}
    0 & 0 & 1\\
    1 & 0 & 0\\
    0 & 1 & 0
    \end{pmatrix}
    =
    \begin{pmatrix}
    2 & 3 & 1\\
    5 & 6 & 4
    \end{pmatrix}.
    $$

    Le colonne di \(\boldsymbol A\) sono state riordinate secondo \(\pi=(2,3,1)\).

### 4.2 Matrici inverse

<a id="box-defInvertible-22"></a>

!!! definizione "Definizione 9: matrice inversa"

    Una matrice quadrata \( \boldsymbol A \in \R^{n\times n} \) è <strong>invertibile</strong> se esiste una matrice \( \boldsymbol A^{-1} \in \R^{n\times n} \) tale che

    $$
    \boldsymbol A\,\boldsymbol A^{-1} = \boldsymbol I
    \qquad \text{e} \qquad
    \boldsymbol A^{-1}\boldsymbol A = \boldsymbol I.
    $$

    Tale matrice \( \boldsymbol A^{-1} \) è detta <strong>inversa</strong> di \( \boldsymbol A \).

- Se esiste, la matrice inversa \( \boldsymbol A^{-1} \) è unica.

### 4.3 Matrici semidefinite

<a id="box-defPSD-23"></a>

!!! definizione "Definizione 10: matrici semidefinite"

    Una matrice quadrata <strong>simmetrica</strong> \( \boldsymbol Q \in \R^{n \times n} \) è 

    - <strong>semidefinita positiva</strong> se

        $$
        \boldsymbol x' \boldsymbol Q \, \boldsymbol x \ge 0, \qquad \forall \boldsymbol x \in \R^n
        $$

    - <strong>definita positiva</strong> se

        $$
        \boldsymbol x' \boldsymbol Q \, \boldsymbol x > 0, \qquad \forall \boldsymbol x \in \R^n \setminus \{\boldsymbol 0\}
        $$

    - <strong>semidefinita negativa</strong> se

        $$
        \boldsymbol x' \boldsymbol Q \, \boldsymbol x \le 0, \qquad \forall \boldsymbol x \in \R^n
        $$

    - <strong>definita negativa</strong> se

        $$
        \boldsymbol x' \boldsymbol Q \, \boldsymbol x < 0, \qquad \forall \boldsymbol x \in \R^n \setminus \{\boldsymbol 0\}
        $$

<a id="box-exPSD-24"></a>

!!! esempio "Esempio 14: matrice semidefinita positiva"

    - La matrice identità

        $$
        \boldsymbol I=
        \begin{pmatrix}
        1 & 0\\[1ex]
        0 & 1 \\
        \end{pmatrix}
        $$

        è semidefinita positiva poiché:

        $$
        \begin{pmatrix} 
        x_1 & x_2 
        \end{pmatrix} 
        \begin{pmatrix}
        1 & 0\\[1ex]
        0 & 1 \\
        \end{pmatrix}
        \begin{pmatrix}
        x_1 \\[1ex]
        x_2 \\
        \end{pmatrix}
        = x_1^2 + x_2^2 \ge 0, 
        \qquad
        \forall \begin{pmatrix}x_1\\x_2\end{pmatrix} \in \R^2.
        $$

    - La matrice

        $$
        \begin{pmatrix}
        2 & -1 \\[1ex]
        -1 & 2
        \end{pmatrix}
        $$

        è semidefinita positiva poiché:

        \begin{align*}
        \begin{pmatrix} 
        x_1 & x_2
        \end{pmatrix} 
        \begin{pmatrix}
        2 & -1 \\[1ex]
        -1 & 2
        \end{pmatrix}
        \begin{pmatrix}
        x_1 \\[1ex]
        x_2
        \end{pmatrix}
        &= 2x_1^2 - 2x_1x_2 + 2x_2^2 \\[1ex]
        &= x_1^2 + (x_1 - x_2)^2 + x_2^2 \ge 0,
        \qquad
        \forall \begin{pmatrix}x_1\\x_2\end{pmatrix} \in \R^2.
        \end{align*}

## 5. Determinante

!!! chiave ""

    - <strong>Determinante di una matrice \(1\times 1\).</strong> Sia

        $$
        \boldsymbol A=
        \begin{pmatrix}
        a 
        \end{pmatrix}\in\R^{1\times 1}.
        $$

        Allora

        \begin{equation}
        \det(\boldsymbol A)=a.
        \end{equation}

    - <strong>Determinante di una matrice \(2\times 2\).</strong> Sia

        $$
        \boldsymbol A=
        \begin{pmatrix}
        a & b\\
        c & d
        \end{pmatrix}\in\R^{2\times 2}.
        $$

        Allora

        \begin{equation}
        \det(\boldsymbol A)=ad-bc.
        \end{equation}

    - <strong>Determinante di una matrice \(3\times 3\) (regola di Sarrus).</strong> Sia

        $$
        \boldsymbol A=
        \begin{pmatrix}
        a & b & c\\
        d & e & f\\
        g & h & i
        \end{pmatrix}\in\R^{3\times 3}.
        $$

        Allora

        \begin{equation}
        \det(\boldsymbol A)
        = aei + bfg + cdh \;-\; ceg - bdi - afh.
        \end{equation}

<a id="box-exDet2x2-25"></a>

!!! esempio "Esempio 15: determinante di una matrice \(2\times2\)"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & -1\\
    3 & 4
    \end{pmatrix}.
    $$

    Allora

    $$
    \det(\boldsymbol A)=2\cdot 4-(-1)\cdot 3=8+3=11.
    $$

<a id="box-exDet3x3Sarrus-26"></a>

!!! esempio "Esempio 16: determinante di una matrice \(3\times3\)"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0\\
    3 & 1 & 4\\
    2 & -1 & 1
    \end{pmatrix}.
    $$

    Con la regola di Sarrus:

    $$
    \det(\boldsymbol A)
    = 1\cdot 1\cdot 1 + 2\cdot 4\cdot 2 + 0\cdot 3\cdot (-1)
    - 0\cdot 1\cdot 2 - 2\cdot 3\cdot 1 - 1\cdot 4\cdot (-1).
    $$

    Quindi

    $$
    \det(\boldsymbol A)=1+16+0-0-6+4=15.
    $$

### 5.1 Sviluppo di Laplace

!!! chiave ""

    Sia \(\boldsymbol A\in\R^{n\times n}\) una matrice quadrata. Il determinante \(\det(\boldsymbol A)\) può essere calcolato ricorsivamente mediante lo <strong>sviluppo di Laplace</strong> lungo una qualsiasi riga o colonna.

    Per ogni riga \(i\in\{1,2,\dots,n\}\) si ha:

    \begin{equation}
    \det(\boldsymbol A)=\sum_{j=1}^{n} a_{ij}\,C_{ij}
    \end{equation}

    Per ogni colonna \(j\in\{1,2,\dots,n\}\) si ha:

    \begin{equation}
    \det(\boldsymbol A)=\sum_{i=1}^{n} a_{ij}\,C_{ij}
    \end{equation}

    dove \(C_{ij}\) è il <strong>cofattore</strong> (o complemento algebrico) dell'elemento \(a_{ij}\), definito da

    \begin{equation}
    C_{ij}=(-1)^{i+j}\,\det(\boldsymbol A_{ij})
    \end{equation}

    dove \(\boldsymbol A_{ij}\) è la sottomatrice complementare ottenuta da \(\boldsymbol A\) eliminando la riga \(i\) e la colonna \(j\) (quindi \(\det(\boldsymbol A_{ij})\) è il minore complementare di \(a_{ij}\)).

<a id="box-exLaplace3x3-27"></a>

!!! esempio "Esempio 17: Determinante mediante lo sviluppo di Laplace"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    -2 & 2 & -3\\
    -1 & 1 & 3\\
    2 & 0 & -1
    \end{pmatrix}.
    $$

    Sviluppiamo lungo la seconda colonna (contiene uno zero):

    $$
    \det(\boldsymbol A)
    =
    2\,C_{12}+1\,C_{22}+0\cdot C_{32}.
    $$

    Calcoliamo i cofattori:

    $$
    C_{12}=(-1)^{1+2}\det
    \begin{pmatrix}
    -1 & 3\\
    2 & -1
    \end{pmatrix}
    =
    -\,\bigl((-1)(-1)-2\cdot 3\bigr)
    =
    -\,\bigl(1-6\bigr)=5,
    $$

    $$
    C_{22}=(-1)^{2+2}\det
    \begin{pmatrix}
    -2 & -3\\
    2 & -1
    \end{pmatrix}
    =
    \bigl((-2)(-1)-2(-3)\bigr)
    =
    2+6=8.
    $$

    Pertanto,

    $$
    \det(\boldsymbol A)=2\cdot 5+1\cdot 8=18.
    $$

### 5.2 Determinante di matrici triangolari e diagonali

- Per le matrici triangolari (superiori o inferiori), il determinante ha una forma particolarmente semplice: è il prodotto degli elementi diagonali.

!!! chiave ""

    Se \(\boldsymbol U \in \R^{n \times n}\) è una <strong>matrice triangolare superiore</strong>, allora

    \begin{equation}
    \det(\boldsymbol U) = \prod_{i=1}^{n} u_{ii}.
    \end{equation}

!!! chiave ""

    Se \(\boldsymbol L \in \R^{n \times n}\) è una <strong>matrice triangolare inferiore</strong>, allora

    \begin{equation}
    \det(\boldsymbol L) = \prod_{i=1}^{n} \ell_{ii}.
    \end{equation}

- In particolare, per una <strong>matrice diagonale</strong> \(\boldsymbol D  \in \R^{n \times n}\):

    $$
    \det(\boldsymbol D)  = \prod_{i=1}^{n} d_{ii}.
    $$

- Per la <strong>matrice identità</strong> \(\boldsymbol I_n\):

    $$
    \det(\boldsymbol I_n) = 1.
    $$

<a id="box-exDetUpperTriangular-28"></a>

!!! esempio "Esempio 18: Determinante di una matrice triangolare superiore"

    Sia

    $$
    \boldsymbol U=
    \begin{pmatrix}
    2 & 3 & -1\\
    0 & -4 & 5\\
    0 & 0 & 3
    \end{pmatrix}.
    $$

    Allora

    $$
    \det(\boldsymbol U) = 2 \cdot (-4) \cdot 3 = -24.
    $$

<a id="box-exDetLowerTriangular-29"></a>

!!! esempio "Esempio 19: Determinante di una matrice triangolare inferiore"

    Sia

    $$
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0 & 0\\
    2 & 3 & 0\\
    -1 & 4 & -2
    \end{pmatrix}.
    $$

    Allora

    $$
    \det(\boldsymbol L) = 1 \cdot 3 \cdot (-2) = -6.
    $$

<a id="box-exDetDiagonal-30"></a>

!!! esempio "Esempio 20: Determinante di una matrice diagonale"

    Sia

    $$
    \boldsymbol D=
    \begin{pmatrix}
    5 & 0 & 0\\
    0 & -2 & 0\\
    0 & 0 & 3
    \end{pmatrix}.
    $$

    Allora

    $$
    \det(\boldsymbol D) = 5 \cdot (-2) \cdot 3 = -30.
    $$

### 5.3 Proprietà del determinante

- Il determinante soddisfa diverse importanti proprietà algebriche che ne rendono più efficienti il calcolo e l'utilizzo.

!!! chiave ""

    Siano \(\boldsymbol A, \boldsymbol B \in \R^{n \times n}\) matrici quadrate e \(\lambda \in \R\) uno scalare. Allora:

    \begin{equation}
    \det(\boldsymbol A \boldsymbol B) = \det(\boldsymbol A) \cdot \det(\boldsymbol B)
    \label{det_prod}
    \end{equation}

    \begin{equation}
    \det(\boldsymbol A') = \det(\boldsymbol A)
    \label{det_transpose}
    \end{equation}

    \begin{equation}
    \det(\lambda \boldsymbol A) = \lambda^n \det(\boldsymbol A)
    \label{det_scalar}
    \end{equation}

    \begin{equation}
    \det(\boldsymbol A^{-1}) = \frac{1}{\det(\boldsymbol A)}, \quad \text{se } \boldsymbol A \text{ è invertibile}
    \label{det_inverse}
    \end{equation}

    \begin{equation}
    \det(\boldsymbol I_n) = 1
    \label{det_identity}
    \end{equation}

- Dalle proprietà \(\eqref{det_prod}\) e \(\eqref{det_identity}\), se \(\boldsymbol A\) è invertibile:

    $$
    \det(\boldsymbol A) \cdot \det(\boldsymbol A^{-1}) = \det(\boldsymbol A \boldsymbol A^{-1}) = \det(\boldsymbol I_n) = 1,
    $$

    da cui segue la proprietà \(\eqref{det_inverse}\).

- La proprietà \(\eqref{det_scalar}\) mostra che il prodotto per uno scalare agisce sul determinante tramite la potenza \(n\)-esima dello scalare (non linearmente).

- La proprietà \(\eqref{det_transpose}\) implica che le operazioni sulle righe e quelle sulle colonne hanno effetti simmetrici sul determinante.

<a id="box-exDetProduct-31"></a>

!!! esempio "Esempio 21: Determinante di un prodotto"

    Siano

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1\\
    0 & 3
    \end{pmatrix},
    \qquad
    \boldsymbol B=
    \begin{pmatrix}
    1 & -1\\
    4 & 2
    \end{pmatrix}.
    $$

    Si ha:

    $$
    \det(\boldsymbol A) = 2 \cdot 3 - 1 \cdot 0 = 6,
    \qquad
    \det(\boldsymbol B) = 1 \cdot 2 - (-1) \cdot 4 = 6.
    $$

    Il prodotto è:

    $$
    \boldsymbol A \boldsymbol B
    =
    \begin{pmatrix}
    2 & 1\\
    0 & 3
    \end{pmatrix}
    \begin{pmatrix}
    1 & -1\\
    4 & 2
    \end{pmatrix}
    =
    \begin{pmatrix}
    6 & 0\\
    12 & 6
    \end{pmatrix}.
    $$

    Allora:

    $$
    \det(\boldsymbol A \boldsymbol B) = 6 \cdot 6 - 0 \cdot 12 = 36 = \det(\boldsymbol A) \cdot \det(\boldsymbol B).
    $$

<a id="box-exDetTranspose-32"></a>

!!! esempio "Esempio 22: Determinante della trasposta"

    Siano

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix},
    \qquad
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 3\\
    2 & 4
    \end{pmatrix}.
    $$

    Si ha:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2,
    \qquad
    \det(\boldsymbol A') = 1 \cdot 4 - 3 \cdot 2 = -2.
    $$

    Pertanto, \(\det(\boldsymbol A') = \det(\boldsymbol A)\).

<a id="box-exDetScalar-33"></a>

!!! esempio "Esempio 23: Determinante del prodotto per uno scalare"

    Siano

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}
    \in \R^{2 \times 2},
    \qquad
    \lambda = 2.
    $$

    Allora:

    $$
    \lambda \boldsymbol A
    =
    \begin{pmatrix}
    2 & 4\\
    6 & 8
    \end{pmatrix}.
    $$

    Si ha:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2,
    \qquad
    \det(\lambda \boldsymbol A) = 2 \cdot 8 - 4 \cdot 6 = -8.
    $$

    Poiché \(n=2\), verifichiamo:

    $$
    \det(\lambda \boldsymbol A) = -8 = 2^2 \cdot (-2) = \lambda^2 \det(\boldsymbol A).
    $$

<a id="box-exDetInverse-34"></a>

!!! esempio "Esempio 24: Determinante dell'inversa"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1\\
    1 & 1
    \end{pmatrix}.
    $$

    Si ha:

    $$
    \det(\boldsymbol A) = 2 \cdot 1 - 1 \cdot 1 = 1.
    $$

    La matrice inversa è:

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    1 & -1\\
    -1 & 2
    \end{pmatrix}.
    $$

    Allora:

    $$
    \det(\boldsymbol A^{-1}) = 1 \cdot 2 - (-1) \cdot (-1) = 1 = \frac{1}{\det(\boldsymbol A)}.
    $$

!!! chiave ""

    Una matrice \( \boldsymbol A \) è invertibile se e solo se \( \det(\boldsymbol A)\neq 0 \).

!!! interattivo "Provalo nel laboratorio"

    lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi.

<div class="la-tool" data-tool="det" data-matrix="1,2,0;3,1,4;2,-1,1"></div>

## 6. Rango

<a id="box-defRank-35"></a>

!!! definizione "Definizione 11: rango di una matrice"

    Sia \( \boldsymbol A \in \R^{m\times n} \). Il <strong>rango</strong> di \( \boldsymbol A \), denotato con \( \mathrm{rank}(\boldsymbol A) \), è il numero massimo di colonne linearmente indipendenti di \( \boldsymbol A \).

- Le colonne di \(\boldsymbol A\) sono vettori di \(\R^{m}\), e l'indipendenza lineare è intesa nel senso della definizione data nel capitolo sui vettori: \(\boldsymbol v_1,\dots,\boldsymbol v_k\) sono linearmente indipendenti se \(\lambda_1\boldsymbol v_1+\dots+\lambda_k\boldsymbol v_k=\boldsymbol 0\) implica \(\lambda_1=\dots=\lambda_k=0\).

- Equivalentemente, \( \mathrm{rank}(\boldsymbol A) \) è il numero massimo di righe linearmente indipendenti di \( \boldsymbol A \).

- Si ha sempre

    $$
    \mathrm{rank}(\boldsymbol A)\le \min\{m,n\}.
    $$

- Se \( \boldsymbol A \in \R^{n\times n} \) è quadrata, allora

    $$
    \mathrm{rank}(\boldsymbol A)=n
    \quad \Longleftrightarrow \quad
    \det(\boldsymbol A)\neq 0.
    $$

<a id="box-exRank2x3-36"></a>

!!! esempio "Esempio 25: rango di una matrice"

    Sia

    $$
    \boldsymbol B=
    \begin{pmatrix}
    1 & 2 & 3\\
    2 & 4 & 6
    \end{pmatrix}\in\R^{2\times 3}.
    $$

    La seconda riga è un multiplo della prima:

    $$
    \begin{pmatrix}2 & 4 & 6\end{pmatrix}
    =2\begin{pmatrix}1 & 2 & 3\end{pmatrix}.
    $$

    Quindi le due righe sono linearmente dipendenti, e c'è una sola riga linearmente indipendente. Pertanto,

    $$
    \mathrm{rank}(\boldsymbol B)=1.
    $$

<a id="box-exRank3x3-37"></a>

!!! esempio "Esempio 26: rango di una matrice \(3\times 3\)"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 0 & 1\\
    2 & 1 & 3\\
    0 & 1 & 1
    \end{pmatrix}\in\R^{3\times 3}.
    $$

    La terza colonna è la somma delle prime due:

    $$
    C_3(\boldsymbol A)=
    \begin{pmatrix}1\\3\\1\end{pmatrix}
    =
    \begin{pmatrix}1\\2\\0\end{pmatrix}
    +
    \begin{pmatrix}0\\1\\1\end{pmatrix}
    =C_1(\boldsymbol A)+C_2(\boldsymbol A),
    $$

    quindi le tre colonne sono linearmente dipendenti e \(\mathrm{rank}(\boldsymbol A)\le 2\). D'altra parte, le prime due colonne sono linearmente indipendenti: \(\lambda_1 C_1(\boldsymbol A)+\lambda_2 C_2(\boldsymbol A)=\boldsymbol 0\) dà \(\lambda_1=0\) (primo elemento) e \(\lambda_2=0\) (terzo elemento). Pertanto,

    $$
    \mathrm{rank}(\boldsymbol A)=2.
    $$

    Coerentemente, sviluppando lungo la prima riga, \(\det(\boldsymbol A)=1\cdot(1\cdot 1-3\cdot 1)-0+1\cdot(2\cdot 1-1\cdot 0)=-2+2=0\).

!!! interattivo "Provalo nel laboratorio"

    lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi.

<div class="la-tool" data-tool="rango" data-matrix="1,2,3;2,4,6"></div>

