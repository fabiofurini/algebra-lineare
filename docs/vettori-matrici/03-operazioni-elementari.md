---
title: "Matrix operations"
---

# Matrix operations

<div class="info-capitolo" markdown>

**Vettori e matrici · Capitolo 4.2** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/vettori-matrici-03-operazioni-elementari.pdf)

</div>

## 1. Elementary row and column operations

- Elementary row and column operations are fundamental tools in linear algebra. They are used in many algorithms, including Gaussian elimination, computation of the inverse matrix, and matrix factorizations (such as the LU decomposition)

!!! chiave ""

    Given a matrix \(\boldsymbol A \in \R^{m \times n}\), the <strong>elementary row operations</strong> are:

    1. <strong>Row swap:</strong> Exchange rows \(i\) and \(k\).

        $$
        R_i \leftrightarrow R_k
        $$

    2. <strong>Row scaling:</strong> Multiply row \(i\) by a nonzero scalar \(\lambda \neq 0\).

        $$
        R_i \leftarrow \lambda R_i
        $$

    3. <strong>Row addition:</strong> Replace row \(i\) by the sum of row \(i\) and \(\lambda\) times row \(k\) (with \(i \neq k\)).

        $$
        R_i \leftarrow R_i + \lambda R_k
        $$

<a id="box-texexpbox1-1"></a>

!!! esempio "Esempio 1: Row swap"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    After swapping rows 1 and 3, i.e., \(R_1 \leftrightarrow R_3\), we obtain:

    $$
    \begin{pmatrix}
    7 & 8 & 9\\
    4 & 5 & 6\\
    1 & 2 & 3
    \end{pmatrix}.
    $$

<a id="box-texexpbox1-2"></a>

!!! esempio "Esempio 2: Row scaling"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    After multiplying row 2 by \(\lambda = -2\), i.e., \(R_2 \leftarrow -2R_2\), we obtain:

    $$
    \begin{pmatrix}
    1 & 2 & 3\\
    -8 & -10 & -12\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

<a id="box-texexpbox1-3"></a>

!!! esempio "Esempio 3: Row addition"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    After replacing row 2 with row 2 minus 4 times row 1, i.e., \(R_2 \leftarrow R_2 - 4R_1\), we obtain:

    $$
    \begin{pmatrix}
    1 & 2 & 3\\
    0 & -3 & -6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    Indeed:

    $$
    \begin{pmatrix}4 \\ 5 \\ 6\end{pmatrix} - 4\begin{pmatrix}1 \\ 2 \\ 3\end{pmatrix} = \begin{pmatrix}0 \\ -3 \\ -6\end{pmatrix}.
    $$

!!! chiave ""

    Given a matrix \(\boldsymbol A \in \R^{m \times n}\), the <strong>elementary column operations</strong> are:

    1. <strong>Column swap:</strong> Exchange columns \(j\) and \(k\).

        $$
        C_j \leftrightarrow C_k
        $$

    2. <strong>Column scaling:</strong> Multiply column \(j\) by a nonzero scalar \(\lambda \neq 0\).

        $$
        C_j \leftarrow \lambda C_j
        $$

    3. <strong>Column addition:</strong> Replace column \(j\) by the sum of column \(j\) and \(\lambda\) times column \(k\) (with \(j \neq k\)).

        $$
        C_j \leftarrow C_j + \lambda C_k
        $$

<a id="box-texexpbox1-4"></a>

!!! esempio "Esempio 4: Column swap"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    After swapping columns 1 and 3, i.e., \(C_1 \leftrightarrow C_3\), we obtain:

    $$
    \begin{pmatrix}
    3 & 2 & 1\\
    6 & 5 & 4\\
    9 & 8 & 7
    \end{pmatrix}.
    $$

<a id="box-texexpbox1-5"></a>

!!! esempio "Esempio 5: Column scaling"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    After multiplying column 2 by \(\lambda = 3\), i.e., \(C_2 \leftarrow 3C_2\), we obtain:

    $$
    \begin{pmatrix}
    1 & 6 & 3\\
    4 & 15 & 6\\
    7 & 24 & 9
    \end{pmatrix}.
    $$

<a id="box-texexpbox1-6"></a>

