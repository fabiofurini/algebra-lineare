---
title: "Sistemi di equazioni lineari"
---

# Sistemi di equazioni lineari

<div class="info-capitolo" markdown>

**Sistemi lineari · Capitolo 6** · dalle dispense di Fabio Furini · [:material-file-pdf-box: PDF del capitolo](../pdf/sistemi-01-sistemi-lineari.pdf)

</div>

## 1. Esistenza e unicità delle soluzioni

!!! chiave ""

    Consideriamo un sistema di $m$ equazioni lineari in $n$ variabili:

    $$
    {\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}
    $$

    dove:

    - ${\boldsymbol A} \in \R^{m \times n}$ è la matrice dei coefficienti ($m$ equazioni, $n$ variabili)

    - ${\boldsymbol x} \in \R^{n \times 1}$ è il vettore delle variabili

    - ${\boldsymbol b} \in \R^{m \times 1}$ è il vettore dei termini noti

    - $({\boldsymbol A} | {\boldsymbol b}) \in \R^{m \times (n+1)}$ è la matrice completa

    <strong>Teorema di Rouché–Capelli.</strong> L'esistenza e l'unicità delle soluzioni del sistema ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$ dipendono dal rango della matrice dei coefficienti ${\boldsymbol A}$ e dal rango della matrice completa $({\boldsymbol A} | {\boldsymbol b})$.

    <strong>Caso 1 - Nessuna soluzione (sistema incompatibile):</strong>

    $$
    \text{rank}({\boldsymbol A}) < \text{rank}({\boldsymbol A} | {\boldsymbol b})
    $$

    Il sistema è incompatibile e non ha soluzioni.

    <strong>Caso 2 - Soluzione unica:</strong>

    $$
    \text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = n
    $$

    Il sistema ha un'unica soluzione.

    <strong>Caso 3 - Infinite soluzioni:</strong>

    $$
    \text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) < n
    $$

    Il sistema ha infinite soluzioni con $n - \text{rank}({\boldsymbol A})$ gradi di libertà (variabili libere). Se $r=\text{rank}({\boldsymbol A})$, le soluzioni si possono descrivere mediante $n-r$ <strong>parametri liberi</strong>.

- Poiché $({\boldsymbol A} | {\boldsymbol b})$ si ottiene da ${\boldsymbol A}$ aggiungendo una colonna, si ha sempre

    $$
    \text{rank}({\boldsymbol A}) \le \text{rank}({\boldsymbol A} | {\boldsymbol b}) \le \text{rank}({\boldsymbol A}) + 1,
    $$

    quindi i tre casi precedenti coprono tutte le possibilità. In particolare, il sistema ha almeno una soluzione (è <strong>compatibile</strong>) se e solo se $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b})$.

- Poiché $\text{rank}({\boldsymbol A}) \le \min\{m,n\}$, una soluzione unica è possibile solo se $m \ge n$.

- Se ${\boldsymbol A} \in \R^{n \times n}$ è quadrata, ricordiamo che $\text{rank}({\boldsymbol A})=n$ se e solo se $\det({\boldsymbol A}) \neq 0$. Quindi, se $\det({\boldsymbol A}) \neq 0$, allora anche $\text{rank}({\boldsymbol A} | {\boldsymbol b})=n$ e il sistema ha un'unica soluzione, per ogni vettore dei termini noti ${\boldsymbol b}$.

## 2. Metodo di eliminazione di Gauss

!!! chiave ""

    Il <strong>metodo di eliminazione di Gauss</strong> è un algoritmo per risolvere sistemi di equazioni lineari che trasforma la matrice completa $({\boldsymbol A} | {\boldsymbol b})$ in <strong>forma a scala</strong> (forma triangolare superiore) mediante operazioni elementari sulle righe.

- Dato il sistema di equazioni lineari:

    $$
    {\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}
    $$

    costruiamo la <strong>matrice completa</strong>:

    $$
    ({\boldsymbol A} | {\boldsymbol b})
    $$

- Il metodo si compone di due fasi:

    <strong>Fase 1 - Eliminazione in avanti:</strong> si trasforma la matrice completa in forma triangolare superiore mediante operazioni elementari sulle righe:

    - Scambiare due righe

    - Moltiplicare una riga per uno scalare non nullo

    - Sommare a una riga un multiplo di un'altra riga

    L'obiettivo è creare zeri sotto la diagonale, ottenendo:

    $$
    \left(\begin{array}{cccc|c}
    \tilde{a}_{11} & \tilde{a}_{12} & \cdots & \tilde{a}_{1n} & \tilde{b}_1 \\
    0 & \tilde{a}_{22} & \cdots & \tilde{a}_{2n} & \tilde{b}_2 \\
    \vdots & \vdots & \ddots & \vdots & \vdots \\
    0 & 0 & \cdots & \tilde{a}_{nn} & \tilde{b}_n
    \end{array}\right)
    $$

    <strong>Fase 2 - Sostituzione all'indietro:</strong> si risolve il sistema triangolare superiore dal basso verso l'alto (supponendo $\tilde{a}_{ii} \neq 0$ per ogni $i$):

    \begin{align*}
    x_n &= \frac{\tilde{b}_n}{\tilde{a}_{nn}}\\
    x_{n-1} &= \frac{\tilde{b}_{n-1} - \tilde{a}_{n-1,n} \; x_n}{\tilde{a}_{n-1,n-1}}\\
    &\vdots\\
    x_i &= \frac{\tilde{b}_i - \sum_{j=i+1}^{n} \tilde{a}_{ij} \; x_j}{\tilde{a}_{ii}}
    \end{align*}

