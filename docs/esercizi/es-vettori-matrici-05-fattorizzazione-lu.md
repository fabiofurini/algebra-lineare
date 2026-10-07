---
title: "Fattorizzazione di matrici"
---

# Fattorizzazione di matrici

<div class="info-capitolo" markdown>

**Esercizi · Vettori e matrici** · con le soluzioni svolte · [:material-file-pdf-box: PDF](../pdf/es-vettori-matrici-05-fattorizzazione-lu.pdf)

</div>

<a id="box-exe_fac_lu_2x2-1"></a>

!!! esercizio "Esercizio 1"

    Calcolare la fattorizzazione LU di \( \boldsymbol A= \begin{pmatrix} 4 & 3\\ 6 & 3 \end{pmatrix} \) e verificare che \(\boldsymbol L\boldsymbol U = \boldsymbol A\).

??? soluzione "Soluzione"

    Il primo pivot è \(a_{11} = 4\) e il moltiplicatore è \(\ell_{21} = \frac{6}{4} = \frac{3}{2}\):

    \begin{align*}
    &\left(
    \begin{array}{cc}
     4 & 3 \\
     6 & 3 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{cc}
     4 & 3 \\[1ex]
     0 & -\tfrac{3}{2} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - \tfrac{3}{2}R_1 \text{)}
    \end{align*}

    Quindi

    $$
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0\\[0.5ex]
    \tfrac{3}{2} & 1
    \end{pmatrix},
    \qquad
    \boldsymbol U=
    \begin{pmatrix}
    4 & 3\\[0.5ex]
    0 & -\tfrac{3}{2}
    \end{pmatrix},
    \qquad
    \boldsymbol L\boldsymbol U=
    \begin{pmatrix}
    4 & 3\\[0.5ex]
    \tfrac{3}{2}\cdot 4 & \tfrac{3}{2}\cdot 3 - \tfrac{3}{2}
    \end{pmatrix}
    =
    \begin{pmatrix}
    4 & 3\\
    6 & 3
    \end{pmatrix}
    = \boldsymbol A.
    $$

<a id="box-exe_fac_lu_3x3-2"></a>

!!! esercizio "Esercizio 2"

    Calcolare la fattorizzazione LU di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    2 & 5 & 7\\
    3 & 8 & 13
    \end{pmatrix}
    $$

    e verificare che \(\boldsymbol L\boldsymbol U = \boldsymbol A\).

??? soluzione "Soluzione"

    I moltiplicatori sono \(\ell_{21} = \frac{2}{1} = 2\), \(\ell_{31} = \frac{3}{1} = 3\) e, dopo il primo passo, \(\ell_{32} = \frac{2}{1} = 2\):

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     2 & 5 & 7 \\
     3 & 8 & 13 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     0 & 1 & 1 \\
     3 & 8 & 13 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     0 & 1 & 1 \\
     0 & 2 & 4 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 3R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     0 & 1 & 1 \\
     0 & 0 & 2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_2 \text{)}
    \end{align*}

    Quindi

    $$
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0 & 0\\
    2 & 1 & 0\\
    3 & 2 & 1
    \end{pmatrix},
    \qquad
    \boldsymbol U=
    \begin{pmatrix}
    1 & 2 & 3\\
    0 & 1 & 1\\
    0 & 0 & 2
    \end{pmatrix}.
    $$

    Verifica:

    $$
    \boldsymbol L\boldsymbol U=
    \begin{pmatrix}
    1 & 2 & 3\\
    2 & 4+1 & 6+1\\
    3 & 6+2 & 9+2+2
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & 2 & 3\\
    2 & 5 & 7\\
    3 & 8 & 13
    \end{pmatrix}
    = \boldsymbol A.
    $$

<a id="box-exe_fac_lu_minors-3"></a>

!!! esercizio "Esercizio 3"

    Si consideri

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 4 & -2\\
    1 & -1 & 5\\
    -1 & 7 & 1
    \end{pmatrix}.
    $$

    1. Verificare, mediante i minori principali di testa, che \(\boldsymbol A\) ammette una fattorizzazione LU senza scambi di righe.

    2. Calcolare la fattorizzazione LU e verificare che i pivot sono \(u_{kk} = \det(\boldsymbol A_{[k]})/\det(\boldsymbol A_{[k-1]})\).

