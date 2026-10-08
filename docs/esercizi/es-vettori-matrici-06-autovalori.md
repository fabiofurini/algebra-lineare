---
title: "Autovalori e autovettori"
---

# Autovalori e autovettori

<div class="info-capitolo" markdown>

**Esercizi · Vettori e matrici** · capitolo [4.5 · Autovalori e autovettori](../vettori-matrici/06-autovalori.md) · con le soluzioni svolte · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf)

</div>

<a id="box-exe_eig_2x2_nonsym-1"></a>

!!! esercizio "Esercizio 1"

    Calcolare gli autovalori della matrice

    $$
    \boldsymbol A=
    \begin{pmatrix}
    4 & 1\\[0.5ex]
    2 & 3
    \end{pmatrix}
    $$

    e un autovettore associato a ciascun autovalore.

??? soluzione "Soluzione"

    L'equazione caratteristica è

    $$
    \det(\boldsymbol A-\lambda\boldsymbol I)
    =
    \det\begin{pmatrix}
    4-\lambda & 1\\[0.5ex]
    2 & 3-\lambda
    \end{pmatrix}
    =(4-\lambda)(3-\lambda)-2
    =\lambda^2-7\lambda+10
    =(\lambda-2)(\lambda-5)=0,
    $$

    quindi $\lambda_1=2$ e $\lambda_2=5$.

    Per $\lambda_1=2$:

    $$
    (\boldsymbol A-2\boldsymbol I)\boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \begin{pmatrix}
    2 & 1\\[0.5ex]
    2 & 1
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    2v_1+v_2=0,
    \qquad
    \boldsymbol v_1=\begin{pmatrix}1\\[0.5ex]-2\end{pmatrix}.
    $$

    Per $\lambda_2=5$:

    $$
    (\boldsymbol A-5\boldsymbol I)\boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    \begin{pmatrix}
    -1 & 1\\[0.5ex]
    2 & -2
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    v_1=v_2,
    \qquad
    \boldsymbol v_2=\begin{pmatrix}1\\[0.5ex]1\end{pmatrix}.
    $$

    Controllo: $\boldsymbol A\boldsymbol v_1=(4-2,\;2-6)'=(2,-4)'=2\,\boldsymbol v_1$ e $\boldsymbol A\boldsymbol v_2=(5,5)'=5\,\boldsymbol v_2$.

<a id="box-exe_eig_2x2_sym-2"></a>

!!! esercizio "Esercizio 2"

    Calcolare gli autovalori e un autovettore per ciascun autovalore della matrice simmetrica

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    5 & 2\\[0.5ex]
    2 & 2
    \end{pmatrix}.
    $$

    $\boldsymbol Q$ è definita positiva?

