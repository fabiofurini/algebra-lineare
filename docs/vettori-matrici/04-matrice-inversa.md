---
title: "Inversione di matrici"
---

# Inversione di matrici

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.3** · dalle dispense di Fabio Furini · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf) · [:material-presentation: Slide (PDF)](../pdf/slide-04-3-inversa.pdf)

</div>

## 1. Proprietà della matrice inversa

- Ricordiamo (si veda il capitolo sulle matrici) che una matrice quadrata \(\boldsymbol A \in \R^{n\times n}\) è <strong>invertibile</strong> se esiste una matrice \(\boldsymbol A^{-1} \in \R^{n\times n}\) tale che \(\boldsymbol A\boldsymbol A^{-1} = \boldsymbol A^{-1}\boldsymbol A = \boldsymbol I\). Una matrice quadrata non invertibile si dice <strong>singolare</strong>.

- In questo capitolo, \(\boldsymbol A'\) denota la trasposta di \(\boldsymbol A\), come nel capitolo sulle matrici.

<a id="box-propInverseUnique-1"></a>

!!! teorema "Proposizione 1: Unicità dell'inversa"

    Sia \(\boldsymbol A \in \R^{n\times n}\) invertibile. Se \(\boldsymbol B, \boldsymbol C \in \R^{n\times n}\) sono tali che \(\boldsymbol A\boldsymbol B = \boldsymbol B\boldsymbol A = \boldsymbol I\) e \(\boldsymbol A\boldsymbol C = \boldsymbol C\boldsymbol A = \boldsymbol I\), allora \(\boldsymbol B = \boldsymbol C\).

??? dimostrazione "Dimostrazione"

    Usando la proprietà associativa del prodotto tra matrici, si ha:

    $$
    \boldsymbol B = \boldsymbol B\boldsymbol I = \boldsymbol B(\boldsymbol A\boldsymbol C) = (\boldsymbol B\boldsymbol A)\boldsymbol C = \boldsymbol I\boldsymbol C = \boldsymbol C.
    $$

    <p class="qed-riga"><span class="qed">□</span></p>

<a id="box-propInverseProperties-2"></a>

!!! teorema "Proposizione 2: Proprietà dell'inversa"

    Siano \(\boldsymbol A, \boldsymbol B \in \R^{n\times n}\) matrici invertibili. Allora:

    1. \(\boldsymbol A^{-1}\) è invertibile e \((\boldsymbol A^{-1})^{-1} = \boldsymbol A\);

    2. \(\boldsymbol A\boldsymbol B\) è invertibile e \((\boldsymbol A\boldsymbol B)^{-1} = \boldsymbol B^{-1}\boldsymbol A^{-1}\);

    3. \(\boldsymbol A'\) è invertibile e \((\boldsymbol A')^{-1} = (\boldsymbol A^{-1})'\);

    4. \(\det(\boldsymbol A) \neq 0\) e \(\det(\boldsymbol A^{-1}) = \dfrac{1}{\det(\boldsymbol A)}\).

??? dimostrazione "Dimostrazione"

    Per l'unicità dell'inversa, in ciascun caso è sufficiente esibire una matrice che, moltiplicata a sinistra e a destra, dia \(\boldsymbol I\).

    1. Da \(\boldsymbol A^{-1}\boldsymbol A = \boldsymbol A\boldsymbol A^{-1} = \boldsymbol I\) segue che la matrice \(\boldsymbol A\) è l'inversa di \(\boldsymbol A^{-1}\).

    2. Usando la proprietà associativa:

        $$
        (\boldsymbol A\boldsymbol B)(\boldsymbol B^{-1}\boldsymbol A^{-1}) = \boldsymbol A(\boldsymbol B\boldsymbol B^{-1})\boldsymbol A^{-1} = \boldsymbol A\boldsymbol I\boldsymbol A^{-1} = \boldsymbol A\boldsymbol A^{-1} = \boldsymbol I,
        $$

        $$
        (\boldsymbol B^{-1}\boldsymbol A^{-1})(\boldsymbol A\boldsymbol B) = \boldsymbol B^{-1}(\boldsymbol A^{-1}\boldsymbol A)\boldsymbol B = \boldsymbol B^{-1}\boldsymbol I\boldsymbol B = \boldsymbol B^{-1}\boldsymbol B = \boldsymbol I.
        $$

    3. Ricordiamo che \((\boldsymbol C\boldsymbol D)' = \boldsymbol D'\boldsymbol C'\) per ogni \(\boldsymbol C, \boldsymbol D \in \R^{n\times n}\): infatti, l'elemento \((i,j)\) di \((\boldsymbol C\boldsymbol D)'\) è l'elemento \((j,i)\) di \(\boldsymbol C\boldsymbol D\), cioè \(\sum_{k=1}^n c_{jk}d_{ki} = \sum_{k=1}^n d'_{ik}c'_{kj}\), che è l'elemento \((i,j)\) di \(\boldsymbol D'\boldsymbol C'\). Quindi, poiché \(\boldsymbol I' = \boldsymbol I\):

        $$
        \boldsymbol A'(\boldsymbol A^{-1})' = (\boldsymbol A^{-1}\boldsymbol A)' = \boldsymbol I' = \boldsymbol I,
        \qquad
        (\boldsymbol A^{-1})'\boldsymbol A' = (\boldsymbol A\boldsymbol A^{-1})' = \boldsymbol I' = \boldsymbol I.
        $$

    4. Dalla regola del prodotto dei determinanti (teorema di Binet):

        $$
        \det(\boldsymbol A)\det(\boldsymbol A^{-1}) = \det(\boldsymbol A\boldsymbol A^{-1}) = \det(\boldsymbol I) = 1.
        $$

        Quindi \(\det(\boldsymbol A)\neq 0\) e \(\det(\boldsymbol A^{-1}) = 1/\det(\boldsymbol A)\).

    <p class="qed-riga"><span class="qed">□</span></p>

- Si noti l'ordine invertito in \((\boldsymbol A\boldsymbol B)^{-1} = \boldsymbol B^{-1}\boldsymbol A^{-1}\): poiché il prodotto tra matrici non è commutativo, in generale \((\boldsymbol A\boldsymbol B)^{-1} \neq \boldsymbol A^{-1}\boldsymbol B^{-1}\).

- La proprietà 4 mostra che una matrice con \(\det(\boldsymbol A) = 0\) non può essere invertibile, cioè è singolare.

## 2. Calcolo dell'inversa

### 2.1 Metodo di Gauss–Jordan

!!! chiave ""

    <strong>Metodo di Gauss–Jordan (idea).</strong> Per calcolare \( \boldsymbol A^{-1} \), si costruisce la matrice aumentata

    $$
    \left(\, \boldsymbol A \mid \boldsymbol I \,\right)
    $$

    e si applicano <strong>operazioni elementari di riga</strong> per trasformare il blocco sinistro nella matrice identità. Se si ottiene

    $$
    \left(\, \boldsymbol I \mid \boldsymbol B \,\right),
    $$

    allora \( \boldsymbol B = \boldsymbol A^{-1} \).

<a id="box-ex_inv-gj-2x2-3"></a>

!!! esempio "Esempio 1: matrice inversa con il metodo di Gauss–Jordan"

    Consideriamo

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1\\[0.5ex]
    1 & 1
    \end{pmatrix}.
    $$

    Calcoliamo la matrice inversa \(\boldsymbol A^{-1}\) con il metodo di Gauss–Jordan.

    \begin{align*}
    &\left(
    \begin{array}{cc|cc}
    2 & 1 & 1 & 0\\
    1 & 1 & 0 & 1
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{cc|cc}
    1 & 1 & 0 & 1\\
    2 & 1 & 1 & 0
    \end{array}
    \right)
    \hspace{1em}\text{(} R_1 \leftrightarrow R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{cc|cc}
    1 & 1 & 0 & 1\\
    0 & -1 & 1 & -2
    \end{array}
    \right)
    \hspace{1em}\text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{cc|cc}
    1 & 1 & 0 & 1\\
    0 & 1 & -1 & 2
    \end{array}
    \right)
    \hspace{1em}\text{(} R_2 \leftarrow -R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{cc|cc}
    1 & 0 & 1 & -1\\
    0 & 1 & -1 & 2
    \end{array}
    \right)
    \hspace{1em}\text{(} R_1 \leftarrow R_1 - R_2 \text{)}
    \end{align*}

    Poiché il blocco sinistro è la matrice identità, otteniamo:

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    1 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix}.
    $$

    Possiamo verificare:

    $$
    \boldsymbol A \boldsymbol A^{-1}
    =
    \begin{pmatrix}
    2 & 1\\[0.5ex]
    1 & 1
    \end{pmatrix}
    \begin{pmatrix}
    1 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & 0\\[0.5ex]
    0 & 1
    \end{pmatrix}
    = \boldsymbol I.
    $$