!!! chiave ""

    <strong>Operazioni elementari sulle righe:</strong>

    - $R_i \leftrightarrow R_j$ : scambia la riga $i$ con la riga $j$

    - $R_i \leftarrow k \; R_i$ : moltiplica la riga $i$ per lo scalare $k \neq 0$

    - $R_i \leftarrow R_i + k \; R_j$ : somma alla riga $i$ la riga $j$ moltiplicata per $k$

    Queste operazioni non cambiano l'insieme delle soluzioni del sistema.

<a id="box-texexpbox1a-1"></a>

!!! esempio "Esempio 1: Risoluzione di un sistema con l'eliminazione di Gauss - Parte 1"

    Consideriamo il sistema di equazioni lineari:

    $$
    \left\{ \begin{array}{ll}
      2 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      4 \; x_1 + 3 \; x_2 + 3 \; x_3  & = 10\\[2ex]
      8 \; x_1 + 7 \; x_2 + 9 \; x_3  & = 24
    \end{array} \right.
    $$

    <strong>Matrice completa:</strong>

    $$
    ({\boldsymbol A} | {\boldsymbol b}) = 
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    4 & 3 & 3 & 10 \\
    8 & 7 & 9 & 24
    \end{array}\right)
    $$

    <strong>Passo 1:</strong> eliminiamo $x_1$ dalle righe 2 e 3

    $R_2 \leftarrow R_2 - 2 \; R_1$ (sottraiamo alla riga 2 la riga 1 moltiplicata per $2$):

    $$
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    0 & 1 & 1 & 2 \\
    8 & 7 & 9 & 24
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - 4 \; R_1$ (sottraiamo alla riga 3 la riga 1 moltiplicata per $4$):

    $$
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    0 & 1 & 1 & 2 \\
    0 & 3 & 5 & 8
    \end{array}\right)
    $$

    <strong>Passo 2:</strong> eliminiamo $x_2$ dalla riga 3

    $R_3 \leftarrow R_3 - 3 \; R_2$ (sottraiamo alla riga 3 la riga 2 moltiplicata per $3$):

    $$
    \left(\begin{array}{ccc|c}
    2 & 1 & 1 & 4 \\
    0 & 1 & 1 & 2 \\
    0 & 0 & 2 & 2
    \end{array}\right)
    $$

    <strong>Forma triangolare superiore ottenuta!</strong> Il sistema corrispondente è:

    $$
    \left\{ \begin{array}{ll}
      2 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      1 \; x_2 + 1 \; x_3  & = 2\\[2ex]
      2 \; x_3  & = 2
    \end{array} \right.
    $$

<a id="box-texexpbox1c-2"></a>

!!! esempio "Esempio 2: Risoluzione di un sistema con l'eliminazione di Gauss - Parte 2"

    <strong>Sostituzione all'indietro:</strong>

    Dalla terza equazione:

    $$
    2 \; x_3 = 2 ~~\Longrightarrow~~ x_3 = 1
    $$

    Dalla seconda equazione:

    $$
    x_2 + x_3 = 2 ~~\Longrightarrow~~ x_2 = 2 - x_3 = 2 - 1 = 1
    $$

    Dalla prima equazione:

    $$
    2 \; x_1 + x_2 + x_3 = 4 ~~\Longrightarrow~~ 2 \; x_1 = 4 - x_2 - x_3 = 4 - 1 - 1 = 2 ~~\Longrightarrow~~ x_1 = 1
    $$

    <strong>Soluzione:</strong>

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

    <strong>Verifica:</strong>

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

## 3. Eliminazione di Gauss e teorema di Rouché–Capelli

- L'eliminazione di Gauss si può applicare a qualunque sistema ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$, con ${\boldsymbol A} \in \R^{m \times n}$. In generale, l'eliminazione in avanti trasforma $({\boldsymbol A} | {\boldsymbol b})$ in <strong>forma a scala</strong>: in ogni riga non nulla, il primo elemento non nullo (detto <strong>pivot</strong>) si trova strettamente a destra del pivot della riga precedente, e le righe nulle (se ci sono) si trovano in fondo.

- Le operazioni elementari sulle righe non cambiano l'insieme delle soluzioni del sistema, e non cambiano né il rango di ${\boldsymbol A}$ né il rango di $({\boldsymbol A} | {\boldsymbol b})$.

- Il rango di una matrice in forma a scala è uguale al numero delle sue righe non nulle. Pertanto, al termine dell'eliminazione in avanti possiamo leggere $\text{rank}({\boldsymbol A})$ e $\text{rank}({\boldsymbol A} | {\boldsymbol b})$ e applicare il teorema di Rouché–Capelli:

    - una riga della forma $\left(\begin{array}{ccc|c} 0 & \cdots & 0 & c \end{array}\right)$ con $c \neq 0$ corrisponde all'equazione impossibile $0=c$: allora $\text{rank}({\boldsymbol A}) < \text{rank}({\boldsymbol A} | {\boldsymbol b})$ e il sistema non ha soluzioni;

    - altrimenti, le variabili le cui colonne contengono un pivot si calcolano con la sostituzione all'indietro, e le restanti $n-r$ variabili sono i <strong>parametri liberi</strong>.

!!! chiave ""

    Quando il sistema ha infinite soluzioni con un parametro libero $t \in \R$, le soluzioni si possono scrivere in <strong>forma parametrica</strong>

    $$
    {\boldsymbol x} = {\boldsymbol x}_0 + t \; {\boldsymbol v}, \qquad t \in \R,
    $$

    dove ${\boldsymbol x}_0$ è una soluzione particolare (ottenuta per $t=0$) e ${\boldsymbol v}$ è un vettore non nullo tale che ${\boldsymbol A} \; {\boldsymbol v} = {\boldsymbol 0}$.

<a id="box-texexpboxRCunique-3"></a>

!!! esempio "Esempio 3: Rouché–Capelli: soluzione unica"

    Consideriamo il sistema di equazioni lineari:

    $$
    \left\{ \begin{array}{ll}
      \phantom{2 \; x_1 +{}} 1 \; x_2 + 1 \; x_3  & = 1\\[2ex]
      1 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 2\\[2ex]
      2 \; x_1 + 1 \; x_2 + 3 \; x_3  & = 1
    \end{array} \right.
    \qquad
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    0 & 1 & 1 & 1 \\
    1 & 1 & 1 & 2 \\
    2 & 1 & 3 & 1
    \end{array}\right)
    $$

    L'elemento in posizione $(1,1)$ è nullo, quindi per prima cosa scambiamo le righe 1 e 2.

    $R_1 \leftrightarrow R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 1 & 1 & 2 \\
    0 & 1 & 1 & 1 \\
    2 & 1 & 3 & 1
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - 2 \; R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 1 & 1 & 2 \\
    0 & 1 & 1 & 1 \\
    0 & -1 & 1 & -3
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 + R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 1 & 1 & 2 \\
    0 & 1 & 1 & 1 \\
    0 & 0 & 2 & -2
    \end{array}\right)
    $$

    Ci sono $3$ righe non nulle sia in ${\boldsymbol A}$ sia in $({\boldsymbol A} | {\boldsymbol b})$: $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 3 = n$, quindi la soluzione è unica. Con la sostituzione all'indietro:

    $$
    2 \; x_3 = -2 ~~\Longrightarrow~~ x_3 = -1,
    \qquad
    x_2 = 1 - x_3 = 2,
    \qquad
    x_1 = 2 - x_2 - x_3 = 2 - 2 + 1 = 1,
    $$

    cioè

    $$
    {\boldsymbol x} =
    \begin{pmatrix}
    1 \\
    2 \\
    -1
    \end{pmatrix}.
    $$

