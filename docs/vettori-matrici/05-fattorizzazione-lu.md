---
title: "Fattorizzazione di matrici"
---

# Fattorizzazione di matrici

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.4** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/vettori-matrici-05-fattorizzazione-lu.pdf)

</div>

## 1. Fattorizzazione LU

- La fattorizzazione LU (o decomposizione LU) è una decomposizione matriciale fondamentale che esprime una matrice come prodotto di una matrice triangolare inferiore e di una matrice triangolare superiore.

!!! chiave ""

    Data una matrice quadrata \(\boldsymbol A \in \R^{n \times n}\), una <strong>fattorizzazione PLU</strong> di \(\boldsymbol A\) è una decomposizione della forma

    $$
    \boldsymbol P \boldsymbol A = \boldsymbol L \boldsymbol U,
    $$

    dove:

    - \(\boldsymbol P \in \R^{n \times n}\) è una <strong>matrice di permutazione</strong> (tiene conto degli eventuali scambi di righe),

    - \(\boldsymbol L \in \R^{n \times n}\) è una <strong>matrice triangolare inferiore</strong> con elementi diagonali uguali a 1,

    - \(\boldsymbol U \in \R^{n \times n}\) è una <strong>matrice triangolare superiore</strong>.

- La fattorizzazione si calcola mediante l'eliminazione di Gauss.

- Se non sono necessari scambi di righe, allora \(\boldsymbol P=\boldsymbol I_n\) e la fattorizzazione si riduce alla <strong>fattorizzazione LU</strong>:

    $$
    \boldsymbol A=\boldsymbol L\boldsymbol U.
    $$

- La fattorizzazione PLU/LU è molto utile per risolvere in modo efficiente i sistemi lineari \(\boldsymbol A\boldsymbol x=\boldsymbol b\).

!!! chiave ""

    <strong>Metodo per calcolare la fattorizzazione PLU (LU con pivoting).</strong>

    Partendo da \(\boldsymbol A\), eseguiamo l'eliminazione di Gauss. Ogni volta che è necessario uno scambio di righe, questo viene registrato nella matrice di permutazione \(\boldsymbol P\). Al termine dell'eliminazione otteniamo la matrice triangolare superiore \(\boldsymbol U\), mentre \(\boldsymbol L\) contiene i moltiplicatori dell'eliminazione.

    Più precisamente:

    - Ogni passo di eliminazione \(R_i \leftarrow R_i - \ell_{ij} R_j\) (con \(i>j\)) crea uno zero in posizione \((i,j)\).

    - Il moltiplicatore \(\ell_{ij}\) viene memorizzato in posizione \((i,j)\) di \(\boldsymbol L\).

    - La diagonale di \(\boldsymbol L\) viene riempita con elementi uguali a 1.

    - Se al passo \(j\) si scambiano le righe \(i\) e \(k\) (\(R_i \leftrightarrow R_k\)), si scambiano anche i moltiplicatori già memorizzati nelle righe \(i\) e \(k\) di \(\boldsymbol L\) (nelle colonne \(1,\dots,j-1\)), e lo stesso scambio viene applicato alle righe di \(\boldsymbol P\) (che inizialmente è \(\boldsymbol I_n\)).

<a id="box-ex_lu-3x3-1"></a>

