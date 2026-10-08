---
title: "Autovalori e autovettori"
---

# Autovalori e autovettori

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.5** · dalle dispense di Fabio Furini · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf) · [:material-presentation: Slide (PDF)](../pdf/slide-04-5-autovalori.pdf)

</div>

## 1. Autovalori

<a id="box-defEigen-1"></a>

!!! definizione "Definizione 1: autovalore e autovettore"

    Sia \( \boldsymbol Q \in \R^{n\times n} \) una matrice quadrata. Uno scalare \( \lambda \in \R \) si dice <strong>autovalore</strong> di \( \boldsymbol Q \) se esiste un vettore non nullo \( \boldsymbol v \in \R^{n} \setminus \{\boldsymbol 0\} \) tale che

    $$
    \boldsymbol Q\,\boldsymbol v = \lambda\,\boldsymbol v.
    $$

    In tal caso, \( \boldsymbol v \) si dice <strong>autovettore</strong> associato a \( \lambda \).

- Gli autovalori sono le soluzioni dell'<strong>equazione caratteristica</strong>

    $$
    \det(\boldsymbol Q - \lambda \boldsymbol I)=0.
    $$

- Se \( \boldsymbol Q \) è simmetrica, allora tutti i suoi autovalori sono reali.

- La funzione \( p(\lambda)=\det(\boldsymbol Q-\lambda\boldsymbol I) \) è un polinomio di grado \( n \) in \( \lambda \), detto <strong>polinomio caratteristico</strong> di \( \boldsymbol Q \).

- Se \( \lambda \) è un autovalore, gli autovettori associati a \( \lambda \) sono le soluzioni non nulle \( \boldsymbol v \) del sistema omogeneo

    $$
    (\boldsymbol Q-\lambda\boldsymbol I)\,\boldsymbol v=\boldsymbol 0 .
    $$

- Se \( \boldsymbol v \) è un autovettore associato a \( \lambda \), allora anche \( \alpha\,\boldsymbol v \) è un autovettore associato a \( \lambda \), per ogni \( \alpha\in\R\setminus\{0\} \). Gli autovettori quindi non sono mai unici: ne indichiamo semplicemente uno (“ad esempio”).

!!! chiave ""

    Una matrice quadrata simmetrica \( \boldsymbol Q \in \R^{n \times n} \) è 

    - semidefinita positiva se e solo se tutti i suoi autovalori sono non negativi.

    - definita positiva se e solo se tutti i suoi autovalori sono strettamente positivi.

    - semidefinita negativa se e solo se tutti i suoi autovalori sono non positivi.

    - definita negativa se e solo se tutti i suoi autovalori sono strettamente negativi.

- Ricordiamo che le matrici (semi)definite sono state definite nel capitolo sulle matrici tramite il segno di \( \boldsymbol x' \boldsymbol Q \, \boldsymbol x \): ad esempio, \( \boldsymbol Q \) è semidefinita positiva se \( \boldsymbol x' \boldsymbol Q \, \boldsymbol x \ge 0 \) per ogni \( \boldsymbol x \in \R^n \). Il riquadro precedente fornisce una caratterizzazione equivalente in termini di autovalori.

