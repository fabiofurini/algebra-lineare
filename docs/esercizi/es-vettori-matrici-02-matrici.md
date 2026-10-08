---
title: "Matrici"
---

# Matrici

<div class="info-capitolo" markdown>

**Esercizi · Vettori e matrici** · capitolo [4.1 · Matrici](../vettori-matrici/02-matrici.md) · con le soluzioni svolte · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf)

</div>

<a id="box-exe_matPSDQ1-1"></a>

!!! esercizio "Esercizio 1"

    Utilizzando la definizione, dimostrare che la matrice

    $$
    {\boldsymbol Q}_1=\begin{pmatrix}
    \frac{1}{3} & 0\\[1ex]
    0 & \frac{1}{2} \\
    \end{pmatrix} \in \R^{2 \times 2}
    $$

    è semidefinita positiva.

??? soluzione "Soluzione"

    Si ha:

    \begin{align*}
    \begin{pmatrix}
    x_1 & x_2
    \end{pmatrix}
    \begin{pmatrix}
    \frac{1}{3} & 0 \\[1ex]
    0 & \frac{1}{2}
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\[1ex]
    x_2
    \end{pmatrix}
    &= \begin{pmatrix}
    \left(\frac{1}{3} x_1 + 0 \cdot x_2 \right) & \left(0 \cdot x_1 + \frac{1}{2} x_2\right)
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\[1ex]
    x_2
    \end{pmatrix}\\[2ex]
    &= \left(\frac{1}{3} x_1 \right) x_1 + \left(\frac{1}{2} x_2\right) x_2 \\[2ex]
    &= \frac{1}{3} x_1^2 + \frac{1}{2} x_2^2 \geq 0, ~~~~~~ \forall (x_1, x_2) \in \mathbb{R}^2
    \end{align*}

    Di conseguenza, la matrice \( {\boldsymbol Q}_1 \) è semidefinita positiva.

<a id="box-exe_matPSDQ2-2"></a>

!!! esercizio "Esercizio 2"

    Utilizzando la definizione, dimostrare che la matrice

    $$
    {\boldsymbol Q}_2 = \begin{pmatrix}
    3 & 1 \\[1ex]
    1 & 3
    \end{pmatrix} \in \R^{2 \times 2}
    $$

    è semidefinita positiva.

??? soluzione "Soluzione"

    Si ha:

    \begin{align*}
    \begin{pmatrix}
    x_1 & x_2
    \end{pmatrix}
    \begin{pmatrix}
    3 & 1 \\[1ex]
    1 & 3
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\[1ex]
    x_2
    \end{pmatrix}
    &= \begin{pmatrix}
    (3\;x_1 + x_2) & (x_1 + 3\;x_2)
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\[1ex]
    x_2
    \end{pmatrix}\\[2ex]
    &= (3\;x_1 + x_2)\;x_1 + (x_1 + 3\;x_2)\;x_2 \\[2ex]
    &= 3\;x_1^2 + x_1\;x_2 + x_1\;x_2 + 3\;x_2^2 \\[2ex]
    &= 3\;x_1^2 + 2\;x_1\;x_2 + 3\;x_2^2 \\[2ex]
    &= (x_1 + x_2)^2 + 2\;x_1^2 + 2\;x_2^2 \geq 0, ~~~~~~
    \forall (x_1, x_2) \in \mathbb{R}^2
    \end{align*}

    di conseguenza la matrice ${\boldsymbol Q}_2$ è semidefinita positiva.

<a id="box-exe_matPSDQ3-3"></a>

!!! esercizio "Esercizio 3"

    Utilizzando la definizione, dimostrare che la matrice

    $$
    {\boldsymbol Q}_3 = \begin{pmatrix}
    2 & -1 & 0 \\[1ex]
    -1 & 2 & -1 \\[1ex]
    0 & -1 & 2 \\
    \end{pmatrix} \in \R^{3 \times 3}
    $$

    è semidefinita positiva.