!!! esempio "Esempio 6: Column addition"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 3\\
    4 & 5 & 6\\
    7 & 8 & 9
    \end{pmatrix}.
    $$

    After replacing column 3 with column 3 plus 2 times column 1, i.e., \(C_3 \leftarrow C_3 + 2C_1\), we obtain:

    $$
    \begin{pmatrix}
    1 & 2 & 5\\
    4 & 5 & 14\\
    7 & 8 & 23
    \end{pmatrix}.
    $$

    Indeed:

    $$
    \begin{pmatrix}3 \\ 6 \\ 9\end{pmatrix} + 2\begin{pmatrix}1 \\ 4 \\ 7\end{pmatrix} = \begin{pmatrix}5 \\ 14 \\ 23\end{pmatrix}.
    $$

## 2. Effect of elementary operations on the determinant

!!! chiave ""

    Let \(\boldsymbol A \in \R^{n \times n}\) be a square matrix. The elementary row operations affect the determinant as follows:

    1. <strong>Row swap:</strong> \(R_i \leftrightarrow R_k\) changes the sign of the determinant.

        $$
        \det(\text{new matrix}) = -\det(\boldsymbol A)
        $$

    2. <strong>Row scaling:</strong> \(R_i \leftarrow \lambda R_i\) (with \(\lambda \neq 0\)) multiplies the determinant by \(\lambda\).

        $$
        \det(\text{new matrix}) = \lambda \det(\boldsymbol A)
        $$

    3. <strong>Row addition:</strong> \(R_i \leftarrow R_i + \lambda R_k\) (with \(i \neq k\)) does not change the determinant.

        $$
        \det(\text{new matrix}) = \det(\boldsymbol A)
        $$

<a id="box-texexpbox1-7"></a>

