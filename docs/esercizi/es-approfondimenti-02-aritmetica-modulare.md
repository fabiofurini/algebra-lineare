---
title: "Aritmetica modulare"
---

# Aritmetica modulare

<div class="info-capitolo" markdown>

**Esercizi · Approfondimenti** · con le soluzioni svolte · [:material-file-pdf-box: PDF](../pdf/es-approfondimenti-02-aritmetica-modulare.pdf)

</div>

<a id="box-exe_mod_euclid_division-1"></a>

!!! esercizio "Esercizio 1"

    Trovare il quoziente $q$ e il resto $r$ (con $0 \le r < |m|$) della divisione euclidea di $n$ per $m$ nei casi seguenti:

    $$
    {\rm a)}~ n=47,~m=5, \qquad {\rm b)}~ n=-47,~m=5, \qquad {\rm c)}~ n=47,~m=-5, \qquad {\rm d)}~ n=-47,~m=-5
    $$

??? soluzione "Soluzione"

    In ciascun caso cerchiamo gli interi $q$ e $r$ tali che $n = q \; m + r$ e $0 \le r < 5$:

    - **a)** $47 = 9 \cdot 5 + 2$, quindi $q = 9$ e $r = 2$.

    - **b)** $-47 = (-10) \cdot 5 + 3$, quindi $q = -10$ e $r = 3$. Si noti che $-47 = (-9)\cdot 5 - 2$ non è la divisione euclidea, poiché $-2 < 0$.

    - **c)** $47 = (-9) \cdot (-5) + 2$, quindi $q = -9$ e $r = 2$.

    - **d)** $-47 = 10 \cdot (-5) + 3$, quindi $q = 10$ e $r = 3$.

<a id="box-exe_mod_compute-2"></a>

!!! esercizio "Esercizio 2"

    Calcolare:

    $$
    {\rm a)}~ 100 \text{~mod~} 7, \qquad {\rm b)}~ -100 \text{~mod~} 7, \qquad {\rm c)}~ 2025 \text{~mod~} 9, \qquad {\rm d)}~ 7 \text{~mod~} 12
    $$

??? soluzione "Soluzione"

    Per definizione, $n \text{~mod~} m$ è il resto della divisione euclidea di $n$ per $m$:

    - **a)** $100 = 14 \cdot 7 + 2$, quindi $100 \text{~mod~} 7 = 2$.

    - **b)** $-100 = (-15) \cdot 7 + 5$, quindi $-100 \text{~mod~} 7 = 5$.

    - **c)** $2025 = 225 \cdot 9 + 0$, quindi $2025 \text{~mod~} 9 = 0$ ($2025$ è un multiplo di $9$).

    - **d)** $7 = 0 \cdot 12 + 7$, quindi $7 \text{~mod~} 12 = 7$.

<a id="box-exe_mod_congruences-3"></a>

!!! esercizio "Esercizio 3"

    Stabilire se valgono le seguenti congruenze, usando sia la definizione (stesso resto) sia la divisibilità della differenza:

    $$
    {\rm a)}~ 38 \equiv 14 \tpmod{6}, \qquad {\rm b)}~ 17 \equiv 4 \tpmod{5}, \qquad {\rm c)}~ 100 \equiv 1 \tpmod{11}
    $$

??? soluzione "Soluzione"

    - **a)** $38 = 6 \cdot 6 + 2$ e $14 = 2 \cdot 6 + 2$ hanno lo stesso resto $2$; equivalentemente $38 - 14 = 24 = 4 \cdot 6$. La congruenza vale.

    - **b)** $17 = 3 \cdot 5 + 2$ e $4 = 0 \cdot 5 + 4$ hanno resti diversi; equivalentemente $17 - 4 = 13$ non è un multiplo di $5$. La congruenza non vale.

    - **c)** $100 = 9 \cdot 11 + 1$ e $1 = 0 \cdot 11 + 1$ hanno lo stesso resto $1$; equivalentemente $100 - 1 = 99 = 9 \cdot 11$. La congruenza vale.

<a id="box-exe_mod_equivalence-4"></a>

!!! esercizio "Esercizio 4"

    Sia $m \ge 1$ un numero naturale. Dimostrare che per ogni coppia di numeri interi $n$ e $k$:

    $$
    n \text{~mod~} m = k \text{~mod~} m \Longleftrightarrow {\rm esiste~un~intero~} q {\rm ~tale~che~} n - k = q \cdot m
    $$

??? soluzione "Soluzione"

    - **($\Rightarrow$)** Sia $r = n \text{~mod~} m = k \text{~mod~} m$. Per la divisione euclidea esistono interi $q_1$ e $q_2$ tali che $n = q_1 \; m + r$ e $k = q_2 \; m + r$. Sottraendo:

        $$
        n - k = (q_1 - q_2) \; m
        $$

        quindi la tesi vale con $q = q_1 - q_2$.

    - **($\Leftarrow$)** Sia $n - k = q \; m$ e sia $k = q_2 \; m + r$ con $0 \le r < m$ (divisione euclidea di $k$ per $m$). Allora:

        $$
        n = k + q \; m = (q + q_2) \; m + r {\rm ~~~~con~~~~} 0 \le r < m
        $$

        Per l'unicità nella divisione euclidea, $r$ è il resto della divisione di $n$ per $m$, cioè $n \text{~mod~} m = r = k \text{~mod~} m$.

<a id="box-exe_mod_sum_product-5"></a>