<a id="box-ex_inv-gj-3x3-4"></a>

!!! esempio "Esempio 2: matrice inversa con il metodo di Gauss–Jordan"

    Consideriamo

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0\\[0.5ex]
    0 & 1 & 1\\[0.5ex]
    2 & 0 & 1
    \end{pmatrix}.
    $$

    Calcoliamo la matrice inversa \(\boldsymbol A^{-1}\) con il metodo di Gauss–Jordan.

    \begin{align*}
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 0 & 1 & 0 & 0 \\
     0 & 1 & 1 & 0 & 1 & 0 \\
     2 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2  & 0 & 1  & 0 & 0 \\
     0 & 1  & 1 & 0  & 1 & 0 \\
     0 & -4 & 1 & -2 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -2 & 1 & -2 & 0 \\
     0 & 1 & 1  & 0 & 1  & 0 \\
     0 & -4 & 1 & -2 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - 2R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -2 & 1  & -2 & 0 \\
     0 & 1 & 1  & 0  & 1  & 0 \\
     0 & 0 & 5  & -2 & 4  & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + 4R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & -2 & 1 & -2 & 0 \\[1ex]
     0 & 1 & 1  & 0 & 1  & 0 \\[1ex]
     0 & 0 & 1  & -\tfrac{2}{5} & \tfrac{4}{5} & \tfrac{1}{5} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow \tfrac{1}{5}R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & \tfrac{1}{5}  & -\tfrac{2}{5} & \tfrac{2}{5} \\[1ex]
     0 & 1 & 1 & 0 & 1 & 0 \\[1ex]
     0 & 0 & 1 & -\tfrac{2}{5} & \tfrac{4}{5} & \tfrac{1}{5} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 + 2R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & \tfrac{1}{5} & -\tfrac{2}{5} & \tfrac{2}{5} \\[1ex]
     0 & 1 & 0 & \tfrac{2}{5} & \tfrac{1}{5} & -\tfrac{1}{5} \\[1ex]
     0 & 0 & 1 & -\tfrac{2}{5} & \tfrac{4}{5} & \tfrac{1}{5} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - R_3 \text{)}
    \end{align*}

    Poiché il blocco sinistro è la matrice identità, otteniamo:

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    \tfrac{1}{5} & -\tfrac{2}{5} & \tfrac{2}{5}\\[0.8ex]
    \tfrac{2}{5} & \tfrac{1}{5}  & -\tfrac{1}{5}\\[0.8ex]
    -\tfrac{2}{5} & \tfrac{4}{5} & \tfrac{1}{5}
    \end{pmatrix}
    =
    \frac{1}{5}
    \begin{pmatrix}
    1 & -2 & 2\\[0.5ex]
    2 & 1  & -1\\[0.5ex]
    -2 & 4 & 1
    \end{pmatrix}
    .
    $$

