---
title: "Višekjubitna stanja i Bornovo pravilo"
short_title: "Bornovo pravilo"
description: Merenje i kolaps višekjubitnog registra — Bornovo pravilo preko projektora, sa primerima.
---

# Višekjubitna stanja i Bornovo pravilo

U [](../poglavlje2/05-measurements.md) merili smo **jedan** kjubit. Sada isti aparat — Bornovo pravilo, projektore i kolaps — proširujemo na **registar** od više kjubita. Videćemo šta se dešava kada izmerimo samo *jedan* kjubit u registru (a ostatak ostane u superpoziciji) i kada izmerimo *više* kjubita odjednom.

## Podsećanje: merenje jednog kjubita

Za jedan kjubit u stanju $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$ svakom ishodu $b \in \{0,1\}$ pridružujemo **projektor** $\Pi_b = \dyad{b}{b}$. Verovatnoća ishoda i stanje posle merenja (kolaps) su

```{math}
:label: eq:born-1q
p(b) = \bra{\psi}\Pi_b\ket{\psi} = |\braket{b}{\psi}|^2, \qquad
\ket{\psi'_b} = \frac{\Pi_b\ket{\psi}}{\sqrt{p(b)}}.
```

Projektori su hermitski i idempotentni ($\Pi_b^2 = \Pi_b$) i zadovoljavaju relaciju potpunosti $\Pi_0 + \Pi_1 = I$; zbog idempotentnosti je merenje **ponovljivo** (ponovno merenje daje isti ishod). Sve ovo, zajedno sa Qiskit primerom, detaljno je razrađeno u [](../poglavlje2/05-measurements.md); ovde ga samo brzo proverimo pre nego što pređemo na više kjubita:

```python
import numpy as np

ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)
P0 = np.outer(ket0, ket0.conj())      # |0><0|
P1 = np.outer(ket1, ket1.conj())      # |1><1|

# stanje |psi> = alpha|0> + beta|1>
alpha, beta = np.sqrt(3)/2, 1/2
psi = alpha*ket0 + beta*ket1

p0 = (psi.conj() @ P0 @ psi).real          # p(0) = <psi|P0|psi>
psi_post = (P0 @ psi)/np.sqrt(p0)          # kolaps -> |0>
print("p(0) =", round(p0, 3), "  kolaps ->", np.round(psi_post, 3))
print("potpunost P0 + P1 = I? ", np.allclose(P0 + P1, np.eye(2)))
```

## Višekjubitna računska baza

Registar od $N$ kjubita živi u prostoru dimenzije $2^N$, sa računskom bazom $\ket{b_1 b_2 \cdots b_N}$, $b_i \in \{0,1\}$. Opšte stanje je superpozicija svih $2^N$ baznih stanja,

```{math}
:label: eq:mq-stanje
\ket{\Psi} = \sum_{\mathbf{x}} a_{\mathbf{x}} \ket{\mathbf{x}}, \qquad \sum_{\mathbf{x}} |a_{\mathbf{x}}|^2 = 1,
```

gde $\mathbf{x} = b_1 b_2 \cdots b_N$ prolazi kroz svih $2^N$ bitskih niski. Za $N = 3$ to je

```{math}
:label: eq:ex-stanje
\ket{\Psi} = a_0\ket{000} + a_1\ket{001} + a_2\ket{010} + a_3\ket{011} + a_4\ket{100} + a_5\ket{101} + a_6\ket{110} + a_7\ket{111},
```

gde je indeks $i$ uz $a_i$ prosto bitska niska pročitana kao binarni broj (npr. $a_6$ stoji uz $\ket{110}$). Formalno je $\ket{b_1 b_2 \cdots b_N} = \ket{b_1}\otimes\cdots\otimes\ket{b_N}$; tenzorski proizvod $\otimes$ i njegova svojstva obrađujemo posebno, a ovde nam treba samo ovaj razvoj po baznim stanjima.

## Merenje jednog kjubita u registru

Kada merimo **samo kjubit $j$** u računskoj bazi, projektor na ishod $b_j$ zadržava sva bazna stanja kod kojih je $j$-ti bit jednak $b_j$:

```{math}
:label: eq:proj-registar
\Pi_{b_j} = \sum_{\mathbf{x}\,:\, x_j = b_j} \dyad{\mathbf{x}}{\mathbf{x}}.
```

Verovatnoća ishoda i stanje posle merenja imaju **isti oblik** kao za jedan kjubit,

```{math}
:label: eq:born-registar
p(b_j) = \bra{\Psi}\Pi_{b_j}^\dagger \Pi_{b_j}\ket{\Psi} = \bra{\Psi}\Pi_{b_j}\ket{\Psi} = \!\!\sum_{\mathbf{x}\,:\, x_j = b_j}\!\! |a_{\mathbf{x}}|^2, \qquad
\ket{\Psi'_{b_j}} = \frac{\Pi_{b_j}\ket{\Psi}}{\sqrt{p(b_j)}}.
```

Ključna razlika u odnosu na jedan kjubit: pošto je izmeren samo kjubit $j$, **preostali kjubiti ostaju u superpoziciji** (i mogu ostati međusobno spregnuti). Kolaps samo „poseče" one delove superpozicije koji nisu u skladu sa ishodom, pa se stanje ponovo normira.

:::{note} Primer 1 — merenje jednog kjubita
Za stanje {eq}`eq:ex-stanje`, projektori za ishod $0$ na **prvom** i ishod $1$ na **drugom** kjubitu su

```{math}
:label: eq:ex1-proj
\begin{aligned}
\Pi_{0_1} &= \dyad{000}{000} + \dyad{001}{001} + \dyad{010}{010} + \dyad{011}{011}, \\
\Pi_{1_2} &= \dyad{010}{010} + \dyad{011}{011} + \dyad{110}{110} + \dyad{111}{111}.
\end{aligned}
```

Odgovarajuća stanja posle merenja (normirana po {eq}`eq:born-registar`) su

```{math}
:label: eq:ex1-post
\begin{aligned}
\ket{\Psi'_{0_1}} &= \frac{a_0\ket{000} + a_1\ket{001} + a_2\ket{010} + a_3\ket{011}}{\sqrt{|a_0|^2 + |a_1|^2 + |a_2|^2 + |a_3|^2}}, \\[6pt]
\ket{\Psi'_{1_2}} &= \frac{a_2\ket{010} + a_3\ket{011} + a_6\ket{110} + a_7\ket{111}}{\sqrt{|a_2|^2 + |a_3|^2 + |a_6|^2 + |a_7|^2}}.
\end{aligned}
```

U imeniocu je uvek zbir $|a_{\mathbf{x}}|^2$ **tačno onih** amplituda koje preživljavaju u brojiocu (a to je baš $p(b_j)$). Prva dva, odnosno preostala dva kjubita ostaju u superpoziciji.
:::

## Merenje više kjubita istovremeno

Ako merimo $L$ kjubita $\{j_1, \dots, j_L\}$ odjednom, projektor zadržava bazna stanja koja se slažu sa **svim** izmerenim ishodima:

```{math}
:label: eq:proj-multi
\Pi_{\{b_{j_1}, \dots, b_{j_L}\}} = \sum_{\mathbf{x}\,:\, x_{j_1}=b_{j_1},\,\dots,\, x_{j_L}=b_{j_L}} \dyad{\mathbf{x}}{\mathbf{x}},
```

a verovatnoća i kolaps su opet istog oblika,

```{math}
:label: eq:born-multi
p(b_{j_1},\dots,b_{j_L}) = \bra{\Psi}\Pi_{\{b_{j_1},\dots,b_{j_L}\}}\ket{\Psi}, \qquad
\ket{\Psi'} = \frac{\Pi_{\{b_{j_1},\dots,b_{j_L}\}}\ket{\Psi}}{\sqrt{p(b_{j_1},\dots,b_{j_L})}}.
```

:::{note} Primer 2 — merenje dva kjubita
Merimo prvi i drugi kjubit stanja {eq}`eq:ex-stanje`. Četiri moguća ishoda daju projektore