??? soluzione "Soluzione"

    L'equazione caratteristica è

    $$
    \det(\boldsymbol Q-\lambda\boldsymbol I)
    =(5-\lambda)(2-\lambda)-4
    =\lambda^2-7\lambda+6
    =(\lambda-1)(\lambda-6)=0,
    $$

    quindi $\lambda_1=1$ e $\lambda_2=6$.

    Per $\lambda_1=1$:

    $$
    \begin{pmatrix}
    4 & 2\\[0.5ex]
    2 & 1
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    2v_1+v_2=0,
    \qquad
    \boldsymbol v_1=\begin{pmatrix}1\\[0.5ex]-2\end{pmatrix}.
    $$

    Per $\lambda_2=6$:

    $$
    \begin{pmatrix}
    -1 & 2\\[0.5ex]
    2 & -4
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0
    \Longleftrightarrow
    v_1=2v_2,
    \qquad
    \boldsymbol v_2=\begin{pmatrix}2\\[0.5ex]1\end{pmatrix}.
    $$

    Poiché $\boldsymbol Q$ è simmetrica ed entrambi gli autovalori sono strettamente positivi, $\boldsymbol Q$ è <strong>definita positiva</strong>. (Si osservi anche che $\boldsymbol v_1'\boldsymbol v_2=2-2=0$.)

<a id="box-exe_eig_triangular-3"></a>

!!! esercizio "Esercizio 3"

    Senza calcolare alcun determinante, trovare gli autovalori di

    $$
    \boldsymbol U=
    \begin{pmatrix}
    3 & 1 & -2\\[0.5ex]
    0 & -1 & 4\\[0.5ex]
    0 & 0 & 2
    \end{pmatrix}.
    $$

    Trovare poi un autovettore per ciascun autovalore e controllare traccia e determinante.

??? soluzione "Soluzione"

    $\boldsymbol U$ è triangolare superiore, quindi i suoi autovalori sono i suoi elementi diagonali:

    $$
    \lambda_1=3,\qquad \lambda_2=-1,\qquad \lambda_3=2.
    $$

    - $\lambda_1=3$: $(\boldsymbol U-3\boldsymbol I)\boldsymbol v=\boldsymbol 0$ dà $v_2-2v_3=0$, $-4v_2+4v_3=0$, $-v_3=0$, quindi $v_2=v_3=0$ e $\boldsymbol v_1=(1,0,0)'$.

    - $\lambda_2=-1$:

        $$
        (\boldsymbol U+\boldsymbol I)\boldsymbol v=
        \begin{pmatrix}
        4 & 1 & -2\\[0.5ex]
        0 & 0 & 4\\[0.5ex]
        0 & 0 & 3
        \end{pmatrix}
        \boldsymbol v=\boldsymbol 0
        \Longrightarrow
        v_3=0,\ \ 4v_1+v_2=0,
        \qquad
        \boldsymbol v_2=\begin{pmatrix}1\\[0.5ex]-4\\[0.5ex]0\end{pmatrix}.
        $$

    - $\lambda_3=2$:

        $$
        (\boldsymbol U-2\boldsymbol I)\boldsymbol v=
        \begin{pmatrix}
        1 & 1 & -2\\[0.5ex]
        0 & -3 & 4\\[0.5ex]
        0 & 0 & 0
        \end{pmatrix}
        \boldsymbol v=\boldsymbol 0
        \Longrightarrow
        v_2=\tfrac{4}{3}v_3,\ \ v_1=-v_2+2v_3=\tfrac{2}{3}v_3.
        $$

        Scegliendo $v_3=3$: $\boldsymbol v_3=(2,4,3)'$.

    Controllo: $\operatorname{tr}(\boldsymbol U)=3-1+2=4=\lambda_1+\lambda_2+\lambda_3$ e $\det(\boldsymbol U)=3\cdot(-1)\cdot 2=-6=\lambda_1\,\lambda_2\,\lambda_3$.

<a id="box-exe_eig_3x3_full-4"></a>

!!! esercizio "Esercizio 4"

    Calcolare il polinomio caratteristico, gli autovalori e un autovettore per ciascun autovalore di

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    -1 & 1 & 0\\[0.5ex]
    1 & 2 & 3\\[0.5ex]
    0 & 3 & -1
    \end{pmatrix}.
    $$

    Classificare $\boldsymbol Q$ (definita, semidefinita o indefinita).

??? soluzione "Soluzione"

    Sviluppando lungo la prima riga:

    \begin{align*}
    \det(\boldsymbol Q-\lambda\boldsymbol I)
    &=
    \det\begin{pmatrix}
    -1-\lambda & 1 & 0\\[0.5ex]
    1 & 2-\lambda & 3\\[0.5ex]
    0 & 3 & -1-\lambda
    \end{pmatrix}\\[1ex]
    &=(-1-\lambda)\big[(2-\lambda)(-1-\lambda)-9\big]-1\cdot\big[1\cdot(-1-\lambda)-3\cdot 0\big]\\[1ex]
    &=(-1-\lambda)\big[(2-\lambda)(-1-\lambda)-9-1\big]
    =(-1-\lambda)(\lambda^2-\lambda-12)\\[1ex]
    &=(-1-\lambda)(\lambda-4)(\lambda+3).
    \end{align*}

    Gli autovalori sono $\lambda_1=-1$, $\lambda_2=4$, $\lambda_3=-3$.

    - $\lambda_1=-1$: $(\boldsymbol Q+\boldsymbol I)\boldsymbol v=\boldsymbol 0$ con $\boldsymbol Q+\boldsymbol I=\begin{pmatrix}0 & 1 & 0\\ 1 & 3 & 3\\ 0 & 3 & 0\end{pmatrix}$ dà $v_2=0$ e $v_1+3v_3=0$: $\boldsymbol v_1=(3,0,-1)'$.

    - $\lambda_2=4$: $\boldsymbol Q-4\boldsymbol I=\begin{pmatrix}-5 & 1 & 0\\ 1 & -2 & 3\\ 0 & 3 & -5\end{pmatrix}$ dà $v_2=5v_1$, $v_3=\frac{3}{5}v_2=3v_1$ (e $v_1-10v_1+9v_1=0$): $\boldsymbol v_2=(1,5,3)'$.

    - $\lambda_3=-3$: $\boldsymbol Q+3\boldsymbol I=\begin{pmatrix}2 & 1 & 0\\ 1 & 5 & 3\\ 0 & 3 & 2\end{pmatrix}$ dà $v_2=-2v_1$, $v_3=-\frac{3}{2}v_2=3v_1$ (e $v_1-10v_1+9v_1=0$): $\boldsymbol v_3=(1,-2,3)'$.

    Controllo: $\operatorname{tr}(\boldsymbol Q)=-1+2-1=0=-1+4-3$ e $\det(\boldsymbol Q)=-1\cdot(-2-9)-1\cdot(-1-0)=12=(-1)\cdot 4\cdot(-3)$.

    $\boldsymbol Q$ è simmetrica con un autovalore positivo e uno negativo, quindi è <strong>indefinita</strong>.

<a id="box-exe_eig_trace_det-5"></a>

!!! esercizio "Esercizio 5"

    La matrice

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    4 & -1 & 1\\[0.5ex]
    -1 & 4 & -1\\[0.5ex]
    1 & -1 & 4
    \end{pmatrix}
    $$

    ha l'autovalore $\lambda=3$ con molteplicità $2$. Usando la traccia, trovare il terzo autovalore; poi controllare il risultato con il determinante e trovare un autovettore associato.

??? soluzione "Soluzione"

    Gli autovalori, contati con la loro molteplicità, sono $\lambda_1=\lambda_2=3$ e $\lambda_3$. Poiché la traccia è la somma degli autovalori:

    $$
    \operatorname{tr}(\boldsymbol Q)=4+4+4=12=3+3+\lambda_3
    \quad\Longrightarrow\quad
    \lambda_3=6.
    $$

    Controllo con il determinante (sviluppo di Laplace lungo la prima riga):

    $$
    \det(\boldsymbol Q)=4\,(16-1)-(-1)\,(-4+1)+1\,(1-4)=60-3-3=54=3\cdot 3\cdot 6. \quad\checkmark
    $$

    Autovettore per $\lambda_3=6$:

    $$
    (\boldsymbol Q-6\boldsymbol I)\boldsymbol v=
    \begin{pmatrix}
    -2 & -1 & 1\\[0.5ex]
    -1 & -2 & -1\\[0.5ex]
    1 & -1 & -2
    \end{pmatrix}
    \boldsymbol v=\boldsymbol 0.
    $$

    Sommando le prime due equazioni: $-3v_1-3v_2=0$, cioè $v_2=-v_1$; poi dalla prima equazione $v_3=2v_1+v_2=v_1$. Quindi $\boldsymbol v=(1,-1,1)'$; infatti $\boldsymbol Q\boldsymbol v=(4+1+1,\,-1-4-1,\,1+1+4)'=(6,-6,6)'=6\,\boldsymbol v$.

<a id="box-exe_eig_definiteness-6"></a>

!!! esercizio "Esercizio 6"

    Usando gli autovalori, classificare le seguenti matrici simmetriche:

    $$
    {\rm a)}~\boldsymbol Q_1=
    \begin{pmatrix}
    -3 & 1\\[0.5ex]
    1 & -3
    \end{pmatrix},
    \qquad
    {\rm b)}~\boldsymbol Q_2=
    \begin{pmatrix}
    1 & 3\\[0.5ex]
    3 & 1
    \end{pmatrix},
    \qquad
    {\rm c)}~\boldsymbol Q_3=
    \begin{pmatrix}
    2 & 2\\[0.5ex]
    2 & 2
    \end{pmatrix}.
    $$