- Un'implicazione è facile da vedere: se \( \boldsymbol Q\boldsymbol v=\lambda\boldsymbol v \) con \( \boldsymbol v\neq\boldsymbol 0 \), allora

    $$
    \boldsymbol v' \boldsymbol Q \, \boldsymbol v=\lambda\,\boldsymbol v'\boldsymbol v=\lambda\sum_{i=1}^n v_i^2,
    \qquad \text{con} \quad \sum_{i=1}^n v_i^2>0,
    $$

    quindi \( \boldsymbol v' \boldsymbol Q \, \boldsymbol v \) e \( \lambda \) hanno lo stesso segno. Ad esempio, se \( \boldsymbol Q \) è semidefinita positiva, allora ogni autovalore soddisfa \( \lambda\ge 0 \).

- Una matrice simmetrica che non è né semidefinita positiva né semidefinita negativa si dice <strong>indefinita</strong>: equivalentemente, ha almeno un autovalore strettamente positivo e almeno uno strettamente negativo.

<a id="box-texexpbox1-2"></a>

!!! esempio "Esempio 1: autovalori e autovettori"

    Consideriamo la matrice

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    2 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix}.
    $$

    L'equazione caratteristica è:

    $$
    \det(\boldsymbol Q-\lambda \boldsymbol I)
    =
    \det\begin{pmatrix}
    2-\lambda & -1\\[0.5ex]
    -1 & 2-\lambda
    \end{pmatrix}
    =
    (2-\lambda)^2-1
    =
    \lambda^2-4\lambda+3.
    $$

    Quindi

    $$
    \det(\boldsymbol Q-\lambda \boldsymbol I)=0
    \Longleftrightarrow
    (\lambda-1)(\lambda-3)=0,
    $$

    e dunque gli autovalori sono:

    $$
    \lambda_1=1,
    \qquad
    \lambda_2=3.
    $$

    Un autovettore associato a \(\lambda_1=1\) si trova risolvendo

    $$
    (\boldsymbol Q-\boldsymbol I)\boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \begin{pmatrix}
    1 & -1\\[0.5ex]
    -1 & 1
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0,
    $$

    da cui (ad esempio)

    $$
    \boldsymbol v_1=
    \begin{pmatrix}
    1\\[0.5ex]
    1
    \end{pmatrix}.
    $$

    Analogamente, un autovettore associato a \(\lambda_2=3\) soddisfa

    $$
    (\boldsymbol Q-3\boldsymbol I)\boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \begin{pmatrix}
    -1 & -1\\[0.5ex]
    -1 & -1
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0,
    $$

    da cui (ad esempio)

    $$
    \boldsymbol v_2=
    \begin{pmatrix}
    1\\[0.5ex]
    -1
    \end{pmatrix}.
    $$

    Pertanto,

    $$
    \boldsymbol Q\,\boldsymbol v_1 = 1\,\boldsymbol v_1,
    \qquad
    \boldsymbol Q\,\boldsymbol v_2 = 3\,\boldsymbol v_2.
    $$

    Possiamo verificarlo direttamente:

    $$
    \boldsymbol Q\,\boldsymbol v_1
    =
    \begin{pmatrix}
    2 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix}
    \begin{pmatrix}
    1\\[0.5ex]
    1
    \end{pmatrix}
    =
    \begin{pmatrix}
    1\\[0.5ex]
    1
    \end{pmatrix}
    = 1\,\boldsymbol v_1,
    \qquad
    \boldsymbol Q\,\boldsymbol v_2
    =
    \begin{pmatrix}
    2 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix}
    \begin{pmatrix}
    1\\[0.5ex]
    -1
    \end{pmatrix}
    =
    \begin{pmatrix}
    3\\[0.5ex]
    -3
    \end{pmatrix}
    = 3\,\boldsymbol v_2.
    $$

    Poiché \( \boldsymbol Q \) è simmetrica ed entrambi gli autovalori sono strettamente positivi, la matrice \( \boldsymbol Q \) è <strong>definita positiva</strong>.

## 2. Proprietà degli autovalori

### 2.1 Matrici triangolari e diagonali

<a id="box-obsTriangularEigen-3"></a>

!!! teorema "Osservazione 1: autovalori di matrici triangolari e diagonali"

    Sia \( \boldsymbol Q \in \R^{n\times n} \) una matrice triangolare superiore, triangolare inferiore o diagonale. Allora gli autovalori di \( \boldsymbol Q \) sono i suoi elementi diagonali \( q_{11}, q_{22}, \dots, q_{nn} \).