<a id="box-ex_inv-gj-3x3-swap-5"></a>

!!! esempio "Esempio 3: matrice inversa con il metodo di Gauss–Jordan e scambio di righe"

    Consideriamo

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 1 & 2\\[0.5ex]
    1 & 0 & 3\\[0.5ex]
    4 & -3 & 8
    \end{pmatrix}.
    $$

    Calcoliamo la matrice inversa \(\boldsymbol A^{-1}\) con il metodo di Gauss–Jordan. Poiché \(a_{11}=0\), iniziamo con uno scambio di righe.

    \begin{align*}
    &\left(
    \begin{array}{ccc|ccc}
     0 & 1 & 2 & 1 & 0 & 0 \\
     1 & 0 & 3 & 0 & 1 & 0 \\
     4 & -3 & 8 & 0 & 0 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 3 & 0 & 1 & 0 \\
     0 & 1 & 2 & 1 & 0 & 0 \\
     4 & -3 & 8 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftrightarrow R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 3 & 0 & 1 & 0 \\
     0 & 1 & 2 & 1 & 0 & 0 \\
     0 & -3 & -4 & 0 & -4 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - 4R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 3 & 0 & 1 & 0 \\
     0 & 1 & 2 & 1 & 0 & 0 \\
     0 & 0 & 2 & 3 & -4 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 + 3R_2 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 3 & 0 & 1 & 0 \\[1ex]
     0 & 1 & 2 & 1 & 0 & 0 \\[1ex]
     0 & 0 & 1 & \tfrac{3}{2} & -2 & \tfrac{1}{2} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow \tfrac{1}{2}R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & -\tfrac{9}{2} & 7 & -\tfrac{3}{2} \\[1ex]
     0 & 1 & 2 & 1 & 0 & 0 \\[1ex]
     0 & 0 & 1 & \tfrac{3}{2} & -2 & \tfrac{1}{2} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_1 \leftarrow R_1 - 3R_3 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 0 & 0 & -\tfrac{9}{2} & 7 & -\tfrac{3}{2} \\[1ex]
     0 & 1 & 0 & -2 & 4 & -1 \\[1ex]
     0 & 0 & 1 & \tfrac{3}{2} & -2 & \tfrac{1}{2} \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_3 \text{)}
    \end{align*}

    Poiché il blocco sinistro è la matrice identità, otteniamo:

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    -\tfrac{9}{2} & 7 & -\tfrac{3}{2}\\[0.8ex]
    -2 & 4  & -1\\[0.8ex]
    \tfrac{3}{2} & -2 & \tfrac{1}{2}
    \end{pmatrix}
    =
    \frac{1}{2}
    \begin{pmatrix}
    -9 & 14 & -3\\[0.5ex]
    -4 & 8  & -2\\[0.5ex]
    3 & -4 & 1
    \end{pmatrix}.
    $$