!!! esempio "Esempio 7: Effect of row swap on determinant"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    The determinant is:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    After swapping rows 1 and 2, i.e., \(R_1 \leftrightarrow R_2\), we obtain:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    3 & 4\\
    1 & 2
    \end{pmatrix}.
    $$

    The determinant of the new matrix is:

    $$
    \det(\boldsymbol A') = 3 \cdot 2 - 4 \cdot 1 = 2 = -\det(\boldsymbol A).
    $$

<a id="box-texexpbox1-8"></a>

!!! esempio "Esempio 8: Effect of row scaling on determinant"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    2 & 1\\
    0 & 3
    \end{pmatrix}.
    $$

    The determinant is:

    $$
    \det(\boldsymbol A) = 2 \cdot 3 - 1 \cdot 0 = 6.
    $$

    After multiplying row 1 by \(\lambda = 2\), i.e., \(R_1 \leftarrow 2R_1\), we obtain:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    4 & 2\\
    0 & 3
    \end{pmatrix}.
    $$

    The determinant of the new matrix is:

    $$
    \det(\boldsymbol A') = 4 \cdot 3 - 2 \cdot 0 = 12 = 2 \cdot \det(\boldsymbol A) = \lambda \det(\boldsymbol A).
    $$

<a id="box-texexpbox1-9"></a>

!!! esempio "Esempio 9: Effect of row addition on determinant"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    The determinant is:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    After replacing row 2 with row 2 minus 3 times row 1, i.e., \(R_2 \leftarrow R_2 - 3R_1\), we obtain:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 2\\
    0 & -2
    \end{pmatrix}.
    $$

    The determinant of the new matrix is:

    $$
    \det(\boldsymbol A') = 1 \cdot (-2) - 2 \cdot 0 = -2 = \det(\boldsymbol A).
    $$

!!! chiave ""

    Let \(\boldsymbol A \in \R^{n \times n}\) be a square matrix. The elementary column operations affect the determinant as follows:

    1. <strong>Column swap:</strong> \(C_j \leftrightarrow C_k\) changes the sign of the determinant.

        $$
        \det(\text{new matrix}) = -\det(\boldsymbol A)
        $$

    2. <strong>Column scaling:</strong> \(C_j \leftarrow \lambda C_j\) (with \(\lambda \neq 0\)) multiplies the determinant by \(\lambda\).

        $$
        \det(\text{new matrix}) = \lambda \det(\boldsymbol A)
        $$

    3. <strong>Column addition:</strong> \(C_j \leftarrow C_j + \lambda C_k\) (with \(j \neq k\)) does not change the determinant.

        $$
        \det(\text{new matrix}) = \det(\boldsymbol A)
        $$

<a id="box-texexpbox1-10"></a>

!!! esempio "Esempio 10: Effect of column swap on determinant"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    The determinant is:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    After swapping columns 1 and 2, i.e., \(C_1 \leftrightarrow C_2\), we obtain:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    2 & 1\\
    4 & 3
    \end{pmatrix}.
    $$

    The determinant of the new matrix is:

    $$
    \det(\boldsymbol A') = 2 \cdot 3 - 1 \cdot 4 = 2 = -\det(\boldsymbol A).
    $$

<a id="box-texexpbox1-11"></a>

!!! esempio "Esempio 11: Effect of column scaling on determinant"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    The determinant is:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    After multiplying column 2 by \(\lambda = 3\), i.e., \(C_2 \leftarrow 3C_2\), we obtain:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 6\\
    3 & 12
    \end{pmatrix}.
    $$

    The determinant of the new matrix is:

    $$
    \det(\boldsymbol A') = 1 \cdot 12 - 6 \cdot 3 = -6 = 3 \cdot (-2) = \lambda \det(\boldsymbol A).
    $$

<a id="box-texexpbox1-12"></a>

!!! esempio "Esempio 12: Effect of column addition on determinant"

    Consider the matrix

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2\\
    3 & 4
    \end{pmatrix}.
    $$

    The determinant is:

    $$
    \det(\boldsymbol A) = 1 \cdot 4 - 2 \cdot 3 = -2.
    $$

    After replacing column 2 with column 2 plus 2 times column 1, i.e., \(C_2 \leftarrow C_2 + 2C_1\), we obtain:

    $$
    \boldsymbol A'=
    \begin{pmatrix}
    1 & 4\\
    3 & 10
    \end{pmatrix}.
    $$

    The determinant of the new matrix is:

    $$
    \det(\boldsymbol A') = 1 \cdot 10 - 4 \cdot 3 = -2 = \det(\boldsymbol A).
    $$

- These properties follow from the fact that \(\det(\boldsymbol A') = \det(\boldsymbol A)\), so column operations have the same effect on the determinant as the corresponding row operations.

- These results are fundamental for understanding how determinants behave under elementary operations, which is crucial in algorithms such as Gaussian elimination and matrix factorization.

## 3. Pivoting and partial pivoting

- In numerical algorithms such as matrix factorizations and row reduction methods, pivoting is a technique used to improve numerical stability and avoid division by zero.

- The pivot element is the element used as the divisor in the elimination process.

### 3.1 Pivoting

!!! chiave ""

    <strong>Pivoting</strong> is the process of selecting a suitable pivot element in a matrix to perform elimination steps in row reduction algorithms.

    When performing row elimination on a matrix \(\boldsymbol A \in \R^{n \times n}\), at step \(k\):

    - The <strong>pivot element</strong> is the entry \(a_{kk}\) (the diagonal element in position \((k,k)\)).

    - If \(a_{kk} = 0\), we cannot use it as a divisor, so we must swap row \(k\) with a row \(i > k\) such that \(a_{ik} \neq 0\).

    - This row swap is called <strong>pivoting</strong>.

<a id="box-texexpbox1-13"></a>

!!! esempio "Esempio 13: Pivoting in row elimination"

    Consider the matrix:

    $$
    \boldsymbol A=
    \begin{pmatrix}
    0 & 2 & 1\\
    1 & -1 & 0\\
    2 & 1 & 3
    \end{pmatrix}.
    $$

    We cannot use \(a_{11} = 0\) as the first pivot. We need to swap row 1 with a row that has a nonzero element in the first column.

    We swap rows 1 and 2 (i.e., \(R_1 \leftrightarrow R_2\)):

    $$
    \begin{pmatrix}
    1 & -1 & 0\\
    0 & 2 & 1\\
    2 & 1 & 3
    \end{pmatrix}.
    $$

    Now \(a_{11} = 1 \neq 0\) and we can proceed with the elimination:

    $$
    R_3 \leftarrow R_3 - 2R_1:
    \quad
    \begin{pmatrix}
    1 & -1 & 0\\
    0 & 2 & 1\\
    0 & 3 & 3
    \end{pmatrix}.
    $$

    Now we use \(a_{22} = 2\) as the second pivot:

    $$
    R_3 \leftarrow R_3 - \frac{3}{2}R_2:
    \quad
    \begin{pmatrix}
    1 & -1 & 0\\[0.5ex]
    0 & 2 & 1\\[0.5ex]
    0 & 0 & \frac{3}{2}
    \end{pmatrix}.
    $$

    The matrix is now in upper triangular form.

### 3.2 Partial pivoting

!!! chiave ""

    <strong>Partial pivoting</strong> is a strategy to improve numerical stability by choosing the largest available pivot in absolute value.

    At step \(k\) of Gaussian elimination:

    1. Find the row \(i \ge k\) such that \(|a_{ik}|\) is maximum among all \(|a_{jk}|\) for \(j \ge k\).

    2. Swap row \(k\) with row \(i\) (i.e., \(R_k \leftrightarrow R_i\)).

    3. Use the new \(a_{kk}\) as the pivot.

    This ensures that:

    - The pivot is the largest element in absolute value in its column (below the diagonal).

    - Division by a larger number reduces round-off errors in floating-point arithmetic.

    - The method is numerically more stable.

<a id="box-texexpbox1-14"></a>

!!! esempio "Esempio 14: Partial pivoting in row elimination"

    Consider the matrix:

    $$
    \boldsymbol A=
    \begin{pmatrix}
    1 & 2 & 1\\
    3 & -1 & 2\\
    2 & 3 & -1
    \end{pmatrix}.
    $$

    <strong>Step 1:</strong> Find the largest element in absolute value in the first column.

    $$
    |a_{11}| = 1, \quad |a_{21}| = 3, \quad |a_{31}| = 2.
    $$

    The maximum is \(|a_{21}| = 3\), so we swap rows 1 and 2:

    $$
    R_1 \leftrightarrow R_2:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\
    1 & 2 & 1\\
    2 & 3 & -1
    \end{pmatrix}.
    $$

    Now eliminate below the pivot \(a_{11} = 3\):

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

    <strong>Step 2:</strong> Find the largest element in absolute value in the second column (rows 2 and 3).

    $$
    \left|\frac{7}{3}\right| = \frac{7}{3}, 
    \quad 
    \left|\frac{11}{3}\right| = \frac{11}{3}.
    $$

    The maximum is \(\left|\frac{11}{3}\right|\), so we swap rows 2 and 3:

    $$
    R_2 \leftrightarrow R_3:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\[0.5ex]
    0 & \frac{11}{3} & -\frac{7}{3}\\[0.5ex]
    0 & \frac{7}{3} & \frac{1}{3}
    \end{pmatrix}.
    $$

    Eliminate below the pivot \(a_{22} = \frac{11}{3}\):

    $$
    R_3 \leftarrow R_3 - \frac{7}{11}R_2:
    \quad
    \begin{pmatrix}
    3 & -1 & 2\\[0.5ex]
    0 & \frac{11}{3} & -\frac{7}{3}\\[0.5ex]
    0 & 0 & \frac{18}{11}
    \end{pmatrix}.
    $$

    The matrix is now in upper triangular form (row echelon form).

<a id="box-texexpbox1-15"></a>

!!! esempio "Esempio 15: Comparison: without and with partial pivoting"

    Consider the matrix:

    $$
    \boldsymbol A =
    \begin{pmatrix}
    \frac{1}{10000} & 1\\
    1 & 1
    \end{pmatrix}.
    $$

    <strong>Without partial pivoting:</strong>

    Using \(a_{11} = \frac{1}{10000}\) as the pivot:

    $$
    R_2 \leftarrow R_2 - 10000\,R_1.
    $$

    This gives:

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

    The large multiplier \(10000\) can cause significant round-off errors in floating-point arithmetic.

    <strong>With partial pivoting:</strong>

    Since \(|a_{21}| = 1 > |a_{11}| = \frac{1}{10000}\), we swap rows:

    $$
    R_1 \leftrightarrow R_2:
    \quad
    \begin{pmatrix}
    1 & 1\\
    \frac{1}{10000} & 1
    \end{pmatrix}.
    $$

    Now eliminate using \(a_{11} = 1\) as the pivot:

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

    The multiplier \(\frac{1}{10000}\) is much smaller, leading to better numerical stability.

- Partial pivoting is crucial in numerical linear algebra to ensure that algorithms produce accurate results, especially when dealing with matrices that have a wide range of magnitudes.

- Most modern numerical software (such as MATLAB, NumPy, CPLEX, Gurobi) automatically uses partial pivoting in Gaussian elimination and LU factorization.

- The computational cost of partial pivoting is minimal compared to the benefit of improved numerical stability.