??? dimostrazione "Dimostrazione (Dimostrazione)"

    Se \( \boldsymbol Q \) è triangolare (o diagonale), allora anche \( \boldsymbol Q-\lambda\boldsymbol I \) è triangolare (o diagonale), con elementi diagonali \( q_{11}-\lambda, \dots, q_{nn}-\lambda \). Ricordiamo che il determinante di una matrice triangolare è il prodotto dei suoi elementi diagonali. Quindi

    $$
    \det(\boldsymbol Q-\lambda\boldsymbol I)=\prod_{i=1}^{n}(q_{ii}-\lambda),
    $$

    che è uguale a zero se e solo se \( \lambda=q_{ii} \) per qualche \( i\in\{1,2,\dots,n\} \). <span class="qed">□</span>

<a id="box-texexpboxTriangEigen-4"></a>

!!! esempio "Esempio 2: autovalori di una matrice triangolare"

    Consideriamo la matrice triangolare superiore

    $$
    \boldsymbol U=
    \begin{pmatrix}
    2 & 1 & 3\\[0.5ex]
    0 & -1 & 4\\[0.5ex]
    0 & 0 & 5
    \end{pmatrix}.
    $$

    L'equazione caratteristica è

    $$
    \det(\boldsymbol U-\lambda\boldsymbol I)
    =
    \det\begin{pmatrix}
    2-\lambda & 1 & 3\\[0.5ex]
    0 & -1-\lambda & 4\\[0.5ex]
    0 & 0 & 5-\lambda
    \end{pmatrix}
    =
    (2-\lambda)(-1-\lambda)(5-\lambda)=0,
    $$

    e dunque gli autovalori sono gli elementi diagonali:

    $$
    \lambda_1=2,
    \qquad
    \lambda_2=-1,
    \qquad
    \lambda_3=5.
    $$

### 2.2 Traccia, determinante e autovalori

<a id="box-defTrace-5"></a>

!!! definizione "Definizione 2: traccia di una matrice"

    Sia \( \boldsymbol Q \in \R^{n\times n} \) una matrice quadrata. La <strong>traccia</strong> di \( \boldsymbol Q \) è la somma dei suoi elementi diagonali:

    $$
    \operatorname{tr}(\boldsymbol Q)=\sum_{i=1}^{n} q_{ii}=q_{11}+q_{22}+\dots+q_{nn}.
    $$

- Il polinomio caratteristico \( p(\lambda)=\det(\boldsymbol Q-\lambda\boldsymbol I) \) ha grado \( n \). Nei numeri complessi, un polinomio di grado \( n \) ha esattamente \( n \) radici \( \lambda_1,\lambda_2,\dots,\lambda_n \in \C \), purché ogni radice sia contata tante volte quanto la sua <strong>molteplicità</strong> (il numero di volte in cui il fattore \( (\lambda_i-\lambda) \) compare nella fattorizzazione). Quindi

    $$
    p(\lambda)=(\lambda_1-\lambda)\,(\lambda_2-\lambda)\cdots(\lambda_n-\lambda).
    $$