<a id="box-obsGJSingular-6"></a>

!!! teorema "Osservazione 1: Matrici singolari e metodo di Gauss–Jordan"

    Sia \(\boldsymbol A \in \R^{n\times n}\). Se, applicando operazioni elementari di riga a \(\left(\boldsymbol A \mid \boldsymbol I\right)\), <strong>compare una riga nulla nel blocco sinistro</strong>, allora \(\det(\boldsymbol A) = 0\) e \(\boldsymbol A\) è singolare: il metodo si arresta e \(\boldsymbol A^{-1}\) non esiste.

??? dimostrazione "Dimostrazione"

    Il blocco sinistro si ottiene da \(\boldsymbol A\) mediante operazioni elementari di riga. Ciascuna di esse moltiplica il determinante per un numero non nullo (\(-1\) per uno scambio di righe, \(\lambda\neq 0\) per la moltiplicazione di una riga per uno scalare, \(1\) per la somma a una riga di un multiplo di un'altra). Una matrice con una riga nulla ha determinante nullo (sviluppo di Laplace lungo quella riga), quindi \(\det(\boldsymbol A) = 0\). Per la proprietà 4 della Proposizione [Proposizione 2](#box-propInverseProperties-2), \(\boldsymbol A\) non è invertibile. <span class="qed">□</span>

<a id="box-ex_inv-gj-singular-7"></a>

!!! esempio "Esempio 4: metodo di Gauss–Jordan su una matrice singolare"

    Consideriamo

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\[0.5ex]
    2 & 5 & 7\\[0.5ex]
    1 & 3 & 4
    \end{pmatrix}.
    $$

    Proviamo a calcolare \(\boldsymbol A^{-1}\) con il metodo di Gauss–Jordan.

    \begin{align*}
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 3 & 1 & 0 & 0 \\
     2 & 5 & 7 & 0 & 1 & 0 \\
     1 & 3 & 4 & 0 & 0 & 1 \\
    \end{array}
    \right) \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 3 & 1 & 0 & 0 \\
     0 & 1 & 1 & -2 & 1 & 0 \\
     1 & 3 & 4 & 0 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_2 \leftarrow R_2 - 2R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 3 & 1 & 0 & 0 \\
     0 & 1 & 1 & -2 & 1 & 0 \\
     0 & 1 & 1 & -1 & 0 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_1 \text{)} \\[2ex]
    &\left(
    \begin{array}{ccc|ccc}
     1 & 2 & 3 & 1 & 0 & 0 \\
     0 & 1 & 1 & -2 & 1 & 0 \\
     0 & 0 & 0 & 1 & -1 & 1 \\
    \end{array}
    \right) \hspace{1em} \text{(} R_3 \leftarrow R_3 - R_2 \text{)}
    \end{align*}

    La terza riga del blocco sinistro è nulla: il blocco sinistro non può essere trasformato nella matrice identità e il metodo si arresta. Dunque \(\boldsymbol A\) è singolare. Infatti, la terza riga di \(\boldsymbol A\) è la differenza tra la seconda e la prima riga, e

    $$
    \det(\boldsymbol A) = 1\cdot(5\cdot 4-7\cdot 3) - 2\cdot(2\cdot 4 - 7\cdot 1) + 3\cdot(2\cdot 3 - 5\cdot 1) = -1 - 2 + 3 = 0.
    $$

