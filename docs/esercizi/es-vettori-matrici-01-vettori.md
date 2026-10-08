---
title: "Vettori"
---

# Vettori

<div class="info-capitolo" markdown>

**Esercizi · Vettori e matrici** · capitolo [3 · Vettori](../vettori-matrici/01-vettori.md) · con le soluzioni svolte · [:material-file-pdf-box: PDF](../pdf/es-vettori-matrici-01-vettori.pdf)

</div>

<a id="box-exe_vecSumScalar-1"></a>

!!! esercizio "Esercizio 1"

    Si considerino i vettori

    $$
    \boldsymbol p=\begin{pmatrix}2\\-1\\3\end{pmatrix},
    \qquad
    \boldsymbol w=\begin{pmatrix}-1\\4\\0\end{pmatrix}\in\R^{3}.
    $$

    Calcolare \(\boldsymbol p+\boldsymbol w\), \(3\boldsymbol p\) e \(2\boldsymbol p-\boldsymbol w\), e verificare che \(\boldsymbol p+\boldsymbol w=\boldsymbol w+\boldsymbol p\).

??? soluzione "Soluzione"

    Somma e prodotto per uno scalare si calcolano elemento per elemento:

    $$
    \boldsymbol p+\boldsymbol w=
    \begin{pmatrix}2+(-1)\\-1+4\\3+0\end{pmatrix}
    =
    \begin{pmatrix}1\\3\\3\end{pmatrix},
    \qquad
    3\boldsymbol p=
    \begin{pmatrix}3\cdot 2\\3\cdot(-1)\\3\cdot 3\end{pmatrix}
    =
    \begin{pmatrix}6\\-3\\9\end{pmatrix}.
    $$

    Per l'ultimo vettore, \(2\boldsymbol p-\boldsymbol w=2\boldsymbol p+(-1)\boldsymbol w\):

    $$
    2\boldsymbol p-\boldsymbol w=
    \begin{pmatrix}4\\-2\\6\end{pmatrix}
    -
    \begin{pmatrix}-1\\4\\0\end{pmatrix}
    =
    \begin{pmatrix}4+1\\-2-4\\6-0\end{pmatrix}
    =
    \begin{pmatrix}5\\-6\\6\end{pmatrix}.
    $$

    Finally, \( \boldsymbol w+\boldsymbol p= \begin{pmatrix}-1+2 & 4-1 & 0+3\end{pmatrix}' = \begin{pmatrix}1 & 3 & 3\end{pmatrix}' =\boldsymbol p+\boldsymbol w, \) come afferma la proprietà commutativa della somma.

<a id="box-exe_vecTranspose-2"></a>

