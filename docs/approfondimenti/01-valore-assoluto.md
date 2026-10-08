---
title: "Valore assoluto"
---

# Valore assoluto

<div class="info-capitolo" markdown>

**Approfondimenti · Capitolo A.1** · dalle dispense di Fabio Furini · [:material-file-pdf-box: Dispensa (PDF)](../pdf/dispense-algebra-lineare.pdf)

</div>

## 1. Definizione

<a id="box-def_absolute-value-1"></a>

!!! definizione "Definizione 1: valore assoluto"

    Il <strong>valore assoluto</strong> $|a|$ di un numero reale $a$ è il seguente numero reale non negativo:

    \begin{equation}
    |a|  =
    \begin{cases}
    a & {\rm se~~} a \ge 0\\
    -a & {\rm se~~} a < 0
    \end{cases}
    \label{ass_1}
    \end{equation}

!!! chiave ""

    Dalla definizione di valore assoluto segue immediatamente che:

    \begin{equation}
    |a| < \varepsilon \Longleftrightarrow -\varepsilon < a < \varepsilon, \qquad \forall \varepsilon > 0, a \in \mathbb{R}
    \label{ass_2}
    \end{equation}

    e, analogamente, per le disuguaglianze non strette:

    \begin{equation}
    |a| \le \varepsilon \Longleftrightarrow -\varepsilon \le a \le \varepsilon, \qquad \forall \varepsilon \ge 0, a \in \mathbb{R}
    \label{ass_2b}
    \end{equation}

## 2. Disuguaglianza triangolare

<a id="box-obs_triangle-inequality-2"></a>

!!! teorema "Osservazione 1: disuguaglianza triangolare"

    \begin{equation}
    |b + c| \le |b| + |c|,  \qquad \forall  b,c \in \mathbb{R}
    \label{ass_3}
    \end{equation}

??? dimostrazione "Dimostrazione"

    Scriviamo le due relazioni:

    $$
    -|b| \le b \le |b|, \quad \quad -|c| \le c \le |c|
    $$

    e sommiamo membro a membro:

    $$
    -(|b| + |c|) \le b + c \le |b| + |c|
    $$

    Quindi per la \(\eqref{ass_2b}\), con $\varepsilon=|b|+|c|\ge 0$ e $a=b+c$, segue la \(\eqref{ass_3}\). <span class="qed">□</span>

- La disuguaglianza triangolare si usa anche nella forma seguente:

    \begin{equation}
    |d - e| \le |d-f| + |e-f| \qquad \forall d,e,f \in \mathbb{R}
    \label{ass_4}
    \end{equation}

    Per ottenerla, basta porre nella \(\eqref{ass_3}\):

    $$
    b = d - f, \quad c =   f-e
    $$

    e si ottiene:

    $$
    |d - f  +f-e|=|d -e| \le |d - f| + |f-e| = |d - f| + |e-f|
    $$

    poiché:

    $$
    |f - e| = |e-f| \qquad \forall e,f \in \mathbb{R}
    $$

- Infine, un'altra forma della disuguaglianza triangolare è:

    \begin{equation}
    |g| \le |g-h| + |h| \text{~~~~~cioè~~~~~} |g| - |h| \le |g-h| \qquad \forall g,h \in \mathbb{R}
     \label{ass_AA}
    \end{equation}

    Per ottenerla, basta porre nella \(\eqref{ass_3}\):

    $$
    b =  g - h, \quad  c = h
    $$

<a id="box-obs_reverse-triangle-inequality-3"></a>

!!! teorema "Osservazione 2: disuguaglianza triangolare inversa"

    \begin{equation}
    \big|\, |g| - |h| \,\big| \le |g-h|, \quad \forall g,h \in \mathbb{R}
    \label{ass_5}
    \end{equation}

??? dimostrazione "Dimostrazione"

    Dalla \(\eqref{ass_AA}\), si ha:

    $$
    |g| - |h| \le |g-h| \qquad \forall g,h \in \mathbb{R}
    $$

    Analogamente, scambiando $g$ con $h$ nella \(\eqref{ass_AA}\) si ottiene:

    $$
    |h| - |g| \le |h-g| = |g-h|  \text{~~~~cioè~~~~} |g| - |h| \ge -|g-h|
    $$

    quindi si ha

    $$
    -(|g-h|) \le  |g| - |h| \le |g-h| \qquad \forall g,h \in \mathbb{R}
    $$

    Di conseguenza, dalla \(\eqref{ass_2b}\), con $\varepsilon = |g-h| \ge 0$ e $a= |g| - |h|$, si ottiene la disuguaglianza triangolare inversa. <span class="qed">□</span>

- La disuguaglianza triangolare \(\eqref{ass_3}\) si generalizza facilmente al caso di $k$ addendi:

    \begin{equation}
    \left| \sum_{i=1}^k  b_i \right| \le  \sum_{i=1}^k  |b_i|.
    \label{ass_6}
    \end{equation}

- Valgono inoltre le seguenti proprietà immediate:

    \begin{equation}
    |b\:c| = |b| \: |c|, \qquad \left| \frac{b}{c}\right|= \frac{|b|}{|c|}, \qquad |-b|=|b| \qquad \forall  b,c \in \mathbb{R} ~ (c \neq 0 {\rm ~nel~quoziente}).
    \label{ass_7}
    \end{equation}

## Esercizi e laboratorio

- :material-pencil-box-multiple: **Esercizi** · [il foglio di esercizi di questo capitolo: 8 esercizi con le soluzioni svolte](../esercizi/es-approfondimenti-01-valore-assoluto.md)

