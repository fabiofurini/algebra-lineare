---
title: "Sistemi di equazioni lineari"
---

# Sistemi di equazioni lineari

<div class="info-capitolo" markdown>

**Esercizi · Sistemi lineari** · capitolo [6 · Sistemi di equazioni lineari](../sistemi/01-sistemi-lineari.md) · con le soluzioni svolte · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf)

</div>

<a id="box-exe_sys_gauss_unique-1"></a>

!!! esercizio "Esercizio 1"

    Risolvere con l'eliminazione di Gauss il sistema

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 6\\[2ex]
      2 \; x_1 + 3 \; x_2 + 1 \; x_3  & = 11\\[2ex]
      1 \; x_1 - 1 \; x_2 + 2 \; x_3  & = 5
    \end{array} \right.
    $$

??? soluzione "Soluzione"

    $$
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    1 & 1 & 1 & 6 \\
    2 & 3 & 1 & 11 \\
    1 & -1 & 2 & 5
    \end{array}\right)
    $$

    $R_2 \leftarrow R_2 - 2 \; R_1$ e $R_3 \leftarrow R_3 - R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 1 & 1 & 6 \\
    0 & 1 & -1 & -1 \\
    0 & -2 & 1 & -1
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 + 2 \; R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 1 & 1 & 6 \\
    0 & 1 & -1 & -1 \\
    0 & 0 & -1 & -3
    \end{array}\right)
    $$

    Sostituzione all'indietro:

    $$
    -x_3 = -3 ~\Longrightarrow~ x_3 = 3,
    \qquad
    x_2 = -1 + x_3 = 2,
    \qquad
    x_1 = 6 - x_2 - x_3 = 1.
    $$

    Quindi ${\boldsymbol x} = (1, 2, 3)'$. Verifica: $2 + 6 + 3 = 11$ e $1 - 2 + 6 = 5$ $\checkmark$

<a id="box-exe_sys_gauss_swap-2"></a>

!!! esercizio "Esercizio 2"

    Risolvere con l'eliminazione di Gauss il sistema

    $$
    \left\{ \begin{array}{ll}
      \phantom{1 \; x_1 +{}} 2 \; x_2 + 1 \; x_3  & = -1\\[2ex]
      1 \; x_1 - 1 \; x_2 + 2 \; x_3  & = 5\\[2ex]
      2 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 4
    \end{array} \right.
    $$

??? soluzione "Soluzione"

    $$
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    0 & 2 & 1 & -1 \\
    1 & -1 & 2 & 5 \\
    2 & 1 & 1 & 4
    \end{array}\right)
    $$

    L'elemento in posizione $(1,1)$ è nullo. $R_1 \leftrightarrow R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & -1 & 2 & 5 \\
    0 & 2 & 1 & -1 \\
    2 & 1 & 1 & 4
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - 2 \; R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & -1 & 2 & 5 \\
    0 & 2 & 1 & -1 \\
    0 & 3 & -3 & -6
    \end{array}\right)
    $$

    $R_3 \leftarrow \frac{1}{3} \; R_3$, poi $R_2 \leftrightarrow R_3$ (per evitare frazioni):

    $$
    \left(\begin{array}{ccc|c}
    1 & -1 & 2 & 5 \\
    0 & 1 & -1 & -2 \\
    0 & 2 & 1 & -1
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - 2 \; R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & -1 & 2 & 5 \\
    0 & 1 & -1 & -2 \\
    0 & 0 & 3 & 3
    \end{array}\right)
    $$

    Sostituzione all'indietro:

    $$
    x_3 = 1,
    \qquad
    x_2 = -2 + x_3 = -1,
    \qquad
    x_1 = 5 + x_2 - 2 \; x_3 = 5 - 1 - 2 = 2.
    $$

    Quindi ${\boldsymbol x} = (2, -1, 1)'$. Verifica: $-2 + 1 = -1$, $2 + 1 + 2 = 5$, $4 - 1 + 1 = 4$ $\checkmark$

<a id="box-exe_sys_infinite_one-3"></a>

!!! esercizio "Esercizio 3"

    Risolvere con l'eliminazione di Gauss il sistema seguente e scriverne le soluzioni in forma parametrica ${\boldsymbol x} = {\boldsymbol x}_0 + t \; {\boldsymbol v}$:

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 - 1 \; x_2 + 2 \; x_3  & = 1\\[2ex]
      2 \; x_1 - 1 \; x_2 + 5 \; x_3  & = 4\\[2ex]
      1 \; x_1 \phantom{{}- 1 \; x_2} + 3 \; x_3  & = 3
    \end{array} \right.
    $$