!!! esempio "Esempio 1: Fattorizzazione LU"

    Calcoliamo la fattorizzazione LU di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1 & 1\\
    4 & -6 & 0\\
    -2 & 7 & 2
    \end{pmatrix}.
    $$

    <strong>Passo 1:</strong> Eliminiamo gli elementi al di sotto del primo pivot \(a_{11} = 2\).

    Dobbiamo eliminare \(a_{21} = 4\). Il moltiplicatore è:

    $$
    \ell_{21} = \frac{a_{21}}{a_{11}} = \frac{4}{2} = 2.
    $$

    Eseguiamo \(R_2 \leftarrow R_2 - 2R_1\):

    $$
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & -8 & -2\\
    -2 & 7 & 2
    \end{pmatrix}.
    $$

    Dobbiamo eliminare \(a_{31} = -2\). Il moltiplicatore è:

    $$
    \ell_{31} = \frac{a_{31}}{a_{11}} = \frac{-2}{2} = -1.
    $$

    Eseguiamo \(R_3 \leftarrow R_3 - (-1)R_1 = R_3 + R_1\):

    $$
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & -8 & -2\\
    0 & 8 & 3
    \end{pmatrix}.
    $$

    <strong>Passo 2:</strong> Eliminiamo gli elementi al di sotto del secondo pivot \(-8\).

    Dobbiamo eliminare l'elemento in posizione \((3,2)\), che attualmente vale 8. Il moltiplicatore è:

    $$
    \ell_{32} = \frac{8}{-8} = -1.
    $$

    Eseguiamo \(R_3 \leftarrow R_3 - (-1)R_2 = R_3 + R_2\):

    $$
    \boldsymbol U = 
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & -8 & -2\\
    0 & 0 & 1
    \end{pmatrix}.
    $$

<a id="box-ex_lu-3x3-cont-2"></a>

!!! esempio "Esempio 2: Fattorizzazione LU (continuazione)"

    <strong>Passo 3:</strong> Costruiamo la matrice \(\boldsymbol L\).

    La matrice \(\boldsymbol L\) ha elementi diagonali uguali a 1 e i moltiplicatori al di sotto della diagonale:

    $$
    \boldsymbol L = 
    \begin{pmatrix}
    1 & 0 & 0\\
    \ell_{21} & 1 & 0\\
    \ell_{31} & \ell_{32} & 1
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & 0 & 0\\
    2 & 1 & 0\\
    -1 & -1 & 1
    \end{pmatrix}.
    $$

    <strong>Verifica:</strong> Controlliamo che \(\boldsymbol L \boldsymbol U = \boldsymbol A\):

    \begin{align*}
    \boldsymbol L \boldsymbol U 
    &= 
    \begin{pmatrix}
    1 & 0 & 0\\
    2 & 1 & 0\\
    -1 & -1 & 1
    \end{pmatrix}
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & -8 & -2\\
    0 & 0 & 1
    \end{pmatrix}\\[2ex]
    &=
    \begin{pmatrix}
    2 & 1 & 1\\
    4 & 2-8 & 2-2\\
    -2 & -1+8 & -1+2+1
    \end{pmatrix}\\[2ex]
    &=
    \begin{pmatrix}
    2 & 1 & 1\\
    4 & -6 & 0\\
    -2 & 7 & 2
    \end{pmatrix}
    = \boldsymbol A.
    \end{align*}

- Dati \(\boldsymbol A \in \R^{n\times n}\) e \(k\in\{1,\dots,n\}\), indichiamo con \(\boldsymbol A_{[k]}\) la <strong>sottomatrice principale di testa</strong> di ordine \(k\), cioè la matrice \(k\times k\) formata dalle prime \(k\) righe e dalle prime \(k\) colonne di \(\boldsymbol A\). Il suo determinante \(\det(\boldsymbol A_{[k]})\) è detto <strong>minore principale di testa</strong> di ordine \(k\). Si noti che \(\boldsymbol A_{[n]} = \boldsymbol A\).

<a id="box-obsLUExistence-3"></a>

!!! teorema "Osservazione 1: Esistenza della fattorizzazione LU senza scambi di righe"

    Sia \(\boldsymbol A \in \R^{n\times n}\) una matrice non singolare. Allora \(\boldsymbol A\) ammette una fattorizzazione

    $$
    \boldsymbol A = \boldsymbol L\boldsymbol U,
    $$

    con \(\boldsymbol L\) triangolare inferiore a diagonale unitaria e \(\boldsymbol U\) triangolare superiore, se e solo se tutti i suoi minori principali di testa sono non nulli:

    $$
    \det(\boldsymbol A_{[k]}) \neq 0, \qquad \forall k \in \{1,\dots,n\}.
    $$

    In tal caso, l'eliminazione di Gauss non richiede mai uno scambio di righe e i pivot sono

    $$
    u_{11} = \det(\boldsymbol A_{[1]}), \qquad u_{kk} = \frac{\det(\boldsymbol A_{[k]})}{\det(\boldsymbol A_{[k-1]})}, \quad k\in\{2,\dots,n\}.
    $$