<a id="box-texexpboxRCinfinite-4"></a>

!!! esempio "Esempio 4: Rouché–Capelli: infinite soluzioni"

    Consideriamo il sistema di equazioni lineari:

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 2 \; x_2 - 1 \; x_3  & = 1\\[2ex]
      2 \; x_1 + 5 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      3 \; x_1 + 7 \; x_2 \phantom{{}+ 1 \; x_3}  & = 5
    \end{array} \right.
    \qquad
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 1 \\
    2 & 5 & 1 & 4 \\
    3 & 7 & 0 & 5
    \end{array}\right)
    $$

    $R_2 \leftarrow R_2 - 2 \; R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 1 \\
    0 & 1 & 3 & 2 \\
    3 & 7 & 0 & 5
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - 3 \; R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 1 \\
    0 & 1 & 3 & 2 \\
    0 & 1 & 3 & 2
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 1 \\
    0 & 1 & 3 & 2 \\
    0 & 0 & 0 & 0
    \end{array}\right)
    $$

    Ci sono $2$ righe non nulle sia in ${\boldsymbol A}$ sia in $({\boldsymbol A} | {\boldsymbol b})$: $\text{rank}({\boldsymbol A}) = \text{rank}({\boldsymbol A} | {\boldsymbol b}) = 2 < 3 = n$, quindi ci sono infinite soluzioni con $n - r = 3 - 2 = 1$ parametro libero. I pivot sono nelle colonne di $x_1$ e $x_2$, quindi $x_3$ è libera: poniamo $x_3 = t$, $t \in \R$. Con la sostituzione all'indietro:

    $$
    x_2 = 2 - 3 \; x_3 = 2 - 3t,
    \qquad
    x_1 = 1 - 2 \; x_2 + x_3 = 1 - 4 + 6t + t = -3 + 7t.
    $$

    In forma parametrica:

    $$
    {\boldsymbol x} =
    \begin{pmatrix}
    -3 + 7t \\
    2 - 3t \\
    t
    \end{pmatrix}
    =
    \underbrace{\begin{pmatrix}
    -3 \\
    2 \\
    0
    \end{pmatrix}}_{{\boldsymbol x}_0}
    + t
    \underbrace{\begin{pmatrix}
    7 \\
    -3 \\
    1
    \end{pmatrix}}_{{\boldsymbol v}},
    \qquad t \in \R.
    $$

    <strong>Verifica:</strong> ${\boldsymbol A} \; {\boldsymbol x}_0 = (-3+4, \; -6+10, \; -9+14)' = (1, 4, 5)' = {\boldsymbol b}$ e ${\boldsymbol A} \; {\boldsymbol v} = (7-6-1, \; 14-15+1, \; 21-21)' = {\boldsymbol 0}$, quindi ${\boldsymbol A}({\boldsymbol x}_0 + t \; {\boldsymbol v}) = {\boldsymbol b}$ per ogni $t \in \R$ $\checkmark$