### 2.2 Inversa mediante la matrice aggiunta

<a id="sec:adjugate"></a>

- Ricordiamo (si veda il capitolo sulle matrici) che, data \(\boldsymbol A \in \R^{n\times n}\), il <strong>cofattore</strong> dell'elemento \(a_{ij}\) è \(C_{ij} = (-1)^{i+j}\det(\boldsymbol A_{ij})\), dove \(\boldsymbol A_{ij}\) è la matrice minore (complementare) ottenuta da \(\boldsymbol A\) eliminando la riga \(i\) e la colonna \(j\).

<a id="box-defAdjugate-8"></a>

!!! definizione "Definizione 1: Matrice dei cofattori e matrice aggiunta"

    Sia \(\boldsymbol A \in \R^{n\times n}\) con \(n\ge 2\). La <strong>matrice dei cofattori</strong> di \(\boldsymbol A\) è la matrice \(\boldsymbol C = (C_{ij}) \in \R^{n\times n}\) dei cofattori di \(\boldsymbol A\). La <strong>matrice aggiunta</strong> di \(\boldsymbol A\) è la trasposta della matrice dei cofattori:

    $$
    \mathrm{adj}(\boldsymbol A) = \boldsymbol C', \qquad \text{cioè} \qquad \big(\mathrm{adj}(\boldsymbol A)\big)_{ij} = C_{ji}.
    $$

<a id="box-theoAdjugate-9"></a>

!!! teorema "Teorema 1: Formula della matrice aggiunta"

    Sia \(\boldsymbol A \in \R^{n\times n}\) con \(n\ge 2\). Allora

    $$
    \boldsymbol A\,\mathrm{adj}(\boldsymbol A) = \mathrm{adj}(\boldsymbol A)\,\boldsymbol A = \det(\boldsymbol A)\,\boldsymbol I.
    $$

    Di conseguenza, se \(\det(\boldsymbol A)\neq 0\), allora \(\boldsymbol A\) è invertibile e

    $$
    \boldsymbol A^{-1} = \frac{1}{\det(\boldsymbol A)}\,\mathrm{adj}(\boldsymbol A).
    $$

