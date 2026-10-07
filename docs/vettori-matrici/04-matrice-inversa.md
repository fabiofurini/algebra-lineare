---
title: "Inversion of matrices"
---

# Inversion of matrices

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.3** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/vettori-matrici-04-matrice-inversa.pdf)

</div>

## 1. Computation of the inverse

!!! chiave ""

    <strong>Gauss–Jordan method (idea).</strong> To compute \( \boldsymbol A^{-1} \), we build the augmented matrix

    $$
    \left(\, \boldsymbol A \mid \boldsymbol I \,\right)
    $$

    and we apply <strong>elementary row operations</strong> to transform the left block into the identity matrix. If we obtain

    $$
    \left(\, \boldsymbol I \mid \boldsymbol B \,\right),
    $$

    then \( \boldsymbol B = \boldsymbol A^{-1} \).

<a id="box-texexpbox1-1"></a>

!!! esempio "Esempio 1: inverse matrix via Gauss–Jordan elimination"

    Let us consider

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1\\[0.5ex]
    1 & 1
    \end{pmatrix}.
    $$

    We compute the inverse matrix \(\boldsymbol A^{-1}\) with the method of Gauss–Jordan.

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

    Since the left block is the identity matrix, we obtain:

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    1 & -1\\[0.5ex]
    -1 & 2
    \end{pmatrix}.
    $$

<a id="box-texexpbox1-2"></a>

!!! esempio "Esempio 2: inverse matrix via Gauss–Jordan elimination"

    Let us consider

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 0\\[0.5ex]
    0 & 1 & 1\\[0.5ex]
    2 & 0 & 1
    \end{pmatrix}.
    $$

    We compute the inverse matrix \(\boldsymbol A^{-1}\) with the method of Gauss–Jordan.

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

    Since the left block is the identity matrix, we obtain:

    $$
    \boldsymbol A^{-1}=
    \begin{pmatrix}
    \tfrac{1}{5} & -\tfrac{2}{5} & \tfrac{2}{5}\\[0.8ex]
    \tfrac{2}{5} & \tfrac{1}{5}  & -\tfrac{1}{5}\\[0.8ex]
    -\tfrac{2}{5} & \tfrac{4}{5} & \tfrac{1}{5}
    \end{pmatrix}.
    $$
