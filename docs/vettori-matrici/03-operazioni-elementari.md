---
title: "Operazioni sulle matrici"
---

# Operazioni sulle matrici

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.2** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/vettori-matrici-03-operazioni-elementari.pdf)

</div>

## 1. Operazioni elementari di riga e di colonna

- Le operazioni elementari di riga e di colonna sono strumenti fondamentali dell'algebra lineare. Sono utilizzate in molti algoritmi, tra cui l'eliminazione di Gauss, il calcolo della matrice inversa e le fattorizzazioni di matrici (come la decomposizione LU)

!!! chiave ""

    Data una matrice \(\boldsymbol A \in \R^{m \times n}\), le <strong>operazioni elementari di riga</strong> sono:

    1. <strong>Scambio di righe:</strong> si scambiano le righe \(i\) e \(k\).

        $$
        R_i \leftrightarrow R_k
        $$

    2. <strong>Moltiplicazione di una riga per uno scalare:</strong> si moltiplica la riga \(i\) per uno scalare non nullo \(\lambda \neq 0\).

        $$
        R_i \leftarrow \lambda R_i
        $$

    3. <strong>Somma di righe:</strong> si sostituisce la riga \(i\) con la somma della riga \(i\) e di \(\lambda\) volte la riga \(k\) (con \(i \neq k\)).

        $$
        R_i \leftarrow R_i + \lambda R_k
        $$

<a id="box-ex_row-swap-1"></a>

!!! esempio "Esempio 1: Scambio di righe"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Scambiando le righe 1 e 3, cioè \(R_1 \leftrightarrow R_3\), otteniamo:

    $$
    \begin{pmatrix}
    7 & 8 & 9\\
    4 & 5 & 6\\
    1 & 2 & 3
    \end{pmatrix}.
    $$

<a id="box-ex_row-scaling-2"></a>

!!! esempio "Esempio 2: Moltiplicazione di una riga per uno scalare"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Moltiplicando la riga 2 per \(\lambda = -2\), cioè \(R_2 \leftarrow -2R_2\), otteniamo:

    $$
    \begin{pmatrix}
    1 & 2 & 3\\
    -8 & -10 & -12\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

<a id="box-ex_row-addition-3"></a>

!!! esempio "Esempio 3: Somma di righe"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Sostituendo la riga 2 con la riga 2 meno 4 volte la riga 1, cioè \(R_2 \leftarrow R_2 - 4R_1\), otteniamo:

    $$
    \begin{pmatrix}
    1 & 2 & 3\\
    0 & -3 & -6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Infatti:

    $$
    \begin{pmatrix}4 \\ 5 \\ 6\end{pmatrix} - 4\begin{pmatrix}1 \\ 2 \\ 3\end{pmatrix} = \begin{pmatrix}0 \\ -3 \\ -6\end{pmatrix}.
    $$

!!! chiave ""

    Data una matrice \(\boldsymbol A \in \R^{m \times n}\), le <strong>operazioni elementari di colonna</strong> sono:

    1. <strong>Scambio di colonne:</strong> si scambiano le colonne \(j\) e \(k\).

        $$
        C_j \leftrightarrow C_k
        $$

    2. <strong>Moltiplicazione di una colonna per uno scalare:</strong> si moltiplica la colonna \(j\) per uno scalare non nullo \(\lambda \neq 0\).

        $$
        C_j \leftarrow \lambda C_j
        $$

    3. <strong>Somma di colonne:</strong> si sostituisce la colonna \(j\) con la somma della colonna \(j\) e di \(\lambda\) volte la colonna \(k\) (con \(j \neq k\)).

        $$
        C_j \leftarrow C_j + \lambda C_k
        $$

<a id="box-ex_col-swap-4"></a>

!!! esempio "Esempio 4: Scambio di colonne"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Scambiando le colonne 1 e 3, cioè \(C_1 \leftrightarrow C_3\), otteniamo:

    $$
    \begin{pmatrix}
    3 & 2 & 1\\
    6 & 5 & 4\\
    9 & 8 & 7
    \end{pmatrix}.
    $$

<a id="box-ex_col-scaling-5"></a>