!!! esercizio "Esercizio 2"

    Si consideri il vettore \( \boldsymbol a=\begin{pmatrix}1 & -2 & 0 & 5\end{pmatrix}'. \)

    1. Scrivere \(\boldsymbol a\) come vettore colonna e indicarne la dimensione.

    2. Scrivere \(\boldsymbol a'\) e \((\boldsymbol a')'\).

    3. Calcolare \(\boldsymbol a'\boldsymbol a\).

??? soluzione "Soluzione"

    1. Il vettore è il trasposto di un vettore riga con \(4\) elementi, quindi

        $$
        \boldsymbol a=\begin{pmatrix}1\\-2\\0\\5\end{pmatrix}\in\R^{4},
        $$

        e la sua dimensione è \(n=4\).

    2. Trasponendo un vettore colonna si ottiene un vettore riga, e trasponendo due volte si ritorna al vettore di partenza:

        $$
        \boldsymbol a'=\begin{pmatrix}1 & -2 & 0 & 5\end{pmatrix}\in\R^{1\times 4},
        \qquad
        (\boldsymbol a')'=\boldsymbol a=\begin{pmatrix}1\\-2\\0\\5\end{pmatrix}.
        $$

    3. Per definizione di prodotto scalare,

        $$
        \boldsymbol a'\boldsymbol a=1\cdot 1+(-2)\cdot(-2)+0\cdot 0+5\cdot 5=1+4+0+25=30.
        $$

        Come atteso, \(\boldsymbol a'\boldsymbol a\ge 0\), e \(\boldsymbol a'\boldsymbol a\neq 0\) poiché \(\boldsymbol a\neq\boldsymbol 0\).

<a id="box-exe_vecScalarProduct-3"></a>

!!! esercizio "Esercizio 3"

    Si considerino i vettori

    $$
    \boldsymbol p=\begin{pmatrix}1\\2\\-3\end{pmatrix},
    \qquad
    \boldsymbol w=\begin{pmatrix}4\\-1\\2\end{pmatrix},
    \qquad
    \boldsymbol u=\begin{pmatrix}0\\3\\1\end{pmatrix}\in\R^{3}.
    $$

    1. Calcolare \(\boldsymbol p'\boldsymbol w\) e \(\boldsymbol w'\boldsymbol p\).

    2. Calcolare \(\boldsymbol p'(\boldsymbol w+\boldsymbol u)\) e verificare che è uguale a \(\boldsymbol p'\boldsymbol w+\boldsymbol p'\boldsymbol u\).

    3. Calcolare \((2\boldsymbol p)'\boldsymbol w\) e confrontarlo con \(2\,(\boldsymbol p'\boldsymbol w)\).

??? soluzione "Soluzione"

    1.

        $$
        \boldsymbol p'\boldsymbol w=1\cdot 4+2\cdot(-1)+(-3)\cdot 2=4-2-6=-4,
        \qquad
        \boldsymbol w'\boldsymbol p=4\cdot 1+(-1)\cdot 2+2\cdot(-3)=-4.
        $$

        I due valori coincidono (simmetria del prodotto scalare).

    2. Si ha \(\boldsymbol w+\boldsymbol u=\begin{pmatrix}4 & 2 & 3\end{pmatrix}'\), quindi

        $$
        \boldsymbol p'(\boldsymbol w+\boldsymbol u)=1\cdot 4+2\cdot 2+(-3)\cdot 3=4+4-9=-1.
        $$

        D'altra parte, \( \boldsymbol p'\boldsymbol u=1\cdot 0+2\cdot 3+(-3)\cdot 1=3 \), quindi \(\boldsymbol p'\boldsymbol w+\boldsymbol p'\boldsymbol u=-4+3=-1\), come atteso.

    3. Si ha \(2\boldsymbol p=\begin{pmatrix}2 & 4 & -6\end{pmatrix}'\), quindi

        $$
        (2\boldsymbol p)'\boldsymbol w=2\cdot 4+4\cdot(-1)+(-6)\cdot 2=8-4-12=-8=2\cdot(-4)=2\,(\boldsymbol p'\boldsymbol w).
        $$

<a id="box-exe_vecOrthogonal-4"></a>

!!! esercizio "Esercizio 4"

    Due vettori \(\boldsymbol p,\boldsymbol w\in\R^{n}\) si dicono <strong>ortogonali</strong> se il loro prodotto scalare è nullo, cioè \(\boldsymbol p'\boldsymbol w=0\).

    1. Verificare che \(\begin{pmatrix}1 & 2 & 2\end{pmatrix}'\) e \(\begin{pmatrix}2 & -2 & 1\end{pmatrix}'\) sono ortogonali.

    2. Trovare il valore di \(\alpha\in\R\) per cui \( \boldsymbol p=\begin{pmatrix}1 & \alpha & 2\end{pmatrix}' \) e \( \boldsymbol w=\begin{pmatrix}3 & -1 & \alpha\end{pmatrix}' \) sono ortogonali.

??? soluzione "Soluzione"

    1. \( \begin{pmatrix}1 & 2 & 2\end{pmatrix}\begin{pmatrix}2\\-2\\1\end{pmatrix}=1\cdot 2+2\cdot(-2)+2\cdot 1=2-4+2=0, \) quindi i due vettori sono ortogonali.

    2. Calcoliamo il prodotto scalare in funzione di \(\alpha\):

        $$
        \boldsymbol p'\boldsymbol w=1\cdot 3+\alpha\cdot(-1)+2\cdot\alpha=3+\alpha.
        $$

        Imponendo \(\boldsymbol p'\boldsymbol w=0\) si ottiene \(3+\alpha=0\), cioè \(\alpha=-3\). Verifica: con \(\alpha=-3\), \(\boldsymbol p=\begin{pmatrix}1 & -3 & 2\end{pmatrix}'\), \(\boldsymbol w=\begin{pmatrix}3 & -1 & -3\end{pmatrix}'\) e \(\boldsymbol p'\boldsymbol w=3+3-6=0\).

<a id="box-exe_vecLinCombCompute-5"></a>

!!! esercizio "Esercizio 5"

    Si considerino i vettori \( \boldsymbol v_1=\begin{pmatrix}1 & 0 & 2\end{pmatrix}' \) e \( \boldsymbol v_2=\begin{pmatrix}-1 & 3 & 1\end{pmatrix}'. \) Calcolare le combinazioni lineari \(3\boldsymbol v_1-2\boldsymbol v_2\) e \(-\boldsymbol v_1+\boldsymbol v_2\).

??? soluzione "Soluzione"

    $$
    3\boldsymbol v_1-2\boldsymbol v_2
    =
    \begin{pmatrix}3\\0\\6\end{pmatrix}
    +
    \begin{pmatrix}2\\-6\\-2\end{pmatrix}
    =
    \begin{pmatrix}5\\-6\\4\end{pmatrix},
    \qquad
    -\boldsymbol v_1+\boldsymbol v_2
    =
    \begin{pmatrix}-1\\0\\-2\end{pmatrix}
    +
    \begin{pmatrix}-1\\3\\1\end{pmatrix}
    =
    \begin{pmatrix}-2\\3\\-1\end{pmatrix}.
    $$

<a id="box-exe_vecIsLinComb-6"></a>

!!! esercizio "Esercizio 6"

    Si considerino i vettori \( \boldsymbol v_1=\begin{pmatrix}1 & 1 & 0\end{pmatrix}' \) e \( \boldsymbol v_2=\begin{pmatrix}0 & 1 & 2\end{pmatrix}'. \) Stabilire se i seguenti vettori sono combinazioni lineari di \(\boldsymbol v_1\) e \(\boldsymbol v_2\) e, in caso affermativo, trovarne i coefficienti:

    $$
    \boldsymbol w=\begin{pmatrix}2\\5\\6\end{pmatrix},
    \qquad
    \boldsymbol u=\begin{pmatrix}1\\2\\3\end{pmatrix}.
    $$

??? soluzione "Soluzione"

    Cerchiamo \(\lambda_1,\lambda_2\in\R\) tali che \(\lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2\) sia uguale al vettore dato. Poiché \( \lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2=\begin{pmatrix}\lambda_1 & \lambda_1+\lambda_2 & 2\lambda_2\end{pmatrix}', \) confrontiamo gli elementi.

    - Per \(\boldsymbol w\):

        $$
        \begin{cases}
        \lambda_1=2\\
        \lambda_1+\lambda_2=5\\
        2\lambda_2=6
        \end{cases}
        $$

        La prima equazione dà \(\lambda_1=2\), la seconda \(\lambda_2=3\), e la terza è soddisfatta (\(2\cdot 3=6\)). Quindi \(\boldsymbol w=2\boldsymbol v_1+3\boldsymbol v_2\).

    - Per \(\boldsymbol u\):

        $$
        \begin{cases}
        \lambda_1=1\\
        \lambda_1+\lambda_2=2\\
        2\lambda_2=3
        \end{cases}
        $$

        Le prime due equazioni danno \(\lambda_1=1\) e \(\lambda_2=1\), ma allora \(2\lambda_2=2\neq 3\). Il sistema non ha soluzione, quindi \(\boldsymbol u\) <strong>non</strong> è combinazione lineare di \(\boldsymbol v_1\) e \(\boldsymbol v_2\).

<a id="box-exe_vecIndepR2-7"></a>

!!! esercizio "Esercizio 7"

    Stabilire se le seguenti coppie di vettori di \(\R^2\) sono linearmente indipendenti:

    $$
    \text{(a)}\quad \begin{pmatrix}2\\1\end{pmatrix},\ \begin{pmatrix}4\\2\end{pmatrix};
    \qquad\qquad
    \text{(b)}\quad \begin{pmatrix}2\\1\end{pmatrix},\ \begin{pmatrix}1\\3\end{pmatrix}.
    $$

??? soluzione "Soluzione"

    - **(a)** Il secondo vettore è il doppio del primo: \(\begin{pmatrix}4 & 2\end{pmatrix}'=2\begin{pmatrix}2 & 1\end{pmatrix}'\). Quindi, con \(\lambda_1=2\) e \(\lambda_2=-1\),

        $$
        2\begin{pmatrix}2\\1\end{pmatrix}-1\begin{pmatrix}4\\2\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix},
        $$

        una combinazione lineare uguale a \(\boldsymbol 0\) con coefficienti non tutti nulli: i vettori sono linearmente <strong>dipendenti</strong>.

    - **(b)** La condizione \(\lambda_1\begin{pmatrix}2 & 1\end{pmatrix}'+\lambda_2\begin{pmatrix}1 & 3\end{pmatrix}'=\boldsymbol 0\) si scrive

        $$
        \begin{cases}
        2\lambda_1+\lambda_2=0\\
        \lambda_1+3\lambda_2=0
        \end{cases}
        $$

        Dalla seconda equazione \(\lambda_1=-3\lambda_2\); sostituendo nella prima, \(-6\lambda_2+\lambda_2=-5\lambda_2=0\), quindi \(\lambda_2=0\) e \(\lambda_1=0\). I vettori sono linearmente <strong>indipendenti</strong>.

<a id="box-exe_vecIndepR3-8"></a>

!!! esercizio "Esercizio 8"

    Stabilire se i seguenti insiemi di vettori di \(\R^3\) sono linearmente indipendenti. Se sono dipendenti, trovare una combinazione lineare uguale a \(\boldsymbol 0\) con coefficienti non tutti nulli.

    1. \(\boldsymbol v_1=\begin{pmatrix}1 & 2 & 1\end{pmatrix}'\), \(\boldsymbol v_2=\begin{pmatrix}0 & 1 & 1\end{pmatrix}'\), \(\boldsymbol v_3=\begin{pmatrix}1 & 3 & 2\end{pmatrix}'\).

    2. \(\boldsymbol w_1=\begin{pmatrix}1 & 0 & 0\end{pmatrix}'\), \(\boldsymbol w_2=\begin{pmatrix}1 & 1 & 0\end{pmatrix}'\), \(\boldsymbol w_3=\begin{pmatrix}1 & 1 & 1\end{pmatrix}'\).

??? soluzione "Soluzione"

    1. La condizione \(\lambda_1\boldsymbol v_1+\lambda_2\boldsymbol v_2+\lambda_3\boldsymbol v_3=\boldsymbol 0\) si scrive

        $$
        \begin{cases}
        \lambda_1+\lambda_3=0\\
        2\lambda_1+\lambda_2+3\lambda_3=0\\
        \lambda_1+\lambda_2+2\lambda_3=0
        \end{cases}
        $$

        Dalla prima equazione \(\lambda_1=-\lambda_3\). Sostituendo nella seconda: \(-2\lambda_3+\lambda_2+3\lambda_3=0\), cioè \(\lambda_2=-\lambda_3\). La terza equazione diventa \(-\lambda_3-\lambda_3+2\lambda_3=0\), che vale per ogni \(\lambda_3\). Scegliendo \(\lambda_3=1\) si ottiene \(\lambda_1=\lambda_2=-1\):

        $$
        -\boldsymbol v_1-\boldsymbol v_2+\boldsymbol v_3
        =
        \begin{pmatrix}-1-0+1\\-2-1+3\\-1-1+2\end{pmatrix}
        =
        \begin{pmatrix}0\\0\\0\end{pmatrix}.
        $$

        I vettori sono linearmente <strong>dipendenti</strong> (infatti \(\boldsymbol v_3=\boldsymbol v_1+\boldsymbol v_2\)).

    2. La condizione \(\lambda_1\boldsymbol w_1+\lambda_2\boldsymbol w_2+\lambda_3\boldsymbol w_3=\boldsymbol 0\) si scrive

        $$
        \begin{cases}
        \lambda_1+\lambda_2+\lambda_3=0\\
        \lambda_2+\lambda_3=0\\
        \lambda_3=0
        \end{cases}
        $$

        Risolvendo dall'ultima equazione verso l'alto: \(\lambda_3=0\), poi \(\lambda_2=0\), poi \(\lambda_1=0\). I vettori sono linearmente <strong>indipendenti</strong>.

<a id="box-exe_vecDependentNoComputation-9"></a>

!!! esercizio "Esercizio 9"

    Senza risolvere alcun sistema, spiegare perché i seguenti insiemi di vettori sono linearmente dipendenti, e fornire una combinazione lineare uguale a \(\boldsymbol 0\) con coefficienti non tutti nulli.

    1. \(\begin{pmatrix}1 & 0 & 0\end{pmatrix}'\), \(\begin{pmatrix}0 & 1 & 0\end{pmatrix}'\), \(\begin{pmatrix}0 & 0 & 1\end{pmatrix}'\), \(\begin{pmatrix}1 & 2 & 3\end{pmatrix}'\in\R^{3}\).

    2. \(\begin{pmatrix}1 & 2\end{pmatrix}'\), \(\begin{pmatrix}0 & 0\end{pmatrix}'\in\R^{2}\).

    3. \(\begin{pmatrix}1 & 2\end{pmatrix}'\), \(\begin{pmatrix}-1 & -2\end{pmatrix}'\in\R^{2}\).

??? soluzione "Soluzione"

    1. Si tratta di \(4>3\) vettori di \(\R^3\), quindi sono linearmente dipendenti. Esplicitamente, i primi tre vettori sono la base canonica \(\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3\) e \(\begin{pmatrix}1 & 2 & 3\end{pmatrix}'=1\boldsymbol e_1+2\boldsymbol e_2+3\boldsymbol e_3\), quindi

        $$
        1\boldsymbol e_1+2\boldsymbol e_2+3\boldsymbol e_3-1\begin{pmatrix}1\\2\\3\end{pmatrix}=\boldsymbol 0.
        $$

    2. L'insieme contiene il vettore nullo, quindi è linearmente dipendente: \( 0\begin{pmatrix}1 & 2\end{pmatrix}'+1\begin{pmatrix}0 & 0\end{pmatrix}'=\boldsymbol 0. \)

    3. Il secondo vettore è combinazione lineare del primo, \(\begin{pmatrix}-1 & -2\end{pmatrix}'=-1\begin{pmatrix}1 & 2\end{pmatrix}'\), hence \( 1\begin{pmatrix}1 & 2\end{pmatrix}'+1\begin{pmatrix}-1 & -2\end{pmatrix}'=\boldsymbol 0. \)

<a id="box-exe_vecBasisCoordinates-10"></a>

!!! esercizio "Esercizio 10"

    Si considerino i vettori

    $$
    \boldsymbol b_1=\begin{pmatrix}1\\1\\0\end{pmatrix},
    \qquad
    \boldsymbol b_2=\begin{pmatrix}0\\1\\1\end{pmatrix},
    \qquad
    \boldsymbol b_3=\begin{pmatrix}1\\0\\1\end{pmatrix}\in\R^{3}.
    $$

    1. Dimostrare che \(\boldsymbol b_1,\boldsymbol b_2,\boldsymbol b_3\) formano una base di \(\R^3\).

    2. Trovare le coordinate di \(\boldsymbol x=\begin{pmatrix}4 & 3 & 5\end{pmatrix}'\) rispetto a questa base e rispetto alla base canonica.

??? soluzione "Soluzione"

    1. Dobbiamo mostrare che i vettori sono linearmente indipendenti e che il loro span è \(\R^3\). Dato \(\boldsymbol y=\begin{pmatrix}a & b & c\end{pmatrix}'\in\R^3\), l'equazione \(\lambda_1\boldsymbol b_1+\lambda_2\boldsymbol b_2+\lambda_3\boldsymbol b_3=\boldsymbol y\) si scrive

        $$
        \begin{cases}
        \lambda_1+\lambda_3=a\\
        \lambda_1+\lambda_2=b\\
        \lambda_2+\lambda_3=c
        \end{cases}
        $$

        Sommando le tre equazioni: \(2(\lambda_1+\lambda_2+\lambda_3)=a+b+c\), cioè \(\lambda_1+\lambda_2+\lambda_3=s\) con \(s=\frac{a+b+c}{2}\). Sottraendo da questa ciascuna equazione si ottiene l'<em>unica</em> soluzione

        $$
        \lambda_1=s-c,\qquad \lambda_2=s-a,\qquad \lambda_3=s-b.
        $$

        - Poiché esiste una soluzione per ogni \(\boldsymbol y\), lo span è \(\R^3\).

        - Per \(\boldsymbol y=\boldsymbol 0\) (\(a=b=c=0\)) si ottiene \(s=0\) e \(\lambda_1=\lambda_2=\lambda_3=0\): i vettori sono linearmente indipendenti.

        Quindi \(\boldsymbol b_1,\boldsymbol b_2,\boldsymbol b_3\) formano una base di \(\R^3\).

    2. Per \(\boldsymbol x\) si ha \(a=4\), \(b=3\), \(c=5\), quindi \(s=\frac{4+3+5}{2}=6\) e \(\lambda_1=6-5=1\), \(\lambda_2=6-4=2\), \(\lambda_3=6-3=3\). Verifica:

        $$
        1\begin{pmatrix}1\\1\\0\end{pmatrix}+2\begin{pmatrix}0\\1\\1\end{pmatrix}+3\begin{pmatrix}1\\0\\1\end{pmatrix}
        =
        \begin{pmatrix}1+0+3\\1+2+0\\0+2+3\end{pmatrix}
        =
        \begin{pmatrix}4\\3\\5\end{pmatrix}.
        $$

        Rispetto alla base canonica le coordinate sono semplicemente gli elementi di \(\boldsymbol x\): \(\boldsymbol x=4\boldsymbol e_1+3\boldsymbol e_2+5\boldsymbol e_3\).
