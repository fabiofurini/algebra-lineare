---
title: "Operazioni sulle matrici"
---

# Operazioni sulle matrici

<div class="info-capitolo" markdown>

**Esercizi · Vettori e matrici** · capitolo [4.2 · Operazioni sulle matrici](../vettori-matrici/03-operazioni-elementari.md) · con le soluzioni svolte · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf)

</div>

<a id="box-exe_ops_row_operations-1"></a>

!!! esercizio "Esercizio 1"

    Si consideri la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & -1\\
    3 & 0 & 2\\
    -2 & 1 & 4
    \end{pmatrix}.
    $$

    Applicare ad \(\boldsymbol A\), una dopo l'altra, le operazioni elementari di riga \(R_1 \leftrightarrow R_3\), \(R_2 \leftarrow -2R_2\) e \(R_3 \leftarrow R_3 + 2R_1\), e scrivere la matrice ottenuta dopo ciascuna operazione.

??? soluzione "Soluzione"

    Ogni operazione viene applicata alla matrice prodotta dalla precedente:

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     1 & 2 & -1 \\
     3 & 0 & 2 \\
     -2 & 1 & 4 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     -2 & 1 & 4 \\
     3 & 0 & 2 \\
     1 & 2 & -1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftrightarrow R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     -2 & 1 & 4 \\
     -6 & 0 & -4 \\
     1 & 2 & -1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow -2R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     -2 & 1 & 4 \\
     -6 & 0 & -4 \\
     -3 & 4 & 7 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + 2R_1 \text{)}
    \end{align*}

    Si osservi che nell'ultimo passo \(R_1\) è la prima riga <em>corrente</em> \((-2,\,1,\,4)\): \((1,\,2,\,-1) + 2\,(-2,\,1,\,4) = (-3,\,4,\,7)\).

<a id="box-exe_ops_column_operations-2"></a>

!!! esercizio "Esercizio 2"

    Si consideri la matrice

    $$
    \boldsymbol B=
    \begin{pmatrix}
    1 & -1 & 2\\
    0 & 3 & 1
    \end{pmatrix}.
    $$

    Applicare a \(\boldsymbol B\), una dopo l'altra, le operazioni elementari di colonna \(C_1 \leftrightarrow C_3\), \(C_2 \leftarrow C_2 + C_1\) e \(C_3 \leftarrow 2C_3\), e scrivere la matrice ottenuta dopo ciascuna operazione.

??? soluzione "Soluzione"

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     1 & -1 & 2 \\
     0 & 3 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & -1 & 1 \\
     1 & 3 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} C_1 \leftrightarrow C_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     1 & 4 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} C_2 \leftarrow C_2 + C_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 2 \\
     1 & 4 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} C_3 \leftarrow 2C_3 \text{)}
    \end{align*}

    Nel secondo passo: \(\begin{pmatrix}-1\\3\end{pmatrix} + \begin{pmatrix}2\\1\end{pmatrix} = \begin{pmatrix}1\\4\end{pmatrix}\).

<a id="box-exe_ops_det_effect-3"></a>

!!! esercizio "Esercizio 3"

    Sia \(\boldsymbol A \in \R^{3\times 3}\) con \(\det(\boldsymbol A) = 5\). Senza calcolare alcun elemento della matrice, determinare il determinante della matrice ottenuta da \(\boldsymbol A\) mediante:

    1. lo scambio di righe \(R_1 \leftrightarrow R_2\);

    2. la moltiplicazione di una riga per uno scalare \(R_2 \leftarrow -3R_2\);

    3. la somma di righe \(R_3 \leftarrow R_3 + 7R_1\);

    4. le tre operazioni precedenti, applicate una dopo l'altra;

    5. lo scambio di colonne \(C_1 \leftrightarrow C_3\) seguito dalla moltiplicazione di una colonna per uno scalare \(C_2 \leftarrow 4C_2\).

    Infine, calcolare \(\det(2\boldsymbol A)\).

