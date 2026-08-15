---
title: "Višekjubitna stanja i Bornovo pravilo"
short_title: "Bornovo pravilo"
description: Merenje i kolaps višekjubitnog registra — Bornovo pravilo preko projektora, sa primerima.
---



Kada je kjubit deo **registra** od više kjubita, isti projektor deluje kao $\Pi_b \otimes I$ na ostatak: zadržava samo one delove superpozicije koji su u skladu sa izmerenim ishodom, dok **preostali kjubiti ostaju u superpoziciji** (i mogu ostati međusobno spregnuti). Taj, bogatiji slučaj radimo kasnije, kada uvedemo višekjubitne registre u [](../poglavlje3/06-multiqubit.md).

Sve ovo lako proverimo u nekoliko linija. Prvo napravimo projektore i uverimo se u njihova osnovna svojstva:

```python
import numpy as np

# računska baza i projektori na ishode 0 i 1
ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)
P0 = ket0 @ ket0.conj().T          # |0><0|
P1 = ket1 @ ket1.conj().T          # |1><1|

print("P0 =\n", P0.real)
print("P0 hermitski (P0^dagger = P0)? ", np.allclose(P0, P0.conj().T))
print("P0 idempotentan (P0^2 = P0)?   ", np.allclose(P0 @ P0, P0))
print("potpunost (P0 + P1 = I)?       ", np.allclose(P0 + P1, np.eye(2)))
```

Sada uzmimo konkretno stanje, izračunajmo verovatnoću ishoda i stanje posle merenja:

```python
# proizvoljno stanje |psi> = alpha|0> + beta|1>
alpha, beta = np.sqrt(3)/2, 1/2            # |alpha|^2 = 3/4, |beta|^2 = 1/4
psi = alpha*ket0 + beta*ket1

# verovatnoća ishoda 0:  p(0) = <psi|P0|psi>
p0 = (psi.conj().T @ P0 @ psi).item().real
print("p(0) =", round(p0, 3), "  (|alpha|^2 =", round(abs(alpha)**2, 3), ")")

# stanje posle merenja:  |psi'> = P0|psi> / sqrt(p0)
psi_post = (P0 @ psi) / np.sqrt(p0)
print("stanje posle merenja ishoda 0:\n", np.round(psi_post, 3))
print("da li je to |0>? ", np.allclose(psi_post, ket0))
```

Pošto je stanje već kolabiralo u $\ket{0}$, ponovno merenje daje isti ishod sa sigurnošću:

```python
# p(0) nakon kolapsa je 1 (merenje je ponovljivo)
p0_opet = (psi_post.conj().T @ P0 @ psi_post).item().real
print("p(0) posle kolapsa =", round(p0_opet, 3))   # 1.0
```

Isto možemo i u Qiskit-u — `Statevector` ima ugrađenu metodu `measure`, koja vrati ishod i već **kolabirano** stanje (ishod je slučajan, pa se pri svakom pokretanju može razlikovati):

```python
from qiskit.quantum_info import Statevector

sv = Statevector([alpha, beta])       # isto stanje, sada kao Qiskit vektor
ishod, sv_post = sv.measure()          # izmeri kjubit -> (ishod, kolabirano stanje)
print("izmereni ishod:", ishod)
print("stanje posle merenja:", np.round(sv_post.data, 3))   # |ishod>
```

## Merenje u drugim bazama i očekivane vrednosti

Merenje u računskoj bazi zapravo meri **operator $Z$**: ishodi $0$ i $1$ odgovaraju njegovim svojstvenim vrednostima $+1$ i $-1$. Prosečna izmerena vrednost je **očekivana vrednost**

```{math}
:label: eq:expectation-z
\langle Z \rangle = (+1)\,p(0) + (-1)\,p(1) = p(0) - p(1).
```

Šta ako želimo $\langle X \rangle$ ili $\langle Y \rangle$? Hardver ume da meri samo u $Z$-bazi, pa željenu osu prvo **zarotiramo u $Z$-osu**, izmerimo, i pročitamo isti izraz $p(0)-p(1)$. Iz [](03-one-qubit-gates.md) znamo prave rotacije: za $X$ je dovoljan $H$ (jer $HXH = Z$), a za $Y$ kombinacija $S^\dagger$ pa $H$.

