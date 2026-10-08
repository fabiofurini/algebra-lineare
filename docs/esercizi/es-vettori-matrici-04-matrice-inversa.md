---
title: "Inversione di matrici"
---

# Inversione di matrici

<div class="info-capitolo" markdown>

**Esercizi · Vettori e matrici** · capitolo [4.3 · Inversione di matrici](../vettori-matrici/04-matrice-inversa.md) · con le soluzioni svolte · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf)

</div>

<a id="box-exe_inv_2x2_formula-1"></a>

!!! esercizio "Esercizio 1"

    Usando la formula per l'inversa di una matrice \(2\times 2\), calcolare (se esiste) l'inversa di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    3 & 5\\
    1 & 2
    \end{pmatrix},
    \qquad
    \boldsymbol B=
    \begin{pmatrix}
    4 & 2\\
    3 & 4
    \end{pmatrix},
    \qquad
    \boldsymbol C=
    \begin{pmatrix}
    2 & 4\\
    3 & 6
    \end{pmatrix}.
    $$

??? soluzione "Soluzione"

    Ricordiamo che, se \(ad-bc\neq 0\), \(\begin{pmatrix} a & b\\ c & d\end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b\\ -c & a\end{pmatrix}\).

    - \(\det(\boldsymbol A) = 3\cdot 2 - 5\cdot 1 = 1\), quindi

        $$
        \boldsymbol A^{-1} = \begin{pmatrix} 2 & -5\\ -1 & 3\end{pmatrix}.
        \qquad
        \text{Verifica: }
        \begin{pmatrix} 3 & 5\\ 1 & 2\end{pmatrix}\begin{pmatrix} 2 & -5\\ -1 & 3\end{pmatrix}
        = \begin{pmatrix} 6-5 & -15+15\\ 2-2 & -5+6\end{pmatrix} = \boldsymbol I.
        $$

    - \(\det(\boldsymbol B) = 4\cdot 4 - 2\cdot 3 = 10\), quindi

        $$
        \boldsymbol B^{-1} = \frac{1}{10}\begin{pmatrix} 4 & -2\\ -3 & 4\end{pmatrix}
        = \begin{pmatrix} \tfrac{2}{5} & -\tfrac{1}{5}\\[0.8ex] -\tfrac{3}{10} & \tfrac{2}{5}\end{pmatrix}.
        $$

    - \(\det(\boldsymbol C) = 2\cdot 6 - 4\cdot 3 = 0\): la matrice \(\boldsymbol C\) è singolare e \(\boldsymbol C^{-1}\) non esiste (la seconda riga è \(\tfrac{3}{2}\) volte la prima).

<a id="box-exe_inv_gauss_jordan_3x3-2"></a>

!!! esercizio "Esercizio 2"

    Calcolare l'inversa di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 1 & 0\\
    1 & 2 & 1\\
    0 & 1 & 2
    \end{pmatrix}
    $$

    con il metodo di Gauss–Jordan e verificare il risultato.

??? soluzione "Soluzione"

    Applichiamo operazioni elementari di riga a \(\left(\boldsymbol A \mid \boldsymbol I\right)\):

    \begin{align*}
    &\left(
    \begin{array}{ccc|ccc}
     1 & 1 & 0 & 1 & 0 & 0 \\
     1 & 2 & 1 & 0 & 1 & 0 \\
     0 & 1 & 2 & 0 & 0 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 1 & 0 & 1 & 0 & 0 \\
     0 & 1 & 1 & -1 & 1 & 0 \\
     0 & 1 & 2 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -1 & 2 & -1 & 0 \\
     0 & 1 & 1 & -1 & 1 & 0 \\
     0 & 1 & 2 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -1 & 2 & -1 & 0 \\
     0 & 1 & 1 & -1 & 1 & 0 \\
     0 & 0 & 1 & 1 & -1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & 3 & -2 & 1 \\
     0 & 1 & 1 & -1 & 1 & 0 \\
     0 & 0 & 1 & 1 & -1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 + R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & 3 & -2 & 1 \\
     0 & 1 & 0 & -2 & 2 & -1 \\
     0 & 0 & 1 & 1 & -1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_3 \text{)}
    \end{align*}

    Quindi

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    3 & -2 & 1\\
    -2 & 2 & -1\\
    1 & -1 & 1
    \end{pmatrix}.
    $$

    Verifica (prodotto righe per colonne): \(\boldsymbol A\boldsymbol A^{-1} = \begin{pmatrix} 3-2 & -2+2 & 1-1\\ 3-4+1 & -2+4-1 & 1-2+1\\ -2+2 & 2-2 & -1+2 \end{pmatrix} = \boldsymbol I\).