??? soluzione "Soluzione"

    Si ha:

    \begin{align*}
    &\begin{pmatrix}
    x_1 & x_2 & x_3
    \end{pmatrix}
    \begin{pmatrix}
    2 & -1 & 0 \\[1ex]
    -1 & 2 & -1 \\[1ex]
    0 & -1 & 2 \\
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\[1ex]
    x_2 \\[1ex]
    x_3 \\
    \end{pmatrix}\\[2ex]
    &= \begin{pmatrix}
    (2\;x_1-x_2) & (-x_1+2\;x_2-x_3)& (-x_2+2\;x_3)
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\[1ex]
    x_2 \\[1ex]
    x_3 \\
    \end{pmatrix}\\[2ex]
    &= (2\;x_1-x_2)\;x_1 + (-x_1+2\;x_2-x_3)\; x_2 + (-x_2+2\;x_3)x_3  \\[2ex]
    &= 2\;x_1^2 - x_2\;x_1 - x_1\;x_2+ 2\;x_2^2 - x_3\;x_2 - x_2\;x_3 + 2\;x_3^2\\[2ex]
    &= 2\;x_1^2 - 2\;x_1\;x_2 + 2\;x_2^2 - 2 \;x_2\;x_3 + 2\;x_3^2 \\[2ex]
    &= x_1^2+ x_1^2 - 2\;x_1\;x_2 + x_2^2 + x_2^2 - 2 \;x_2\;x_3 + x_3^2 + x_3^2 \\[2ex]
    &= x_1^2 + (x_1-x_2)^2 + (x_2-x_3)^2 + x_3^2 \ge 0,
    ~~~~~~
    \forall (
    x_1, x_2, x_3 ) \in \R^3
    \end{align*}

    di conseguenza la matrice ${\boldsymbol Q}_3$ è semidefinita positiva.

<a id="box-exe_matSumTranspose-4"></a>

!!! esercizio "Esercizio 4"

    Si considerino le matrici

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & -2 & 3\\
    0 & 4 & -1
    \end{pmatrix},
    \qquad
    \boldsymbol B=
    \begin{pmatrix}
    2 & 1 & 0\\
    -3 & 2 & 5
    \end{pmatrix}
    \in\R^{2\times 3}.
    $$

    Calcolare \(\boldsymbol A+\boldsymbol B\), \(2\boldsymbol A-\boldsymbol B\), \(\boldsymbol A'\), e verificare che \((\boldsymbol A+\boldsymbol B)'=\boldsymbol A'+\boldsymbol B'\).