??? soluzione "Soluzione"

    - **a)** $(-3-\lambda)^2-1=\lambda^2+6\lambda+8=(\lambda+2)(\lambda+4)$: gli autovalori sono $-2$ e $-4$, entrambi strettamente negativi, quindi $\boldsymbol Q_1$ è <strong>definita negativa</strong>.

    - **b)** $(1-\lambda)^2-9=\lambda^2-2\lambda-8=(\lambda-4)(\lambda+2)$: gli autovalori sono $4$ e $-2$, quindi $\boldsymbol Q_2$ è <strong>indefinita</strong>.

    - **c)** $(2-\lambda)^2-4=\lambda^2-4\lambda=\lambda(\lambda-4)$: gli autovalori sono $0$ e $4$, entrambi non negativi, quindi $\boldsymbol Q_3$ è <strong>semidefinita positiva</strong> (ma non definita positiva, poiché $0$ è un autovalore).

<a id="box-exe_eig_sylvester_pd-7"></a>

!!! esercizio "Esercizio 7"

    Usando il criterio di Sylvester, dimostrare che la matrice

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    2 & -1 & 0\\[0.5ex]
    -1 & 2 & -1\\[0.5ex]
    0 & -1 & 2
    \end{pmatrix}
    $$

    è definita positiva.