<a id="box-exe_inv_gauss_jordan_swap-3"></a>

!!! esercizio "Esercizio 3"

    Calcolare l'inversa di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 2 & 1\\
    1 & 1 & 0\\
    2 & 3 & 1
    \end{pmatrix}
    $$

    con il metodo di Gauss–Jordan.

??? soluzione "Soluzione"

    Poiché \(a_{11}=0\), iniziamo con uno scambio di righe. Successivamente, scambiamo le righe 2 e 3 per ottenere un pivot uguale a \(1\) (ed evitare le frazioni):

    \begin{align*}
    &\left(
    \begin{array}{ccc|ccc}
     0 & 2 & 1 & 1 & 0 & 0 \\
     1 & 1 & 0 & 0 & 1 & 0 \\
     2 & 3 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 1 & 0 & 0 & 1 & 0 \\
     0 & 2 & 1 & 1 & 0 & 0 \\
     2 & 3 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftrightarrow R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 1 & 0 & 0 & 1 & 0 \\
     0 & 2 & 1 & 1 & 0 & 0 \\
     0 & 1 & 1 & 0 & -2 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 1 & 0 & 0 & 1 & 0 \\
     0 & 1 & 1 & 0 & -2 & 1 \\
     0 & 2 & 1 & 1 & 0 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftrightarrow R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -1 & 0 & 3 & -1 \\
     0 & 1 & 1 & 0 & -2 & 1 \\
     0 & 2 & 1 & 1 & 0 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -1 & 0 & 3 & -1 \\
     0 & 1 & 1 & 0 & -2 & 1 \\
     0 & 0 & -1 & 1 & 4 & -2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -1 & 0 & 3 & -1 \\
     0 & 1 & 1 & 0 & -2 & 1 \\
     0 & 0 & 1 & -1 & -4 & 2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow -R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & -1 & -1 & 1 \\
     0 & 1 & 1 & 0 & -2 & 1 \\
     0 & 0 & 1 & -1 & -4 & 2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 + R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & -1 & -1 & 1 \\
     0 & 1 & 0 & 1 & 2 & -1 \\
     0 & 0 & 1 & -1 & -4 & 2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_3 \text{)}
    \end{align*}

    Quindi

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    -1 & -1 & 1\\
    1 & 2 & -1\\
    -1 & -4 & 2
    \end{pmatrix}.
    $$

<a id="box-exe_inv_singular-4"></a>

!!! esercizio "Esercizio 4"

    Applicare il metodo di Gauss–Jordan a

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & -1\\
    2 & 3 & 1\\
    3 & 5 & 0
    \end{pmatrix}.
    $$

    La matrice \(\boldsymbol A\) è invertibile?

??? soluzione "Soluzione"

    \begin{align*}
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & -1 & 1 & 0 & 0 \\
     2 & 3 & 1 & 0 & 1 & 0 \\
     3 & 5 & 0 & 0 & 0 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & -1 & 1 & 0 & 0 \\
     0 & -1 & 3 & -2 & 1 & 0 \\
     3 & 5 & 0 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & -1 & 1 & 0 & 0 \\
     0 & -1 & 3 & -2 & 1 & 0 \\
     0 & -1 & 3 & -3 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 3R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & -1 & 1 & 0 & 0 \\
     0 & -1 & 3 & -2 & 1 & 0 \\
     0 & 0 & 0 & -1 & -1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_2 \text{)}
    \end{align*}

    Nel blocco sinistro compare una riga nulla: il metodo si arresta e \(\boldsymbol A\) <strong>non è invertibile</strong>. Infatti, la terza riga di \(\boldsymbol A\) è la somma delle prime due righe, e

    $$
    \det(\boldsymbol A) = 1\cdot(0-5) - 2\cdot(0-3) + (-1)\cdot(10-9) = -5 + 6 - 1 = 0.
    $$

