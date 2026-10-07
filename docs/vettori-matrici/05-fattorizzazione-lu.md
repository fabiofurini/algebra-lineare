---
title: "Factorization of matrices"
---

# Factorization of matrices

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.4** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/vettori-matrici-05-fattorizzazione-lu.pdf)

</div>

## 1. LU factorization

- The LU factorization (or LU decomposition) is a fundamental matrix decomposition that expresses a matrix as the product of a lower triangular matrix and an upper triangular matrix.

!!! chiave ""

    Given a square matrix \(\boldsymbol A \in \R^{n \times n}\), a <strong>PLU factorization</strong> of \(\boldsymbol A\) is a decomposition of the form

    $$
    \boldsymbol P \boldsymbol A = \boldsymbol L \boldsymbol U,
    $$

    where:

    - \(\boldsymbol P \in \R^{n \times n}\) is a <strong>permutation matrix</strong> (it accounts for possible row swaps),

    - \(\boldsymbol L \in \R^{n \times n}\) is a <strong>lower triangular matrix</strong> with ones on the diagonal,

    - \(\boldsymbol U \in \R^{n \times n}\) is an <strong>upper triangular matrix</strong>.

- The factorization is computed by Gaussian elimination.

- If no row swaps are needed, then \(\boldsymbol P=\boldsymbol I_n\) and the factorization reduces to the <strong>LU factorization</strong>:

    $$
    \boldsymbol A=\boldsymbol L\boldsymbol U.
    $$

- The PLU/LU factorization is very useful for solving linear systems \(\boldsymbol A\boldsymbol x=\boldsymbol b\) efficiently.

!!! chiave ""

    <strong>Method to compute the PLU (LU with pivoting) factorization.</strong>

    Starting from \(\boldsymbol A\), we perform Gaussian elimination. Whenever a row swap is required, it is recorded in the permutation matrix \(\boldsymbol P\). At the end of the elimination we obtain the upper triangular matrix \(\boldsymbol U\), while \(\boldsymbol L\) stores the elimination multipliers.

    Specifically:

    - Each elimination step \(R_i \leftarrow R_i - \ell_{ij} R_j\) (with \(i>j\)) creates a zero in position \((i,j)\).

    - The multiplier \(\ell_{ij}\) is stored in position \((i,j)\) of \(\boldsymbol L\).

    - The diagonal of \(\boldsymbol L\) is filled with ones.

<a id="box-texexpbox1-1"></a>

!!! esempio "Esempio 1: LU factorization"

    Let us compute the LU factorization of

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1 & 1\\
    4 & -6 & 0\\
    -2 & 7 & 2
    \end{pmatrix}.
    $$

    <strong>Step 1:</strong> Eliminate the entries below the first pivot \(a_{11} = 2\).

    We need to eliminate \(a_{21} = 4\). The multiplier is:

    $$
    \ell_{21} = \frac{a_{21}}{a_{11}} = \frac{4}{2} = 2.
    $$

    We perform \(R_2 \leftarrow R_2 - 2R_1\):

    $$
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & -8 & -2\\
    -2 & 7 & 2
    \end{pmatrix}.
    $$

    We need to eliminate \(a_{31} = -2\). The multiplier is:

    $$
    \ell_{31} = \frac{a_{31}}{a_{11}} = \frac{-2}{2} = -1.
    $$

    We perform \(R_3 \leftarrow R_3 - (-1)R_1 = R_3 + R_1\):

    $$
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & -8 & -2\\
    0 & 8 & 3
    \end{pmatrix}.
    $$

    <strong>Step 2:</strong> Eliminate the entries below the second pivot \(-8\).

    We need to eliminate the entry in position \((3,2)\), which is currently 8. The multiplier is:

    $$
    \ell_{32} = \frac{8}{-8} = -1.
    $$

    We perform \(R_3 \leftarrow R_3 - (-1)R_2 = R_3 + R_2\):

    $$
    \boldsymbol U = 
    \begin{pmatrix}
    2 & 1 & 1\\
    0 & -8 & -2\\
    0 & 0 & 1
    \end{pmatrix}.
    $$

<a id="box-texexpbox1-2"></a>

!!! esempio "Esempio 2: LU factorization"

    <strong>Step 3:</strong> Build the matrix \(\boldsymbol L\).

    The matrix \(\boldsymbol L\) has ones on the diagonal and the multipliers below the diagonal:

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

    <strong>Verification:</strong> We check that \(\boldsymbol L \boldsymbol U = \boldsymbol A\):

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

<a id="box-texexpbox1-3"></a>

!!! esempio "Esempio 3: PLU factorization with row permutation"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 1\\
    1 & 1
    \end{pmatrix}.
    $$

    Since \(a_{11} = 0\), we cannot use it as a pivot. We need to swap rows 1 and 2.

    Let

    $$
    \boldsymbol P=
    \begin{pmatrix}
    0 & 1\\
    1 & 0
    \end{pmatrix}
    $$

    be the permutation matrix that swaps rows 1 and 2.

    Then:

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

    Now \(\boldsymbol{PA}\) already has an upper triangular form (no elimination needed below the diagonal), so:

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

    Therefore, the PLU factorization is:

    $$
    \boldsymbol{PA} = \boldsymbol L \boldsymbol U,
    $$

    where \(\boldsymbol P = \begin{pmatrix}0 & 1\\1 & 0\end{pmatrix}\), \(\boldsymbol L = \boldsymbol I\), and \(\boldsymbol U = \begin{pmatrix}1 & 1\\0 & 1\end{pmatrix}\).