??? soluzione "Soluzione"

    1. \(\det(\boldsymbol A_{[1]}) = 2\), \(\det(\boldsymbol A_{[2]}) = 2\cdot(-1) - 4\cdot 1 = -6\) e, sviluppando con Laplace lungo la prima riga,

        $$
        \det(\boldsymbol A_{[3]}) = \det(\boldsymbol A) = 2\cdot(-1-35) - 4\cdot(1+5) + (-2)\cdot(7-1) = -72 - 24 - 12 = -108.
        $$

        Tutti i minori principali di testa sono non nulli, quindi la fattorizzazione LU esiste.

    2. I moltiplicatori sono \(\ell_{21} = \frac{1}{2}\), \(\ell_{31} = \frac{-1}{2} = -\frac{1}{2}\) e, dopo il primo passo, \(\ell_{32} = \frac{9}{-3} = -3\):

        \begin{align*}
        &\left(
        \begin{array}{ccc}
         2 & 4 & -2 \\
         1 & -1 & 5 \\
         -1 & 7 & 1 \\
        \end{array}
        \right) \\[2ex]
        &\left(
        \begin{array}{ccc}
         2 & 4 & -2 \\
         0 & -3 & 6 \\
         -1 & 7 & 1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - \tfrac{1}{2}R_1 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc}
         2 & 4 & -2 \\
         0 & -3 & 6 \\
         0 & 9 & 0 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + \tfrac{1}{2}R_1 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc}
         2 & 4 & -2 \\
         0 & -3 & 6 \\
         0 & 0 & 18 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + 3R_2 \text{)}
        \end{align*}

        Quindi

        $$
        \boldsymbol L=
        \begin{pmatrix}
        1 & 0 & 0\\[0.5ex]
        \tfrac{1}{2} & 1 & 0\\[0.5ex]
        -\tfrac{1}{2} & -3 & 1
        \end{pmatrix},
        \qquad
        \boldsymbol U=
        \begin{pmatrix}
        2 & 4 & -2\\
        0 & -3 & 6\\
        0 & 0 & 18
        \end{pmatrix}.
        $$

        Infatti \(u_{11} = 2\), \(u_{22} = \frac{-6}{2} = -3\) e \(u_{33} = \frac{-108}{-6} = 18\). Verifica:

        $$
        \boldsymbol L\boldsymbol U=
        \begin{pmatrix}
        2 & 4 & -2\\
        1 & 2-3 & -1+6\\
        -1 & -2+9 & 1-18+18
        \end{pmatrix}
        =
        \begin{pmatrix}
        2 & 4 & -2\\
        1 & -1 & 5\\
        -1 & 7 & 1
        \end{pmatrix}
        = \boldsymbol A.
        $$

<a id="box-exe_fac_plu_step2-4"></a>

!!! esercizio "Esercizio 4"

    Si consideri

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0\\
    2 & 4 & 1\\
    0 & 1 & 1
    \end{pmatrix}.
    $$

    Mostrare che \(\boldsymbol A\) è non singolare ma non ammette una fattorizzazione LU senza scambi di righe. Calcolare quindi una fattorizzazione PLU \(\boldsymbol P\boldsymbol A = \boldsymbol L\boldsymbol U\) e verificarla.

??? soluzione "Soluzione"

    Si ha \(\det(\boldsymbol A) = 1\cdot(4-1) - 2\cdot(2-0) + 0 = -1 \neq 0\), ma \(\det(\boldsymbol A_{[2]}) = 1\cdot 4 - 2\cdot 2 = 0\): la fattorizzazione LU senza scambi di righe non esiste.

    Eliminazione di Gauss: \(\ell_{21} = 2\) e \(\ell_{31} = 0\) (l'elemento \(a_{31}\) è già nullo). A questo punto l'elemento in posizione \((2,2)\) è nullo e scambiamo le righe 2 e 3, scambiando anche i moltiplicatori (ora \(\ell_{21} = 0\), \(\ell_{31} = 2\)):

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     1 & 2 & 0 \\
     2 & 4 & 1 \\
     0 & 1 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 0 \\
     0 & 0 & 1 \\
     0 & 1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 0 \\
     0 & 1 & 1 \\
     0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftrightarrow R_3 \text{)}
    \end{align*}

    L'elemento al di sotto del secondo pivot è già nullo, quindi \(\ell_{32} = 0\). Quindi

    $$
    \boldsymbol P=
    \begin{pmatrix}
    1 & 0 & 0\\
    0 & 0 & 1\\
    0 & 1 & 0
    \end{pmatrix},
    \qquad
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    2 & 0 & 1
    \end{pmatrix},
    \qquad
    \boldsymbol U=
    \begin{pmatrix}
    1 & 2 & 0\\
    0 & 1 & 1\\
    0 & 0 & 1
    \end{pmatrix}.
    $$

    Verifica:

    $$
    \boldsymbol P\boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0\\
    0 & 1 & 1\\
    2 & 4 & 1
    \end{pmatrix},
    \qquad
    \boldsymbol L\boldsymbol U=
    \begin{pmatrix}
    1 & 2 & 0\\
    0 & 1 & 1\\
    2 & 4 & 0+1
    \end{pmatrix}
    = \boldsymbol P\boldsymbol A.
    $$