!!! esercizio "Esercizio 5"

    Siano $m \ge 1$, $n$, $n'$, $k$, $k'$ numeri naturali tali che $n \equiv n' \tpmod{m}$ e $k \equiv k' \tpmod{m}$. Dimostrare che:

    $$
    {\rm a)}~ n + k \equiv n' + k' \tpmod{m}, \qquad {\rm b)}~ n \; k \equiv n' \; k' \tpmod{m}
    $$

    Calcolare poi $(123 \cdot 456 + 789) \text{~mod~} 10$ senza calcolare il prodotto.

??? soluzione "Soluzione"

    Per l'Esercizio [Esercizio 4](#box-exe_mod_equivalence-4) esistono interi $a$ e $b$ tali che $n = n' + a \; m$ e $k = k' + b \; m$.

    - **a)** $n + k = n' + k' + (a + b) \; m$, quindi $(n+k) - (n'+k')$ è un multiplo di $m$.

    - **b)** $n \; k = (n' + a\:m)\:(k' + b\:m) = n'\:k' + (n'\:b + k'\:a + a\:b\:m) \; m$, quindi $n\:k - n'\:k'$ è un multiplo di $m$.

    Poiché $123 \equiv 3$, $456 \equiv 6$ e $789 \equiv 9 \tpmod{10}$, si ha:

    $$
    123 \cdot 456 + 789 \equiv 3 \cdot 6 + 9 = 27 \equiv 7 \tpmod{10}
    $$

    quindi $(123 \cdot 456 + 789) \text{~mod~} 10 = 7$. Verifica: $123 \cdot 456 + 789 = 56088 + 789 = 56877$.

<a id="box-exe_mod_powers-6"></a>

!!! esercizio "Esercizio 6"

    Calcolare:

    $$
    {\rm a)}~ 2^{10} \text{~mod~} 7, \qquad {\rm b)}~ 3^{100} \text{~mod~} 4, \qquad {\rm c)}~ 5^{21} \text{~mod~} 6
    $$

??? soluzione "Soluzione"

    Usiamo ripetutamente l'Esercizio [Esercizio 5](#box-exe_mod_sum_product-5) b): se $n \equiv n' \tpmod{m}$, allora $n^p \equiv (n')^p \tpmod{m}$ per ogni numero naturale $p \ge 1$.

    - **a)** $2^3 = 8 \equiv 1 \tpmod{7}$, quindi $2^{10} = (2^3)^3 \cdot 2 \equiv 1^3 \cdot 2 = 2 \tpmod{7}$. Pertanto $2^{10} \text{~mod~} 7 = 2$ (verifica: $1024 = 146 \cdot 7 + 2$).

    - **b)** $3^2 = 9 \equiv 1 \tpmod{4}$, quindi $3^{100} = (3^2)^{50} \equiv 1^{50} = 1 \tpmod{4}$. Pertanto $3^{100} \text{~mod~} 4 = 1$.

    - **c)** $5^2 = 25 \equiv 1 \tpmod{6}$, quindi $5^{21} = (5^2)^{10} \cdot 5 \equiv 1^{10} \cdot 5 = 5 \tpmod{6}$. Pertanto $5^{21} \text{~mod~} 6 = 5$.

<a id="box-exe_mod_squares-7"></a>

!!! esercizio "Esercizio 7"

    Dimostrare che per ogni numero intero $n$ si ha $n^2 \text{~mod~} 4 \in \{0, 1\}$. Dedurre che $2023$ non è il quadrato di un numero intero.

??? soluzione "Soluzione"

    Per la divisione euclidea di $n$ per $2$, ogni intero $n$ è pari, $n = 2\:t$, oppure dispari, $n = 2\:t+1$, con $t$ intero:

    - se $n = 2\:t$, allora $n^2 = 4\:t^2 = 4\:t^2 + 0$, quindi $n^2 \text{~mod~} 4 = 0$;

    - se $n = 2\:t+1$, allora $n^2 = 4\:t^2 + 4\:t + 1 = 4\:(t^2 + t) + 1$, quindi $n^2 \text{~mod~} 4 = 1$.

    Poiché $2023 = 505 \cdot 4 + 3$, si ha $2023 \text{~mod~} 4 = 3 \notin \{0,1\}$, quindi $2023$ non è il quadrato di un numero intero.

<a id="box-exe_mod_digit_sum-8"></a>

!!! esercizio "Esercizio 8"

    Dimostrare che ogni numero naturale è congruo modulo $9$ alla somma delle sue cifre decimali. Usare questo risultato per calcolare $123456789 \text{~mod~} 9$ e $20251007 \text{~mod~} 9$.

??? soluzione "Soluzione"

    Un numero naturale $n$ con cifre decimali $c_p, c_{p-1}, \dots, c_1, c_0$ si può scrivere come:

    $$
    n = \sum_{j=0}^{p} c_j \; 10^j
    $$

    Poiché $10 = 1 \cdot 9 + 1$, si ha $10 \equiv 1 \tpmod{9}$ e quindi (Esercizio [Esercizio 6](#box-exe_mod_powers-6)) $10^j \equiv 1 \tpmod{9}$ per ogni $j \ge 1$ (e banalmente per $j=0$). Usando l'Esercizio [Esercizio 5](#box-exe_mod_sum_product-5) per ciascun termine della sommatoria:

    $$
    n = \sum_{j=0}^{p} c_j \; 10^j \equiv \sum_{j=0}^{p} c_j \tpmod{9}
    $$

    - $1+2+3+4+5+6+7+8+9 = 45 = 5 \cdot 9$, quindi $123456789 \text{~mod~} 9 = 0$.

    - $2+0+2+5+1+0+0+7 = 17 = 1 \cdot 9 + 8$, quindi $20251007 \text{~mod~} 9 = 8$.
