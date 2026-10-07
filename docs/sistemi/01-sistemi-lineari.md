---
title: "System of linear equations"
---

# System of linear equations

<div class="info-capitolo" markdown>

**Sistemi lineari · Capitolo 6** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/sistemi-01-sistemi-lineari.pdf)

</div>

## 1. Existence and uniqueness of solutions

!!! chiave ""

    Consider a system of $m$ linear equations with $n$ variables:

    $$
    {\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}
    $$

    where:

    - ${\boldsymbol A} \in \R^{m \times n}$ is the coefficient matrix ($m$ equations, $n$ variables)

    - ${\boldsymbol x} \in \R^{n \times 1}$ is the vector of variables

    - ${\boldsymbol b} \in \R^{m \times 1}$ is the right-hand side vector

    - $({\boldsymbol A} | {\boldsymbol b}) \in \R^{m \times (n+1)}$ is the augmented matrix

    The existence and uniqueness of solutions to the system ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$ depend on the rank of the coefficient matrix ${\boldsymbol A}$ and the rank of the augmented matrix $({\boldsymbol A} | {\boldsymbol b})$.

    <strong>Case 1 - No solution (inconsistent system):</strong>

    $$
    \text{rank}({\boldsymbol A}) < \text{rank}({\boldsymbol A} | {\boldsymbol b})
    $$

    The system is inconsistent and has no solution.

    <strong>Case 2 - Unique solution:</strong>

    $$
    \text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = n
    $$

    The system has a unique solution.

    <strong>Case 3 - Infinite solutions:</strong>

    $$
    \text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) < n
    $$

    The system has infinitely many solutions with $n - \text{rank}({\boldsymbol A})$ degrees of freedom (free variables).

## 2. Gaussian Elimination Method

!!! chiave ""

    The <strong>Gaussian elimination method</strong> is an algorithm for solving systems of linear equations by transforming the augmented matrix $({\boldsymbol A} | {\boldsymbol b})$ into <strong>row echelon form</strong> (upper triangular form) through elementary row operations.

- Given the system of linear equations:

    $$
    {\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}
    $$

    we form the <strong>augmented matrix</strong>:

    $$
    ({\boldsymbol A} | {\boldsymbol b})
    $$

- The method consists of two phases:

    <strong>Phase 1 - Forward elimination:</strong> Transform the augmented matrix into upper triangular form using elementary row operations:

    - Swap two rows

    - Multiply a row by a non-zero scalar

    - Add a multiple of one row to another row

    The goal is to create zeros below the diagonal, obtaining:

    $$
    \left(\begin{array}{cccc|c}
    \tilde{a}_{11} & \tilde{a}_{12} & \cdots & \tilde{a}_{1n} & \tilde{b}_1 \\
    0 & \tilde{a}_{22} & \cdots & \tilde{a}_{2n} & \tilde{b}_2 \\
    \vdots & \vdots & \ddots & \vdots & \vdots \\
    0 & 0 & \cdots & \tilde{a}_{nn} & \tilde{b}_n
    \end{array}\right)
    $$

    <strong>Phase 2 - Backward substitution:</strong> Solve the upper triangular system from bottom to top:

    \begin{align*}
    x_n &= \frac{\tilde{b}_n}{\tilde{a}_{nn}}\\
    x_{n-1} &= \frac{\tilde{b}_{n-1} - \tilde{a}_{n-1,n} \; x_n}{\tilde{a}_{n-1,n-1}}\\
    &\vdots\\
    x_i &= \frac{\tilde{b}_i - \sum_{j=i+1}^{n} \tilde{a}_{ij} \; x_j}{\tilde{a}_{ii}}
    \end{align*}

!!! chiave ""

    <strong>Elementary row operations:</strong>

    - $R_i \leftrightarrow R_j$ : swap row $i$ with row $j$

    - $R_i \leftarrow k \; R_i$ : multiply row $i$ by scalar $k \neq 0$

    - $R_i \leftarrow R_i + k \; R_j$ : add $k$ times row $j$ to row $i$

    These operations do not change the solution set of the system.