<a id="box-texexpboxRCnone-5"></a>

!!! esempio "Esempio 5: Rouché–Capelli: nessuna soluzione"

    Cambiamo solo l'ultimo termine noto del sistema precedente:

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 2 \; x_2 - 1 \; x_3  & = 1\\[2ex]
      2 \; x_1 + 5 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      3 \; x_1 + 7 \; x_2 \phantom{{}+ 1 \; x_3}  & = 6
    \end{array} \right.
    \qquad
    ({\boldsymbol A} | {\boldsymbol b}) =
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 1 \\
    2 & 5 & 1 & 4 \\
    3 & 7 & 0 & 6
    \end{array}\right)
    $$

    Con le stesse operazioni sulle righe $R_2 \leftarrow R_2 - 2 \; R_1$, $R_3 \leftarrow R_3 - 3 \; R_1$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 1 \\
    0 & 1 & 3 & 2 \\
    0 & 1 & 3 & 3
    \end{array}\right)
    $$

    $R_3 \leftarrow R_3 - R_2$:

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 1 \\
    0 & 1 & 3 & 2 \\
    0 & 0 & 0 & 1
    \end{array}\right)
    $$

    L'ultima riga corrisponde all'equazione $0 \; x_1 + 0 \; x_2 + 0 \; x_3 = 1$, che è impossibile. Infatti ${\boldsymbol A}$ ha $2$ righe non nulle mentre $({\boldsymbol A} | {\boldsymbol b})$ ne ha $3$:

    $$
    \text{rank}({\boldsymbol A}) = 2 < 3 = \text{rank}({\boldsymbol A} | {\boldsymbol b}),
    $$

    quindi il sistema è incompatibile e <strong>non ha soluzioni</strong>.

## 4. Sistemi omogenei

<a id="box-defHomogeneous-6"></a>

!!! definizione "Definizione 1: sistema omogeneo"

    Un sistema di equazioni lineari ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$ con ${\boldsymbol A} \in \R^{m \times n}$ si dice <strong>omogeneo</strong> se ${\boldsymbol b} = {\boldsymbol 0}$, cioè se ha la forma

    $$
    {\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol 0}.
    $$

<a id="box-obsHomogeneous-7"></a>

!!! teorema "Osservazione 1: soluzioni di un sistema omogeneo"

    Sia ${\boldsymbol A} \in \R^{m \times n}$. Allora:

    - il sistema omogeneo ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol 0}$ ha sempre la soluzione ${\boldsymbol x} = {\boldsymbol 0}$, detta <strong>soluzione banale</strong>;

    - ha soluzioni non banali (${\boldsymbol x} \neq {\boldsymbol 0}$) se e solo se $\text{rank}({\boldsymbol A}) < n$; in tal caso ha infinite soluzioni, con $n - \text{rank}({\boldsymbol A})$ parametri liberi;

    - se ${\boldsymbol A} \in \R^{n \times n}$ è quadrata, ha soluzioni non banali se e solo se $\det({\boldsymbol A}) = 0$.

??? dimostrazione "Dimostrazione (Dimostrazione)"

    Aggiungere una colonna di zeri non cambia il rango, quindi $\text{rank}({\boldsymbol A} | {\boldsymbol 0}) = \text{rank}({\boldsymbol A})$ e il sistema è sempre compatibile (come mostra ${\boldsymbol x} = {\boldsymbol 0}$). Per il teorema di Rouché–Capelli, la soluzione ${\boldsymbol x} = {\boldsymbol 0}$ è l'unica se e solo se $\text{rank}({\boldsymbol A}) = n$; altrimenti ci sono infinite soluzioni con $n - \text{rank}({\boldsymbol A})$ parametri liberi. Per una matrice quadrata, $\text{rank}({\boldsymbol A}) < n$ se e solo se $\det({\boldsymbol A}) = 0$. <span class="qed">□</span>

- In particolare, se $m < n$ (meno equazioni che variabili), allora $\text{rank}({\boldsymbol A}) \le m < n$ e il sistema omogeneo ha sempre soluzioni non banali.

- Se ${\boldsymbol x}_0$ è una soluzione di ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$ e ${\boldsymbol v}$ è una soluzione di ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol 0}$, allora ${\boldsymbol A}({\boldsymbol x}_0 + {\boldsymbol v}) = {\boldsymbol b} + {\boldsymbol 0} = {\boldsymbol b}$. Questo spiega la forma parametrica ${\boldsymbol x} = {\boldsymbol x}_0 + t \; {\boldsymbol v}$ dell'Esempio [Esempio 4](#box-texexpboxRCinfinite-4).