??? soluzione "Soluzione"

    Utilizziamo l'effetto delle operazioni elementari sul determinante: uno scambio ne cambia il segno, una moltiplicazione per \(\lambda\) lo moltiplica per \(\lambda\), una somma non lo cambia.

    1. \(\det = -\det(\boldsymbol A) = -5\).

    2. \(\det = -3\det(\boldsymbol A) = -15\).

    3. \(\det = \det(\boldsymbol A) = 5\).

    4. \(\det = (-1)\cdot(-3)\cdot 1\cdot\det(\boldsymbol A) = 15\).

    5. \(\det = (-1)\cdot 4\cdot\det(\boldsymbol A) = -20\) (le operazioni di colonna agiscono come le operazioni di riga).

    Infine, \(2\boldsymbol A\) si ottiene moltiplicando ciascuna delle \(3\) righe per \(2\), quindi

    $$
    \det(2\boldsymbol A) = 2^3\det(\boldsymbol A) = 8\cdot 5 = 40.
    $$

    Per esempio, tutti questi valori possono essere verificati su \(\boldsymbol A = \begin{pmatrix}1 & 2 & 0\\ 0 & 1 & 1\\ 2 & 0 & 1\end{pmatrix}\), che ha \(\det(\boldsymbol A) = 5\).

<a id="box-exe_ops_det_zero_row-4"></a>

!!! esercizio "Esercizio 4"

    Utilizzando le operazioni elementari di riga (e nessuna formula di sviluppo), mostrare che le seguenti matrici hanno determinante uguale a zero:

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    2 & 4 & 6
    \end{pmatrix},
    \qquad
    \boldsymbol B=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

??? soluzione "Soluzione"

    Le somme di righe non cambiano il determinante, e una matrice con una riga nulla ha determinante zero (sviluppo di Laplace lungo quella riga).

    Per \(\boldsymbol A\), la terza riga è il doppio della prima:

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     4 & 5 & 6 \\
     2 & 4 & 6 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     4 & 5 & 6 \\
     0 & 0 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_1 \text{)}
    \end{align*}

    Quindi \(\det(\boldsymbol A) = 0\).

    Per \(\boldsymbol B\):

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     4 & 5 & 6 \\
     7 & 8 & 9 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     0 & -3 & -6 \\
     7 & 8 & 9 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 4R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     0 & -3 & -6 \\
     0 & -6 & -12 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 7R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 2 & 3 \\
     0 & -3 & -6 \\
     0 & 0 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_2 \text{)}
    \end{align*}

    Quindi \(\det(\boldsymbol B) = 0\).

<a id="box-exe_ops_echelon_recognize-5"></a>

!!! esercizio "Esercizio 5"

    Quali delle seguenti matrici sono in forma a scala? Giustificare la risposta.

    $$
    \boldsymbol M_1=
    \begin{pmatrix}
    1 & 2 & 0\\
    0 & 0 & 3\\
    0 & 0 & 0
    \end{pmatrix},
    \quad
    \boldsymbol M_2=
    \begin{pmatrix}
    0 & 1 & 2\\
    1 & 0 & 0\\
    0 & 0 & 1
    \end{pmatrix},
    \quad
    \boldsymbol M_3=
    \begin{pmatrix}
    2 & 1 & 4 & 1\\
    0 & 0 & 0 & 0\\
    0 & 0 & 1 & 5
    \end{pmatrix},
    \quad
    \boldsymbol M_4=
    \begin{pmatrix}
    3 & 0 & 1\\
    0 & 2 & 0\\
    0 & 0 & 0
    \end{pmatrix}.
    $$

??? soluzione "Soluzione"

    - \(\boldsymbol M_1\): <strong>sì</strong>. I pivot si trovano nelle colonne 1 e 3 (spostandosi strettamente verso destra) e la riga nulla è in fondo.

    - \(\boldsymbol M_2\): <strong>no</strong>. Il pivot della riga 2 si trova nella colonna 1, che è a sinistra del pivot della riga 1 (colonna 2).

    - \(\boldsymbol M_3\): <strong>no</strong>. La riga nulla (riga 2) si trova sopra una riga non nulla (riga 3).

    - \(\boldsymbol M_4\): <strong>sì</strong>. I pivot si trovano nelle colonne 1 e 2 e la riga nulla è in fondo.