<a id="box-texexpbox1a-1"></a>

!!! esempio "Esempio 1: Solving a system using Gaussian elimination - Part 1"

    Consider the system of linear equations:

    $$
    \left\{ \begin{array}{ll}
      2 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      4 \; x_1 + 3 \; x_2 + 3 \; x_3  & = 10\\[2ex]
      8 \; x_1 + 7 \; x_2 + 9 \; x_3  & = 24
    \end{array} \right.
    $$

    <strong>Augmented matrix:</strong>

    $$
    ({\boldsymbol A} | {\boldsymbol b}) = 
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    4 & 3 & 3 & 10 \\
    8 & 7 & 9 & 24
    \end{array}\right)
    $$

    <strong>Step 1:</strong> Eliminate $x_1$ from rows 2 and 3

    $R_2 \leftarrow R_2 - 2 \; R_1$ (subtract $2$ times row 1 from row 2):

    $$
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    0 & 1 & 1 & 2 \\
    8 & 7 & 9 & 24
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - 4 \; R_1$ (subtract $4$ times row 1 from row 3):

    $$
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    0 & 1 & 1 & 2 \\
    0 & 3 & 5 & 8
    \end{array}\right)
    $$

    <strong>Step 2:</strong> Eliminate $x_2$ from row 3

    $R_3 \leftarrow R_3 - 3 \; R_2$ (subtract $3$ times row 2 from row 3):

    $$
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    0 & 1 & 1 & 2 \\
    0 & 0 & 2 & 2
    \end{array}\right)
    $$

    <strong>Upper triangular form achieved!</strong> The corresponding system is:

    $$
    \left\{ \begin{array}{ll}
      2 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      1 \; x_2 + 1 \; x_3  & = 2\\[2ex]
      2 \; x_3  & = 2
    \end{array} \right.
    $$

<a id="box-texexpbox1c-2"></a>

!!! esempio "Esempio 2: Solving a system using Gaussian elimination - Part 2"

    <strong>Backward substitution:</strong>

    From the third equation:

    $$
    2 \; x_3 = 2 ~~\Longrightarrow~~ x_3 = 1
    $$

    From the second equation:

    $$
    x_2 + x_3 = 2 ~~\Longrightarrow~~ x_2 = 2 - x_3 = 2 - 1 = 1
    $$

    From the first equation:

    $$
    2 \; x_1 + x_2 + x_3 = 4 ~~\Longrightarrow~~ 2 \; x_1 = 4 - x_2 - x_3 = 4 - 1 - 1 = 2 ~~\Longrightarrow~~ x_1 = 1
    $$

    <strong>Solution:</strong>

    $$
    {\boldsymbol x} = 
    \begin{pmatrix}
    x_1 \\
    x_2 \\
    x_3
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 \\
    1 \\
    1
    \end{pmatrix}
    $$

    <strong>Verification:</strong>

    $$
    {\boldsymbol A} \; {\boldsymbol x} = 
    \begin{pmatrix}
    2 & 1 & 1 \\
    4 & 3 & 3 \\
    8 & 7 & 9
    \end{pmatrix}
    \begin{pmatrix}
    1 \\
    1 \\
    1
    \end{pmatrix}
    =
    \begin{pmatrix}
    2+1+1 \\
    4+3+3 \\
    8+7+9
    \end{pmatrix}
    =
    \begin{pmatrix}
    4 \\
    10 \\
    24
    \end{pmatrix}
    = {\boldsymbol b} \quad \checkmark
    $$

## 3. LU Factorization Method

!!! chiave ""

    The <strong>LU factorization</strong> (or <strong>LU decomposition</strong>) is a method for solving systems of linear equations by decomposing the coefficient matrix ${\boldsymbol A}$ into the product of two triangular matrices:

    $$
    {\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U}
    $$

    where ${\boldsymbol L}$ is a <strong>lower triangular matrix</strong> (with 1's on the diagonal) and ${\boldsymbol U}$ is an <strong>upper triangular matrix</strong>.

- Given the system of linear equations:

    $$
    {\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}
    $$

    if we have the LU factorization ${\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U}$, we can substitute:

    $$
    {\boldsymbol L} \; {\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol b}
    $$

- We introduce the <strong>auxiliary variable</strong> ${\boldsymbol y}$ defined as:

    $$
    {\boldsymbol y} \;:=\; {\boldsymbol U} \; {\boldsymbol x}
    $$

    so that ${\boldsymbol L} \; {\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol b}$ becomes ${\boldsymbol L} \; {\boldsymbol y} = {\boldsymbol b}$.

    <strong>Why does this work?</strong>  We are splitting the original system ${\boldsymbol A}\,{\boldsymbol x}={\boldsymbol b}$ into two simpler triangular systems:

    1. Find ${\boldsymbol y}$ such that ${\boldsymbol L}\,{\boldsymbol y} = {\boldsymbol b}$.

    2. Find ${\boldsymbol x}$ such that ${\boldsymbol U}\,{\boldsymbol x} = {\boldsymbol y}$.

    If both steps succeed, then ${\boldsymbol A}\,{\boldsymbol x} = {\boldsymbol L}\,{\boldsymbol U}\,{\boldsymbol x} = {\boldsymbol L}\,{\boldsymbol y} = {\boldsymbol b}$, so ${\boldsymbol x}$ is indeed a solution of the original system. Since both ${\boldsymbol L}$ and ${\boldsymbol U}$ are triangular, each of the two systems can be solved in $O(n^2)$ operations by simple substitution.

- We then solve the system in two steps:

    <strong>Step 1 - Forward substitution:</strong> Solve ${\boldsymbol L} \; {\boldsymbol y} = {\boldsymbol b}$ for ${\boldsymbol y}$

    Since ${\boldsymbol L}$ is lower triangular, we can solve this system easily from top to bottom:

    \begin{align*}
    y_1 &= b_1\\
    y_2 &= b_2 - \ell_{21} \; y_1\\
    y_3 &= b_3 - \ell_{31} \; y_1 - \ell_{32} \; y_2\\
    &\vdots\\
    y_i &= b_i - \sum_{j=1}^{i-1} \ell_{ij} \; y_j
    \end{align*}

    <strong>Step 2 - Backward substitution:</strong> Solve ${\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol y}$ for ${\boldsymbol x}$

    Since ${\boldsymbol U}$ is upper triangular, we can solve this system easily from bottom to top:

    \begin{align*}
    x_n &= \frac{y_n}{u_{nn}}\\
    x_{n-1} &= \frac{y_{n-1} - u_{n-1,n} \; x_n}{u_{n-1,n-1}}\\
    &\vdots\\
    x_i &= \frac{y_i - \sum_{j=i+1}^{n} u_{ij} \; x_j}{u_{ii}}
    \end{align*}

!!! chiave ""

    <strong>Advantages of LU factorization:</strong>

    - Once the factorization ${\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U}$ is computed, we can solve the system for different right-hand sides ${\boldsymbol b}$ efficiently

    - Both forward and backward substitution require only $O(n^2)$ operations

    - The factorization itself requires $O(n^3)$ operations, but it needs to be done only once

<a id="box-texexpbox2a-3"></a>

!!! esempio "Esempio 3: Solving a system using LU factorization - Part 1"

    Consider the system of linear equations:

    $$
    \left\{ \begin{array}{ll}
      2 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      4 \; x_1 + 3 \; x_2 + 3 \; x_3  & = 10\\[2ex]
      8 \; x_1 + 7 \; x_2 + 9 \; x_3  & = 24
    \end{array} \right.
    $$

    In matrix form: ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$ where

    $$
    {\boldsymbol A} = 
    \begin{pmatrix}
    2 & 1 & 1 \\
    4 & 3 & 3 \\
    8 & 7 & 9
    \end{pmatrix}
    \qquad
    {\boldsymbol b} = 
    \begin{pmatrix}
    4 \\
    10 \\
    24
    \end{pmatrix}
    $$

    <strong>Given</strong> the LU factorization of ${\boldsymbol A}$:

    $$
    {\boldsymbol L} = 
    \begin{pmatrix}
    1 & 0 & 0 \\
    2 & 1 & 0 \\
    4 & 3 & 1
    \end{pmatrix}
    \qquad
    {\boldsymbol U} = 
    \begin{pmatrix}
    2 & 1 & 1 \\
    0 & 1 & 1 \\
    0 & 0 & 2
    \end{pmatrix}
    $$

    <strong>Verification:</strong>

    $$
    {\boldsymbol L} \; {\boldsymbol U} = 
    \begin{pmatrix}
    1 & 0 & 0 \\
    2 & 1 & 0 \\
    4 & 3 & 1
    \end{pmatrix}
    \begin{pmatrix}
    2 & 1 & 1 \\
    0 & 1 & 1 \\
    0 & 0 & 2
    \end{pmatrix}
    =
    \begin{pmatrix}
    2 & 1 & 1 \\
    4 & 3 & 3 \\
    8 & 7 & 9
    \end{pmatrix}
    = {\boldsymbol A} \quad \checkmark
    $$

<a id="box-texexpbox2b-4"></a>

!!! esempio "Esempio 4: Solving a system using LU factorization - Part 2"

    <strong>Step 1 - Forward substitution:</strong> Solve ${\boldsymbol L} \; {\boldsymbol y} = {\boldsymbol b}$

    $$
    \begin{pmatrix}
    1 & 0 & 0 \\
    2 & 1 & 0 \\
    4 & 3 & 1
    \end{pmatrix}
    \begin{pmatrix}
    y_1 \\
    y_2 \\
    y_3
    \end{pmatrix}
    =
    \begin{pmatrix}
    4 \\
    10 \\
    24
    \end{pmatrix}
    $$

    From the first equation:

    $$
    y_1 = 4
    $$

    From the second equation:

    $$
    2 \; y_1 + y_2 = 10 ~~\Longrightarrow~~ y_2 = 10 - 2 \cdot 4 = 10 - 8 = 2
    $$

    From the third equation:

    $$
    4 \; y_1 + 3 \; y_2 + y_3 = 24 ~~\Longrightarrow~~ y_3 = 24 - 4 \cdot 4 - 3 \cdot 2 = 24 - 16 - 6 = 2
    $$

    Thus:

    $$
    {\boldsymbol y} = 
    \begin{pmatrix}
    4 \\
    2 \\
    2
    \end{pmatrix}
    $$

    <strong>Step 2 - Backward substitution:</strong> Solve ${\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol y}$

    $$
    \begin{pmatrix}
    2 & 1 & 1 \\
    0 & 1 & 1 \\
    0 & 0 & 2
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\
    x_2 \\
    x_3
    \end{pmatrix}
    =
    \begin{pmatrix}
    4 \\
    2 \\
    2
    \end{pmatrix}
    $$

    From the third equation:

    $$
    2 \; x_3 = 2 ~~\Longrightarrow~~ x_3 = 1
    $$

    From the second equation:

    $$
    x_2 + x_3 = 2 ~~\Longrightarrow~~ x_2 = 2 - 1 = 1
    $$

    From the first equation:

    $$
    2 \; x_1 + x_2 + x_3 = 4 ~~\Longrightarrow~~ 2 \; x_1 = 4 - 1 - 1 = 2 ~~\Longrightarrow~~ x_1 = 1
    $$

    <strong>Solution:</strong>

    $$
    {\boldsymbol x} = 
    \begin{pmatrix}
    x_1 \\
    x_2 \\
    x_3
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 \\
    1 \\
    1
    \end{pmatrix}
    $$

    <strong>Verification:</strong>

    $$
    {\boldsymbol A} \; {\boldsymbol x} = 
    \begin{pmatrix}
    2 & 1 & 1 \\
    4 & 3 & 3 \\
    8 & 7 & 9
    \end{pmatrix}
    \begin{pmatrix}
    1 \\
    1 \\
    1
    \end{pmatrix}
    =
    \begin{pmatrix}
    2+1+1 \\
    4+3+3 \\
    8+7+9
    \end{pmatrix}
    =
    \begin{pmatrix}
    4 \\
    10 \\
    24
    \end{pmatrix}
    = {\boldsymbol b} \quad \checkmark
    $$

## 4. Cramer's rule

!!! chiave ""

    Cramer's rule is an explicit formula for the solution of a system of $m$ linear equations with $m$ variables (valid whenever the system has a unique solution).

- Given a column vector ${\boldsymbol  b} \in \mathbb{\R}^{m \times 1}$ of $m$ rows, a matrix ${\boldsymbol  A } \in \mathbb{\R}^{m \times m}$ of $m$ rows and $m$ columns and a column vector ${\boldsymbol  x} \in \R^{m \times 1}$ of $m$ rows containing the $m$ variables:

    $$
    {\boldsymbol  A}=
    \begin{pmatrix}
    a_{11} & a_{12} & \dots & a_{1m}\\
    a_{21} & a_{22} & \dots & a_{2m}\\
    \vdots  & \vdots  & \dots & \vdots \\
    a_{m1} & a_{m2} & \dots & a_{mm}\\
    \end{pmatrix}
    \qquad
    {\boldsymbol  b}=
    \begin{pmatrix}
    b_{1} \\
    b_{2} \\
    \vdots  \\
    b_{n} \\
    \end{pmatrix}
    \qquad
    {\boldsymbol  x}=
    \begin{pmatrix}
    x_{1} \\
    x_{2} \\
    \vdots  \\
    x_{n} \\
    \end{pmatrix}
    $$

    if $\det({\boldsymbol  A}) \neq 0$, the solution ${\tilde{\boldsymbol  x}}$ of the system of $m$ linear equations:

    $$
    {\boldsymbol  A} \; {\boldsymbol  x}= {\boldsymbol  b}
    $$

    is given by the formula:

    \begin{equation}
    \label{CCCC}
    \tilde{x}_j = \frac{\det({\boldsymbol  A}_j) }{\det({\boldsymbol  A})},~~~~~ \forall j \in \{1,2,\dots,m\}
    \end{equation}

    where ${\boldsymbol  A}_j$ is the matrix formed by replacing the $j$-th column of ${\boldsymbol  A}$ by the column vector ${\boldsymbol  b}$.

### 4.1 Systems of two equations and two variables

!!! chiave ""

    With $m=2$, we have:

    $$
    {\boldsymbol  A}=
    \begin{pmatrix}
    a_{11} & a_{12} \\[1ex]
    a_{21} & a_{22} 
    \end{pmatrix}
    \qquad
    {\boldsymbol  b}=
    \begin{pmatrix}
    b_{1} \\[1ex]
    b_{2} 
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_1=
    \begin{pmatrix}
    b_{1} & a_{12} \\[1ex]
    b_{2} & a_{22} 
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_2=
    \begin{pmatrix}
    a_{11} & b_{1} \\[1ex]
    a_{21} & b_{2} 
    \end{pmatrix}
    $$

    and

    \begin{align*}
    \det({\boldsymbol  A})   &= a_{11} \; a_{22} - a_{12} \; a_{21}\\[1ex]
    \det({\boldsymbol  A}_1) &= b_1 \; a_{22}-a_{12}\;b_2\\[1ex]
    \det({\boldsymbol  A}_2) &= a_{11}\;b_2  - b_{1} \; a_{21}
    \end{align*}

    If $\det({\boldsymbol  A}) \neq 0$, we then have:

    $$
    \left\{ \begin{array}{ll}
      a_{11} \; {x}_1 + a_{12} \; {x}_2  & = b_1\\[2ex]
      a_{21} \; {x}_1 + a_{22} \; {x}_2  & = b_2
    \end{array} \right.
    ~~~\Longrightarrow~~~
    (\tilde{x}_1, \tilde{x}_2) = \left(~~{\frac{\det({\boldsymbol  A}_1)}{\det({\boldsymbol  A})},~~ \frac{\det({\boldsymbol  A}_2)}{\det({\boldsymbol  A})}} ~~\right)
    $$

<a id="box-texexpbox1-5"></a>

!!! esempio "Esempio 5: solution of a systems of two equations and two variables"

    - Given

        $$
        {\boldsymbol  A}=
        \begin{pmatrix}
        -1 & 1 \\[1ex]
        8 & 2 
        \end{pmatrix}
        \qquad
        {\boldsymbol  b}=
        \begin{pmatrix}
        2 \\[1ex]
        19 
        \end{pmatrix}
        $$

        we have

        $$
        {\boldsymbol  A_1}=
        \begin{pmatrix}
        2 & 1 \\[1ex]
        19 & 2 
        \end{pmatrix}
        ~~~
        {\boldsymbol  A_2}=
        \begin{pmatrix}
        -1 & 2 \\[1ex]
        8 & 19 
        \end{pmatrix}
        $$

        and

        \begin{align*}
        \det({\boldsymbol  A})   &= (-1) \cdot 2  - 1 \cdot 8 =-10\\[1ex]
        \det({\boldsymbol  A}_1) &= 2 \cdot 2  - 1 \cdot 19 = -15\\[1ex]
        \det({\boldsymbol  A}_2) &= (-1) \cdot 19  - 2 \cdot 8  = -35
        \end{align*}

        Since $\det({\boldsymbol  A}) \neq 0$, we then have:

        \begin{equation*}
        \begin{cases}
                    \begin{tabular}{rrrrrrrrrrrrr}											
        $-x_1$ & $+$ & $x_2$ & $=$ &$2$\\[2ex]
        $8\;x_1$ & $+$ & $2\;x_2$ & $=$ &$19$
                    \end{tabular}
                \end{cases}
                ~~\Longrightarrow~~
        ({x}_1, {x}_2) 
         = \left(\frac{-15}{-10}, \frac{-35}{-10}\right) = \left(\frac{3}{2}, \frac{7}{2}\right)
        \end{equation*}

    - Given

        $$
        {\boldsymbol  A}=
        \begin{pmatrix}
        -1 & -1 \\[1ex]
        1 & -1 
        \end{pmatrix}
        \qquad
        {\boldsymbol  b}=
        \begin{pmatrix}
        -2 \\[1ex]
        0 
        \end{pmatrix}
        $$

        we have

        $$
        {\boldsymbol  A_1}=
        \begin{pmatrix}
        -2 & -1 \\[1ex]
        0 & -1 
        \end{pmatrix}
        ~~~
        {\boldsymbol  A_2}=
        \begin{pmatrix}
        -1 & -2 \\[1ex]
        1 & 0 
        \end{pmatrix}
        $$

        and

        \begin{align*}
        \det({\boldsymbol  A})   &= (-1) \cdot (-1)   - (-1) \cdot 1 =2\\[1ex]
        \det({\boldsymbol  A}_1) &= (-2) \cdot (-1)  - (-1) \cdot 0 = 2\\[1ex]
        \det({\boldsymbol  A}_2) &= (-1) \cdot 0  - (-2) \cdot 1  = 2
        \end{align*}

        Since $\det({\boldsymbol  A}) \neq 0$, we then have:

        \begin{equation*}
        \begin{cases}
                    \begin{tabular}{rrrrrrrrrrrrr}											
        $-x_1$ & $-$ & $x_2$ & $=$ &$-2$\\[2ex]
        $x_1$ & $-$ & $x_2$ & $=$ &$0$
                    \end{tabular}
                \end{cases}
                ~~\Longrightarrow~~
        (\tilde{x}_1, \tilde{x}_2) 
         = \left(\frac{2}{2}, \frac{2}{2}\right) = \left(1, 1\right)
        \end{equation*}