??? soluzione "Soluzione"

    Somma e prodotto per uno scalare si calcolano elemento per elemento:

    $$
    \boldsymbol A+\boldsymbol B=
    \begin{pmatrix}
    1+2 & -2+1 & 3+0\\
    0-3 & 4+2 & -1+5
    \end{pmatrix}
    =
    \begin{pmatrix}
    3 & -1 & 3\\
    -3 & 6 & 4
    \end{pmatrix},
    $$

    $$
    2\boldsymbol A-\boldsymbol B=
    \begin{pmatrix}
    2 & -4 & 6\\
    0 & 8 & -2
    \end{pmatrix}
    -
    \begin{pmatrix}
    2 & 1 & 0\\
    -3 & 2 & 5
    \end{pmatrix}
    =
    \begin{pmatrix}
    0 & -5 & 6\\
    3 & 6 & -7
    \end{pmatrix}.
    $$

    La trasposta si ottiene scambiando righe e colonne (\(\boldsymbol A'\in\R^{3\times 2}\)):

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 0\\
    -2 & 4\\
    3 & -1
    \end{pmatrix},
    \qquad
    \boldsymbol B'=
    \begin{pmatrix}
    2 & -3\\
    1 & 2\\
    0 & 5
    \end{pmatrix}.
    $$

    Infine,

    $$
    \boldsymbol A'+\boldsymbol B'=
    \begin{pmatrix}
    3 & -3\\
    -1 & 6\\
    3 & 4
    \end{pmatrix}
    =(\boldsymbol A+\boldsymbol B)'.
    $$

<a id="box-exe_matProductDimensions-5"></a>

!!! esercizio "Esercizio 5"

    Si considerino le matrici

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 0 & 2\\
    3 & -1 & 1
    \end{pmatrix}\in\R^{2\times 3},
    \qquad
    \boldsymbol B=
    \begin{pmatrix}
    1 & 0\\
    2 & 1\\
    -1 & 3
    \end{pmatrix}\in\R^{3\times 2},
    \qquad
    \boldsymbol C=
    \begin{pmatrix}
    1 & 2\\
    0 & -1
    \end{pmatrix}\in\R^{2\times 2}.
    $$

    1. Tra i prodotti \(\boldsymbol A\boldsymbol B\), \(\boldsymbol B\boldsymbol A\), \(\boldsymbol A\boldsymbol C\), \(\boldsymbol C\boldsymbol A\), \(\boldsymbol B\boldsymbol C\), \(\boldsymbol C\boldsymbol B\), dire quali sono definiti e indicare le dimensioni del risultato.

    2. Calcolare \(\boldsymbol C\boldsymbol A\), \(\boldsymbol A\boldsymbol B\) e \(\boldsymbol B\boldsymbol C\).

??? soluzione "Soluzione"

    1. Il prodotto di una matrice di \(\R^{m\times n}\) per una matrice di \(\R^{q\times p}\) è definito solo se \(n=q\) (numero di colonne della prima = numero di righe della seconda), e il risultato appartiene a \(\R^{m\times p}\). Quindi:

        - \(\boldsymbol A\boldsymbol B\): \((2\times 3)(3\times 2)\), definito, risultato in \(\R^{2\times 2}\);

        - \(\boldsymbol B\boldsymbol A\): \((3\times 2)(2\times 3)\), definito, risultato in \(\R^{3\times 3}\);

        - \(\boldsymbol A\boldsymbol C\): \((2\times 3)(2\times 2)\), <strong>non</strong> definito (\(3\neq 2\));

        - \(\boldsymbol C\boldsymbol A\): \((2\times 2)(2\times 3)\), definito, risultato in \(\R^{2\times 3}\);

        - \(\boldsymbol B\boldsymbol C\): \((3\times 2)(2\times 2)\), definito, risultato in \(\R^{3\times 2}\);

        - \(\boldsymbol C\boldsymbol B\): \((2\times 2)(3\times 2)\), <strong>non</strong> definito (\(2\neq 3\)).

    2. Ogni elemento \((i,k)\) è il prodotto scalare della riga \(i\) della prima matrice e della colonna \(k\) della seconda:

        $$
        \boldsymbol C\boldsymbol A=
        \begin{pmatrix}
        1\cdot 1+2\cdot 3 & 1\cdot 0+2\cdot(-1) & 1\cdot 2+2\cdot 1\\
        0\cdot 1+(-1)\cdot 3 & 0\cdot 0+(-1)\cdot(-1) & 0\cdot 2+(-1)\cdot 1
        \end{pmatrix}
        =
        \begin{pmatrix}
        7 & -2 & 4\\
        -3 & 1 & -1
        \end{pmatrix},
        $$

        $$
        \boldsymbol A\boldsymbol B=
        \begin{pmatrix}
        1\cdot 1+0\cdot 2+2\cdot(-1) & 1\cdot 0+0\cdot 1+2\cdot 3\\
        3\cdot 1+(-1)\cdot 2+1\cdot(-1) & 3\cdot 0+(-1)\cdot 1+1\cdot 3
        \end{pmatrix}
        =
        \begin{pmatrix}
        -1 & 6\\
        0 & 2
        \end{pmatrix},
        $$

        $$
        \boldsymbol B\boldsymbol C=
        \begin{pmatrix}
        1\cdot 1+0\cdot 0 & 1\cdot 2+0\cdot(-1)\\
        2\cdot 1+1\cdot 0 & 2\cdot 2+1\cdot(-1)\\
        -1\cdot 1+3\cdot 0 & -1\cdot 2+3\cdot(-1)
        \end{pmatrix}
        =
        \begin{pmatrix}
        1 & 2\\
        2 & 3\\
        -1 & -5
        \end{pmatrix}.
        $$

<a id="box-exe_matNonCommutative-6"></a>

!!! esercizio "Esercizio 6"

    1. Siano \( \boldsymbol A=\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix} \) e \( \boldsymbol B=\begin{pmatrix}1 & 0\\ 1 & 1\end{pmatrix}. \) Calcolare \(\boldsymbol A\boldsymbol B\) e \(\boldsymbol B\boldsymbol A\). Il prodotto è commutativo?

    2. Siano \( \boldsymbol A=\begin{pmatrix}1 & 1\\ 1 & 1\end{pmatrix} \) e \( \boldsymbol B=\begin{pmatrix}1 & -1\\ -1 & 1\end{pmatrix}. \) Calcolare \(\boldsymbol A\boldsymbol B\). Che cosa si osserva?

??? soluzione "Soluzione"

    1.

        $$
        \boldsymbol A\boldsymbol B=
        \begin{pmatrix}
        1\cdot 1+1\cdot 1 & 1\cdot 0+1\cdot 1\\
        0\cdot 1+1\cdot 1 & 0\cdot 0+1\cdot 1
        \end{pmatrix}
        =
        \begin{pmatrix}
        2 & 1\\
        1 & 1
        \end{pmatrix},
        \qquad
        \boldsymbol B\boldsymbol A=
        \begin{pmatrix}
        1\cdot 1+0\cdot 0 & 1\cdot 1+0\cdot 1\\
        1\cdot 1+1\cdot 0 & 1\cdot 1+1\cdot 1
        \end{pmatrix}
        =
        \begin{pmatrix}
        1 & 1\\
        1 & 2
        \end{pmatrix}.
        $$

        Poiché \(\boldsymbol A\boldsymbol B\neq\boldsymbol B\boldsymbol A\), il prodotto non è commutativo (anche per matrici quadrate dello stesso ordine).

    2.

        $$
        \boldsymbol A\boldsymbol B=
        \begin{pmatrix}
        1\cdot 1+1\cdot(-1) & 1\cdot(-1)+1\cdot 1\\
        1\cdot 1+1\cdot(-1) & 1\cdot(-1)+1\cdot 1
        \end{pmatrix}
        =
        \begin{pmatrix}
        0 & 0\\
        0 & 0
        \end{pmatrix}.
        $$

        Il prodotto di due matrici non nulle può essere la matrice nulla: a differenza dei numeri reali, \(\boldsymbol A\boldsymbol B=\boldsymbol 0\) <strong>non</strong> implica \(\boldsymbol A=\boldsymbol 0\) o \(\boldsymbol B=\boldsymbol 0\).

<a id="box-exe_matSpecial-7"></a>

!!! esercizio "Esercizio 7"

    1. Per ciascuna delle seguenti matrici, dire se è quadrata, diagonale, simmetrica, triangolare superiore, triangolare inferiore:

        $$
        \boldsymbol M_1=\begin{pmatrix}1 & 2\\ 2 & 3\end{pmatrix},
        \quad
        \boldsymbol M_2=\begin{pmatrix}4 & 0 & 0\\ 0 & -1 & 0\\ 0 & 0 & 2\end{pmatrix},
        \quad
        \boldsymbol M_3=\begin{pmatrix}1 & 0 & 0\\ 5 & 2 & 0\\ -1 & 3 & 4\end{pmatrix},
        \quad
        \boldsymbol M_4=\begin{pmatrix}1 & 2 & 3\\ 4 & 5 & 6\end{pmatrix}.
        $$

    2. Calcolare il prodotto delle matrici triangolari superiori \( \boldsymbol U_1=\begin{pmatrix}1 & 2\\ 0 & 3\end{pmatrix} \) e \( \boldsymbol U_2=\begin{pmatrix}2 & -1\\ 0 & 4\end{pmatrix}. \) Che tipo di matrice si ottiene?

    3. Siano \( \boldsymbol D=\begin{pmatrix}2 & 0\\ 0 & 3\end{pmatrix} \) e \( \boldsymbol A=\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}. \) Calcolare \(\boldsymbol D\boldsymbol A\) e \(\boldsymbol A\boldsymbol D\) e descrivere l'effetto della matrice diagonale.