??? dimostrazione "Dimostrazione"

    (\(\Leftarrow\)) Eseguiamo l'eliminazione di Gauss senza scambi di righe. Un'operazione \(R_i \leftarrow R_i - \ell_{ij}R_j\) con \(j<i\) non modifica alcun minore principale di testa: se \(k \ge i\), essa agisce su \(\boldsymbol A_{[k]}\) come la somma a una riga di un multiplo di un'altra riga; se \(k < i\), non modifica \(\boldsymbol A_{[k]}\). Supponiamo di aver eseguito i primi \(k-1\) passi. Allora la sottomatrice principale di testa di ordine \(k\) della matrice corrente è triangolare superiore con elementi diagonali \(u_{11},\dots,u_{kk}\), quindi

    $$
    \det(\boldsymbol A_{[k]}) = u_{11}\,u_{22}\cdots u_{kk}.
    $$

    Poiché \(\det(\boldsymbol A_{[k]})\neq 0\), il pivot \(u_{kk} = \det(\boldsymbol A_{[k]})/\det(\boldsymbol A_{[k-1]})\) è non nullo e il passo \(k\) può essere eseguito senza scambi di righe.

    (\(\Rightarrow\)) Se \(\boldsymbol A = \boldsymbol L\boldsymbol U\), poiché \(\boldsymbol L\) è triangolare inferiore e \(\boldsymbol U\) è triangolare superiore, le prime \(k\) righe e colonne del prodotto coinvolgono soltanto le prime \(k\) righe e colonne dei fattori: \(\boldsymbol A_{[k]} = \boldsymbol L_{[k]}\boldsymbol U_{[k]}\). Quindi \(\det(\boldsymbol A_{[k]}) = 1\cdot u_{11}\cdots u_{kk}\). Poiché \(\det(\boldsymbol A) = u_{11}\cdots u_{nn} \neq 0\), tutti gli \(u_{ii}\) sono non nulli, e lo sono quindi anche tutti i minori principali di testa. <span class="qed">□</span>

- Per la matrice dell'Esempio [Esempio 1](#box-ex_lu-3x3-1) si ha \(\det(\boldsymbol A_{[1]}) = 2\), \(\det(\boldsymbol A_{[2]}) = 2\cdot(-6) - 1\cdot 4 = -16\) e \(\det(\boldsymbol A_{[3]}) = \det(\boldsymbol A) = -16\), da cui si ottengono i pivot \(u_{11} = 2\), \(u_{22} = -16/2 = -8\) e \(u_{33} = -16/(-16) = 1\).

- Se qualche minore principale di testa è nullo, è necessario uno scambio di righe e occorre calcolare una fattorizzazione PLU (con \(\boldsymbol P\neq\boldsymbol I\)). Questo accade negli esempi seguenti.

<a id="box-ex_plu-2x2-4"></a>