??? soluzione "Soluzione"

    $\boldsymbol Q$ è simmetrica e i suoi minori principali di guida sono

    $$
    \Delta_1=2>0,
    \qquad
    \Delta_2=\det\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix}=4-1=3>0,
    $$

    $$
    \Delta_3=\det(\boldsymbol Q)=2\,(4-1)-(-1)\,(-2-0)+0=6-2=4>0.
    $$

    Tutti i minori principali di guida sono strettamente positivi, quindi $\boldsymbol Q$ è <strong>definita positiva</strong>. (Qui il criterio di Sylvester è conveniente: gli autovalori di $\boldsymbol Q$ sono $2$ e $2\pm\sqrt 2$, che non sono interi.)

<a id="box-exe_eig_sylvester_nd-8"></a>

!!! esercizio "Esercizio 8"

    Usando il criterio di Sylvester, classificare

    $$
    \boldsymbol Q=
    \begin{pmatrix}
    -2 & 1 & 0\\[0.5ex]
    1 & -3 & 1\\[0.5ex]
    0 & 1 & -2
    \end{pmatrix}.
    $$

??? soluzione "Soluzione"

    $\boldsymbol Q$ è simmetrica e i suoi minori principali di guida sono

    $$
    \Delta_1=-2<0,
    \qquad
    \Delta_2=\det\begin{pmatrix}-2 & 1\\ 1 & -3\end{pmatrix}=6-1=5>0,
    $$

    $$
    \Delta_3=\det(\boldsymbol Q)=-2\,(6-1)-1\,(-2-0)=-10+2=-8<0.
    $$

    I minori principali di guida hanno segni alterni a partire da uno negativo, quindi $\boldsymbol Q$ è <strong>definita negativa</strong>. (Infatti, i suoi autovalori sono $-1$, $-2$ e $-4$.)

<a id="box-exe_eig_semidefinite_minors-9"></a>

!!! esercizio "Esercizio 9"

    Usando i minori principali, stabilire se le seguenti matrici simmetriche sono semidefinite positive:

    $$
    {\rm a)}~\boldsymbol Q_a=
    \begin{pmatrix}
    2 & -2 & 0\\[0.5ex]
    -2 & 2 & 0\\[0.5ex]
    0 & 0 & 1
    \end{pmatrix},
    \qquad
    {\rm b)}~\boldsymbol Q_b=
    \begin{pmatrix}
    1 & 1 & 0\\[0.5ex]
    1 & 1 & 0\\[0.5ex]
    0 & 0 & -1
    \end{pmatrix}.
    $$