<a id="box-exe_inv_parametric_3x3-5"></a>

!!! esercizio "Esercizio 5"

    Si consideri, per \(k\in\R\), la matrice

    $$
    \boldsymbol A(k)=
    \begin{pmatrix}
    1 & 1 & 1\\
    1 & k & 1\\
    1 & 1 & k^2
    \end{pmatrix}.
    $$

    1. Per quali valori di \(k\) la matrice \(\boldsymbol A(k)\) è invertibile?

    2. Calcolare \(\boldsymbol A(0)^{-1}\) con il metodo di Gauss–Jordan.

??? soluzione "Soluzione"

    1. Calcoliamo \(\det(\boldsymbol A(k))\) mediante eliminazione di Gauss (solo somme di multipli di righe):

        \begin{align*}
        &\left(
        \begin{array}{ccc}
         1 & 1 & 1 \\
         1 & k & 1 \\
         1 & 1 & k^2 \\
        \end{array}
        \right) \\[2ex]
        &\left(
        \begin{array}{ccc}
         1 & 1 & 1 \\
         0 & k-1 & 0 \\
         1 & 1 & k^2 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_1 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc}
         1 & 1 & 1 \\
         0 & k-1 & 0 \\
         0 & 0 & k^2-1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_1 \text{)}
        \end{align*}

        L'ultima matrice è triangolare superiore, quindi

        $$
        \det(\boldsymbol A(k)) = 1\cdot(k-1)\cdot(k^2-1) = (k-1)^2(k+1).
        $$

        Pertanto \(\boldsymbol A(k)\) è invertibile se e solo se \(k\neq 1\) e \(k\neq -1\).

    2. Per \(k=0\) si ha \(\det(\boldsymbol A(0)) = 1\), e:

        \begin{align*}
        &\left(
        \begin{array}{ccc|ccc}
         1 & 1 & 1 & 1 & 0 & 0 \\
         1 & 0 & 1 & 0 & 1 & 0 \\
         1 & 1 & 0 & 0 & 0 & 1 \\
        \end{array}
        \right) \\[2ex]
        &\left(
        \begin{array}{ccc|ccc}
         1 & 1 & 1 & 1 & 0 & 0 \\
         0 & -1 & 0 & -1 & 1 & 0 \\
         1 & 1 & 0 & 0 & 0 & 1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_1 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc|ccc}
         1 & 1 & 1 & 1 & 0 & 0 \\
         0 & -1 & 0 & -1 & 1 & 0 \\
         0 & 0 & -1 & -1 & 0 & 1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_1 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc|ccc}
         1 & 1 & 1 & 1 & 0 & 0 \\
         0 & 1 & 0 & 1 & -1 & 0 \\
         0 & 0 & -1 & -1 & 0 & 1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_2 \leftarrow -R_2 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc|ccc}
         1 & 1 & 1 & 1 & 0 & 0 \\
         0 & 1 & 0 & 1 & -1 & 0 \\
         0 & 0 & 1 & 1 & 0 & -1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_3 \leftarrow -R_3 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc|ccc}
         1 & 0 & 1 & 0 & 1 & 0 \\
         0 & 1 & 0 & 1 & -1 & 0 \\
         0 & 0 & 1 & 1 & 0 & -1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - R_2 \text{)} \\[2ex]
        &\left(
        \begin{array}{ccc|ccc}
         1 & 0 & 0 & -1 & 1 & 1 \\
         0 & 1 & 0 & 1 & -1 & 0 \\
         0 & 0 & 1 & 1 & 0 & -1 \\
        \end{array}
        \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - R_3 \text{)}
        \end{align*}

        Quindi

        $$
        \boldsymbol A(0)^{-1}=
        \begin{pmatrix}
        -1 & 1 & 1\\
        1 & -1 & 0\\
        1 & 0 & -1
        \end{pmatrix}.
        $$