??? dimostrazione "Dimostrazione"

    L'elemento \((i,j)\) di \(\boldsymbol A\,\mathrm{adj}(\boldsymbol A)\) è

    $$
    \sum_{k=1}^{n} a_{ik}\,C_{jk}.
    $$

    - Se \(i=j\), questo è lo sviluppo di Laplace di \(\det(\boldsymbol A)\) lungo la riga \(i\).

    - Se \(i\neq j\), questo è lo sviluppo di Laplace lungo la riga \(j\) della matrice \(\widetilde{\boldsymbol A}\) ottenuta da \(\boldsymbol A\) sostituendo la riga \(j\) con la riga \(i\) (i cofattori \(C_{jk}\) non dipendono dalla riga \(j\)). La matrice \(\widetilde{\boldsymbol A}\) ha due righe uguali: scambiandole, \(\widetilde{\boldsymbol A}\) resta invariata mentre il suo determinante cambia segno, quindi \(\det(\widetilde{\boldsymbol A}) = -\det(\widetilde{\boldsymbol A})\), cioè \(\det(\widetilde{\boldsymbol A}) = 0\).

    Quindi \(\boldsymbol A\,\mathrm{adj}(\boldsymbol A) = \det(\boldsymbol A)\,\boldsymbol I\). L'identità \(\mathrm{adj}(\boldsymbol A)\,\boldsymbol A = \det(\boldsymbol A)\,\boldsymbol I\) si ottiene allo stesso modo, usando sviluppi di Laplace lungo le colonne. Se \(\det(\boldsymbol A) \neq 0\), dividendo per \(\det(\boldsymbol A)\) si ottiene che \(\frac{1}{\det(\boldsymbol A)}\mathrm{adj}(\boldsymbol A)\) è l'inversa di \(\boldsymbol A\). <span class="qed">□</span>

<a id="box-obsInvDet-10"></a>

!!! teorema "Osservazione 2: Invertibilità e determinante"

    Una matrice quadrata \(\boldsymbol A \in \R^{n\times n}\) è invertibile se e solo se \(\det(\boldsymbol A) \neq 0\).