```python
def izmeri_ocekivanu(prep, osa, shots=20000):
    """Proceni <P> (P = 'X','Y','Z') merenjem pripremljenog stanja u odgovarajućoj bazi."""
    qc = QuantumCircuit(1, 1)
    qc.compose(prep, inplace=True)     # 1) pripremi stanje
    if osa == 'X':
        qc.h(0)                        # 2) X-baza -> Z-baza
    elif osa == 'Y':
        qc.sdg(0); qc.h(0)             #    Y-baza -> Z-baza
    qc.measure(0, 0)                   # 3) izmeri u Z-bazi
    c = sampler.run([qc], shots=shots).result()[0].data.c.get_counts()
    p0 = c.get('0', 0)/shots
    p1 = c.get('1', 0)/shots
    return p0 - p1                     # <P> = p(0) - p(1)

prep = QuantumCircuit(1)
prep.ry(0.7, 0)                        # neko stanje na Blohovoj sferi
print("<X>, <Y>, <Z> =", [round(izmeri_ocekivanu(prep, os), 2) for os in ['X', 'Y', 'Z']])
```

Ove tri očekivane vrednosti nisu ništa drugo do **koordinate Blohovog vektora** $\mathbf{r} = (\langle X\rangle, \langle Y\rangle, \langle Z\rangle)$ koji smo uveli u [](../dan1/02-qubits.md).

## Kvantna tomografija

Ako izmerimo sve tri komponente $\langle X\rangle, \langle Y\rangle, \langle Z\rangle$, možemo da **rekonstruišemo** Blohov vektor — dakle celo (nepoznato) jednokjubitno stanje. To je najprostiji primer **kvantne tomografije**.

:::{important} Zašto treba mnogo kopija?
:class: simple
Jedno merenje daje samo jedan bit i **uništi** stanje. Zato za tomografiju moramo iznova da pripremimo isto stanje mnogo puta i podelimo merenja na tri grupe (po jednu za $X$, $Y$ i $Z$ osu). Kopiranje nepoznatog stanja nije rešenje — to zabranjuje teorema o nekloniranju.
:::

```python
prep = QuantumCircuit(1)
prep.ry(0.7, 0); prep.rz(1.1, 0)       # "nepoznato" stanje koje rekonstruišemo

# procenjen Blohov vektor iz merenja:
r_est = np.array([izmeri_ocekivanu(prep, os) for os in ['X', 'Y', 'Z']])
print("Procenjen Blohov vektor:", np.round(r_est, 2))

# tačan Blohov vektor iz statevektora (za proveru):
sv = Statevector(prep)
r_true = np.array([sv.expectation_value(Pauli(P)).real for P in ['X', 'Y', 'Z']])
print("Tačan Blohov vektor:    ", np.round(r_true, 2))
print("Dužina |r| (čisto stanje => 1):", round(float(np.linalg.norm(r_est)), 3))
```

Vektor treba da leži (do na statističku grešku) na **površini** Blohove sfere, $|\mathbf{r}| = 1$, jer je stanje čisto. Više merenja (`shots`) daje precizniju procenu.

## Izvršenje na pravom kvantnom računaru

Do sada je `sampler` bio lokalni simulator. Lepota Qiskit-ovih **primitiva** je što se isto kolo pokreće na **pravom** kvantnom računaru promenom svega nekoliko linija — kolo, `measure` i „shots" ostaju isti. Na IBM-ovom hardveru (uz besplatan nalog na [IBM Quantum](https://quantum.ibm.com)) obrazac je:

```python
# Potreban je nalog na IBM Quantum; kolo se prvo "transpiluje" za konkretan uređaj.
# from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
# from qiskit import transpile
#
# service = QiskitRuntimeService()                  # učita sačuvani nalog
# backend = service.least_busy(operational=True)    # izaberi slobodan uređaj
# qc_hw   = transpile(qc, backend)                  # prilagodi kolo hardveru
# sampler = SamplerV2(backend)
# counts  = sampler.run([qc_hw], shots=1000).result()[0].data.c.get_counts()
```