<a id="box-exe_ops_echelon_rectangular-6"></a>

!!! esercizio "Esercizio 6"

    Ridurre la seguente matrice in forma a scala con l'eliminazione di Gauss e indicarne i pivot:

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 1 & 3\\
    2 & 4 & 3 & 7\\
    1 & 2 & 2 & 4
    \end{pmatrix}.
    $$

??? soluzione "Soluzione"

    Il primo pivot è \(a_{11} = 1\); eliminiamo gli elementi sotto di esso, poi cerchiamo il pivot successivo:

    \begin{align*}
    &\left(
    \begin{array}{cccc}
     1 & 2 & 1 & 3 \\
     2 & 4 & 3 & 7 \\
     1 & 2 & 2 & 4 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{cccc}
     1 & 2 & 1 & 3 \\
     0 & 0 & 1 & 1 \\
     1 & 2 & 2 & 4 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{cccc}
     1 & 2 & 1 & 3 \\
     0 & 0 & 1 & 1 \\
     0 & 0 & 1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{cccc}
     1 & 2 & 1 & 3 \\
     0 & 0 & 1 & 1 \\
     0 & 0 & 0 & 0 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_2 \text{)}
    \end{align*}

    Dopo il primo passo, la seconda colonna non ha elementi non nulli nelle righe 2 e 3, quindi passiamo alla terza colonna: il secondo pivot è l'elemento \(1\) in posizione \((2,3)\). L'ultima matrice è in forma a scala, con pivot \(1\) (posizione \((1,1)\)) e \(1\) (posizione \((2,3)\)), e una riga nulla.

<a id="box-exe_ops_gauss_upper-7"></a>

!!! esercizio "Esercizio 7"

    Ridurre la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1 & 1\\
    4 & 3 & 3\\
    8 & 7 & 9
    \end{pmatrix}
    $$

    in forma triangolare superiore con l'eliminazione di Gauss, e utilizzare il risultato per calcolare \(\det(\boldsymbol A)\).

??? soluzione "Soluzione"

    I moltiplicatori sono \(\frac{4}{2} = 2\) e \(\frac{8}{2} = 4\) per la prima colonna, e \(\frac{3}{1} = 3\) per la seconda colonna:

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     4 & 3 & 3 \\
     8 & 7 & 9 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     0 & 1 & 1 \\
     8 & 7 & 9 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     0 & 1 & 1 \\
     0 & 3 & 5 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 4R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     0 & 1 & 1 \\
     0 & 0 & 2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 3R_2 \text{)}
    \end{align*}

    Sono state utilizzate soltanto somme di righe (\(s=0\) scambi di righe), quindi

    $$
    \det(\boldsymbol A) = 2\cdot 1\cdot 2 = 4.
    $$

<a id="box-exe_ops_det_gauss_swap-8"></a>

!!! esercizio "Esercizio 8"

    Calcolare il determinante di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 2 & 4\\
    1 & 1 & 2\\
    3 & 1 & 1
    \end{pmatrix}
    $$

    mediante l'eliminazione di Gauss. Verificare il risultato con lo sviluppo di Laplace lungo la prima riga.

??? soluzione "Soluzione"

    Poiché \(a_{11} = 0\), iniziamo con uno scambio di righe:

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     0 & 2 & 4 \\
     1 & 1 & 2 \\
     3 & 1 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 1 & 2 \\
     0 & 2 & 4 \\
     3 & 1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftrightarrow R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 1 & 2 \\
     0 & 2 & 4 \\
     0 & -2 & -5 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 3R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 1 & 2 \\
     0 & 2 & 4 \\
     0 & 0 & -1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + R_2 \text{)}
    \end{align*}

    Abbiamo effettuato \(s=1\) scambio di righe, quindi

    $$
    \det(\boldsymbol A) = (-1)^1\cdot 1\cdot 2\cdot(-1) = 2.
    $$

    Verifica: \(\det(\boldsymbol A) = 0\cdot(1-2) - 2\cdot(1-6) + 4\cdot(1-3) = 10 - 8 = 2\).

<a id="box-exe_ops_det_gauss_4x4-9"></a>