!!! esempio "Esempio 3: Fattorizzazione PLU con permutazione di righe"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 1\\
    1 & 1
    \end{pmatrix}.
    $$

    Poiché \(a_{11} = 0\), non possiamo usarlo come pivot. Dobbiamo scambiare le righe 1 e 2.

    Sia

    $$
    \boldsymbol P=
    \begin{pmatrix}
    0 & 1\\
    1 & 0
    \end{pmatrix}
    $$

    la matrice di permutazione che scambia le righe 1 e 2.

    Allora:

    $$
    \boldsymbol{PA}=
    \begin{pmatrix}
    0 & 1\\
    1 & 0
    \end{pmatrix}
    \begin{pmatrix}
    0 & 1\\
    1 & 1
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & 1\\
    0 & 1
    \end{pmatrix}.
    $$

    Ora \(\boldsymbol{PA}\) è già in forma triangolare superiore (non è necessaria alcuna eliminazione al di sotto della diagonale), quindi:

    $$
    \boldsymbol L=
    \begin{pmatrix}
    1 & 0\\
    0 & 1
    \end{pmatrix}
    = \boldsymbol I,
    \qquad
    \boldsymbol U=
    \begin{pmatrix}
    1 & 1\\
    0 & 1
    \end{pmatrix}.
    $$

    Pertanto, la fattorizzazione PLU è:

    $$
    \boldsymbol{PA} = \boldsymbol L \boldsymbol U,
    $$

    dove \(\boldsymbol P = \begin{pmatrix}0 & 1\\1 & 0\end{pmatrix}\), \(\boldsymbol L = \boldsymbol I\) e \(\boldsymbol U = \begin{pmatrix}1 & 1\\0 & 1\end{pmatrix}\).

<a id="box-ex_plu-3x3-5"></a>

!!! esempio "Esempio 4: Fattorizzazione PLU con uno scambio di righe durante l'eliminazione"

    Calcoliamo la fattorizzazione PLU di

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1 & 1\\
    4 & 2 & 3\\
    -2 & 3 & 1
    \end{pmatrix}.
    $$

    Si noti che \(\det(\boldsymbol A_{[2]}) = 2\cdot 2 - 1\cdot 4 = 0\): sarà necessario uno scambio di righe.

    <strong>Passo 1:</strong> Eliminiamo gli elementi al di sotto del primo pivot \(a_{11} = 2\). I moltiplicatori sono \(\ell_{21} = \frac{4}{2} = 2\) e \(\ell_{31} = \frac{-2}{2} = -1\):

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     0 & 0 & 1 \\
     -2 & 3 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     0 & 0 & 1 \\
     0 & 4 & 2 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + R_1 \text{)}
    \end{align*}

    <strong>Passo 2:</strong> L'elemento in posizione \((2,2)\) è \(0\) e non può essere usato come pivot. Scambiamo le righe 2 e 3:

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     2 & 1 & 1 \\
     0 & 4 & 2 \\
     0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftrightarrow R_3 \text{)}
    \end{align*}

    Si scambiano anche i moltiplicatori già calcolati per le righe 2 e 3: ora \(\ell_{21} = -1\) e \(\ell_{31} = 2\). L'elemento al di sotto del nuovo pivot \(4\) è già nullo, quindi \(\ell_{32} = 0\), e l'eliminazione è completa:

    $$
    \boldsymbol U=
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & 4 & 2\\
    0 & 0 & 1
    \end{pmatrix}.
    $$

    <strong>Passo 3:</strong> Costruiamo \(\boldsymbol P\) e \(\boldsymbol L\). La matrice \(\boldsymbol P\) si ottiene da \(\boldsymbol I_3\) scambiando le righe 2 e 3, e \(\boldsymbol L\) contiene i moltiplicatori (scambiati):

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
    -1 & 1 & 0\\
    2 & 0 & 1
    \end{pmatrix}.
    $$

    <strong>Verifica:</strong> Controlliamo che \(\boldsymbol P\boldsymbol A = \boldsymbol L\boldsymbol U\):

    $$
    \boldsymbol P\boldsymbol A=
    \begin{pmatrix}
    1 & 0 & 0\\
    0 & 0 & 1\\
    0 & 1 & 0
    \end{pmatrix}
    \begin{pmatrix}
    2 & 1 & 1\\
    4 & 2 & 3\\
    -2 & 3 & 1
    \end{pmatrix}
    =
    \begin{pmatrix}
    2 & 1 & 1\\
    -2 & 3 & 1\\
    4 & 2 & 3
    \end{pmatrix},
    $$

    \begin{align*}
    \boldsymbol L\boldsymbol U
    &=
    \begin{pmatrix}
    1 & 0 & 0\\
    -1 & 1 & 0\\
    2 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & 4 & 2\\
    0 & 0 & 1
    \end{pmatrix}
    =
    \begin{pmatrix}
    2 & 1 & 1\\
    -2 & -1+4 & -1+2\\
    4 & 2 & 2+1
    \end{pmatrix}
    =
    \begin{pmatrix}
    2 & 1 & 1\\
    -2 & 3 & 1\\
    4 & 2 & 3
    \end{pmatrix}
    = \boldsymbol P\boldsymbol A.
    \end{align*}