??? soluzione "Soluzione"

    $$
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    1 & -1 & 2 & 1 \\
    2 & -1 & 5 & 4 \\
    1 & 0 & 3 & 3
    \end{array}\right)
    $$

    $R_2 \leftarrow R_2 - 2 \; R_1$ e $R_3 \leftarrow R_3 - R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & -1 & 2 & 1 \\
    0 & 1 & 1 & 2 \\
    0 & 1 & 1 & 2
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & -1 & 2 & 1 \\
    0 & 1 & 1 & 2 \\
    0 & 0 & 0 & 0
    \end{array}\right)
    $$

    $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 2 < 3$: infinite soluzioni con $3 - 2 = 1$ parametro libero. Ponendo $x_3 = t$:

    $$
    x_2 = 2 - t,
    \qquad
    x_1 = 1 + x_2 - 2 \; x_3 = 1 + 2 - t - 2t = 3 - 3t,
    $$

    $$
    {\boldsymbol x} =
    \begin{pmatrix}
    3 - 3t \\
    2 - t \\
    t
    \end{pmatrix}
    =
    \begin{pmatrix}
    3 \\
    2 \\
    0
    \end{pmatrix}
    + t
    \begin{pmatrix}
    -3 \\
    -1 \\
    1
    \end{pmatrix},
    \qquad t \in \R.
    $$

<a id="box-exe_sys_infinite_two-4"></a>

!!! esercizio "Esercizio 4"

    Risolvere il sistema di $2$ equazioni in $4$ variabili

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 2 \; x_2 - 1 \; x_3 + 1 \; x_4  & = 2\\[2ex]
      2 \; x_1 + 4 \; x_2 - 1 \; x_3 + 3 \; x_4  & = 5
    \end{array} \right.
    $$

??? soluzione "Soluzione"

    $$
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{cccc|c}
    1 & 2 & -1 & 1 & 2 \\
    2 & 4 & -1 & 3 & 5
    \end{array}\right)
    \qquad
    R_2 \leftarrow R_2 - 2 \; R_1:
    \qquad
    \left(\begin{array}{cccc|c}
    1 & 2 & -1 & 1 & 2 \\
    0 & 0 & 1 & 1 & 1
    \end{array}\right)
    $$

    $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 2 < 4$: infinite soluzioni con $4 - 2 = 2$ parametri liberi. I pivot sono nelle colonne di $x_1$ e $x_3$, quindi $x_2 = s$ e $x_4 = t$ sono libere:

    $$
    x_3 = 1 - x_4 = 1 - t,
    \qquad
    x_1 = 2 - 2 \; x_2 + x_3 - x_4 = 2 - 2s + 1 - t - t = 3 - 2s - 2t,
    $$

    $$
    {\boldsymbol x} =
    \begin{pmatrix}
    3 \\
    0 \\
    1 \\
    0
    \end{pmatrix}
    + s
    \begin{pmatrix}
    -2 \\
    1 \\
    0 \\
    0
    \end{pmatrix}
    + t
    \begin{pmatrix}
    -2 \\
    0 \\
    -1 \\
    1
    \end{pmatrix},
    \qquad s, t \in \R.
    $$

<a id="box-exe_sys_inconsistent-5"></a>

!!! esercizio "Esercizio 5"

    Mostrare che il sistema seguente non ha soluzioni:

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 2 \; x_2 + 1 \; x_3  & = 1\\[2ex]
      2 \; x_1 + 3 \; x_2 + 1 \; x_3  & = 2\\[2ex]
      3 \; x_1 + 5 \; x_2 + 2 \; x_3  & = 4
    \end{array} \right.
    $$

??? soluzione "Soluzione"

    $$
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    1 & 2 & 1 & 1 \\
    2 & 3 & 1 & 2 \\
    3 & 5 & 2 & 4
    \end{array}\right)
    $$

    $R_2 \leftarrow R_2 - 2 \; R_1$ e $R_3 \leftarrow R_3 - 3 \; R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & 1 & 1 \\
    0 & -1 & -1 & 0 \\
    0 & -1 & -1 & 1
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & 1 & 1 \\
    0 & -1 & -1 & 0 \\
    0 & 0 & 0 & 1
    \end{array}\right)
    $$

    L'ultima riga dice $0 = 1$: $\text{rank}({\boldsymbol A}) = 2 < 3 = \text{rank}({\boldsymbol A} | {\boldsymbol b})$, quindi per il teorema di Rouché–Capelli il sistema <strong>non ha soluzioni</strong>. (Si noti che la terza riga di ${\boldsymbol A}$ è la somma delle prime due, mentre $4 \neq 1 + 2$.)