??? dimostrazione "Dimostrazione"

    Se \(\boldsymbol A\) è invertibile, allora \(\det(\boldsymbol A)\neq 0\) per la proprietà 4 della Proposizione [Proposizione 2](#box-propInverseProperties-2). Viceversa, se \(\det(\boldsymbol A)\neq 0\), allora \(\boldsymbol A\) è invertibile per il Teorema [Teorema 1](#box-theoAdjugate-9) (per \(n=1\), \(\boldsymbol A = (a)\) con \(a\neq 0\) e \(\boldsymbol A^{-1} = (1/a)\)). <span class="qed">□</span>

<a id="box-obsInverse2x2-11"></a>

!!! teorema "Osservazione 3: Inversa di una matrice \(2\times 2\)"

    Sia

    $$
    \boldsymbol A=
    \begin{pmatrix}
    a & b\\
    c & d
    \end{pmatrix}
    \in \R^{2\times 2}
    \quad \text{con} \quad
    \det(\boldsymbol A) = ad - bc \neq 0.
    $$

    Allora

    $$
    \boldsymbol A^{-1} = \frac{1}{ad-bc}
    \begin{pmatrix}
    d & -b\\
    -c & a
    \end{pmatrix}.
    $$

??? dimostrazione "Dimostrazione"

    Le matrici minori di \(\boldsymbol A\) sono \(1\times 1\), quindi i cofattori sono \(C_{11} = d\), \(C_{12} = -c\), \(C_{21} = -b\), \(C_{22} = a\). Quindi

    $$
    \boldsymbol C =
    \begin{pmatrix}
    d & -c\\
    -b & a
    \end{pmatrix},
    \qquad
    \mathrm{adj}(\boldsymbol A) = \boldsymbol C' =
    \begin{pmatrix}
    d & -b\\
    -c & a
    \end{pmatrix},
    $$

    e la formula segue dal Teorema [Teorema 1](#box-theoAdjugate-9). <span class="qed">□</span>

!!! chiave ""

    <strong>Inversa di una matrice \(2\times 2\) (regola).</strong> Si scambiano i due elementi della diagonale, si cambia segno ai due elementi fuori diagonale e si divide per il determinante.

<a id="box-ex_inv-2x2-formula-12"></a>

!!! esempio "Esempio 5: inversa di una matrice \(2\times 2\) con la formula"

    Consideriamo di nuovo

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1\\[0.5ex]
    1 & 1
    \end{pmatrix}.
    $$

    Si ha \(\det(\boldsymbol A) = 2\cdot 1 - 1\cdot 1 = 1 \neq 0\), quindi

    $$
    \boldsymbol A^{-1} = \frac{1}{1}
    \begin{pmatrix}
    1 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix},
    $$

    che è la matrice ottenuta con il metodo di Gauss–Jordan nell'Esempio [Esempio 1](#box-ex_inv-gj-2x2-3).

<a id="box-ex_inv-3x3-adjugate-13"></a>

!!! esempio "Esempio 6: inversa di una matrice \(3\times 3\) con la formula della matrice aggiunta"

    Consideriamo di nuovo

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0\\[0.5ex]
    0 & 1 & 1\\[0.5ex]
    2 & 0 & 1
    \end{pmatrix}.
    $$

    Con lo sviluppo di Laplace lungo la prima riga:

    $$
    \det(\boldsymbol A) = 1\cdot(1\cdot 1 - 1\cdot 0) - 2\cdot(0\cdot 1 - 1\cdot 2) + 0 = 1 + 4 = 5 \neq 0.
    $$

    I cofattori sono:

    \begin{align*}
    C_{11} &= +\det\begin{pmatrix} 1 & 1\\ 0 & 1\end{pmatrix} = 1, &
    C_{12} &= -\det\begin{pmatrix} 0 & 1\\ 2 & 1\end{pmatrix} = 2, &
    C_{13} &= +\det\begin{pmatrix} 0 & 1\\ 2 & 0\end{pmatrix} = -2,\\[1ex]
    C_{21} &= -\det\begin{pmatrix} 2 & 0\\ 0 & 1\end{pmatrix} = -2, &
    C_{22} &= +\det\begin{pmatrix} 1 & 0\\ 2 & 1\end{pmatrix} = 1, &
    C_{23} &= -\det\begin{pmatrix} 1 & 2\\ 2 & 0\end{pmatrix} = 4,\\[1ex]
    C_{31} &= +\det\begin{pmatrix} 2 & 0\\ 1 & 1\end{pmatrix} = 2, &
    C_{32} &= -\det\begin{pmatrix} 1 & 0\\ 0 & 1\end{pmatrix} = -1, &
    C_{33} &= +\det\begin{pmatrix} 1 & 2\\ 0 & 1\end{pmatrix} = 1.
    \end{align*}

    Quindi

    $$
    \boldsymbol C =
    \begin{pmatrix}
    1 & 2 & -2\\
    -2 & 1 & 4\\
    2 & -1 & 1
    \end{pmatrix},
    \qquad
    \mathrm{adj}(\boldsymbol A) = \boldsymbol C' =
    \begin{pmatrix}
    1 & -2 & 2\\
    2 & 1 & -1\\
    -2 & 4 & 1
    \end{pmatrix},
    $$

    e

    $$
    \boldsymbol A^{-1} = \frac{1}{5}
    \begin{pmatrix}
    1 & -2 & 2\\
    2 & 1 & -1\\
    -2 & 4 & 1
    \end{pmatrix},
    $$

    che è la matrice ottenuta con il metodo di Gauss–Jordan nell'Esempio [Esempio 2](#box-ex_inv-gj-3x3-4).

- Per \(n=2\) (e spesso per \(n=3\)) la formula della matrice aggiunta è comoda per i calcoli a mano. Per matrici di dimensioni maggiori, il metodo di Gauss–Jordan richiede molte meno operazioni.

!!! interattivo "Provalo nel laboratorio"

    lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi.

<div class="la-tool" data-tool="inversa" data-matrix="2,1;1,1"></div>

## Esercizi e laboratorio

- :material-pencil-box-multiple: **Esercizi** · [il foglio di esercizi di questo capitolo: 10 esercizi con le soluzioni svolte](../esercizi/es-vettori-matrici-04-matrice-inversa.md)
- :material-calculator-variant: **Laboratorio** · [Matrice inversa](../laboratorio/inversa.md) — Gauss–Jordan su \((\boldsymbol A \mid \boldsymbol I)\) oppure la formula con i cofattori.