Ključna razlika je **šum**: pravi kjubiti nisu savršeni, pa se javljaju greške (slučajna obrtanja bita, dekoherencija). Zato rezultati sa hardvera odstupaju od idealnih verovatnoća — recimo, za $\ket{+}$ nećemo dobiti tačno pola-pola, već blisko tome, sa malim „repom" pogrešnih ishoda. Upravo zato uvek pokrećemo mnogo `shots` i radimo sa **statistikom**, a ispravljanje grešaka (za koje su ključne Klifordove i $T$ kapije iz [](03-one-qubit-gates.md)) tema je naprednijih lekcija.

:::{important} Šta pamtimo iz ove lekcije
:class: simple
Merenje u računskoj bazi meri operator $Z$ i vraća jedan klasičan bit; verovatnoće dobijamo ponavljanjem (`shots`). Formalno, ishod $b$ opisuje projektor $\Pi_b = \dyad{b}{b}$: verovatnoća je $p(b) = \bra{\psi}\Pi_b\ket{\psi}$, a stanje se posle merenja **kolabira** u $\ket{\psi'_b} = \Pi_b\ket{\psi}/\sqrt{p(b)}$. Očekivana vrednost je $\langle Z\rangle = p(0)-p(1)$, a $\langle X\rangle$ i $\langle Y\rangle$ merimo tako što osu prvo zarotiramo u $Z$. Tri očekivane vrednosti čine Blohov vektor, pa merenjem u tri baze rekonstruišemo celo stanje (tomografija). Isto kolo pokrećemo na pravom hardveru promenom „samplera"; tamo se javlja šum, pa je statistika neophodna.
:::


Trebalo bi napomenuti gde zapravo kvantni računar igra ulogu. Recimo on izvrši fizički neki proračun u fizičkom prostoru a ne u kompjuterskoj memoriji koja skalira $2^{N}$, gde je $N$ broj kubita. Do sada u simulatoru smo imali tolike vektore i $2^N \times 2^N$ matrice, dok krajnji rezultat nekog merenja je klasični bit koji samo vektora brojeva. 


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



```{figure} ../images/example_multi_qubit_decomposition.png
:label: fig:decomposition
:alt: Bloh
:width: 420px
:align: center

Decomposition of a 3 qubit gate. When applied to U = X, this gives a decomposition of the Toffoli gate with 6 CNOTs and 7 T gates.
```



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




## Vežbe

:::{admonition} Vežba 1
:class: tip
Za stanje $\ket{+}$ izračunaj „na papiru" $\langle Z\rangle$ i $\langle X\rangle$, pa proveri merenjem. (Uputstvo: $\ket{+}$ leži na $+x$ osi Blohove sfere.)
:::

:::{admonition} Rešenje
:class: dropdown
$\ket{+}$ je na ekvatoru, na $+x$ osi, pa je $\langle Z\rangle = 0$ (pola-pola) i $\langle X\rangle = 1$ (sa sigurnošću $+1$).

```python
prep = QuantumCircuit(1); prep.h(0)      # |+>
print("<Z> =", round(izmeri_ocekivanu(prep, 'Z'), 2))   # ~ 0
print("<X> =", round(izmeri_ocekivanu(prep, 'X'), 2))   # ~ 1
```
:::

:::{admonition} Vežba 2
:class: tip
Pokaži da za **bilo koje** stanje važi $\langle Z\rangle = p(0) - p(1)$, i da iz toga sledi $p(0) = \tfrac{1+\langle Z\rangle}{2}$.
:::

:::{admonition} Rešenje
:class: dropdown
Operator $Z$ ima svojstvene vrednosti $+1$ (za $\ket{0}$) i $-1$ (za $\ket{1}$), pa je $\langle Z\rangle = (+1)p(0) + (-1)p(1) = p(0)-p(1)$ (to je {eq}`eq:expectation-z`). Kako je $p(0)+p(1)=1$, sabiranjem dobijamo $p(0) = \tfrac{1+\langle Z\rangle}{2}$.

```python
prep = QuantumCircuit(1); prep.ry(1.0, 0)
sv = Statevector(prep); p = sv.probabilities()
print("p(0)-p(1) =", round(p[0]-p[1], 3),
      " <Z> =", round(sv.expectation_value(Pauli('Z')).real, 3))
```
:::

:::{admonition} Vežba 3
:class: tip
**Tomografija magičnog stanja.** Pripremi $\ket{T} = T\ket{+}$ (kolo $\ket{0}\,\text{–}\,H\,\text{–}\,T\,\text{–}$ iz prošle lekcije) i rekonstruiši mu Blohov vektor. Proveri da leži na sferi ($|\mathbf{r}|=1$) i da mu je azimut $\varphi = 45^\circ$.
:::

:::{admonition} Rešenje
:class: dropdown
$\ket{T}$ ima $\theta = \arccos\tfrac{1}{\sqrt3}$ i $\varphi = \tfrac{\pi}{4}$, pa je $\mathbf{r} = (\tfrac{1}{\sqrt3}, \tfrac{1}{\sqrt3}, \tfrac{1}{\sqrt3}) \approx (0.58, 0.58, 0.58)$ — jednake $x$ i $y$ komponente daju azimut od $45^\circ$.

```python
prep = QuantumCircuit(1); prep.h(0); prep.t(0)     # |T> = T H |0>
r = np.array([izmeri_ocekivanu(prep, os) for os in ['X', 'Y', 'Z']])
print("r =", np.round(r, 2), " |r| =", round(float(np.linalg.norm(r)), 2))
print("azimut =", round(np.degrees(np.arctan2(r[1], r[0])), 1), "stepeni")   # ~ 45
```
:::

:::{admonition} Vežba 4
:class: tip
Za stanje $\ket{+} = \tfrac{1}{\sqrt2}(\ket{0}+\ket{1})$ napiši projektore $\Pi_0, \Pi_1$, izračunaj verovatnoće $p(0), p(1)$ i oba moguća stanja posle merenja u računskoj bazi.
:::

:::{admonition} Rešenje
:class: dropdown
Projektori su $\Pi_0 = \dyad{0}{0}$ i $\Pi_1 = \dyad{1}{1}$. Kako je $\braket{0}{+} = \braket{1}{+} = \tfrac{1}{\sqrt2}$, obe verovatnoće su $p(0) = p(1) = \tfrac12$. Kolabirana stanja su $\ket{\psi'_0} = \Pi_0\ket{+}/\sqrt{p(0)} = \ket{0}$ i $\ket{\psi'_1} = \ket{1}$ — stanje $\ket{+}$ se sa po $50\%$ obori na $\ket{0}$ ili $\ket{1}$.

```python
ket0 = np.array([[1], [0]], dtype=complex); ket1 = np.array([[0], [1]], dtype=complex)
P0 = ket0 @ ket0.conj().T;  P1 = ket1 @ ket1.conj().T
plus = (ket0 + ket1)/np.sqrt(2)

for P, b in [(P0, "0"), (P1, "1")]:
    p = (plus.conj().T @ P @ plus).item().real
    post = (P @ plus)/np.sqrt(p)
    print("p(" + b + ") =", round(p, 3), " kolaps ->", np.round(post.ravel(), 3))
```
:::

:::{admonition} Vežba 5
:class: tip
Pokaži da su $\Pi_0$ i $\Pi_1$ pravi projektori ($\Pi^\dagger = \Pi$, $\Pi^2 = \Pi$) i da važi relacija potpunosti $\Pi_0 + \Pi_1 = I$. Objasni zašto iz $\Pi^2 = \Pi$ sledi da je ponovljeno merenje „stabilno" (isti ishod sa sigurnošću).
:::

:::{admonition} Rešenje
:class: dropdown
Direktno: $\Pi_b^\dagger = \Pi_b$ (matrice su realne i dijagonalne), a $\Pi_b^2 = \dyad{b}{b}\dyad{b}{b} = \ket{b}\braket{b}{b}\bra{b} = \dyad{b}{b} = \Pi_b$ (jer je $\braket{b}{b} = 1$). Zbir je $\Pi_0 + \Pi_1 = \left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right) + \left(\begin{smallmatrix}0&0\\0&1\end{smallmatrix}\right) = I$. Posle kolapsa u $\ket{b}$ je $p(b) = \bra{b}\Pi_b\ket{b} = 1$, pa svako naredno merenje daje isti ishod.

```python
print("P0 hermitski?  ", np.allclose(P0, P0.conj().T))
print("P0^2 = P0?     ", np.allclose(P0 @ P0, P0))
print("P0 + P1 = I?   ", np.allclose(P0 + P1, np.eye(2)))
```
:::