!!! esempio "Esempio 5: Moltiplicazione di una colonna per uno scalare"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Moltiplicando la colonna 2 per \(\lambda = 3\), cioè \(C_2 \leftarrow 3C_2\), otteniamo:

    $$
    \begin{pmatrix}
    1 & 6 & 3\\
    4 & 15 & 6\\
    7 & 24 & 9
    \end{pmatrix}.
    $$

<a id="box-ex_col-addition-6"></a>

!!! esempio "Esempio 6: Somma di colonne"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Sostituendo la colonna 3 con la colonna 3 più 2 volte la colonna 1, cioè \(C_3 \leftarrow C_3 + 2C_1\), otteniamo:

    $$
    \begin{pmatrix}
    1 & 2 & 5\\
    4 & 5 & 14\\
    7 & 8 & 23
    \end{pmatrix}.
    $$

    Infatti:

    $$
    \begin{pmatrix}3 \\ 6 \\ 9\end{pmatrix} + 2\begin{pmatrix}1 \\ 4 \\ 7\end{pmatrix} = \begin{pmatrix}5 \\ 14 \\ 23\end{pmatrix}.
    $$

## 2. Effetto delle operazioni elementari sul determinante

!!! chiave ""

    Sia \(\boldsymbol A \in \R^{n \times n}\) una matrice quadrata. Le operazioni elementari di riga agiscono sul determinante nel modo seguente:

    1. <strong>Scambio di righe:</strong> \(R_i \leftrightarrow R_k\) cambia il segno del determinante.

        $$
        \det(\text{nuova matrice}) = -\det(\boldsymbol A)
        $$

    2. <strong>Moltiplicazione di una riga per uno scalare:</strong> \(R_i \leftarrow \lambda R_i\) (con \(\lambda \neq 0\)) moltiplica il determinante per \(\lambda\).

        $$
        \det(\text{nuova matrice}) = \lambda \det(\boldsymbol A)
        $$

    3. <strong>Somma di righe:</strong> \(R_i \leftarrow R_i + \lambda R_k\) (con \(i \neq k\)) non cambia il determinante.

        $$
        \det(\text{nuova matrice}) = \det(\boldsymbol A)
        $$

<a id="box-ex_det-row-swap-7"></a>

