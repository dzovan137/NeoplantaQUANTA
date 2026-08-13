---
title: "Kvantno merenje"
short_title: Kvantno merenje
description: Šta je to merenje kvantnog stanja?
---

# Kvantno merenje (quantum measurement)

U prethodnoj lekciji svako kolo se završavalo **merenjem**, tj. trećim i poslednjim korakom svakog kvantnog procesa. Sada se fokusiramo baš na taj korak: 
- šta merenje daje, 
- kako iz njega izvlačimo informaciju o stanju, 
- kako se kolo pokreće na **pravom** kvantnom računaru! 🚀



## Merenje u računskoj bazi

Merenje kubita u računskoj bazi $\{\ket{0}, \ket{1}\}$ vraća **jedan klasičan bit**: 
- ishod $0$ sa verovatnoćom $p(0) = |\braket{0}{\psi}|^2$, ili
- ishod $1$ sa $p(1) = |\braket{1}{\psi}|^2$.

Merenje je **nepovratno**: superpozicija „kolabira" u izmereno bazno stanje, pa jedno kolo daje tačno jedan bit.

Zato do *verovatnoća* dolazimo tek **ponavljanjem**: isto kolo pokrenemo mnogo puta tj. kreiramo **uzorake** (eng. **shots**) i prebrojimo ishode. Za stanje $\ket{+} = H\ket{0}$ očekujemo otprilike pola-pola:

```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli
from qiskit.primitives import StatevectorSampler

# lokalni "simulator"; kasnije ga menjamo pravim hardverom
sampler = StatevectorSampler()   

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

## Merenje kao projekcija: projektori i kolaps

Do sada smo merenje opisivali preko *verovatnoća* ishoda. Sada formalizujemo i drugu stranu merenja — šta se sa stanjem dešava **posle** merenja, tj. onaj „kolaps" koji smo gore samo pomenuli. Ključni alat je **projektor**.

Svakom ishodu $b \in \{0, 1\}$ u računskoj bazi pridružujemo projektor na odgovarajuće bazno stanje,

```{math}
:label: eq:projektor
\Pi_0 = \dyad{0}{0} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad
\Pi_1 = \dyad{1}{1} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.
```

Projektori su **hermitski** ($\Pi_b^\dagger = \Pi_b$) i **idempotentni** ($\Pi_b^2 = \Pi_b$) — primeniti isti projektor dvaput isto je što i primeniti ga jednom. Uz to važi **relacija potpunosti**

```{math}
:label: eq:potpunost
\Pi_0 + \Pi_1 = I.
```

**Verovatnoća** ishoda $b$ tada se zapisuje kao

```{math}
:label: eq:born-projektor
p(b) = \bra{\psi}\Pi_b^\dagger \Pi_b \ket{\psi} = \bra{\psi}\Pi_b\ket{\psi} = |\braket{b}{\psi}|^2,
```

gde smo iskoristili $\Pi_b^\dagger \Pi_b = \Pi_b^2 = \Pi_b$. Za stanje $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$ ovo daje $p(0) = |\alpha|^2$ i $p(1) = |\beta|^2$ — dakle isto Bornovo pravilo kao gore, samo zapisano preko projektora.

Ono što je **novo** jeste stanje *posle* merenja. Ako izmerimo ishod $b$, stanje se „kolabira" u

```{math}
:label: eq:kolaps
\ket{\psi'_b} = \frac{\Pi_b \ket{\psi}}{\sqrt{p(b)}},
```

gde deljenje sa $\sqrt{p(b)}$ služi da novo stanje ostane **normirano**. Za jedan kjubit u računskoj bazi je $\Pi_0\ket{\psi} = \alpha\ket{0}$, pa je

```{math}
\ket{\psi'_0} = \frac{\alpha}{|\alpha|}\,\ket{0} \;\equiv\; \ket{0}
```

(faktor $\alpha/|\alpha|$ je samo nebitna globalna faza). Merenje, dakle, jedan kjubit **deterministički** obara na $\ket{0}$ ili $\ket{1}$ — to je precizan smisao „kolapsa" superpozicije.

:::{important} Merenje je ponovljivo
:class: simple
Pošto je $\Pi_b^2 = \Pi_b$, čim stanje jednom kolabira u $\ket{b}$, ponovno merenje u istoj bazi daje **isti** ishod sa sigurnošću: $p(b) = \bra{b}\Pi_b\ket{b} = 1$. Kvantno merenje je zato *stabilno* — drugo merenje ne „pokvari" ništa.
:::

:::{note} Merenje u proizvoljnoj bazi (klik)
:class: dropdown
Projektorski zapis ne zavisi od baze. Merenje u bilo kojoj ortonormiranoj bazi $\{\ket{u_0}, \ket{u_1}\}$ koristi projektore $\Pi_{u} = \dyad{u}{u}$. Na primer, merenje u $X$-bazi koristi $\Pi_{+} = \dyad{+}{+}$ i $\Pi_{-} = \dyad{-}{-}$ — a to je upravo „projektorska" verzija trika *zarotiraj-pa-izmeri-u-$Z$* iz narednog odeljka.
:::

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