!!! esercizio "Esercizio 9"

    Calcolare il determinante della matrice \(4\times 4\)

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0 & 1\\
    2 & 5 & 1 & 2\\
    1 & 3 & 2 & 0\\
    0 & 1 & 1 & 3
    \end{pmatrix}
    $$

    mediante l'eliminazione di Gauss.

??? soluzione "Soluzione"

    \begin{align*}
    &\left(
    \begin{array}{cccc}
     1 & 2 & 0 & 1 \\
     2 & 5 & 1 & 2 \\
     1 & 3 & 2 & 0 \\
     0 & 1 & 1 & 3 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{cccc}
     1 & 2 & 0 & 1 \\
     0 & 1 & 1 & 0 \\
     1 & 3 & 2 & 0 \\
     0 & 1 & 1 & 3 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{cccc}
     1 & 2 & 0 & 1 \\
     0 & 1 & 1 & 0 \\
     0 & 1 & 2 & -1 \\
     0 & 1 & 1 & 3 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{cccc}
     1 & 2 & 0 & 1 \\
     0 & 1 & 1 & 0 \\
     0 & 0 & 1 & -1 \\
     0 & 1 & 1 & 3 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{cccc}
     1 & 2 & 0 & 1 \\
     0 & 1 & 1 & 0 \\
     0 & 0 & 1 & -1 \\
     0 & 0 & 0 & 3 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_4 \leftarrow R_4 - R_2 \text{)}
    \end{align*}

    La matrice è triangolare superiore e sono state utilizzate soltanto somme di righe, quindi

    $$
    \det(\boldsymbol A) = 1\cdot 1\cdot 1\cdot 3 = 3.
    $$

    (Con lo sviluppo di Laplace dovremmo calcolare quattro determinanti \(3\times 3\).)

<a id="box-exe_ops_partial_pivoting-10"></a>

!!! esercizio "Esercizio 10"

    Ridurre la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 3 & 1\\
    2 & 1 & 3\\
    4 & 4 & 2
    \end{pmatrix}
    $$

    in forma triangolare superiore utilizzando l'eliminazione di Gauss con <strong>pivoting parziale</strong>. Calcolare poi \(\det(\boldsymbol A)\) e verificare che tutti i moltiplicatori abbiano valore assoluto al più \(1\).

??? soluzione "Soluzione"

    <strong>Passo 1:</strong> nella prima colonna \(|1| < |2| < |4|\): il pivot è \(4\), nella riga 3. <strong>Passo 2:</strong> dopo l'eliminazione, nella seconda colonna (righe 2 e 3) si ha \(|-1| < |2|\): il pivot è \(2\), nella riga 3.

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     1 & 3 & 1 \\
     2 & 1 & 3 \\
     4 & 4 & 2 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     4 & 4 & 2 \\
     2 & 1 & 3 \\
     1 & 3 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftrightarrow R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     4 & 4 & 2 \\
     0 & -1 & 2 \\
     1 & 3 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - \tfrac{1}{2}R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     4 & 4 & 2 \\[1ex]
     0 & -1 & 2 \\[1ex]
     0 & 2 & \tfrac{1}{2} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - \tfrac{1}{4}R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     4 & 4 & 2 \\[1ex]
     0 & 2 & \tfrac{1}{2} \\[1ex]
     0 & -1 & 2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftrightarrow R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     4 & 4 & 2 \\[1ex]
     0 & 2 & \tfrac{1}{2} \\[1ex]
     0 & 0 & \tfrac{9}{4} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + \tfrac{1}{2}R_2 \text{)}
    \end{align*}

    I moltiplicatori sono \(\frac{2}{4} = \frac{1}{2}\), \(\frac{1}{4}\) e \(\frac{-1}{2} = -\frac{1}{2}\): hanno tutti valore assoluto al più \(1\), perché ogni pivot è l'elemento di valore assoluto massimo nella sua colonna (sulla diagonale o sotto di essa).

    Abbiamo effettuato \(s = 2\) scambi di righe, quindi

    $$
    \det(\boldsymbol A) = (-1)^2\cdot 4\cdot 2\cdot\frac{9}{4} = 18.
    $$