<a id="box-exe_fac_plu_step1-5"></a>

!!! esercizio "Esercizio 5"

    Calcolare una fattorizzazione PLU di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 1 & 1\\
    2 & 1 & 3\\
    4 & 5 & 4
    \end{pmatrix},
    $$

    verificare che \(\boldsymbol P\boldsymbol A = \boldsymbol L\boldsymbol U\) e calcolare \(\det(\boldsymbol A)\) a partire da \(\boldsymbol U\).

??? soluzione "Soluzione"

    Poiché \(a_{11} = 0\), scambiamo le righe 1 e 2 (non è stato ancora calcolato alcun moltiplicatore). Allora \(\ell_{21} = \frac{0}{2} = 0\), \(\ell_{31} = \frac{4}{2} = 2\) e, dopo il primo passo, \(\ell_{32} = \frac{3}{1} = 3\):

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     0 & 1 & 1 \\
     2 & 1 & 3 \\
     4 & 5 & 4 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 3 \\
     0 & 1 & 1 \\
     4 & 5 & 4 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftrightarrow R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 3 \\
     0 & 1 & 1 \\
     0 & 3 & -2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 3 \\
     0 & 1 & 1 \\
     0 & 0 & -5 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 3R_2 \text{)}
    \end{align*}

    Quindi

    $$
    \boldsymbol P=
    \begin{pmatrix}
    0 & 1 & 0\\
    1 & 0 & 0\\
    0 & 0 & 1
    \end{pmatrix},
    \qquad
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    2 & 3 & 1
    \end{pmatrix},
    \qquad
    \boldsymbol U=
    \begin{pmatrix}
    2 & 1 & 3\\
    0 & 1 & 1\\
    0 & 0 & -5
    \end{pmatrix}.
    $$

    Verifica:

    $$
    \boldsymbol P\boldsymbol A=
    \begin{pmatrix}
    2 & 1 & 3\\
    0 & 1 & 1\\
    4 & 5 & 4
    \end{pmatrix},
    \qquad
    \boldsymbol L\boldsymbol U=
    \begin{pmatrix}
    2 & 1 & 3\\
    0 & 1 & 1\\
    4 & 2+3 & 6+3-5
    \end{pmatrix}
    = \boldsymbol P\boldsymbol A.
    $$

    È stato effettuato uno scambio di righe (\(s=1\)), quindi \(\det(\boldsymbol A) = -(2\cdot 1\cdot(-5)) = 10\).

<a id="box-exe_fac_det_from_u-6"></a>

!!! esercizio "Esercizio 6"

    Calcolare la fattorizzazione LU di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    3 & 1 & 2\\
    6 & 3 & 4\\
    3 & 1 & 5
    \end{pmatrix}
    $$

    e utilizzarla per calcolare \(\det(\boldsymbol A)\) e \(\det(\boldsymbol A^{-1})\).

??? soluzione "Soluzione"

    I moltiplicatori sono \(\ell_{21} = \frac{6}{3} = 2\) e \(\ell_{31} = \frac{3}{3} = 1\):

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     3 & 1 & 2 \\
     6 & 3 & 4 \\
     3 & 1 & 5 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     3 & 1 & 2 \\
     0 & 1 & 0 \\
     3 & 1 & 5 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     3 & 1 & 2 \\
     0 & 1 & 0 \\
     0 & 0 & 3 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_1 \text{)}
    \end{align*}

    L'elemento in posizione \((3,2)\) è già nullo, quindi \(\ell_{32} = 0\) e

    $$
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0 & 0\\
    2 & 1 & 0\\
    1 & 0 & 1
    \end{pmatrix},
    \qquad
    \boldsymbol U=
    \begin{pmatrix}
    3 & 1 & 2\\
    0 & 1 & 0\\
    0 & 0 & 3
    \end{pmatrix}.
    $$

    Non sono stati effettuati scambi di righe, quindi

    $$
    \det(\boldsymbol A) = \det(\boldsymbol L)\det(\boldsymbol U) = 1\cdot(3\cdot 1\cdot 3) = 9,
    \qquad
    \det(\boldsymbol A^{-1}) = \frac{1}{9}.
    $$