- Senza scambiare i moltiplicatori al Passo 2 otterremmo la matrice errata \(\widetilde{\boldsymbol L}\) con \(\tilde\ell_{21}=2\) e \(\tilde\ell_{31}=-1\), e \(\widetilde{\boldsymbol L}\boldsymbol U \neq \boldsymbol P\boldsymbol A\) (la sua seconda riga sarebbe \((4,\,6,\,4)\)).

## 2. Determinante dalla fattorizzazione PLU

<a id="box-obsDetPLU-6"></a>

!!! teorema "Osservazione 2: Determinante dalla fattorizzazione PLU"

    Sia \(\boldsymbol P\boldsymbol A = \boldsymbol L\boldsymbol U\) una fattorizzazione PLU di \(\boldsymbol A\in\R^{n\times n}\), dove \(\boldsymbol P\) si ottiene da \(\boldsymbol I_n\) con \(s\) scambi di righe. Allora

    $$
    \det(\boldsymbol A) = (-1)^{s}\prod_{i=1}^{n} u_{ii} = \pm \prod_{i=1}^{n} u_{ii}.
    $$

    In particolare, \(\boldsymbol A\) è invertibile se e solo se tutti gli elementi diagonali di \(\boldsymbol U\) sono non nulli.

??? dimostrazione "Dimostrazione"

    Ogni scambio di righe cambia il segno del determinante, quindi \(\det(\boldsymbol P) = (-1)^{s}\det(\boldsymbol I_n) = (-1)^s\). Le matrici \(\boldsymbol L\) e \(\boldsymbol U\) sono triangolari, quindi \(\det(\boldsymbol L) = 1\) e \(\det(\boldsymbol U) = \prod_{i=1}^n u_{ii}\). Da \(\det(\boldsymbol P\boldsymbol A) = \det(\boldsymbol L\boldsymbol U)\) e dal teorema di Binet,

    $$
    (-1)^s \det(\boldsymbol A) = \prod_{i=1}^{n} u_{ii},
    $$

    e moltiplichiamo entrambi i membri per \((-1)^s\). <span class="qed">□</span>

<a id="box-ex_det-plu-7"></a>

!!! esempio "Esempio 5: Determinante dalla fattorizzazione PLU"

    - Esempio [Esempio 1](#box-ex_lu-3x3-1): nessuno scambio di righe (\(s=0\)), quindi \(\det(\boldsymbol A) = 2\cdot(-8)\cdot 1 = -16\).

    - Esempio [Esempio 3](#box-ex_plu-2x2-4): uno scambio di righe (\(s=1\)), quindi \(\det(\boldsymbol A) = -(1\cdot 1) = -1\). Infatti, \(\det(\boldsymbol A) = 0\cdot 1 - 1\cdot 1 = -1\).

    - Esempio [Esempio 4](#box-ex_plu-3x3-5): uno scambio di righe (\(s=1\)), quindi \(\det(\boldsymbol A) = -(2\cdot 4\cdot 1) = -8\). Infatti, sviluppando con Laplace lungo la prima riga, \(\det(\boldsymbol A) = 2\cdot(2-9) - 1\cdot(4+6) + 1\cdot(12+4) = -14 - 10 + 16 = -8\).