<a id="box-exe_sys_rouche_capelli-6"></a>

!!! esercizio "Esercizio 6"

    Le seguenti matrici complete sono già in forma a scala. Usando il teorema di Rouché–Capelli, dire se ciascun sistema ha un'unica soluzione, infinite soluzioni o nessuna soluzione (variabili $x_1, x_2, x_3$). Risolvere poi i sistemi che hanno soluzioni.

    $$
    {\rm a)}~
    \left(\begin{array}{ccc|c}
    1 & 2 & 3 & 1 \\
    0 & 1 & 4 & 2 \\
    0 & 0 & 5 & 3
    \end{array}\right)
    \qquad
    {\rm b)}~
    \left(\begin{array}{ccc|c}
    1 & 2 & 3 & 1 \\
    0 & 0 & 1 & 2 \\
    0 & 0 & 0 & 0
    \end{array}\right)
    \qquad
    {\rm c)}~
    \left(\begin{array}{ccc|c}
    1 & 2 & 3 & 1 \\
    0 & 1 & 1 & 2 \\
    0 & 0 & 0 & 4
    \end{array}\right)
    $$

??? soluzione "Soluzione"

    - **a)** $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 3 = n$: <strong>soluzione unica</strong>. $x_3 = \frac{3}{5}$, $x_2 = 2 - 4 \; x_3 = -\frac{2}{5}$, $x_1 = 1 - 2 \; x_2 - 3 \; x_3 = 1 + \frac{4}{5} - \frac{9}{5} = 0$. Quindi ${\boldsymbol x} = \left(0, -\frac{2}{5}, \frac{3}{5}\right)'$.

    - **b)** $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 2 < 3$: <strong>infinite soluzioni</strong> con $1$ parametro libero. I pivot sono nelle colonne di $x_1$ e $x_3$, quindi $x_2 = t$ è libera: $x_3 = 2$, $x_1 = 1 - 2t - 3 \cdot 2 = -5 - 2t$, cioè ${\boldsymbol x} = (-5, 0, 2)' + t \; (-2, 1, 0)'$, $t \in \R$.

    - **c)** $\text{rank}({\boldsymbol A}) = 2 < 3 = \text{rank}({\boldsymbol A} | {\boldsymbol b})$ (l'ultima riga dice $0 = 4$): <strong>nessuna soluzione</strong>.

<a id="box-exe_sys_parametric-7"></a>

!!! esercizio "Esercizio 7"

    Discutere, al variare di $k \in \R$, il numero di soluzioni del sistema

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 1 \; x_2 + k \; x_3  & = 1\\[2ex]
      1 \; x_1 + k \; x_2 + 1 \; x_3  & = 1\\[2ex]
      k \; x_1 + 1 \; x_2 + 1 \; x_3  & = 1
    \end{array} \right.
    $$

    e risolverlo quando ha soluzioni.

??? soluzione "Soluzione"

    $$
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    1 & 1 & k & 1 \\
    1 & k & 1 & 1 \\
    k & 1 & 1 & 1
    \end{array}\right)
    $$

    $R_2 \leftarrow R_2 - R_1$ e $R_3 \leftarrow R_3 - k \; R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 1 & k & 1 \\
    0 & k-1 & 1-k & 0 \\
    0 & 1-k & 1-k^2 & 1-k
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 + R_2$ (si noti che $(1-k) + (1-k^2) = (1-k)(2+k)$):

    $$
    \left(\begin{array}{ccc|c}
    1 & 1 & k & 1 \\
    0 & k-1 & 1-k & 0 \\
    0 & 0 & (1-k)(2+k) & 1-k
    \end{array}\right)
    $$

    - <strong>Caso $k \neq 1$ e $k \neq -2$</strong>: tre pivot, $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 3$, <strong>soluzione unica</strong>. Dividendo per $1-k \neq 0$: $(2+k) \; x_3 = 1$, cioè $x_3 = \frac{1}{k+2}$; la seconda riga dà $(k-1)(x_2 - x_3) = 0$, cioè $x_2 = x_3 = \frac{1}{k+2}$; infine $x_1 = 1 - x_2 - k \; x_3 = 1 - \frac{1+k}{k+2} = \frac{1}{k+2}$. Quindi

        $$
        {\boldsymbol x} = \frac{1}{k+2} \; (1, 1, 1)'.
        $$

    - <strong>Caso $k = 1$</strong>: la seconda e la terza riga diventano nulle. $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 1 < 3$: <strong>infinite soluzioni</strong> con $2$ parametri liberi. Il sistema si riduce a $x_1 + x_2 + x_3 = 1$; con $x_2 = s$, $x_3 = t$: ${\boldsymbol x} = (1 - s - t, \; s, \; t)'$, $s, t \in \R$.

    - <strong>Caso $k = -2$</strong>: l'ultima riga diventa $\left(\begin{array}{ccc|c} 0 & 0 & 0 & 3 \end{array}\right)$, cioè $0 = 3$. $\text{rank}({\boldsymbol A}) = 2 < 3 = \text{rank}({\boldsymbol A} | {\boldsymbol b})$: <strong>nessuna soluzione</strong>.

    (Coerentemente, $\det({\boldsymbol A}) = -(k-1)^2 (k+2)$ si annulla esattamente per $k = 1$ e $k = -2$.)