??? soluzione "Soluzione"

    1. - \(\boldsymbol M_1\): quadrata e simmetrica (\(m_{12}=m_{21}=2\)); non è né diagonale né triangolare.

        - \(\boldsymbol M_2\): quadrata e diagonale; quindi è anche simmetrica, triangolare superiore e triangolare inferiore.

        - \(\boldsymbol M_3\): quadrata e triangolare inferiore (tutti gli elementi al di sopra della diagonale principale sono nulli); non è simmetrica (ad esempio \(m_{21}=5\neq 0=m_{12}\)).

        - \(\boldsymbol M_4\in\R^{2\times 3}\): non è quadrata, quindi nessuna delle altre proprietà si applica.

    2.

        $$
        \boldsymbol U_1\boldsymbol U_2=
        \begin{pmatrix}
        1\cdot 2+2\cdot 0 & 1\cdot(-1)+2\cdot 4\\
        0\cdot 2+3\cdot 0 & 0\cdot(-1)+3\cdot 4
        \end{pmatrix}
        =
        \begin{pmatrix}
        2 & 7\\
        0 & 12
        \end{pmatrix},
        $$

        che è ancora triangolare superiore, con elementi diagonali \(1\cdot 2=2\) e \(3\cdot 4=12\).

    3.

        $$
        \boldsymbol D\boldsymbol A=
        \begin{pmatrix}
        2\cdot 1 & 2\cdot 2\\
        3\cdot 3 & 3\cdot 4
        \end{pmatrix}
        =
        \begin{pmatrix}
        2 & 4\\
        9 & 12
        \end{pmatrix},
        \qquad
        \boldsymbol A\boldsymbol D=
        \begin{pmatrix}
        1\cdot 2 & 2\cdot 3\\
        3\cdot 2 & 4\cdot 3
        \end{pmatrix}
        =
        \begin{pmatrix}
        2 & 6\\
        6 & 12
        \end{pmatrix}.
        $$

        La moltiplicazione a sinistra per \(\boldsymbol D\) moltiplica la \(i\)-esima <strong>riga</strong> di \(\boldsymbol A\) per \(d_{ii}\); la moltiplicazione a destra moltiplica la \(j\)-esima <strong>colonna</strong> di \(\boldsymbol A\) per \(d_{jj}\).