```{math}
:label: eq:ex2-proj
\begin{aligned}
\Pi_{\{0_1, 0_2\}} &= \dyad{000}{000} + \dyad{001}{001}, &
\Pi_{\{0_1, 1_2\}} &= \dyad{010}{010} + \dyad{011}{011}, \\
\Pi_{\{1_1, 0_2\}} &= \dyad{100}{100} + \dyad{101}{101}, &
\Pi_{\{1_1, 1_2\}} &= \dyad{110}{110} + \dyad{111}{111}.
\end{aligned}
```

Ako, na primer, izmerimo $\{1_1, 1_2\}$, stanje se kolabira na potprostor $\{\ket{110}, \ket{111}\}$:

```{math}
:label: eq:ex2-post
\ket{\Psi'_{\{1_1, 1_2\}}} = \frac{\Pi_{\{1_1,1_2\}}\ket{\Psi}}{\sqrt{p(1_1,1_2)}} = \frac{a_6\ket{110} + a_7\ket{111}}{\sqrt{|a_6|^2 + |a_7|^2}}.
```

Pošto smo fiksirali prva dva kjubita, samo **treći** kjubit ostaje u superpoziciji.
:::

## Kod: Bornovo pravilo i kolaps za registar

Napravimo mali alat koji za proizvoljno stanje registra gradi projektor {eq}`eq:proj-multi`, računa verovatnoću i kolaps, pa njime proverimo oba primera. Projektor je (radi nastave) prosto dijagonalna matrica sa jedinicama na baznim stanjima koja prežive:

```python
import numpy as np
from itertools import product

N = 3
baza = [''.join(bits) for bits in product('01', repeat=N)]   # '000','001',...,'111'

def slucajno_stanje(N=3, seed=0):
    rng = np.random.default_rng(seed)
    a = rng.normal(size=2**N) + 1j*rng.normal(size=2**N)
    return a/np.linalg.norm(a)                                # normirano stanje

def projektor(mereni, ishodi, N=3):
    """Dijagonalni projektor: zadrži bazna stanja gde su 'mereni' kjubiti = 'ishodi'.
       mereni: 1-indeksirani kjubiti; ishodi: pripadni bitovi."""
    diag = [1.0 if all(int(s[q-1]) == b for q, b in zip(mereni, ishodi)) else 0.0
            for s in baza]
    return np.diag(diag).astype(complex)

def izmeri(psi, mereni, ishodi):
    P = projektor(mereni, ishodi)
    p = (psi.conj() @ P @ psi).real                          # p = <psi|P|psi>
    psi_post = (P @ psi)/np.sqrt(p)                          # kolaps + normiranje
    return p, psi_post
```

**Primer 1** — merimo prvi kjubit (ishod $0$), pa drugi kjubit (ishod $1$):

```python
psi = slucajno_stanje(seed=1)
a = psi                                    # a[i] je amplituda uz |i>  (i = 0..7)

# --- prvi kjubit = 0  (prežive |000>,|001>,|010>,|011>, tj. indeksi 0,1,2,3) ---
p, post = izmeri(psi, mereni=[1], ishodi=[0])
print("p(0_1) =", round(p, 4), " (rucno:", round(np.sum(np.abs(a[[0, 1, 2, 3]])**2), 4), ")")

ocek = np.zeros(8, complex); ocek[[0, 1, 2, 3]] = a[[0, 1, 2, 3]]
ocek /= np.linalg.norm(ocek)
print("kolaps = ocekivano stanje? ", np.allclose(post, ocek))

# --- drugi kjubit = 1  (prežive |010>,|011>,|110>,|111>, indeksi 2,3,6,7) ---
p2, post2 = izmeri(psi, mereni=[2], ishodi=[1])
print("p(1_2) =", round(p2, 4), " (rucno:", round(np.sum(np.abs(a[[2, 3, 6, 7]])**2), 4), ")")
```

**Primer 2** — merimo prva dva kjubita, ishod $\{1_1, 1_2\}$ (prežive samo $\ket{110}, \ket{111}$):