<a id="box-exe_inv_parametric_2x2-6"></a>

!!! esercizio "Esercizio 6"

    Si consideri, per \(k\in\R\), la matrice \( \boldsymbol A(k)= \begin{pmatrix} k & 1\\ 4 & k \end{pmatrix}. \) Per quali valori di \(k\) la matrice \(\boldsymbol A(k)\) è invertibile? Per tali valori, scrivere \(\boldsymbol A(k)^{-1}\) e calcolare \(\boldsymbol A(3)^{-1}\).

??? soluzione "Soluzione"

    Si ha \(\det(\boldsymbol A(k)) = k^2 - 4 = (k-2)(k+2)\), quindi \(\boldsymbol A(k)\) è invertibile se e solo se \(k\neq 2\) e \(k\neq -2\). In questo caso

    $$
    \boldsymbol A(k)^{-1} = \frac{1}{k^2-4}
    \begin{pmatrix}
    k & -1\\
    -4 & k
    \end{pmatrix}.
    $$

    Per \(k=3\): \(\det(\boldsymbol A(3)) = 5\) e

    $$
    \boldsymbol A(3)^{-1} = \frac{1}{5}
    \begin{pmatrix}
    3 & -1\\
    -4 & 3
    \end{pmatrix}.
    $$

<a id="box-exe_inv_adjugate_3x3-7"></a>

!!! esercizio "Esercizio 7"

    Calcolare l'inversa di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 0 & 1\\
    1 & 1 & 0\\
    0 & 3 & 1
    \end{pmatrix}
    $$

    con la formula della matrice aggiunta (dei cofattori) \(\boldsymbol A^{-1} = \frac{1}{\det(\boldsymbol A)}\,\mathrm{adj}(\boldsymbol A)\).

??? soluzione "Soluzione"

    Sviluppo di Laplace lungo la prima riga: \(\det(\boldsymbol A) = 2\cdot(1-0) - 0 + 1\cdot(3-0) = 5\neq 0\). I cofattori \(C_{ij} = (-1)^{i+j}\det(\boldsymbol A_{ij})\) sono:

    \begin{align*}
    C_{11} &= +\det\begin{pmatrix} 1 & 0\\ 3 & 1\end{pmatrix} = 1, &
    C_{12} &= -\det\begin{pmatrix} 1 & 0\\ 0 & 1\end{pmatrix} = -1, &
    C_{13} &= +\det\begin{pmatrix} 1 & 1\\ 0 & 3\end{pmatrix} = 3,\\[1ex]
    C_{21} &= -\det\begin{pmatrix} 0 & 1\\ 3 & 1\end{pmatrix} = 3, &
    C_{22} &= +\det\begin{pmatrix} 2 & 1\\ 0 & 1\end{pmatrix} = 2, &
    C_{23} &= -\det\begin{pmatrix} 2 & 0\\ 0 & 3\end{pmatrix} = -6,\\[1ex]
    C_{31} &= +\det\begin{pmatrix} 0 & 1\\ 1 & 0\end{pmatrix} = -1, &
    C_{32} &= -\det\begin{pmatrix} 2 & 1\\ 1 & 0\end{pmatrix} = 1, &
    C_{33} &= +\det\begin{pmatrix} 2 & 0\\ 1 & 1\end{pmatrix} = 2.
    \end{align*}

    La matrice aggiunta è la trasposta della matrice dei cofattori:

    $$
    \mathrm{adj}(\boldsymbol A) =
    \begin{pmatrix}
    1 & -1 & 3\\
    3 & 2 & -6\\
    -1 & 1 & 2
    \end{pmatrix}'
    =
    \begin{pmatrix}
    1 & 3 & -1\\
    -1 & 2 & 1\\
    3 & -6 & 2
    \end{pmatrix},
    \qquad
    \boldsymbol A^{-1} = \frac{1}{5}
    \begin{pmatrix}
    1 & 3 & -1\\
    -1 & 2 & 1\\
    3 & -6 & 2
    \end{pmatrix}.
    $$