<a id="box-exe_fac_parametric-7"></a>

!!! esercizio "Esercizio 7"

    Si consideri, per \(k\in\R\), la matrice

    $$
    \boldsymbol A(k)=
    \begin{pmatrix}
    1 & 1 & 0\\
    1 & k & 1\\
    0 & 1 & 1
    \end{pmatrix}.
    $$

    1. Per quali valori di \(k\) la matrice \(\boldsymbol A(k)\) è non singolare e ammette una fattorizzazione LU senza scambi di righe? Calcolarla.

    2. Per \(k = 1\), calcolare una fattorizzazione PLU.

??? soluzione "Soluzione"

    1. I minori principali di testa sono

        $$
        \det(\boldsymbol A_{[1]}) = 1,
        \quad
        \det(\boldsymbol A_{[2]}) = k - 1,
        \quad
        \det(\boldsymbol A_{[3]}) = 1\cdot(k-1) - 1\cdot(1-0) + 0 = k-2.
        $$

        Sono tutti non nulli se e solo se \(k\neq 1\) e \(k\neq 2\). Per tali valori, \(\ell_{21} = 1\), \(\ell_{31} = 0\) e \(\ell_{32} = \frac{1}{k-1}\):

        \begin{align*}
        &\left(
        \begin{array}{ccc}
         1 & 1 & 0 \\
         0 & k-1 & 1 \\
         0 & 1 & 1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_1 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc}
         1 & 1 & 0 \\
         0 & k-1 & 1 \\
         0 & 0 & \tfrac{k-2}{k-1} \\
        \end{array}
        \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - \tfrac{1}{k-1}R_2 \text{)}
        \end{align*}

        poiché \(1 - \frac{1}{k-1} = \frac{k-2}{k-1}\). Quindi

        $$
        \boldsymbol L=
        \begin{pmatrix}
        1 & 0 & 0\\[0.5ex]
        1 & 1 & 0\\[0.5ex]
        0 & \tfrac{1}{k-1} & 1
        \end{pmatrix},
        \qquad
        \boldsymbol U=
        \begin{pmatrix}
        1 & 1 & 0\\[0.5ex]
        0 & k-1 & 1\\[0.5ex]
        0 & 0 & \tfrac{k-2}{k-1}
        \end{pmatrix},
        $$

        e infatti \(u_{11}u_{22}u_{33} = k-2 = \det(\boldsymbol A(k))\). Per \(k=2\) la matrice è singolare.

    2. Per \(k=1\) si ha \(\det(\boldsymbol A(1)) = -1 \neq 0\) ma \(\det(\boldsymbol A_{[2]}) = 0\). Dopo \(R_2 \leftarrow R_2 - R_1\) (\(\ell_{21} = 1\), \(\ell_{31} = 0\)) l'elemento in posizione \((2,2)\) è nullo, quindi scambiamo le righe 2 e 3 insieme ai rispettivi moltiplicatori (ora \(\ell_{21} = 0\), \(\ell_{31} = 1\)):

        \begin{align*}
        &\left(
        \begin{array}{ccc}
         1 & 1 & 0 \\
         1 & 1 & 1 \\
         0 & 1 & 1 \\
        \end{array}
        \right) \\[2ex]
        &\left(
        \begin{array}{ccc}
         1 & 1 & 0 \\
         0 & 0 & 1 \\
         0 & 1 & 1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_1 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc}
         1 & 1 & 0 \\
         0 & 1 & 1 \\
         0 & 0 & 1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_2 \leftrightarrow R_3 \text{)}
        \end{align*}

        Allora \(\ell_{32} = 0\) e

        $$
        \boldsymbol P=
        \begin{pmatrix}
        1 & 0 & 0\\
        0 & 0 & 1\\
        0 & 1 & 0
        \end{pmatrix},
        \quad
        \boldsymbol L=
        \begin{pmatrix}
        1 & 0 & 0\\
        0 & 1 & 0\\
        1 & 0 & 1
        \end{pmatrix},
        \quad
        \boldsymbol U=
        \begin{pmatrix}
        1 & 1 & 0\\
        0 & 1 & 1\\
        0 & 0 & 1
        \end{pmatrix},
        $$

        e

        $$
        \boldsymbol P\boldsymbol A(1) = \boldsymbol L\boldsymbol U =
        \begin{pmatrix}
        1 & 1 & 0\\
        0 & 1 & 1\\
        1 & 1 & 1
        \end{pmatrix}.
        $$
