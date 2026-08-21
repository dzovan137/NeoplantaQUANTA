---
title: "Merenje više kubita"
short_title: "Merenje više kubita"
description: Merenje i kolaps u slučaju više kubita
---



## Merenje više kubita istovremeno

Ako merimo $L$ kjubita $\{j_1, \dots, j_L\}$ odjednom, projektor zadržava bazna stanja koja se slažu sa **svim** izmerenim ishodima:

```{math}
:label: eq:proj-multi
\Pi_{\{b_{j_1}, \dots, b_{j_L}\}} = \sum_{\mathbf{x}\,:\, x_{j_1}=b_{j_1},\,\dots,\, x_{j_L}=b_{j_L}} \dyad{\mathbf{x}}{\mathbf{x}},
```

a verovatnoća

```{math}
:label: eq:born-multi1
p(b_{j_1},\dots,b_{j_L}) = \bra{\Psi}\Pi_{\{b_{j_1},\dots,b_{j_L}\}}\ket{\Psi}, 
```
i kolaps su opet istog oblika

```{math}
:label: eq:born-multi2
\ket{\Psi'} = \frac{\Pi_{\{b_{j_1},\dots,b_{j_L}\}}\ket{\Psi}}{\sqrt{p(b_{j_1},\dots,b_{j_L})}}
```

### Primer 1
Hajde da se skoncentrišemo na primer $N = 3$ kubita. Merimo prvi i drugi kubit stanja {eq}`eq:ex-stanje`. Četiri moguća ishoda daju projektore

```{math}
:label: eq:ex2-proj
\begin{aligned}
\Pi_{\{0_1, 0_2\}} &= \dyad{{\color{red}00}0}{{\color{red}00}0} + \dyad{{\color{red}00}1}{{\color{red}00}1}, \\
\Pi_{\{0_1, 1_2\}} &= \dyad{{\color{red}01}0}{{\color{red}01}0} + \dyad{{\color{red}01}1}{{\color{red}01}1}, \\
\Pi_{\{1_1, 0_2\}} &= \dyad{{\color{red}10}0}{{\color{red}10}0} + \dyad{{\color{red}10}1}{{\color{red}10}1}, \\
\Pi_{\{1_1, 1_2\}} &= \dyad{{\color{red}11}0}{{\color{red}11}0} + \dyad{{\color{red}11}1}{{\color{red}11}1}.
\end{aligned}
```

Uzimamo za primer generalno stanje 3 kubita i to:
```{math}
:label: eq:n3ponovo
\ket{\Psi} = a_0\ket{000} + a_1\ket{001} + a_2\ket{010} + a_3\ket{011} + a_4\ket{100} + a_5\ket{101} + a_6\ket{110} + a_7\ket{111},
```

Evo svih mogućih kolapsa i odgovarajućih stanja za sve četiri moguće kombinacije ishoda prvog i drugog kubita:

```{math}
:label: eq:ex2-post
\begin{aligned}
\ket{\Psi'_{\{0_1, 0_2\}}} &= \frac{a_0\ket{000} + a_1\ket{001}}{\sqrt{|a_0|^2 + |a_1|^2}}, \\
\ket{\Psi'_{\{0_1, 1_2\}}} &= \frac{a_2\ket{010} + a_3\ket{011}}{\sqrt{|a_2|^2 + |a_3|^2}}, \\
\ket{\Psi'_{\{1_1, 0_2\}}} &= \frac{a_4\ket{100} + a_5\ket{101}}{\sqrt{|a_4|^2 + |a_5|^2}}, \\
\ket{\Psi'_{\{1_1, 1_2\}}} &= \frac{a_6\ket{110} + a_7\ket{111}}{\sqrt{|a_6|^2 + |a_7|^2}}.
\end{aligned}
```

Pošto smo fiksirali prva dva kjubita, samo **treći** kubit ostaje u superpoziciji. Možemo primetiti da ova stanja možemo zapisati i kao
```{math}
:label: eq:ex3-post
\begin{aligned}
\ket{\Psi'_{\{0_1, 0_2\}}} &= \frac{\ket{00}}{\sqrt{|a_0|^2 + |a_1|^2}} \otimes \left( a_0 \ket{0} + a_1 \ket{1} \right), \\
\ket{\Psi'_{\{0_1, 1_2\}}} &= \frac{\ket{01}}{\sqrt{|a_2|^2 + |a_3|^2}} \otimes \left( a_2 \ket{0} + a_3 \ket{1} \right), \\
\ket{\Psi'_{\{1_1, 0_2\}}} &= \frac{\ket{10}}{\sqrt{|a_4|^2 + |a_5|^2}} \otimes \left( a_4 \ket{0} + a_5 \ket{1} \right), \\
\ket{\Psi'_{\{1_1, 1_2\}}} &= \frac{\ket{11}}{\sqrt{|a_6|^2 + |a_7|^2}} \otimes \left( a_6 \ket{0} + a_7 \ket{1} \right).
\end{aligned}
```

Grafički, u reprezentaciji **kvantnog kola**, ovakvo merenje možemo predstaviti na sledeći način.

```{figure} ../images/stvari.png
:label: fig:stvari
:alt: purity
:width: 520px
:align: center

Osnovno kolo za prvi primer. 
```


Uzmimo za primer koji je superpozicija svih stanja računske baze, tj.

```{math}
:label: eq:prim
a_0 = a_1 = \cdots = a_7 = \dfrac{1}{\sqrt{8}},

```