??? soluzione "Soluzione"

    - **a)** I minori principali di guida sono $\Delta_1=2$, $\Delta_2=4-4=0$, $\Delta_3=\det(\boldsymbol Q_a)=0$: $\boldsymbol Q_a$ non è definita positiva. Controlliamo <strong>tutti</strong> i minori principali:

        - ordine 1: $2,\ 2,\ 1$;

        - ordine 2: $\det\begin{pmatrix}2 & -2\\ -2 & 2\end{pmatrix}=0$, $\det\begin{pmatrix}2 & 0\\ 0 & 1\end{pmatrix}=2$, $\det\begin{pmatrix}2 & 0\\ 0 & 1\end{pmatrix}=2$;

        - ordine 3: $\det(\boldsymbol Q_a)=0$.

        Sono tutti $\ge 0$: $\boldsymbol Q_a$ è <strong>semidefinita positiva</strong>. Infatti $\boldsymbol x'\boldsymbol Q_a\boldsymbol x=2(x_1-x_2)^2+x_3^2\ge 0$, e gli autovalori sono $0,1,4$.

    - **b)** I minori principali di guida sono $\Delta_1=1$, $\Delta_2=1-1=0$, $\Delta_3=\det(\boldsymbol Q_b)=-1\cdot 0=0$: sono tutti $\ge 0$, ma questo <strong>non</strong> basta. Il minore principale di ordine 1 dato dall'elemento $q_{33}=-1$ è negativo, quindi $\boldsymbol Q_b$ <strong>non</strong> è semidefinita positiva: per $\boldsymbol x=(0,0,1)'$ si ha $\boldsymbol x'\boldsymbol Q_b\boldsymbol x=-1<0$. Poiché per $\boldsymbol x=(1,0,0)'$ si ha $\boldsymbol x'\boldsymbol Q_b\boldsymbol x=1>0$, la matrice è <strong>indefinita</strong> (i suoi autovalori sono $2,0,-1$).

<a id="box-exe_eig_parametric-10"></a>

!!! esercizio "Esercizio 10"

    Sia $k\in\R$ e

    $$
    \boldsymbol Q(k)=
    \begin{pmatrix}
    2 & 1 & 0\\[0.5ex]
    1 & k & 1\\[0.5ex]
    0 & 1 & 2
    \end{pmatrix}.
    $$

    Per quali valori di $k$ la matrice $\boldsymbol Q(k)$ è definita positiva? Per quali valori è semidefinita positiva?

??? soluzione "Soluzione"

    $\boldsymbol Q(k)$ è simmetrica per ogni $k$. I suoi minori principali di guida sono

    $$
    \Delta_1=2,
    \qquad
    \Delta_2=\det\begin{pmatrix}2 & 1\\ 1 & k\end{pmatrix}=2k-1,
    \qquad
    \Delta_3=2\,(2k-1)-1\cdot(2-0)=4k-4.
    $$

    Per il criterio di Sylvester, $\boldsymbol Q(k)$ è definita positiva se e solo se

    $$
    2>0,\qquad 2k-1>0 \Leftrightarrow k>\tfrac{1}{2},\qquad 4k-4>0 \Leftrightarrow k>1,
    $$

    cioè se e solo se $\boldsymbol{k>1}$.

    Per la semidefinitezza positiva servono tutti i minori principali $\ge 0$: ordine 1: $2,\ k,\ 2$; ordine 2: $2k-1$, $\det\begin{pmatrix}2 & 0\\ 0 & 2\end{pmatrix}=4$, $2k-1$; ordine 3: $4k-4$. Sono tutti $\ge 0$ se e solo se $k\ge 0$, $k\ge\frac{1}{2}$ e $k\ge 1$, cioè se e solo se $\boldsymbol{k\ge 1}$. Per $k=1$ la matrice è semidefinita positiva ma non definita positiva: i suoi autovalori sono $0,2,3$.