<a id="box-exe_sys_homogeneous-8"></a>

!!! esercizio "Esercizio 8"

    Trovare i valori di $k \in \R$ per cui il sistema omogeneo

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 2 \; x_2 + 1 \; x_3  & = 0\\[2ex]
      2 \; x_1 + k \; x_2 + 3 \; x_3  & = 0\\[2ex]
      1 \; x_1 + 1 \; x_2 + 2 \; x_3  & = 0
    \end{array} \right.
    $$

    ha soluzioni non banali, e calcolarle.

??? soluzione "Soluzione"

    La matrice ${\boldsymbol A}$ è quadrata, quindi ci sono soluzioni non banali se e solo se $\det({\boldsymbol A}) = 0$. Con la regola di Sarrus:

    $$
    \det({\boldsymbol A}) = 2k + 6 + 2 - k - 8 - 3 = k - 3,
    $$

    quindi esistono soluzioni non banali se e solo se $k = 3$ (per $k \neq 3$ l'unica soluzione è ${\boldsymbol x} = {\boldsymbol 0}$).

    Per $k = 3$, $R_2 \leftarrow R_2 - 2 \; R_1$ e $R_3 \leftarrow R_3 - R_1$, poi $R_3 \leftarrow R_3 - R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & 1 & 0 \\
    2 & 3 & 3 & 0 \\
    1 & 1 & 2 & 0
    \end{array}\right)
    \rightarrow
    \left(\begin{array}{ccc|c}
    1 & 2 & 1 & 0 \\
    0 & -1 & 1 & 0 \\
    0 & -1 & 1 & 0
    \end{array}\right)
    \rightarrow
    \left(\begin{array}{ccc|c}
    1 & 2 & 1 & 0 \\
    0 & -1 & 1 & 0 \\
    0 & 0 & 0 & 0
    \end{array}\right)
    $$

    Ponendo $x_3 = t$: $x_2 = x_3 = t$ e $x_1 = -2 \; x_2 - x_3 = -3t$. Quindi

    $$
    {\boldsymbol x} = t \; (-3, 1, 1)', \qquad t \in \R.
    $$

<a id="box-exe_sys_cramer_2x2-9"></a>