<a id="box-texexpboxHomogeneous-8"></a>

!!! esempio "Esempio 6: un sistema omogeneo"

    Consideriamo il sistema omogeneo con la matrice dei coefficienti dell'Esempio [Esempio 4](#box-texexpboxRCinfinite-4):

    $$
    \left\{ \begin{array}{ll}
      1 \; x_1 + 2 \; x_2 - 1 \; x_3  & = 0\\[2ex]
      2 \; x_1 + 5 \; x_2 + 1 \; x_3  & = 0\\[2ex]
      3 \; x_1 + 7 \; x_2 \phantom{{}+ 1 \; x_3}  & = 0
    \end{array} \right.
    $$

    Con la regola di Sarrus,

    $$
    \det({\boldsymbol A}) = 1 \cdot 5 \cdot 0 + 2 \cdot 1 \cdot 3 + (-1) \cdot 2 \cdot 7 - (-1) \cdot 5 \cdot 3 - 2 \cdot 2 \cdot 0 - 1 \cdot 1 \cdot 7 = 0 + 6 - 14 + 15 - 0 - 7 = 0,
    $$

    quindi ci sono soluzioni non banali. Con le stesse operazioni sulle righe dell'Esempio [Esempio 4](#box-texexpboxRCinfinite-4) (l'ultima colonna resta nulla):

    $$
    \left(\begin{array}{ccc|c}
    1 & 2 & -1 & 0 \\
    0 & 1 & 3 & 0 \\
    0 & 0 & 0 & 0
    \end{array}\right)
    $$

    Ponendo $x_3 = t$: $x_2 = -3t$ e $x_1 = -2 \; x_2 + x_3 = 6t + t = 7t$. Quindi le soluzioni sono

    $$
    {\boldsymbol x} = t
    \begin{pmatrix}
    7 \\
    -3 \\
    1
    \end{pmatrix},
    \qquad t \in \R,
    $$

    e la soluzione banale si ottiene per $t = 0$.

## 5. Metodo della fattorizzazione LU

!!! chiave ""

    La <strong>fattorizzazione LU</strong> (o <strong>decomposizione LU</strong>) è un metodo per risolvere sistemi di equazioni lineari che scompone la matrice dei coefficienti ${\boldsymbol A}$ nel prodotto di due matrici triangolari:

    $$
    {\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U}
    $$

    dove ${\boldsymbol L}$ è una <strong>matrice triangolare inferiore</strong> (con elementi diagonali uguali a 1) e ${\boldsymbol U}$ è una <strong>matrice triangolare superiore</strong>.

- Dato il sistema di equazioni lineari:

    $$
    {\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}
    $$

    se disponiamo della fattorizzazione LU ${\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U}$, possiamo sostituire:

    $$
    {\boldsymbol L} \; {\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol b}
    $$

- Introduciamo la <strong>variabile ausiliaria</strong> ${\boldsymbol y}$ definita come:

    $$
    {\boldsymbol y} \;:=\; {\boldsymbol U} \; {\boldsymbol x}
    $$

    così che ${\boldsymbol L} \; {\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol b}$ diventa ${\boldsymbol L} \; {\boldsymbol y} = {\boldsymbol b}$.

    <strong>Perché funziona?</strong>  Stiamo spezzando il sistema originale ${\boldsymbol A}\,{\boldsymbol x}={\boldsymbol b}$ in due sistemi triangolari più semplici:

    1. Trovare ${\boldsymbol y}$ tale che ${\boldsymbol L}\,{\boldsymbol y} = {\boldsymbol b}$.

    2. Trovare ${\boldsymbol x}$ tale che ${\boldsymbol U}\,{\boldsymbol x} = {\boldsymbol y}$.

    Se entrambi i passi riescono, allora ${\boldsymbol A}\,{\boldsymbol x} = {\boldsymbol L}\,{\boldsymbol U}\,{\boldsymbol x} = {\boldsymbol L}\,{\boldsymbol y} = {\boldsymbol b}$, quindi ${\boldsymbol x}$ è effettivamente una soluzione del sistema originale. Poiché sia ${\boldsymbol L}$ sia ${\boldsymbol U}$ sono triangolari, ciascuno dei due sistemi si risolve in $O(n^2)$ operazioni per semplice sostituzione.

- Risolviamo quindi il sistema in due passi:

    <strong>Passo 1 - Sostituzione in avanti:</strong> risolvere ${\boldsymbol L} \; {\boldsymbol y} = {\boldsymbol b}$ rispetto a ${\boldsymbol y}$

    Poiché ${\boldsymbol L}$ è triangolare inferiore, possiamo risolvere facilmente questo sistema dall'alto verso il basso:

    \begin{align*}
    y_1 &= b_1\\
    y_2 &= b_2 - \ell_{21} \; y_1\\
    y_3 &= b_3 - \ell_{31} \; y_1 - \ell_{32} \; y_2\\
    &\vdots\\
    y_i &= b_i - \sum_{j=1}^{i-1} \ell_{ij} \; y_j
    \end{align*}

    <strong>Passo 2 - Sostituzione all'indietro:</strong> risolvere ${\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol y}$ rispetto a ${\boldsymbol x}$

    Poiché ${\boldsymbol U}$ è triangolare superiore, possiamo risolvere facilmente questo sistema dal basso verso l'alto:

    \begin{align*}
    x_n &= \frac{y_n}{u_{nn}}\\
    x_{n-1} &= \frac{y_{n-1} - u_{n-1,n} \; x_n}{u_{n-1,n-1}}\\
    &\vdots\\
    x_i &= \frac{y_i - \sum_{j=i+1}^{n} u_{ij} \; x_j}{u_{ii}}
    \end{align*}

