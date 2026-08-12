---
title: "Kvantno merenje"
short_title: Merenje
description: Šta je to merenje kvantnog stanja?
---

# Kvantno merenje (measurement)

U prethodnoj lekciji svako kolo se završavalo **merenjem** — trećim i poslednjim korakom svakog kvantnog procesa. Sada se fokusiramo baš na taj korak: šta merenje daje, kako iz njega izvlačimo informaciju o stanju, i kako se kolo pokreće na **pravom** kvantnom računaru.

Za sve primere koristićemo iste alate, uz jedan novi — **Sampler**, koji pokreće kolo zadati broj puta i vraća broj ishoda:

```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli
from qiskit.primitives import StatevectorSampler

sampler = StatevectorSampler()   # lokalni "simulator"; kasnije ga menjamo pravim hardverom
```

## Merenje u računskoj bazi

Merenje kjubita u računskoj bazi $\{\ket{0}, \ket{1}\}$ vraća **jedan klasičan bit**: ishod $0$ sa verovatnoćom $p(0) = |\braket{0}{\psi}|^2$ ili ishod $1$ sa $p(1) = |\braket{1}{\psi}|^2$ (Bornovo pravilo iz [](../dan1/02-qubits.md)). Merenje je **nepovratno** — superpozicija „kolabira" u izmereno bazno stanje, pa jedno kolo daje tačno jedan bit.

Zato do *verovatnoća* dolazimo tek **ponavljanjem**: isto kolo pokrenemo mnogo puta (tzv. **shots**) i prebrojimo ishode. Za stanje $\ket{+} = H\ket{0}$ očekujemo otprilike pola-pola:

```python
# priprema stanja |+> (bez merenja) -> tačne verovatnoće
prep = QuantumCircuit(1)
prep.h(0)
print("Bornove verovatnoće p(0), p(1):", Statevector(prep).probabilities())   # [0.5, 0.5]

# isto kolo, ali sa merenjem, pokrenuto 1000 puta
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)                       # kjubit -> klasični bit
counts = sampler.run([qc], shots=1000).result()[0].data.c.get_counts()
print("Ishodi 1000 merenja:", counts)  # ~ {'0': 500, '1': 500}
```

Kako broj ponavljanja raste, izmerene učestanosti $\tfrac{\text{broj nula}}{\text{shots}}$ se približavaju tačnim verovatnoćama $p(0), p(1)$.

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
Merenje u računskoj bazi meri operator $Z$ i vraća jedan klasičan bit; verovatnoće dobijamo ponavljanjem (`shots`). Očekivana vrednost je $\langle Z\rangle = p(0)-p(1)$, a $\langle X\rangle$ i $\langle Y\rangle$ merimo tako što osu prvo zarotiramo u $Z$. Tri očekivane vrednosti čine Blohov vektor, pa merenjem u tri baze rekonstruišemo celo stanje (tomografija). Isto kolo pokrećemo na pravom hardveru promenom „samplera"; tamo se javlja šum, pa je statistika neophodna.
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