- Le radici reali sono gli autovalori della Definizione [Definizione 1](#box-defEigen-1). Le radici non reali si dicono <strong>autovalori complessi</strong> di \( \boldsymbol Q \) (i loro autovettori hanno componenti complesse). Se \( \boldsymbol Q \) è simmetrica, tutte le radici sono reali.

<a id="box-obsDetTrace-6"></a>

!!! teorema "Osservazione 2: determinante, traccia e autovalori"

    Sia \( \boldsymbol Q \in \R^{n\times n} \) e siano \( \lambda_1,\lambda_2,\dots,\lambda_n \in \C \) le radici del suo polinomio caratteristico, ciascuna ripetuta secondo la sua molteplicità. Allora

    $$
    \det(\boldsymbol Q)=\prod_{i=1}^{n}\lambda_i,
    \qquad\qquad
    \operatorname{tr}(\boldsymbol Q)=\sum_{i=1}^{n}\lambda_i.
    $$

??? dimostrazione "Dimostrazione (Idea della dimostrazione)"

    Per il determinante basta porre \( \lambda=0 \) in \( p(\lambda)=(\lambda_1-\lambda)\cdots(\lambda_n-\lambda) \): si ottiene \( \det(\boldsymbol Q)=p(0)=\lambda_1\,\lambda_2\cdots\lambda_n \). Per la traccia, confrontiamo i coefficienti di \( \lambda^{n-1} \): nel prodotto \( (\lambda_1-\lambda)\cdots(\lambda_n-\lambda) \) tale coefficiente è \( (-1)^{n-1}\sum_{i=1}^n\lambda_i \), mentre in \( \det(\boldsymbol Q-\lambda\boldsymbol I) \) la potenza \( \lambda^{n-1} \) proviene solo dal prodotto \( (q_{11}-\lambda)\cdots(q_{nn}-\lambda) \) degli elementi diagonali, e il suo coefficiente è \( (-1)^{n-1}\sum_{i=1}^n q_{ii} \). <span class="qed">□</span>

<a id="box-texexpboxTraceDet-7"></a>

!!! esempio "Esempio 3: traccia e determinante"

    - Per la matrice dell'Esempio [Esempio 1](#box-texexpbox1-2) si ha \( \lambda_1=1 \) e \( \lambda_2=3 \), e infatti

        $$
        \operatorname{tr}\begin{pmatrix}
        2 & -1\\[0.5ex]
        -1 & 2
        \end{pmatrix}
        =2+2=4=1+3,
        \qquad
        \det\begin{pmatrix}
        2 & -1\\[0.5ex]
        -1 & 2
        \end{pmatrix}
        =4-1=3=1\cdot 3.
        $$

    - Bisogna tenere conto delle molteplicità. La matrice diagonale

        $$
        \boldsymbol D=
        \begin{pmatrix}
        4 & 0 & 0\\[0.5ex]
        0 & -3 & 0\\[0.5ex]
        0 & 0 & 4
        \end{pmatrix}
        $$

        ha polinomio caratteristico \( (4-\lambda)^2(-3-\lambda) \): l'autovalore \( 4 \) ha molteplicità \( 2 \) e l'autovalore \( -3 \) ha molteplicità \( 1 \). Quindi \( \lambda_1=\lambda_2=4 \), \( \lambda_3=-3 \), e

        $$
        \operatorname{tr}(\boldsymbol D)=4+4-3=5,
        \qquad
        \det(\boldsymbol D)=4\cdot 4\cdot(-3)=-48.
        $$

    - Bisogna tenere conto delle radici complesse. Per la matrice (non simmetrica)

        $$
        \boldsymbol R=
        \begin{pmatrix}
        0 & -1\\[0.5ex]
        1 & 0
        \end{pmatrix}
        \quad\text{si ha}\quad
        \det(\boldsymbol R-\lambda\boldsymbol I)=\lambda^2+1,
        $$

        che non ha radici reali: \( \boldsymbol R \) non ha autovalori (reali). I suoi autovalori complessi sono \( \lambda_1=i \) e \( \lambda_2=-i \), e infatti

        $$
        \operatorname{tr}(\boldsymbol R)=0=i+(-i),
        \qquad
        \det(\boldsymbol R)=1=i\cdot(-i).
        $$

### 2.3 Autovettori di autovalori distinti

- Ricordiamo che i vettori \( \boldsymbol v_1,\dots,\boldsymbol v_k \) sono linearmente indipendenti se \( \alpha_1\boldsymbol v_1+\dots+\alpha_k\boldsymbol v_k=\boldsymbol 0 \) implica \( \alpha_1=\dots=\alpha_k=0 \).

<a id="box-obsEigenIndep-8"></a>

!!! teorema "Osservazione 3: autovettori di autovalori distinti"

    Siano \( \lambda_1,\lambda_2,\dots,\lambda_k \) autovalori <strong>distinti</strong> di \( \boldsymbol Q \in \R^{n\times n} \) e siano \( \boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k \) autovettori associati (\( \boldsymbol Q\boldsymbol v_i=\lambda_i\boldsymbol v_i \)). Allora \( \boldsymbol v_1,\boldsymbol v_2,\dots,\boldsymbol v_k \) sono linearmente indipendenti.

- In particolare, se \( \boldsymbol Q \in \R^{n\times n} \) ha \( n \) autovalori reali distinti, allora scegliendo un autovettore per ciascun autovalore si ottengono \( n \) vettori linearmente indipendenti di \( \R^n \).

- Nell'Esempio [Esempio 1](#box-texexpbox1-2), gli autovettori \( \boldsymbol v_1=(1,1)' \) e \( \boldsymbol v_2=(1,-1)' \) sono linearmente indipendenti, poiché nessuno dei due è multiplo dell'altro.

## 3. Un esempio completo con una matrice $3\times 3$

<a id="box-texexpboxEigen3x3-9"></a>

!!! esempio "Esempio 4: autovalori e autovettori di una matrice \(3\times 3\)"

    Consideriamo la matrice simmetrica

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    2 & 1 & 0\\[0.5ex]
    1 & 3 & 1\\[0.5ex]
    0 & 1 & 2
    \end{pmatrix}.
    $$

    <strong>Polinomio caratteristico.</strong> Sviluppando lungo la prima riga (sviluppo di Laplace):

    \begin{align*}
    \det(\boldsymbol Q-\lambda \boldsymbol I)
    &=
    \det\begin{pmatrix}
    2-\lambda & 1 & 0\\[0.5ex]
    1 & 3-\lambda & 1\\[0.5ex]
    0 & 1 & 2-\lambda
    \end{pmatrix}\\[1ex]
    &=
    (2-\lambda)\big[(3-\lambda)(2-\lambda)-1\big]
    -1\cdot\big[1\cdot(2-\lambda)-1\cdot 0\big]\\[1ex]
    &=
    (2-\lambda)\big[(3-\lambda)(2-\lambda)-2\big]
    =
    (2-\lambda)\,(\lambda^2-5\lambda+4)\\[1ex]
    &=
    (2-\lambda)(\lambda-1)(\lambda-4).
    \end{align*}

    Dunque gli autovalori sono

    $$
    \lambda_1=1,
    \qquad
    \lambda_2=2,
    \qquad
    \lambda_3=4.
    $$

    <strong>Autovettore per \( \lambda_1=1 \).</strong> Risolviamo

    $$
    (\boldsymbol Q-\boldsymbol I)\boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \begin{pmatrix}
    1 & 1 & 0\\[0.5ex]
    1 & 2 & 1\\[0.5ex]
    0 & 1 & 1
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \left\{
    \begin{array}{l}
    v_1+v_2=0\\[0.5ex]
    v_1+2v_2+v_3=0\\[0.5ex]
    v_2+v_3=0
    \end{array}
    \right.
    $$

    Dalla prima e dalla terza equazione, \( v_1=-v_2 \) e \( v_3=-v_2 \) (la seconda equazione è allora soddisfatta). Scegliendo \( v_2=-1 \):

    $$
    \boldsymbol v_1=
    \begin{pmatrix}
    1\\[0.5ex]
    -1\\[0.5ex]
    1
    \end{pmatrix}.
    $$

    <strong>Autovettore per \( \lambda_2=2 \).</strong> Risolviamo

    $$
    (\boldsymbol Q-2\boldsymbol I)\boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \begin{pmatrix}
    0 & 1 & 0\\[0.5ex]
    1 & 1 & 1\\[0.5ex]
    0 & 1 & 0
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \left\{
    \begin{array}{l}
    v_2=0\\[0.5ex]
    v_1+v_2+v_3=0
    \end{array}
    \right.
    $$

    quindi \( v_2=0 \), \( v_3=-v_1 \) e, ad esempio,

    $$
    \boldsymbol v_2=
    \begin{pmatrix}
    1\\[0.5ex]
    0\\[0.5ex]
    -1
    \end{pmatrix}.
    $$

    <strong>Autovettore per \( \lambda_3=4 \).</strong> Risolviamo

    $$
    (\boldsymbol Q-4\boldsymbol I)\boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \begin{pmatrix}
    -2 & 1 & 0\\[0.5ex]
    1 & -1 & 1\\[0.5ex]
    0 & 1 & -2
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \left\{
    \begin{array}{l}
    -2v_1+v_2=0\\[0.5ex]
    v_1-v_2+v_3=0\\[0.5ex]
    v_2-2v_3=0
    \end{array}
    \right.
    $$

    Dalla prima e dalla terza equazione, \( v_2=2v_1 \) e \( v_3=v_2/2=v_1 \) (la seconda equazione è allora soddisfatta: \( v_1-2v_1+v_1=0 \)). Scegliendo \( v_1=1 \):

    $$
    \boldsymbol v_3=
    \begin{pmatrix}
    1\\[0.5ex]
    2\\[0.5ex]
    1
    \end{pmatrix}.
    $$

    <strong>Controlli.</strong> Per l'Osservazione [Osservazione 2](#box-obsDetTrace-6),

    $$
    \operatorname{tr}(\boldsymbol Q)=2+3+2=7=1+2+4,
    \qquad
    \det(\boldsymbol Q)=2\cdot(6-1)-1\cdot(2-0)=8=1\cdot 2\cdot 4.
    $$

    Poiché i tre autovalori sono distinti, per l'Osservazione [Osservazione 3](#box-obsEigenIndep-8) gli autovettori \( \boldsymbol v_1,\boldsymbol v_2,\boldsymbol v_3 \) sono linearmente indipendenti. Infine, \( \boldsymbol Q \) è simmetrica con autovalori strettamente positivi, quindi è <strong>definita positiva</strong>.

## 4. Criterio di Sylvester

- Calcolare tutti gli autovalori di una matrice può essere difficile. Per le matrici simmetriche, il fatto di essere definite o semidefinite si può verificare anche calcolando i determinanti di opportune sottomatrici quadrate.

<a id="box-defPrincipalMinors-10"></a>

!!! definizione "Definizione 3: minori principali"

    Sia \( \boldsymbol Q \in \R^{n\times n} \).

    - Un <strong>minore principale</strong> di ordine \( k \) di \( \boldsymbol Q \) è il determinante della sottomatrice \( k\times k \) ottenuta da \( \boldsymbol Q \) conservando le righe e le colonne con gli <strong>stessi</strong> indici \( i_1<i_2<\dots<i_k \) (equivalentemente, eliminando le stesse \( n-k \) righe e colonne).

    - Il <strong>minore principale di guida</strong> (o di nord-ovest) di ordine \( k \) è il minore principale ottenuto conservando le prime \( k \) righe e colonne:

        $$
        \Delta_k=\det
        \begin{pmatrix}
        q_{11} & \cdots & q_{1k}\\
        \vdots & \ddots & \vdots\\
        q_{k1} & \cdots & q_{kk}
        \end{pmatrix},
        \qquad k=1,2,\dots,n.
        $$

- Una matrice \( \boldsymbol Q\in\R^{n\times n} \) ha esattamente \( n \) minori principali di guida \( \Delta_1=q_{11},\ \Delta_2,\ \dots,\ \Delta_n=\det(\boldsymbol Q) \).

- Per \( n=3 \), i minori principali sono: di ordine 1, \( q_{11},q_{22},q_{33} \); di ordine 2, i determinanti delle sottomatrici con indici \( \{1,2\} \), \( \{1,3\} \), \( \{2,3\} \); di ordine 3, \( \det(\boldsymbol Q) \).

<a id="box-theoSylvester-11"></a>

!!! teorema "Teorema 1: criterio di Sylvester"

    Sia \( \boldsymbol Q \in \R^{n\times n} \) una matrice <strong>simmetrica</strong> con minori principali di guida \( \Delta_1,\Delta_2,\dots,\Delta_n \). Allora

    - \( \boldsymbol Q \) è <strong>definita positiva</strong> se e solo se

        $$
        \Delta_k>0, \qquad \forall k\in\{1,2,\dots,n\};
        $$

    - \( \boldsymbol Q \) è <strong>definita negativa</strong> se e solo se i minori principali di guida hanno segni alterni a partire da uno negativo:

        $$
        \Delta_1<0,\quad \Delta_2>0,\quad \Delta_3<0,\quad \dots
        \qquad\text{cioè}\qquad
        (-1)^k\,\Delta_k>0, \qquad \forall k\in\{1,2,\dots,n\}.
        $$

<a id="box-obsSylvesterSemi-12"></a>

!!! teorema "Osservazione 4: matrici semidefinite e minori principali"

    Sia \( \boldsymbol Q \in \R^{n\times n} \) una matrice simmetrica. Allora

    - \( \boldsymbol Q \) è <strong>semidefinita positiva</strong> se e solo se <strong>tutti</strong> i suoi minori principali (non solo quelli di guida) sono \( \ge 0 \);

    - \( \boldsymbol Q \) è <strong>semidefinita negativa</strong> se e solo se ogni minore principale di ordine \( k \) ha il segno di \( (-1)^k \) oppure è nullo, cioè \( (-1)^k\,(\text{minore principale di ordine } k) \ge 0 \), per ogni \( k \).

    Per la semidefinitezza <strong>non</strong> basta verificare \( \Delta_k\ge 0 \) per i soli minori principali di guida.

<a id="box-texexpboxSylPD-13"></a>

!!! esempio "Esempio 5: una matrice definita positiva"

    Per la matrice dell'Esempio [Esempio 4](#box-texexpboxEigen3x3-9)

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    2 & 1 & 0\\[0.5ex]
    1 & 3 & 1\\[0.5ex]
    0 & 1 & 2
    \end{pmatrix}
    $$

    i minori principali di guida sono

    $$
    \Delta_1=2>0,
    \qquad
    \Delta_2=\det\begin{pmatrix}
    2 & 1\\[0.5ex]
    1 & 3
    \end{pmatrix}=6-1=5>0,
    \qquad
    \Delta_3=\det(\boldsymbol Q)=8>0.
    $$

    Per il criterio di Sylvester, \( \boldsymbol Q \) è definita positiva, in accordo con i suoi autovalori \( 1,2,4 \).

<a id="box-texexpboxSylInd-14"></a>

!!! esempio "Esempio 6: una matrice indefinita"

    Consideriamo

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    1 & 2\\[0.5ex]
    2 & 1
    \end{pmatrix}.
    $$

    Si ha \( \Delta_1=1>0 \) e \( \Delta_2=1-4=-3<0 \). Quindi:

    - \( \boldsymbol Q \) non è definita positiva (\( \Delta_2<0 \)) e non è definita negativa (\( \Delta_1>0 \));

    - \( \boldsymbol Q \) non è semidefinita positiva (il minore principale \( \Delta_2 \) di ordine 2 è negativo) e non è semidefinita negativa (\( (-1)^2\Delta_2<0 \)).

    Pertanto \( \boldsymbol Q \) è <strong>indefinita</strong>. Infatti, ricordando la definizione tramite \( \boldsymbol x' \boldsymbol Q \, \boldsymbol x \):

    $$
    \boldsymbol x=\begin{pmatrix}1\\0\end{pmatrix}:\ \ \boldsymbol x' \boldsymbol Q \, \boldsymbol x=1>0,
    \qquad
    \boldsymbol x=\begin{pmatrix}1\\-1\end{pmatrix}:\ \ \boldsymbol x' \boldsymbol Q \, \boldsymbol x=1-4+1=-2<0.
    $$

    Gli autovalori sono le radici di \( (1-\lambda)^2-4=(\lambda-3)(\lambda+1) \), cioè \( 3 \) e \( -1 \): uno positivo e uno negativo.

<a id="box-texexpboxSylPSD-15"></a>

!!! esempio "Esempio 7: una matrice semidefinita positiva singolare"

    Consideriamo

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    1 & 1 & 0\\[0.5ex]
    1 & 2 & 1\\[0.5ex]
    0 & 1 & 1
    \end{pmatrix}.
    $$

    I minori principali di guida sono \( \Delta_1=1 \), \( \Delta_2=2-1=1 \) e \( \Delta_3=\det(\boldsymbol Q)=1\cdot(2-1)-1\cdot(1-0)=0 \). Poiché \( \Delta_3=0 \), \( \boldsymbol Q \) <strong>non</strong> è definita positiva.

    Per stabilire se è semidefinita positiva controlliamo <strong>tutti</strong> i minori principali:

    - ordine 1: \( q_{11}=1,\ q_{22}=2,\ q_{33}=1 \);

    - ordine 2: \( \det\begin{pmatrix}1 & 1\\ 1 & 2\end{pmatrix}=1,\ \ \det\begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}=1,\ \ \det\begin{pmatrix}2 & 1\\ 1 & 1\end{pmatrix}=1 \);

    - ordine 3: \( \det(\boldsymbol Q)=0 \).

    Tutti i minori principali sono \( \ge 0 \), quindi \( \boldsymbol Q \) è <strong>semidefinita positiva</strong>. Infatti

    $$
    \boldsymbol x' \boldsymbol Q \, \boldsymbol x = x_1^2+2x_1x_2+2x_2^2+2x_2x_3+x_3^2=(x_1+x_2)^2+(x_2+x_3)^2\ge 0,
    $$

    e gli autovalori sono \( 0,1,3 \) (\( \boldsymbol v=(1,-1,1)' \) soddisfa \( \boldsymbol Q\boldsymbol v=\boldsymbol 0=0\,\boldsymbol v \)).

<a id="box-texexpboxSylCounter-16"></a>

!!! esempio "Esempio 8: i minori principali di guida non bastano per la semidefinitezza"

    Consideriamo

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    0 & 0\\[0.5ex]
    0 & -1
    \end{pmatrix}.
    $$

    I minori principali di guida sono \( \Delta_1=0\ge 0 \) e \( \Delta_2=0\ge 0 \). Tuttavia \( \boldsymbol Q \) <strong>non</strong> è semidefinita positiva: per

    $$
    \boldsymbol x=\begin{pmatrix}0\\1\end{pmatrix}
    \qquad\text{si ha}\qquad
    \boldsymbol x' \boldsymbol Q \, \boldsymbol x=-1<0.
    $$

    Il minore principale \( q_{22}=-1 \) (che non è di guida) lo rivela. In effetti, gli autovalori sono \( 0 \) e \( -1 \), e \( \boldsymbol Q \) è semidefinita negativa.

!!! interattivo "Provalo nel laboratorio"

    lo stesso calcolo passo per passo: cambia la matrice e guarda come cambiano i passaggi.

<div class="la-tool" data-tool="autovalori" data-matrix="2,-1;-1,2"></div>

## Esercizi e laboratorio

- :material-pencil-box-multiple: **Esercizi** · [il foglio di esercizi di questo capitolo: 10 esercizi con le soluzioni svolte](../esercizi/es-vettori-matrici-06-autovalori.md)
- :material-calculator-variant: **Laboratorio** · [Autovalori e definitezza](../laboratorio/autovalori.md) — Polinomio caratteristico, autovettori e criterio di Sylvester.