!!! chiave ""

    <strong>Vantaggi della fattorizzazione LU:</strong>

    - Una volta calcolata la fattorizzazione ${\boldsymbol A} = {\boldsymbol L} \; {\boldsymbol U}$, possiamo risolvere in modo efficiente il sistema per diversi vettori dei termini noti ${\boldsymbol b}$

    - Sia la sostituzione in avanti sia quella all'indietro richiedono solo $O(n^2)$ operazioni

    - La fattorizzazione richiede $O(n^3)$ operazioni, ma va calcolata una sola volta

<a id="box-texexpbox2a-9"></a>

!!! esempio "Esempio 7: Risoluzione di un sistema con la fattorizzazione LU - Parte 1"

    Consideriamo il sistema di equazioni lineari:

    $$
    \left\{ \begin{array}{ll}
      2 \; x_1 + 1 \; x_2 + 1 \; x_3  & = 4\\[2ex]
      4 \; x_1 + 3 \; x_2 + 3 \; x_3  & = 10\\[2ex]
      8 \; x_1 + 7 \; x_2 + 9 \; x_3  & = 24
    \end{array} \right.
    $$

    In forma matriciale: ${\boldsymbol A} \; {\boldsymbol x} = {\boldsymbol b}$ dove

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

    <strong>Data</strong> la fattorizzazione LU di ${\boldsymbol A}$:

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

    <strong>Verifica:</strong>

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

<a id="box-texexpbox2b-10"></a>

!!! esempio "Esempio 8: Risoluzione di un sistema con la fattorizzazione LU - Parte 2"

    <strong>Passo 1 - Sostituzione in avanti:</strong> risolvere ${\boldsymbol L} \; {\boldsymbol y} = {\boldsymbol b}$

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

    Dalla prima equazione:

    $$
    y_1 = 4
    $$

    Dalla seconda equazione:

    $$
    2 \; y_1 + y_2 = 10 ~~\Longrightarrow~~ y_2 = 10 - 2 \cdot 4 = 10 - 8 = 2
    $$

    Dalla terza equazione:

    $$
    4 \; y_1 + 3 \; y_2 + y_3 = 24 ~~\Longrightarrow~~ y_3 = 24 - 4 \cdot 4 - 3 \cdot 2 = 24 - 16 - 6 = 2
    $$

    Quindi:

    $$
    {\boldsymbol y} = 
    \begin{pmatrix}
    4 \\
    2 \\
    2
    \end{pmatrix}
    $$

    <strong>Passo 2 - Sostituzione all'indietro:</strong> risolvere ${\boldsymbol U} \; {\boldsymbol x} = {\boldsymbol y}$

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

    Dalla terza equazione:

    $$
    2 \; x_3 = 2 ~~\Longrightarrow~~ x_3 = 1
    $$

    Dalla seconda equazione:

    $$
    x_2 + x_3 = 2 ~~\Longrightarrow~~ x_2 = 2 - 1 = 1
    $$

    Dalla prima equazione:

    $$
    2 \; x_1 + x_2 + x_3 = 4 ~~\Longrightarrow~~ 2 \; x_1 = 4 - 1 - 1 = 2 ~~\Longrightarrow~~ x_1 = 1
    $$

    <strong>Soluzione:</strong>

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

    <strong>Verifica:</strong>

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

## 6. Regola di Cramer

!!! chiave ""

    La regola di Cramer è una formula esplicita per la soluzione di un sistema di $m$ equazioni lineari in $m$ variabili (valida quando il sistema ha un'unica soluzione).

- Dati un vettore colonna ${\boldsymbol  b} \in \R^{m \times 1}$ di $m$ righe, una matrice ${\boldsymbol  A } \in \R^{m \times m}$ di $m$ righe e $m$ colonne e un vettore colonna ${\boldsymbol  x} \in \R^{m \times 1}$ di $m$ righe contenente le $m$ variabili:

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
    b_{m} \\
    \end{pmatrix}
    \qquad
    {\boldsymbol  x}=
    \begin{pmatrix}
    x_{1} \\
    x_{2} \\
    \vdots  \\
    x_{m} \\
    \end{pmatrix}
    $$

    se $\det({\boldsymbol  A}) \neq 0$, la soluzione ${\tilde{\boldsymbol  x}}$ del sistema di $m$ equazioni lineari:

    $$
    {\boldsymbol  A} \; {\boldsymbol  x}= {\boldsymbol  b}
    $$

    è data dalla formula:

    \begin{equation}
    \label{CCCC}
    \tilde{x}_j = \frac{\det({\boldsymbol  A}_j) }{\det({\boldsymbol  A})},~~~~~ \forall j \in \{1,2,\dots,m\}
    \end{equation}

    dove ${\boldsymbol  A}_j$ è la matrice ottenuta sostituendo la $j$-esima colonna di ${\boldsymbol  A}$ con il vettore colonna ${\boldsymbol  b}$.

### 6.1 Sistemi di due equazioni in due variabili

!!! chiave ""

    Con $m=2$, si ha:

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

    e

    \begin{align*}
    \det({\boldsymbol  A})   &= a_{11} \; a_{22} - a_{12} \; a_{21}\\[1ex]
    \det({\boldsymbol  A}_1) &= b_1 \; a_{22}-a_{12}\;b_2\\[1ex]
    \det({\boldsymbol  A}_2) &= a_{11}\;b_2  - b_{1} \; a_{21}
    \end{align*}

    Se $\det({\boldsymbol  A}) \neq 0$, si ha allora:

    $$
    \left\{ \begin{array}{ll}
      a_{11} \; {x}_1 + a_{12} \; {x}_2  & = b_1\\[2ex]
      a_{21} \; {x}_1 + a_{22} \; {x}_2  & = b_2
    \end{array} \right.
    ~~~\Longrightarrow~~~
    (\tilde{x}_1, \tilde{x}_2) = \left(~~{\frac{\det({\boldsymbol  A}_1)}{\det({\boldsymbol  A})},~~ \frac{\det({\boldsymbol  A}_2)}{\det({\boldsymbol  A})}} ~~\right)
    $$

<a id="box-texexpbox1-11"></a>

!!! esempio "Esempio 9: soluzione di un sistema di due equazioni in due variabili"

    - Dati

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

        si ha

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

        e

        \begin{align*}
        \det({\boldsymbol  A})   &= (-1) \cdot 2  - 1 \cdot 8 =-10\\[1ex]
        \det({\boldsymbol  A}_1) &= 2 \cdot 2  - 1 \cdot 19 = -15\\[1ex]
        \det({\boldsymbol  A}_2) &= (-1) \cdot 19  - 2 \cdot 8  = -35
        \end{align*}

        Poiché $\det({\boldsymbol  A}) \neq 0$, si ha allora:

        \begin{equation*}
        \begin{cases}
                    \begin{array}{rrrrrrrrrrrrr}											
        -x_1 & + & x_2 & = &2\\[2ex]
        8\;x_1 & + & 2\;x_2 & = &19
                    \end{array}
                \end{cases}
                ~~\Longrightarrow~~
        (\tilde{x}_1, \tilde{x}_2) 
         = \left(\frac{-15}{-10}, \frac{-35}{-10}\right) = \left(\frac{3}{2}, \frac{7}{2}\right)
        \end{equation*}

    - Dati

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

        si ha

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

        e

        \begin{align*}
        \det({\boldsymbol  A})   &= (-1) \cdot (-1)   - (-1) \cdot 1 =2\\[1ex]
        \det({\boldsymbol  A}_1) &= (-2) \cdot (-1)  - (-1) \cdot 0 = 2\\[1ex]
        \det({\boldsymbol  A}_2) &= (-1) \cdot 0  - (-2) \cdot 1  = 2
        \end{align*}

        Poiché $\det({\boldsymbol  A}) \neq 0$, si ha allora:

        \begin{equation*}
        \begin{cases}
                    \begin{array}{rrrrrrrrrrrrr}											
        -x_1 & - & x_2 & = &-2\\[2ex]
        x_1 & - & x_2 & = &0
                    \end{array}
                \end{cases}
                ~~\Longrightarrow~~
        (\tilde{x}_1, \tilde{x}_2) 
         = \left(\frac{2}{2}, \frac{2}{2}\right) = \left(1, 1\right)
        \end{equation*}

### 6.2 Sistemi di tre equazioni in tre variabili

!!! chiave ""

    Con $m=3$, si ha:

    $$
    {\boldsymbol  A}=
    \begin{pmatrix}
    a_{11} & a_{12} & a_{13} \\[1ex]
    a_{21} & a_{22} & a_{23} \\[1ex]
    a_{31} & a_{32} & a_{33}
    \end{pmatrix}
    \qquad
    {\boldsymbol  b}=
    \begin{pmatrix}
    b_{1} \\[1ex]
    b_{2} \\[1ex]
    b_{3}
    \end{pmatrix}
    $$

    $$
    {\boldsymbol  A}_1=
    \begin{pmatrix}
    b_{1} & a_{12} & a_{13} \\[1ex]
    b_{2} & a_{22} & a_{23} \\[1ex]
    b_{3} & a_{32} & a_{33}
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_2=
    \begin{pmatrix}
    a_{11} & b_{1} & a_{13} \\[1ex]
    a_{21} & b_{2} & a_{23} \\[1ex]
    a_{31} & b_{3} & a_{33}
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_3=
    \begin{pmatrix}
    a_{11} & a_{12} & b_{1} \\[1ex]
    a_{21} & a_{22} & b_{2} \\[1ex]
    a_{31} & a_{32} & b_{3}
    \end{pmatrix}
    $$

    e (regola di Sarrus)

    \begin{align*}
    \det({\boldsymbol  A})   &= a_{11} a_{22} a_{33} + a_{12} a_{23} a_{31} + a_{13} a_{21} a_{32} -  a_{13} a_{22} a_{31} - a_{12} a_{21} a_{33} - a_{11} a_{23} a_{32}\\[1ex]
    \det({\boldsymbol  A}_1)   &= b_1 a_{22} a_{33} + a_{12} a_{23} b_3 + a_{13} b_2 a_{32} -  a_{13} a_{22} b_3 - a_{12} b_2 a_{33} - b_1 a_{23} a_{32}\\[1ex]
    \det({\boldsymbol  A}_2)   &= a_{11} b_2 a_{33} + b_1 a_{23} a_{31} + a_{13} a_{21} b_3 -  a_{13} b_2 a_{31} - b_1 a_{21} a_{33} - a_{11} a_{23} b_3\\[1ex]
    \det({\boldsymbol  A}_3)   &= a_{11} a_{22} b_3 + a_{12} b_2 a_{31} + b_1 a_{21} a_{32} -  b_1 a_{22} a_{31} - a_{12} a_{21} b_3 - a_{11} b_2 a_{32}
    \end{align*}

    Se $\det({\boldsymbol  A}) \neq 0$, si ha allora:

    $$
    (\tilde{x}_1, \tilde{x}_2, \tilde{x}_3) = \left(~~{\frac{\det({\boldsymbol  A}_1)}{\det({\boldsymbol  A})},~~ \frac{\det({\boldsymbol  A}_2)}{\det({\boldsymbol  A})},~~ \frac{\det({\boldsymbol  A}_3)}{\det({\boldsymbol  A})}} ~~\right)
    $$

<a id="box-texexpboxCramer3-12"></a>

!!! esempio "Esempio 10: soluzione di un sistema di tre equazioni in tre variabili"

    Risolviamo con la regola di Cramer il sistema dell'Esempio [Esempio 1](#box-texexpbox1a-1):

    $$
    {\boldsymbol  A}=
    \begin{pmatrix}
    2 & 1 & 1 \\
    4 & 3 & 3 \\
    8 & 7 & 9
    \end{pmatrix}
    \qquad
    {\boldsymbol  b}=
    \begin{pmatrix}
    4 \\
    10 \\
    24
    \end{pmatrix}
    $$

    Si ha

    $$
    {\boldsymbol  A}_1=
    \begin{pmatrix}
    4 & 1 & 1 \\
    10 & 3 & 3 \\
    24 & 7 & 9
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_2=
    \begin{pmatrix}
    2 & 4 & 1 \\
    4 & 10 & 3 \\
    8 & 24 & 9
    \end{pmatrix}
    \qquad
    {\boldsymbol  A}_3=
    \begin{pmatrix}
    2 & 1 & 4 \\
    4 & 3 & 10 \\
    8 & 7 & 24
    \end{pmatrix}
    $$

    e

    \begin{align*}
    \det({\boldsymbol  A})   &= 54 + 24 + 28 - 24 - 36 - 42 = 4\\[1ex]
    \det({\boldsymbol  A}_1) &= 108 + 72 + 70 - 72 - 90 - 84 = 4\\[1ex]
    \det({\boldsymbol  A}_2) &= 180 + 96 + 96 - 80 - 144 - 144 = 4\\[1ex]
    \det({\boldsymbol  A}_3) &= 144 + 80 + 112 - 96 - 96 - 140 = 4
    \end{align*}

    Poiché $\det({\boldsymbol  A}) \neq 0$, si ha allora:

    $$
    (\tilde{x}_1, \tilde{x}_2, \tilde{x}_3) = \left(\frac{4}{4}, \frac{4}{4}, \frac{4}{4}\right) = (1, 1, 1),
    $$

    che è la soluzione trovata con l'eliminazione di Gauss.

### 6.3 Costo computazionale

- La regola di Cramer fornisce una formula esplicita, molto utile per sistemi piccoli ($m=2$ o $m=3$) e per scopi teorici. Tuttavia, <strong>non</strong> è un metodo pratico per sistemi grandi.

- Per applicare la regola di Cramer servono $m+1$ determinanti di ordine $m$: $\det({\boldsymbol A})$, $\det({\boldsymbol A}_1)$, $\dots$, $\det({\boldsymbol A}_m)$. Se ogni determinante è calcolato con lo sviluppo di Laplace, il numero di operazioni aritmetiche cresce all'incirca come $m!$ per ciascun determinante.

- L'eliminazione di Gauss, invece, risolve il sistema con un numero di operazioni che cresce all'incirca come $m^3$ (circa $\frac{2}{3} m^3$ operazioni).

- Ad esempio, con $m=10$ si ha $10! = 3\,628\,800$, mentre $\frac{2}{3} \cdot 10^3 \approx 667$; con $m=20$, $20!$ è maggiore di $2 \cdot 10^{18}$, mentre $\frac{2}{3}\cdot 20^3 \approx 5\,333$.

- Anche se i determinanti vengono calcolati in modo più efficiente (ad esempio con la stessa eliminazione di Gauss), la regola di Cramer ne richiede comunque $m+1$, e resta più costosa che risolvere direttamente il sistema con l'eliminazione di Gauss.