!!! esempio "Esempio 7: Effetto dello scambio di righe sul determinante"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    Il determinante è:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    Scambiando le righe 1 e 2, cioè \(R_1 \leftrightarrow R_2\), otteniamo:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    3 & 4\\
    1 & 2
    \end{pmatrix}.
    $$

    Il determinante della nuova matrice è:

    $$
    \det(\boldsymbol A') = 3 \cdot 2 - 4 \cdot 1 = 2 = -\det(\boldsymbol A).
    $$

<a id="box-ex_det-row-scaling-8"></a>

!!! esempio "Esempio 8: Effetto della moltiplicazione di una riga per uno scalare sul determinante"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1\\
    0 & 3
    \end{pmatrix}.
    $$

    Il determinante è:

    $$
    \det(\boldsymbol A) = 2 \cdot 3 - 1 \cdot 0 = 6.
    $$

    Moltiplicando la riga 1 per \(\lambda = 2\), cioè \(R_1 \leftarrow 2R_1\), otteniamo:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    4 & 2\\
    0 & 3
    \end{pmatrix}.
    $$

    Il determinante della nuova matrice è:

    $$
    \det(\boldsymbol A') = 4 \cdot 3 - 2 \cdot 0 = 12 = 2 \cdot \det(\boldsymbol A) = \lambda \det(\boldsymbol A).
    $$

<a id="box-ex_det-row-addition-9"></a>

!!! esempio "Esempio 9: Effetto della somma di righe sul determinante"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    Il determinante è:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    Sostituendo la riga 2 con la riga 2 meno 3 volte la riga 1, cioè \(R_2 \leftarrow R_2 - 3R_1\), otteniamo:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 2\\
    0 & -2
    \end{pmatrix}.
    $$

    Il determinante della nuova matrice è:

    $$
    \det(\boldsymbol A') = 1 \cdot (-2) - 2 \cdot 0 = -2 = \det(\boldsymbol A).
    $$

!!! chiave ""

    Sia \(\boldsymbol A \in \R^{n \times n}\) una matrice quadrata. Le operazioni elementari di colonna agiscono sul determinante nel modo seguente:

    1. <strong>Scambio di colonne:</strong> \(C_j \leftrightarrow C_k\) cambia il segno del determinante.

        $$
        \det(\text{nuova matrice}) = -\det(\boldsymbol A)
        $$

    2. <strong>Moltiplicazione di una colonna per uno scalare:</strong> \(C_j \leftarrow \lambda C_j\) (con \(\lambda \neq 0\)) moltiplica il determinante per \(\lambda\).

        $$
        \det(\text{nuova matrice}) = \lambda \det(\boldsymbol A)
        $$

    3. <strong>Somma di colonne:</strong> \(C_j \leftarrow C_j + \lambda C_k\) (con \(j \neq k\)) non cambia il determinante.

        $$
        \det(\text{nuova matrice}) = \det(\boldsymbol A)
        $$

<a id="box-ex_det-col-swap-10"></a>

!!! esempio "Esempio 10: Effetto dello scambio di colonne sul determinante"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    Il determinante è:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    Scambiando le colonne 1 e 2, cioè \(C_1 \leftrightarrow C_2\), otteniamo:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    2 & 1\\
    4 & 3
    \end{pmatrix}.
    $$

    Il determinante della nuova matrice è:

    $$
    \det(\boldsymbol A') = 2 \cdot 3 - 1 \cdot 4 = 2 = -\det(\boldsymbol A).
    $$

<a id="box-ex_det-col-scaling-11"></a>

!!! esempio "Esempio 11: Effetto della moltiplicazione di una colonna per uno scalare sul determinante"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    Il determinante è:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    Moltiplicando la colonna 2 per \(\lambda = 3\), cioè \(C_2 \leftarrow 3C_2\), otteniamo:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 6\\
    3 & 12
    \end{pmatrix}.
    $$

    Il determinante della nuova matrice è:

    $$
    \det(\boldsymbol A') = 1 \cdot 12 - 6 \cdot 3 = -6 = 3 \cdot (-2) = \lambda \det(\boldsymbol A).
    $$

<a id="box-ex_det-col-addition-12"></a>

!!! esempio "Esempio 12: Effetto della somma di colonne sul determinante"

    Consideriamo la matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    Il determinante è:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    Sostituendo la colonna 2 con la colonna 2 più 2 volte la colonna 1, cioè \(C_2 \leftarrow C_2 + 2C_1\), otteniamo:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 4\\
    3 & 10
    \end{pmatrix}.
    $$

    Il determinante della nuova matrice è:

    $$
    \det(\boldsymbol A') = 1 \cdot 10 - 4 \cdot 3 = -2 = \det(\boldsymbol A).
    $$

- Queste proprietà discendono dal fatto che il determinante di una matrice è uguale al determinante della sua trasposta (si vedano le proprietà dei determinanti nel capitolo sulle matrici) e che un'operazione di colonna su una matrice corrisponde alla relativa operazione di riga sulla sua trasposta. Di conseguenza, le operazioni di colonna hanno sul determinante lo stesso effetto delle corrispondenti operazioni di riga.

- Questi risultati sono fondamentali per comprendere come si comporta il determinante rispetto alle operazioni elementari, aspetto cruciale in algoritmi come l'eliminazione di Gauss e la fattorizzazione di matrici.

## 3. Eliminazione di Gauss e forma a scala

- Le operazioni elementari di riga permettono di trasformare qualsiasi matrice in una matrice con una struttura “a scala”, dalla quale si possono leggere facilmente molte proprietà della matrice originale (per esempio, il suo determinante). La procedura sistematica che realizza questa trasformazione si chiama <strong>eliminazione di Gauss</strong>.

<a id="box-defRowEchelonForm-13"></a>

!!! definizione "Definizione 1: Forma a scala per righe"

    Una matrice \(\boldsymbol U \in \R^{m \times n}\) è in <strong>forma a scala (per righe)</strong> se:

    1. tutte le sue righe nulle (se presenti) si trovano sotto tutte le sue righe non nulle;

    2. il primo elemento non nullo di ogni riga non nulla (detto <strong>pivot</strong> della riga) si trova strettamente a destra del pivot della riga precedente.

- Di conseguenza, tutti gli elementi sotto un pivot sono uguali a zero.

- Una matrice quadrata in forma a scala è triangolare superiore.

!!! chiave ""

    <strong>Eliminazione di Gauss.</strong> Data \(\boldsymbol A \in \R^{m \times n}\), si esaminano le colonne da sinistra verso destra. A ogni passo, considerando le righe non ancora utilizzate come righe pivot:

    1. si individua la prima colonna che contiene un elemento non nullo in queste righe; se necessario, si porta tale elemento nella prima di queste righe con uno scambio di righe \(R_k \leftrightarrow R_i\) (questo elemento non nullo è il pivot);

    2. per ogni riga \(i\) sotto la riga pivot \(k\), si crea uno zero sotto il pivot con la somma di righe

        $$
        R_i \leftarrow R_i - \frac{a_{ij}}{a_{kj}}\, R_k,
        $$

        dove \(a_{kj}\) è il pivot e \(a_{ij}\) è l'elemento da eliminare (nella matrice corrente);

    3. si ripete il procedimento sulle righe rimanenti.

    Al termine, la matrice è in forma a scala. Si utilizzano soltanto scambi di righe e somme di righe.

<a id="box-obsDetGauss-14"></a>

!!! teorema "Osservazione 1: Determinante tramite eliminazione di Gauss"

    Sia \(\boldsymbol A \in \R^{n \times n}\) e sia \(\boldsymbol U\) una forma a scala di \(\boldsymbol A\) ottenuta con l'eliminazione di Gauss mediante \(s\) scambi di righe (e un numero qualsiasi di somme di righe). Allora

    $$
    \det(\boldsymbol A) = (-1)^{s} \prod_{i=1}^{n} u_{ii}.
    $$

    In particolare, \(\det(\boldsymbol A) = 0\) se e solo se \(\boldsymbol U\) ha uno zero sulla diagonale.

??? dimostrazione "Dimostrazione"

    Ogni somma di righe non cambia il determinante e ogni scambio di righe ne cambia il segno. Quindi \(\det(\boldsymbol U) = (-1)^{s}\det(\boldsymbol A)\), cioè \(\det(\boldsymbol A) = (-1)^{s}\det(\boldsymbol U)\). Poiché \(\boldsymbol U\) è quadrata e in forma a scala, essa è triangolare superiore, e il suo determinante è il prodotto degli elementi diagonali. <span class="qed">□</span>

<a id="box-ex_det-gauss-15"></a>

!!! esempio "Esempio 13: Determinante tramite eliminazione di Gauss"

    Consideriamo

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 1 & 2\\
    1 & 1 & 1\\
    2 & 1 & 3
    \end{pmatrix}.
    $$

    Riduciamo \(\boldsymbol A\) in forma a scala con l'eliminazione di Gauss.

    \begin{align*}
    &\left(
    \begin{array}{ccc}
     0 & 1 & 2 \\
     1 & 1 & 1 \\
     2 & 1 & 3 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 1 & 1 \\
     0 & 1 & 2 \\
     2 & 1 & 3 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftrightarrow R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 1 & 1 \\
     0 & 1 & 2 \\
     0 & -1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc}
     1 & 1 & 1 \\
     0 & 1 & 2 \\
     0 & 0 & 3 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + R_2 \text{)}
    \end{align*}

    La matrice è ora in forma a scala. Abbiamo effettuato \(s=1\) scambio di righe, quindi

    $$
    \det(\boldsymbol A) = (-1)^{1}\cdot 1 \cdot 1 \cdot 3 = -3.
    $$

    Infatti, con lo sviluppo di Laplace lungo la prima riga: \(\det(\boldsymbol A) = 0\cdot(3-1) - 1\cdot(3-2) + 2\cdot(1-2) = -3\).

## 4. Pivoting e pivoting parziale

- Negli algoritmi numerici, come le fattorizzazioni di matrici e i metodi di riduzione per righe, il pivoting è una tecnica utilizzata per migliorare la stabilità numerica ed evitare divisioni per zero.

- L'elemento pivot è l'elemento utilizzato come divisore nel processo di eliminazione.

### 4.1 Pivoting

!!! chiave ""

    Il <strong>pivoting</strong> è il procedimento con cui si sceglie un opportuno elemento pivot in una matrice per eseguire i passi di eliminazione negli algoritmi di riduzione per righe.

    Quando si esegue l'eliminazione per righe su una matrice \(\boldsymbol A \in \R^{n \times n}\), al passo \(k\):

    - L'<strong>elemento pivot</strong> è l'elemento \(a_{kk}\) (l'elemento diagonale in posizione \((k,k)\)).

    - Se \(a_{kk} = 0\), non possiamo usarlo come divisore, quindi dobbiamo scambiare la riga \(k\) con una riga \(i > k\) tale che \(a_{ik} \neq 0\).

    - Questo scambio di righe si chiama <strong>pivoting</strong>.

<a id="box-ex_pivoting-16"></a>

!!! esempio "Esempio 14: Pivoting nell'eliminazione per righe"

    Consideriamo la matrice:

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 2 & 1\\
    1 & -1 & 0\\
    2 & 1 & 3
    \end{pmatrix}.
    $$

    Non possiamo usare \(a_{11} = 0\) come primo pivot. Dobbiamo scambiare la riga 1 con una riga che abbia un elemento non nullo nella prima colonna.

    Scambiamo le righe 1 e 2 (cioè \(R_1 \leftrightarrow R_2\)):

    $$
    \begin{pmatrix}
    1 & -1 & 0\\
    0 & 2 & 1\\
    2 & 1 & 3
    \end{pmatrix}.
    $$

    Ora \(a_{11} = 1 \neq 0\) e possiamo procedere con l'eliminazione:

    $$
    R_3 \leftarrow R_3 - 2R_1:
    \quad
    \begin{pmatrix}
    1 & -1 & 0\\
    0 & 2 & 1\\
    0 & 3 & 3
    \end{pmatrix}.
    $$

    Usiamo ora \(a_{22} = 2\) come secondo pivot:

    $$
    R_3 \leftarrow R_3 - \frac{3}{2}R_2:
    \quad
    \begin{pmatrix}
    1 & -1 & 0\\[0.5ex]
    0 & 2 & 1\\[0.5ex]
    0 & 0 & \frac{3}{2}
    \end{pmatrix}.
    $$

    La matrice è ora in forma triangolare superiore.

### 4.2 Pivoting parziale

!!! chiave ""

    Il <strong>pivoting parziale</strong> è una strategia per migliorare la stabilità numerica che consiste nello scegliere come pivot l'elemento disponibile di valore assoluto massimo.

    Al passo \(k\) dell'eliminazione di Gauss:

    1. Si trova la riga \(i \ge k\) tale che \(|a_{ik}|\) sia massimo tra tutti i \(|a_{jk}|\) con \(j \ge k\).

    2. Si scambia la riga \(k\) con la riga \(i\) (cioè \(R_k \leftrightarrow R_i\)).

    3. Si usa il nuovo \(a_{kk}\) come pivot.

    In questo modo:

    - Il pivot è l'elemento di valore assoluto massimo nella sua colonna, tra gli elementi sulla diagonale o sotto di essa.

    - La divisione per un numero più grande riduce gli errori di arrotondamento nell'aritmetica in virgola mobile.

    - Il metodo è numericamente più stabile.

<a id="box-ex_partial-pivoting-17"></a>

!!! esempio "Esempio 15: Pivoting parziale nell'eliminazione per righe"

    Consideriamo la matrice:

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 1\\
    3 & -1 & 2\\
    2 & 3 & -1
    \end{pmatrix}.
    $$

    <strong>Passo 1:</strong> troviamo l'elemento di valore assoluto massimo nella prima colonna.

    $$
    |a_{11}| = 1, \quad |a_{21}| = 3, \quad |a_{31}| = 2.
    $$

    Il massimo è \(|a_{21}| = 3\), quindi scambiamo le righe 1 e 2:

    $$
    R_1 \leftrightarrow R_2:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\
    1 & 2 & 1\\
    2 & 3 & -1
    \end{pmatrix}.
    $$

    Eliminiamo ora gli elementi sotto il pivot \(a_{11} = 3\):

    \begin{align*}
    &R_2 \leftarrow R_2 - \frac{1}{3}R_1:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\[0.5ex]
    0 & \frac{7}{3} & \frac{1}{3}\\[0.5ex]
    2 & 3 & -1
    \end{pmatrix},\\[2ex]
    &R_3 \leftarrow R_3 - \frac{2}{3}R_1:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\[0.5ex]
    0 & \frac{7}{3} & \frac{1}{3}\\[0.5ex]
    0 & \frac{11}{3} & -\frac{7}{3}
    \end{pmatrix}.
    \end{align*}

    <strong>Passo 2:</strong> troviamo l'elemento di valore assoluto massimo nella seconda colonna (righe 2 e 3).

    $$
    \left|\frac{7}{3}\right| = \frac{7}{3}, 
    \quad 
    \left|\frac{11}{3}\right| = \frac{11}{3}.
    $$

    Il massimo è \(\left|\frac{11}{3}\right|\), quindi scambiamo le righe 2 e 3:

    $$
    R_2 \leftrightarrow R_3:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\[0.5ex]
    0 & \frac{11}{3} & -\frac{7}{3}\\[0.5ex]
    0 & \frac{7}{3} & \frac{1}{3}
    \end{pmatrix}.
    $$

    Eliminiamo l'elemento sotto il pivot \(a_{22} = \frac{11}{3}\):

    $$
    R_3 \leftarrow R_3 - \frac{7}{11}R_2:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\[0.5ex]
    0 & \frac{11}{3} & -\frac{7}{3}\\[0.5ex]
    0 & 0 & \frac{20}{11}
    \end{pmatrix}.
    $$

    La matrice è ora in forma triangolare superiore (forma a scala).

<a id="box-ex_pivoting-comparison-18"></a>

!!! esempio "Esempio 16: Confronto: senza e con pivoting parziale"

    Consideriamo la matrice:

    $$
    \boldsymbol A =
    \begin{pmatrix}
    \frac{1}{10000} & 1\\
    1 & 1
    \end{pmatrix}.
    $$

    <strong>Senza pivoting parziale:</strong>

    Usando \(a_{11} = \frac{1}{10000}\) come pivot:

    $$
    R_2 \leftarrow R_2 - 10000\,R_1.
    $$

    Si ottiene:

    $$
    \begin{pmatrix}
    \frac{1}{10000} & 1\\
    0 & 1 - 10000
    \end{pmatrix}
    =
    \begin{pmatrix}
    \frac{1}{10000} & 1\\
    0 & -9999
    \end{pmatrix}.
    $$

    Il moltiplicatore elevato \(10000\) può causare errori di arrotondamento significativi nell'aritmetica in virgola mobile.

    <strong>Con pivoting parziale:</strong>

    Poiché \(|a_{21}| = 1 > |a_{11}| = \frac{1}{10000}\), scambiamo le righe:

    $$
    R_1 \leftrightarrow R_2:
    \quad
    \begin{pmatrix}
    1 & 1\\
    \frac{1}{10000} & 1
    \end{pmatrix}.
    $$

    Eliminiamo ora usando \(a_{11} = 1\) come pivot:

    $$
    R_2 \leftarrow R_2 - \frac{1}{10000}R_1:
    \quad
    \begin{pmatrix}
    1 & 1\\
    0 & 1 - \frac{1}{10000}
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & 1\\
    0 & \frac{9999}{10000}
    \end{pmatrix}.
    $$

    Il moltiplicatore \(\frac{1}{10000}\) è molto più piccolo, e ciò porta a una migliore stabilità numerica.

- Il pivoting parziale è cruciale nell'algebra lineare numerica per garantire che gli algoritmi producano risultati accurati, specialmente quando si lavora con matrici i cui elementi hanno ordini di grandezza molto diversi.

- La maggior parte dei software numerici moderni (come MATLAB, NumPy, CPLEX, Gurobi) utilizza automaticamente il pivoting parziale nell'eliminazione di Gauss e nella fattorizzazione LU.

- Il costo computazionale del pivoting parziale è minimo rispetto al beneficio in termini di stabilità numerica.