<a id="box-exe_inv_properties_product-8"></a>

!!! esercizio "Esercizio 8"

    Siano \( \boldsymbol A= \begin{pmatrix} 2 & 1\\ 1 & 1 \end{pmatrix} \) e \( \boldsymbol B= \begin{pmatrix} 1 & 2\\ 0 & 3 \end{pmatrix}. \)

    1. Calcolare \(\boldsymbol A^{-1}\), \(\boldsymbol B^{-1}\) e poi \((\boldsymbol A\boldsymbol B)^{-1}\) usando le proprietà dell'inversa. Verificare il risultato invertendo direttamente \(\boldsymbol A\boldsymbol B\).

    2. Mostrare che \(\boldsymbol A^{-1}\boldsymbol B^{-1} \neq (\boldsymbol A\boldsymbol B)^{-1}\).

    3. Calcolare \((\boldsymbol B')^{-1}\) e \(\det\big((\boldsymbol A\boldsymbol B)^{-1}\big)\).

??? soluzione "Soluzione"

    1. \(\det(\boldsymbol A) = 1\) e \(\det(\boldsymbol B) = 3\), quindi

        $$
        \boldsymbol A^{-1} = \begin{pmatrix} 1 & -1\\ -1 & 2\end{pmatrix},
        \qquad
        \boldsymbol B^{-1} = \frac{1}{3}\begin{pmatrix} 3 & -2\\ 0 & 1\end{pmatrix},
        $$

        $$
        (\boldsymbol A\boldsymbol B)^{-1} = \boldsymbol B^{-1}\boldsymbol A^{-1}
        = \frac{1}{3}\begin{pmatrix} 3 & -2\\ 0 & 1\end{pmatrix}\begin{pmatrix} 1 & -1\\ -1 & 2\end{pmatrix}
        = \frac{1}{3}\begin{pmatrix} 5 & -7\\ -1 & 2\end{pmatrix}.
        $$

        Verifica: \(\boldsymbol A\boldsymbol B = \begin{pmatrix} 2 & 7\\ 1 & 5\end{pmatrix}\), \(\det(\boldsymbol A\boldsymbol B) = 10-7 = 3\), e la formula per le matrici \(2\times 2\) fornisce \((\boldsymbol A\boldsymbol B)^{-1} = \frac{1}{3}\begin{pmatrix} 5 & -7\\ -1 & 2\end{pmatrix}\).

    2. \(\boldsymbol A^{-1}\boldsymbol B^{-1} = \frac{1}{3}\begin{pmatrix} 1 & -1\\ -1 & 2\end{pmatrix}\begin{pmatrix} 3 & -2\\ 0 & 1\end{pmatrix} = \frac{1}{3}\begin{pmatrix} 3 & -3\\ -3 & 4\end{pmatrix} \neq (\boldsymbol A\boldsymbol B)^{-1}\).

    3. \((\boldsymbol B')^{-1} = (\boldsymbol B^{-1})' = \frac{1}{3}\begin{pmatrix} 3 & 0\\ -2 & 1\end{pmatrix}\) (verifica con la formula per le matrici \(2\times 2\) applicata a \(\boldsymbol B' = \begin{pmatrix} 1 & 0\\ 2 & 3\end{pmatrix}\)). Inoltre

        $$
        \det\big((\boldsymbol A\boldsymbol B)^{-1}\big) = \frac{1}{\det(\boldsymbol A\boldsymbol B)} = \frac{1}{\det(\boldsymbol A)\det(\boldsymbol B)} = \frac{1}{3}.
        $$

<a id="box-exe_inv_properties_proofs-9"></a>

!!! esercizio "Esercizio 9"

    1. Siano \(\boldsymbol A\in\R^{n\times n}\) invertibile e \(\lambda\in\R\), \(\lambda\neq 0\). Mostrare che \(\lambda\boldsymbol A\) è invertibile e \((\lambda\boldsymbol A)^{-1} = \frac{1}{\lambda}\boldsymbol A^{-1}\).

    2. Sia \(\boldsymbol A\in\R^{n\times n}\) tale che \(\boldsymbol A^2 - 3\boldsymbol A + \boldsymbol I = \boldsymbol 0\). Mostrare che \(\boldsymbol A\) è invertibile e \(\boldsymbol A^{-1} = 3\boldsymbol I - \boldsymbol A\). Verificarlo per \(\boldsymbol A = \begin{pmatrix} 2 & 1\\ 1 & 1\end{pmatrix}\).

??? soluzione "Soluzione"

    1. Usando le proprietà del prodotto per uno scalare:

        $$
        (\lambda\boldsymbol A)\Big(\tfrac{1}{\lambda}\boldsymbol A^{-1}\Big) = \lambda\cdot\tfrac{1}{\lambda}\,\boldsymbol A\boldsymbol A^{-1} = \boldsymbol I,
        \qquad
        \Big(\tfrac{1}{\lambda}\boldsymbol A^{-1}\Big)(\lambda\boldsymbol A) = \tfrac{1}{\lambda}\cdot\lambda\,\boldsymbol A^{-1}\boldsymbol A = \boldsymbol I.
        $$

    2. Da \(\boldsymbol A^2 - 3\boldsymbol A + \boldsymbol I = \boldsymbol 0\) si ottiene \(3\boldsymbol A - \boldsymbol A^2 = \boldsymbol I\), cioè

        $$
        \boldsymbol A(3\boldsymbol I - \boldsymbol A) = \boldsymbol I
        \quad\text{e}\quad
        (3\boldsymbol I - \boldsymbol A)\boldsymbol A = \boldsymbol I.
        $$

        Quindi \(\boldsymbol A^{-1} = 3\boldsymbol I - \boldsymbol A\). Per \(\boldsymbol A = \begin{pmatrix} 2 & 1\\ 1 & 1\end{pmatrix}\):

        $$
        \boldsymbol A^2 = \begin{pmatrix} 5 & 3\\ 3 & 2\end{pmatrix},
        \qquad
        \boldsymbol A^2 - 3\boldsymbol A + \boldsymbol I = \begin{pmatrix} 5-6+1 & 3-3\\ 3-3 & 2-3+1\end{pmatrix} = \boldsymbol 0,
        $$

        e \(3\boldsymbol I - \boldsymbol A = \begin{pmatrix} 1 & -1\\ -1 & 2\end{pmatrix}\), che è proprio \(\boldsymbol A^{-1}\).

<a id="box-exe_inv_upper_triangular-10"></a>

!!! esercizio "Esercizio 10"

    Calcolare l'inversa della matrice triangolare superiore

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    0 & 1 & 4\\
    0 & 0 & 1
    \end{pmatrix}
    $$

    con il metodo di Gauss–Jordan. Che tipo di matrice è \(\boldsymbol A^{-1}\)?

??? soluzione "Soluzione"

    Il blocco sinistro è già triangolare superiore con elementi diagonali uguali a uno: è sufficiente annullare gli elementi al di sopra dei pivot, partendo dall'ultima colonna.

    \begin{align*}
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 3 & 1 & 0 & 0 \\
     0 & 1 & 4 & 0 & 1 & 0 \\
     0 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 0 & 1 & 0 & -3 \\
     0 & 1 & 4 & 0 & 1 & 0 \\
     0 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - 3R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 0 & 1 & 0 & -3 \\
     0 & 1 & 0 & 0 & 1 & -4 \\
     0 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 4R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & 1 & -2 & 5 \\
     0 & 1 & 0 & 0 & 1 & -4 \\
     0 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - 2R_2 \text{)}
    \end{align*}

    Quindi

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    1 & -2 & 5\\
    0 & 1 & -4\\
    0 & 0 & 1
    \end{pmatrix},
    $$

    che è ancora triangolare superiore con elementi diagonali uguali a uno.