<a id="box-exe_matPermutation-8"></a>

!!! esercizio "Esercizio 8"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}
    $$

    e sia \(\pi=(2,3,1)\).

    1. Scrivere la matrice di permutazione \(\boldsymbol P_{\pi}\) e calcolare \(\boldsymbol P_{\pi}\boldsymbol A\).

    2. Calcolare \(\boldsymbol A\boldsymbol P_{\pi}'\) e verificare che le colonne di \(\boldsymbol A\) sono riordinate secondo \(\pi\).

    3. Verificare che \(\boldsymbol P_{\pi}\boldsymbol P_{\pi}'=\boldsymbol I_3\).

??? soluzione "Soluzione"

    1. \(\boldsymbol P_{\pi}\) si ottiene da \(\boldsymbol I_3\) mettendo per prima la riga \(2\), poi la riga \(3\), poi la riga \(1\):

        $$
        \boldsymbol P_{\pi}=
        \begin{pmatrix}
        0 & 1 & 0\\
        0 & 0 & 1\\
        1 & 0 & 0
        \end{pmatrix},
        \qquad
        \boldsymbol P_{\pi}\boldsymbol A=
        \begin{pmatrix}
        4 & 5 & 6\\
        7 & 8 & 9\\
        1 & 2 & 3
        \end{pmatrix}.
        $$

        Le righe di \(\boldsymbol A\) compaiono nell'ordine \(2,3,1\).

    2.

        $$
        \boldsymbol A\boldsymbol P_{\pi}'=
        \begin{pmatrix}
        1 & 2 & 3\\
        4 & 5 & 6\\
        7 & 8 & 9
        \end{pmatrix}
        \begin{pmatrix}
        0 & 0 & 1\\
        1 & 0 & 0\\
        0 & 1 & 0
        \end{pmatrix}
        =
        \begin{pmatrix}
        2 & 3 & 1\\
        5 & 6 & 4\\
        8 & 9 & 7
        \end{pmatrix}.
        $$

        Le colonne di \(\boldsymbol A\) compaiono nell'ordine \(2,3,1\).

    3.

        $$
        \boldsymbol P_{\pi}\boldsymbol P_{\pi}'=
        \begin{pmatrix}
        0 & 1 & 0\\
        0 & 0 & 1\\
        1 & 0 & 0
        \end{pmatrix}
        \begin{pmatrix}
        0 & 0 & 1\\
        1 & 0 & 0\\
        0 & 1 & 0
        \end{pmatrix}
        =
        \begin{pmatrix}
        1 & 0 & 0\\
        0 & 1 & 0\\
        0 & 0 & 1
        \end{pmatrix}
        =\boldsymbol I_3.
        $$

        Quindi \(\boldsymbol P_{\pi}\) è invertibile e \(\boldsymbol P_{\pi}^{-1}=\boldsymbol P_{\pi}'\) (allo stesso modo si verifica che \(\boldsymbol P_{\pi}'\boldsymbol P_{\pi}=\boldsymbol I_3\)).

<a id="box-exe_matLaplace3x3-9"></a>

!!! esercizio "Esercizio 9"

    Calcolare il determinante di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 0 & 1\\
    3 & 0 & -2\\
    1 & 4 & 5
    \end{pmatrix}
    $$

    mediante lo sviluppo di Laplace lungo la riga o colonna più conveniente, e verificare il risultato con la regola di Sarrus.

??? soluzione "Soluzione"

    La seconda colonna contiene due zeri, quindi sviluppiamo lungo di essa: contribuisce solo l'elemento \(a_{32}=4\),

    $$
    \det(\boldsymbol A)=0\cdot C_{12}+0\cdot C_{22}+4\cdot C_{32}.
    $$

    Il cofattore è

    $$
    C_{32}=(-1)^{3+2}\det
    \begin{pmatrix}
    2 & 1\\
    3 & -2
    \end{pmatrix}
    =
    -\bigl(2\cdot(-2)-1\cdot 3\bigr)
    =
    -(-4-3)=7.
    $$

    Pertanto \(\det(\boldsymbol A)=4\cdot 7=28\).

    Verifica con la regola di Sarrus (\(a=2,b=0,c=1,d=3,e=0,f=-2,g=1,h=4,i=5\)):

    $$
    \det(\boldsymbol A)=2\cdot 0\cdot 5+0\cdot(-2)\cdot 1+1\cdot 3\cdot 4-1\cdot 0\cdot 1-0\cdot 3\cdot 5-2\cdot(-2)\cdot 4
    =0+0+12-0-0+16=28.
    $$

<a id="box-exe_matLaplace4x4-10"></a>

!!! esercizio "Esercizio 10"

    Calcolare il determinante di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0 & 3\\
    0 & 0 & 2 & 0\\
    4 & 1 & 0 & 2\\
    1 & 0 & 1 & 3
    \end{pmatrix}
    \in\R^{4\times 4}
    $$

    scegliendo la riga o colonna che minimizza il numero di calcoli.

??? soluzione "Soluzione"

    La seconda riga ha un solo elemento non nullo, \(a_{23}=2\). Sviluppando lungo la seconda riga:

    $$
    \det(\boldsymbol A)=a_{23}\,C_{23}=2\cdot(-1)^{2+3}\det(\boldsymbol A_{23})=-2\det(\boldsymbol A_{23}),
    $$

    dove \(\boldsymbol A_{23}\) si ottiene eliminando la riga \(2\) e la colonna \(3\):

    $$
    \boldsymbol A_{23}=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 1 & 2\\
    1 & 0 & 3
    \end{pmatrix}.
    $$

    Sviluppiamo \(\det(\boldsymbol A_{23})\) lungo la sua terza riga, che contiene uno zero:

    \begin{align*}
    \det(\boldsymbol A_{23})
    &=
    1\cdot(-1)^{3+1}\det\begin{pmatrix}2 & 3\\ 1 & 2\end{pmatrix}
    +0
    +3\cdot(-1)^{3+3}\det\begin{pmatrix}1 & 2\\ 4 & 1\end{pmatrix}\\
    &=1\cdot(4-3)+3\cdot(1-8)=1-21=-20.
    \end{align*}

    Pertanto

    $$
    \det(\boldsymbol A)=-2\cdot(-20)=40.
    $$

<a id="box-exe_matDetProperties-11"></a>

!!! esercizio "Esercizio 11"

    Si considerino le matrici

    $$
    \boldsymbol U=
    \begin{pmatrix}
    2 & 5 & -1\\
    0 & -3 & 4\\
    0 & 0 & 1
    \end{pmatrix},
    \qquad
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0 & 0\\
    7 & 2 & 0\\
    -3 & 4 & 5
    \end{pmatrix}.
    $$

    1. Calcolare \(\det(\boldsymbol U)\) e \(\det(\boldsymbol L)\).

    2. Senza calcolare alcun prodotto, trovare \(\det(\boldsymbol U\boldsymbol L)\), \(\det(\boldsymbol U')\), \(\det(3\boldsymbol U)\) e \(\det(\boldsymbol U^{-1})\). Perché \(\boldsymbol U^{-1}\) esiste?

    3. Verificare che \( \begin{pmatrix}2 & -1\\ -5 & 3\end{pmatrix} \) è l'inversa di \( \boldsymbol A=\begin{pmatrix}3 & 1\\ 5 & 2\end{pmatrix} \), e controllare che \(\det(\boldsymbol A^{-1})=1/\det(\boldsymbol A)\).

??? soluzione "Soluzione"

    1. Entrambe le matrici sono triangolari, quindi il loro determinante è il prodotto degli elementi diagonali:

        $$
        \det(\boldsymbol U)=2\cdot(-3)\cdot 1=-6,
        \qquad
        \det(\boldsymbol L)=1\cdot 2\cdot 5=10.
        $$

    2. Usando le proprietà del determinante (con \(n=3\)):

        $$
        \det(\boldsymbol U\boldsymbol L)=\det(\boldsymbol U)\det(\boldsymbol L)=-6\cdot 10=-60,
        \qquad
        \det(\boldsymbol U')=\det(\boldsymbol U)=-6,
        $$

        $$
        \det(3\boldsymbol U)=3^3\det(\boldsymbol U)=27\cdot(-6)=-162.
        $$

        Poiché \(\det(\boldsymbol U)=-6\neq 0\), la matrice \(\boldsymbol U\) è invertibile, e \( \det(\boldsymbol U^{-1})=\frac{1}{\det(\boldsymbol U)}=-\frac{1}{6}. \)

    3.

        $$
        \begin{pmatrix}3 & 1\\ 5 & 2\end{pmatrix}
        \begin{pmatrix}2 & -1\\ -5 & 3\end{pmatrix}
        =
        \begin{pmatrix}6-5 & -3+3\\ 10-10 & -5+6\end{pmatrix}
        =\boldsymbol I_2,
        $$

        $$
        \begin{pmatrix}2 & -1\\ -5 & 3\end{pmatrix}
        \begin{pmatrix}3 & 1\\ 5 & 2\end{pmatrix}
        =
        \begin{pmatrix}6-5 & 2-2\\ -15+15 & -5+6\end{pmatrix}
        =\boldsymbol I_2.
        $$

        Quindi è l'inversa di \(\boldsymbol A\). Inoltre \(\det(\boldsymbol A)=3\cdot 2-1\cdot 5=1\) e \(\det(\boldsymbol A^{-1})=2\cdot 3-(-1)\cdot(-5)=1=\frac{1}{1}\).

<a id="box-exe_matRank-12"></a>

!!! esercizio "Esercizio 12"

    Calcolare il rango delle seguenti matrici:

    $$
    \boldsymbol A_1=\begin{pmatrix}1 & 2\\ 3 & 6\end{pmatrix},
    \qquad
    \boldsymbol A_2=\begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 1\\ 1 & 3 & 4\end{pmatrix},
    \qquad
    \boldsymbol A_3=\begin{pmatrix}1 & 0 & 2\\ 0 & 1 & 1\\ 1 & 1 & 0\end{pmatrix}.
    $$

??? soluzione "Soluzione"

    - \(\boldsymbol A_1\): la seconda colonna è il doppio della prima, \(\begin{pmatrix}2 & 6\end{pmatrix}'=2\begin{pmatrix}1 & 3\end{pmatrix}'\), quindi le due colonne sono linearmente dipendenti; la prima colonna è non nulla, quindi da sola è linearmente indipendente. Pertanto \(\mathrm{rank}(\boldsymbol A_1)=1\) (coerentemente, \(\det(\boldsymbol A_1)=6-6=0\)).

    - \(\boldsymbol A_2\): la terza colonna è la somma delle prime due, \(\begin{pmatrix}3 & 1 & 4\end{pmatrix}'=\begin{pmatrix}1 & 0 & 1\end{pmatrix}'+\begin{pmatrix}2 & 1 & 3\end{pmatrix}'\), quindi le tre colonne sono linearmente dipendenti e \(\mathrm{rank}(\boldsymbol A_2)\le 2\). Le prime due colonne sono linearmente indipendenti: \(\lambda_1\begin{pmatrix}1 & 0 & 1\end{pmatrix}'+\lambda_2\begin{pmatrix}2 & 1 & 3\end{pmatrix}'=\boldsymbol 0\) dà \(\lambda_2=0\) (secondo elemento) e poi \(\lambda_1=0\) (primo elemento). Quindi \(\mathrm{rank}(\boldsymbol A_2)=2\). Coerentemente, sviluppando lungo la prima riga, \(\det(\boldsymbol A_2)=1\cdot(4-3)-2\cdot(0-1)+3\cdot(0-1)=1+2-3=0\).

    - \(\boldsymbol A_3\): sviluppando lungo la prima riga,

        $$
        \det(\boldsymbol A_3)=1\cdot(1\cdot 0-1\cdot 1)-0\cdot(0\cdot 0-1\cdot 1)+2\cdot(0\cdot 1-1\cdot 1)=-1-0-2=-3\neq 0.
        $$

        Poiché \(\boldsymbol A_3\) è quadrata e \(\det(\boldsymbol A_3)\neq 0\), si ha \(\mathrm{rank}(\boldsymbol A_3)=3\).