!!! esercizio "Esercizio 9"

    Risolvere con la regola di Cramer il sistema

    $$
    \left\{ \begin{array}{ll}
      3 \; x_1 + 2 \; x_2  & = 7\\[2ex]
      1 \; x_1 - 1 \; x_2  & = -1
    \end{array} \right.
    $$

??? soluzione "Soluzione"

    $$
    {\boldsymbol  A}=
    \begin{pmatrix}
    3 & 2 \\[1ex]
    1 & -1
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_1=
    \begin{pmatrix}
    7 & 2 \\[1ex]
    -1 & -1
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_2=
    \begin{pmatrix}
    3 & 7 \\[1ex]
    1 & -1
    \end{pmatrix}
    $$

    \begin{align*}
    \det({\boldsymbol  A})   &= 3 \cdot (-1) - 2 \cdot 1 = -5\\[1ex]
    \det({\boldsymbol  A}_1) &= 7 \cdot (-1) - 2 \cdot (-1) = -5\\[1ex]
    \det({\boldsymbol  A}_2) &= 3 \cdot (-1) - 7 \cdot 1 = -10
    \end{align*}

    Poiché $\det({\boldsymbol A}) \neq 0$:

    $$
    (\tilde{x}_1, \tilde{x}_2) = \left(\frac{-5}{-5}, \frac{-10}{-5}\right) = (1, 2).
    $$

    Verifica: $3 + 4 = 7$ e $1 - 2 = -1$ $\checkmark$

<a id="box-exe_sys_cramer_3x3-10"></a>

!!! esercizio "Esercizio 10"

    Risolvere con la regola di Cramer il sistema

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 6\\[2ex]
      1 \; x_1 - 1 \; x_2 + 2 \; x_3  & = 5\\[2ex]
      2 \; x_1 + 1 \; x_2 - 1 \; x_3  & = 1
    \end{array} \right.
    $$

??? soluzione "Soluzione"

    $$
    {\boldsymbol  A}=
    \begin{pmatrix}
    1 & 1 & 1 \\
    1 & -1 & 2 \\
    2 & 1 & -1
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_1=
    \begin{pmatrix}
    6 & 1 & 1 \\
    5 & -1 & 2 \\
    1 & 1 & -1
    \end{pmatrix}
    $$

    $$
    {\boldsymbol  A}_2=
    \begin{pmatrix}
    1 & 6 & 1 \\
    1 & 5 & 2 \\
    2 & 1 & -1
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_3=
    \begin{pmatrix}
    1 & 1 & 6 \\
    1 & -1 & 5 \\
    2 & 1 & 1
    \end{pmatrix}
    $$

    Con la regola di Sarrus:

    \begin{align*}
    \det({\boldsymbol  A})   &= 1 + 4 + 1 - (-2) - (-1) - 2 = 7\\[1ex]
    \det({\boldsymbol  A}_1) &= 6 + 2 + 5 - (-1) - (-5) - 12 = 7\\[1ex]
    \det({\boldsymbol  A}_2) &= -5 + 24 + 1 - 10 - (-6) - 2 = 14\\[1ex]
    \det({\boldsymbol  A}_3) &= -1 + 10 + 6 - (-12) - 1 - 5 = 21
    \end{align*}

    Poiché $\det({\boldsymbol A}) \neq 0$:

    $$
    (\tilde{x}_1, \tilde{x}_2, \tilde{x}_3) = \left(\frac{7}{7}, \frac{14}{7}, \frac{21}{7}\right) = (1, 2, 3).
    $$

    Verifica: $1 + 2 + 3 = 6$, $1 - 2 + 6 = 5$, $2 + 2 - 3 = 1$ $\checkmark$

<a id="box-exe_sys_lu-11"></a>

!!! esercizio "Esercizio 11"

    Data la fattorizzazione LU ${\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U}$ con

    $$
    {\boldsymbol L} =
    \begin{pmatrix}
    1 & 0 & 0 \\
    3 & 1 & 0 \\
    -1 & 2 & 1
    \end{pmatrix}
    \qquad
    {\boldsymbol U} =
    \begin{pmatrix}
    2 & 1 & -1 \\
    0 & 1 & 2 \\
    0 & 0 & 3
    \end{pmatrix},
    $$

    risolvere il sistema ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$ con ${\boldsymbol b} = (-1, 0, 13)'$.

??? soluzione "Soluzione"

    <strong>Passo 1 - Sostituzione in avanti:</strong> risolvere ${\boldsymbol L} \; {\boldsymbol y} = {\boldsymbol b}$:

    $$
    y_1 = -1,
    \qquad
    y_2 = 0 - 3 \; y_1 = 3,
    \qquad
    y_3 = 13 - (-1) \; y_1 - 2 \; y_2 = 13 - 1 - 6 = 6.
    $$

    <strong>Passo 2 - Sostituzione all'indietro:</strong> risolvere ${\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol y}$ con ${\boldsymbol y} = (-1, 3, 6)'$:

    $$
    3 \; x_3 = 6 ~\Longrightarrow~ x_3 = 2,
    \qquad
    x_2 = 3 - 2 \; x_3 = -1,
    $$

    $$
    2 \; x_1 = -1 - x_2 + x_3 = -1 + 1 + 2 = 2 ~\Longrightarrow~ x_1 = 1.
    $$

    Quindi ${\boldsymbol x} = (1, -1, 2)'$.

    <strong>Verifica:</strong>

    $$
    {\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U} =
    \begin{pmatrix}
    2 & 1 & -1 \\
    6 & 4 & -1 \\
    -2 & 1 & 8
    \end{pmatrix},
    \qquad
    {\boldsymbol A} \; {\boldsymbol x} =
    \begin{pmatrix}
    2 - 1 - 2 \\
    6 - 4 - 2 \\
    -2 - 1 + 16
    \end{pmatrix}
    =
    \begin{pmatrix}
    -1 \\
    0 \\
    13
    \end{pmatrix}
    = {\boldsymbol b} \quad \checkmark
    $$