```python
p11, post11 = izmeri(psi, mereni=[1, 2], ishodi=[1, 1])
print("p(1_1,1_2) =", round(p11, 4), " (rucno:", round(np.sum(np.abs(a[[6, 7]])**2), 4), ")")

ocek11 = np.zeros(8, complex); ocek11[[6, 7]] = a[[6, 7]]
ocek11 /= np.linalg.norm(ocek11)
print("kolaps na {|110>, |111>}? ", np.allclose(post11, ocek11))

# relacija potpunosti: zbir verovatnoća svih ishoda na kjubitu 1 je 1
print("p(0_1) + p(1_1) =", round(izmeri(psi, [1], [0])[0] + izmeri(psi, [1], [1])[0], 6))
```

:::{note} Qiskit i redosled kjubita (klik)
:class: dropdown
Isto se može uraditi i u Qiskit-u sa `Statevector(psi).measure([j])`, ali oprez: Qiskit numeriše kjubite **obrnuto** (little-endian, kjubit $0$ je krajnje desni bit), pa se indeksi i niske razlikuju od konvencije $\ket{b_1 b_2 b_3}$ koju ovde koristimo. Zbog jasnoće smo gore ostali na `numpy`-ju, gde sami držimo redosled pod kontrolom.
:::

:::{important} Šta pamtimo iz ove lekcije
:class: simple
Bornovo pravilo i kolaps za registar imaju **isti oblik** kao za jedan kjubit; samo je projektor $\Pi = \sum_{\mathbf{x}} \dyad{\mathbf{x}}{\mathbf{x}}$ zbir po baznim stanjima koja se slažu sa izmerenim ishodima: $p = \bra{\Psi}\Pi\ket{\Psi}$ i $\ket{\Psi'} = \Pi\ket{\Psi}/\sqrt{p}$. Verovatnoća je zbir $|a_{\mathbf{x}}|^2$ preživelih amplituda, a stanje se posle merenja normira istim tim korenom. Kada izmerimo samo deo registra, **preostali kjubiti ostaju u superpoziciji** — to je polazna tačka za spletenost i teleportaciju.
:::


## Pogled unapred: dva kjubita i Bell stanje

Prava moć kola vidi se tek sa **više kjubita** i kapijama koje ih *povezuju*. Najvažnija dvokjubitna kapija je **CNOT** (kontrolisano-NE): ako je kontrolni kjubit $\ket{1}$, ona obrne ciljni kjubit; ako je $\ket{0}$, ne radi ništa. Kolo u kom prvom kjubitu damo $H$, a zatim primenimo CNOT, pravi čuveno **Bell stanje**:

```{figure} ../images/kolo-bell.png
:label: fig:kolo-bell
:alt: Kolo za Bell stanje: H na prvom kjubitu, zatim CNOT, pa merenje oba kjubita.
:width: 440px
:align: center

Kolo za Bell stanje: $H$ na kjubitu $q_0$ napravi superpoziciju, a CNOT (tačka = kontrola, $\oplus$ = meta) je „prepiše" na kjubit $q_1$. Merenjem dobijamo dva korelisana klasična bita.
```

```python
bell = QuantumCircuit(2)
bell.h(0)            # superpozicija na prvom kjubitu
bell.cx(0, 1)        # CNOT: kontrola = kjubit 0, meta = kjubit 1
print(bell.draw())

sv = Statevector(bell)
print("Verovatnoće:", sv.probabilities_dict())   # {'00': 0.5, '11': 0.5}
print("1000 merenja:", sv.sample_counts(1000))    # ~ {'00': 500, '11': 500}
```

Rezultat je iznenađujući: pojavljuju se **samo** ishodi $00$ i $11$, nikad $01$ ili $10$ — dva kjubita su savršeno **korelisana**. Takva stanja, koja ne možemo razložiti na „prvi kjubit puta drugi kjubit", zovu se **spregnuta** (entangled) i srce su kvantne prednosti. Formalni aparat (tenzorski proizvod $\otimes$ i zašto je stanje spregnuto) uvodimo u narednoj lekciji o više kjubita.

:::{important} Šta pamtimo iz ove lekcije
:class: simple
Kvantno kolo je dijagram koji se čita s leva na desno; niz kapija $A, B, C$ odgovara **obrnutom** proizvodu matrica $C B A$. Kjubit pripremamo iz $\ket{0}$, evoluiramo kapijama i merimo u računskoj bazi, čime dobijamo klasičan bit. Ista kola gradimo i „ručno" (numpy matrice) i u Qiskit-u, gde `QuantumCircuit` sam vodi računa o redosledu. Sa dva kjubita i CNOT-om dobijamo spregnuta (Bell) stanja.
:::



## Vežbe

:::{admonition} Vežba 1
:class: tip
Za stanje {eq}`eq:ex-stanje` napiši projektor $\Pi_{1_3}$ (merenje **trećeg** kjubita, ishod $1$) i pripadno stanje posle merenja $\ket{\Psi'_{1_3}}$.
:::

:::{admonition} Rešenje
:class: dropdown
Treći bit je $1$ za bazna stanja $\ket{001}, \ket{011}, \ket{101}, \ket{111}$ (indeksi $1,3,5,7$), pa je
$\Pi_{1_3} = \dyad{001}{001} + \dyad{011}{011} + \dyad{101}{101} + \dyad{111}{111}$ i
$\ket{\Psi'_{1_3}} = \big(a_1\ket{001} + a_3\ket{011} + a_5\ket{101} + a_7\ket{111}\big)/\sqrt{|a_1|^2+|a_3|^2+|a_5|^2+|a_7|^2}$.

```python
p, post = izmeri(slucajno_stanje(seed=1), mereni=[3], ishodi=[1])
print("p(1_3) =", round(p, 4))
```
:::

:::{admonition} Vežba 2
:class: tip
Pokaži (na papiru i kodom) da za merenje bilo kog kjubita $j$ važi $p(0_j) + p(1_j) = 1$. Koji uslov na stanje $\ket{\Psi}$ koristiš?
:::

:::{admonition} Rešenje
:class: dropdown
Svako bazno stanje ima $j$-ti bit ili $0$ ili $1$, pa se sume $\sum_{x_j=0}|a_{\mathbf{x}}|^2$ i $\sum_{x_j=1}|a_{\mathbf{x}}|^2$ zajedno svode na $\sum_{\mathbf{x}}|a_{\mathbf{x}}|^2 = 1$ (normiranost stanja). Ekvivalentno, $\Pi_{0_j} + \Pi_{1_j} = I$.

```python
psi = slucajno_stanje(seed=7)
print("p(0_2) + p(1_2) =", round(izmeri(psi, [2], [0])[0] + izmeri(psi, [2], [1])[0], 6))
```
:::

:::{admonition} Vežba 3
:class: tip
Izmeri prvo kjubit $1$ (ishod $0$), a zatim na dobijenom stanju izmeri kjubit $2$ (ishod $1$). Uporedi konačno stanje i ukupnu verovatnoću sa **istovremenim** merenjem $\{0_1, 1_2\}$. Da li je svejedno kojim redom merimo?
:::

:::{admonition} Rešenje
:class: dropdown
Da — uzastopna merenja *različitih* kjubita komutiraju, jer $\Pi_{0_1}$ i $\Pi_{1_2}$ deluju na različite kjubite, pa $\Pi_{0_1}\Pi_{1_2} = \Pi_{1_2}\Pi_{0_1} = \Pi_{\{0_1,1_2\}}$. Ukupna verovatnoća je $p(0_1)\,p(1_2\,|\,0_1) = p(0_1, 1_2)$ (lančano pravilo), a konačno stanje je isto u oba redosleda.

```python
psi = slucajno_stanje(seed=3)
# uzastopno: prvo kjubit 1 = 0, pa kjubit 2 = 1
p1, s1 = izmeri(psi, [1], [0])
p2, s2 = izmeri(s1,  [2], [1])
# istovremeno: {0_1, 1_2}
pj, sj = izmeri(psi, [1, 2], [0, 1])
print("uzastopno p =", round(p1*p2, 4), "  istovremeno p =", round(pj, 4))
print("ista konačna stanja? ", np.allclose(s2, sj))
```
:::
