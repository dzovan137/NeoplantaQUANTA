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
- ishod $\textbf{0}$ sa verovatnoćom $p(0) = |\braket{0}{\psi}|^2$, ili
- ishod $\textbf{1}$ sa $p(1) = |\braket{1}{\psi}|^2$.

Merenje je **nepovratno**: superpozicija „kolabira" u izmereno bazno stanje, pa jedno kolo daje tačno jedan bit.

Zato do *verovatnoća* dolazimo tek **ponavljanjem**: isto kolo pokrenemo mnogo puta tj. kreiramo **uzorake** (eng. **shots**) i prebrojimo ishode. Za stanje 
```{math}
:label: eq:plus
\ket{+} = H\ket{0} = \dfrac{1}{\sqrt{2}} \left( \ket{0} + \ket{1} \right)
```
očekujemo otprilike pola-pola raspodelu zastupljenosti na svakom od računskih stanja. 


### Python kod
#### osnovni kod
```python
import numpy as np

# Korak 1: definisanje stanja  
amplitudes = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)

# Korak 2: Dobijanje verovatnoća 
probs = np.abs(amplitudes) ** 2          # [0.5, 0.5]

# Korak 3: uzorkovanje
shots = 20
basis_states = np.arange(len(amplitudes))  # [0, 1]
outcomes = np.random.choice(basis_states, size=shots, p=probs)

# Korak 4: sakupi sva uzorkovanja
counts = np.bincount(outcomes, minlength=len(amplitudes))
probabilities = counts / shots

# Korak 5: prikaži
print('Pojedinačni uzorci: ',counts)
print('Verovatnoće: ',probabilities)
```
#### Vizuelizacija
```python
import matplotlib.pyplot as plt

# kod za procesiranje pre prikazivanje histograma
qubit_number = len(bin(len(probabilities) - 1)) - 2 if len(probabilities) > 0 else 0
bit_strings = [bin(i)[2:].zfill(qubit_number) for i in range(len(probabilities))]

# Kreiranje histogram
plt.figure(figsize=(12, 6))
plt.bar(bit_strings, probabilities)

# Ose i naziv
plt.xlabel("Bit Stringovi")
plt.ylabel("Verovatnoća")
plt.title("Histogram verovatnoća")

plt.tight_layout()
plt.show()
```


```{figure} ../images/merenje_histogram.png
:label: fig:merenje_histogram
:alt: vizuelizacija histograma
:width: 520px
:align: center

Primer vizuelizacije histograma merenja. Ovo je izlaz za 20 uzoraka na primeru $\ket{+}$ stanju. Pojedinačni uzorci:  [11  9], Verovatnoće:  [0.55 0.45]. 
```

### Ekvivalent u QisKit
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
qc.measure(0, 0)                       # kubit -> klasični bit
counts = sampler.run([qc], shots=1000).result()[0].data.c.get_counts()
print("Ishodi 1000 merenja:", counts)  # ~ {'0': 500, '1': 500}
```

Kako se broj ponavljanja povećava, tako se vrednosti približavaju tačnim verovatnoćama $p(0), p(1)$!

Sa sledećim kodom možemo da vidimo kako! 

```python
import numpy as np
import matplotlib.pyplot as plt

# Stanje: |+> = (|0> + |1>)/sqrt(2)
amplitudes = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
true_probs = np.abs(amplitudes) ** 2          # [0.5, 0.5]

# Menjaj broj uzorkovanja na logaritomskoj skali (logaritamska zbog bolje vizuelizacije kasnije)
shot_counts = np.unique(np.logspace(0, 5, 60).astype(int))  # 1 ... 100000

p0, p1 = [], []
rng = np.random.default_rng()
for shots in shot_counts:
    outcomes = rng.choice(2, size=shots, p=true_probs)
    counts = np.bincount(outcomes, minlength=2) / shots
    p0.append(counts[0])
    p1.append(counts[1])

# Grafik
plt.figure(figsize=(12, 6))
plt.plot(shot_counts, p0, color="blue", marker="o", markersize=4,
         linewidth=1.2, label="P(0)")
plt.plot(shot_counts, p1, color="red", marker="o", markersize=4,
         linewidth=1.2, label="P(1)")


plt.axhline(0.5, color="black", linestyle="--", linewidth=1, alpha=0.7,
            label="Očekivane vrednosti (0.5)")

plt.xscale("log")
plt.xlabel("Broj uzorkovanja")
plt.ylabel("Verovatnoća")
plt.title(r"Kako merenja konvergiraju?")
plt.grid(True, alpha=0.2)
plt.legend()
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
```

```{figure} ../images/konvergencija.png
:label: fig:konvergencija
:alt: vizuelizacija konvergencije
:width: 520px
:align: center

Primer vizuelizacije konvergencije ka očekivanim verovatnoćama sa povećavanjem broja uzoraka. 
```


## Koliko je kvantna mehanika zapravo nasumična?!

Vratimo se na stanje $\ket{+}$. Ono nam je davalo raspodelu **pola-pola**, pa deluje kao da je „slučajnost" ugrađena u sam kubit. Ali to nije sasvim tačno: 


:::{important} O nasumičnosti
:class: simple
Nasumičnost nije vezana za isključivo stanje kubita, već u odnosu stanja ali i baze u kojoj taj kubit merimo!
:::

Setimo se Blohove sfere. Bazna stanja u kojima čitamo rezultat, $\ket{0}$ i $\ket{1}$, sede na **polovima** ($+z$ i $-z$). Stanje $\ket{+}$ leži na **ekvatoru** (duž $+x$), tačno podjednako udaljeno od oba pola. Otud i savršeno neodlučnih $50\%$–$50\%$. Ako želimo **deterministički** ishod, dovoljno je da stanje **zarotiramo** tako da njegov Blohov vektor pokazuje pravo na jedan od polova.

```{figure} ../images/blohova_rotacija.png
:label: fig:blohova_rotacija
:alt: rotacija Blohovog vektora sa ekvatora na pol
:width: 460px
:align: center

$\ket{+}$ (crveno, $+x$) leži na ekvatoru: merenje u računskoj bazi je maksimalno neodlučno. Rotacijom oko $y$-ose za $-\pi/2$ vektor dovodimo na pol $\ket{0}$ ($+z$), gde merenje postaje deterministično.
```

### Rotacija oko $y$-ose

Za tako nešto koristimo **rotacionu kapiju** $R_y(\theta)$, koji rotira Blohov vektor u $x$–$z$ ravni:

$$
R_y(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\[4pt] \sin\frac{\theta}{2} & \phantom{-}\cos\frac{\theta}{2} \end{pmatrix}.
$$

Primenimo ga na $\ket{+} = \tfrac{1}{\sqrt{2}}\big(\ket{0} + \ket{1}\big)$:

$$
R_y(\theta)\ket{+} = \frac{1}{\sqrt{2}}\begin{pmatrix} \cos\frac{\theta}{2} - \sin\frac{\theta}{2} \\[4pt] \sin\frac{\theta}{2} + \cos\frac{\theta}{2} \end{pmatrix}.
$$

Verovatnoća ishoda $0$ je kvadrat gornje amplitude, što se lepo izrazi (koristeći trigonometrijski identitet $\sin{(2 \theta)} = 2 \sin{(\theta)} \cos{(\theta)}$)

$$
p(0) = \frac{1}{2}\Big(\cos\tfrac{\theta}{2} - \sin\tfrac{\theta}{2}\Big)^2 = \frac{1 - \sin\theta}{2}, \qquad p(1) = \frac{1 + \sin\theta}{2}.
$$

Sada samo tražimo ugao koji daje $p(0) = 1$. To je $\sin\theta = -1$, tj. **$\theta = -\pi/2$**. Uvrstimo:

$$
R_y\!\left(-\tfrac{\pi}{2}\right)\ket{+} = \frac{1}{\sqrt{2}}\begin{pmatrix} \cos\frac{\pi}{4} + \sin\frac{\pi}{4} \\[4pt] -\sin\frac{\pi}{4} + \cos\frac{\pi}{4} \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \ket{0}.
$$

Dakle $R_y(-\pi/2)$ vodi $\ket{+} \to \ket{0}$, i merenje sada **uvek** vraća $0$. Analogno, $R_y(+\pi/2)$ vodi $\ket{+} \to \ket{1}$ (uvek $1$).

```{note}
Najkraća rotacija koja radi isti posao je — ponovni $H$! Pošto je $H^2 = I$, važi $H\ket{+} = HH\ket{0} = \ket{0}$. $R_y(\theta)$ nam je ipak koristniji jer *geometrijski* pokazuje šta se dešava i lako se uopštava na proizvoljan ugao.
```

### Python kod (samo NumPy)

```python
import numpy as np

# Korak 1: polazno stanje |+> = (|0> + |1>)/sqrt(2)
plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)

# Korak 2: rotacioni gejt R_y(theta) oko y-ose
def Ry(theta):
    c, s = np.cos(theta/2), np.sin(theta/2)
    return np.array([[c, -s],
                     [s,  c]], dtype=complex)

# Korak 3: ugao koji |+> vodi u |0>
theta = -np.pi/2
psi = Ry(theta) @ plus
print("Stanje posle rotacije:", np.round(psi, 6))     # [1, 0]

# Korak 4: Bornove verovatnoće
probs = np.abs(psi) ** 2
print("Verovatnoće p(0), p(1):", np.round(probs, 6))  # [1, 0]

# Korak 5: uzorkovanje — svih 1000 ishoda je 0
shots = 1000
outcomes = np.random.choice([0, 1], size=shots, p=probs)
counts = np.bincount(outcomes, minlength=2)
print("Ishodi 1000 merenja:", counts)                 # [1000, 0]
```

Histogram ovog kola nema više dve stubića! Sva verovatnoća je skoncentrisana na ishodu $0$:

```{figure} ../images/deterministicko_merenje.png
:label: fig:deterministicko_merenje
:alt: histogram deterministickog ishoda
:width: 520px
:align: center

Nakon $R_y(-\pi/2)$ primenjenog na $\ket{+}$, svih 1000 uzoraka daje ishod $0$. Slučajnosti više nema.
```

### Nasumičnost se može „otkloniti"

Pošto je $p(0) = \tfrac{1 - \sin\theta}{2}$, ugao rotacije nam je zapravo promenljiva kojom biramo bilo koju verovatnoću između 0 i 1: dve tačke su potpuno determinističke.

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi, np.pi, 400)
p0 = (1 - np.sin(theta)) / 2
p1 = (1 + np.sin(theta)) / 2

plt.figure(figsize=(12, 6))
plt.plot(theta, p0, color="blue", lw=2, label="p(0)")
plt.plot(theta, p1, color="red",  lw=2, label="p(1)")
plt.axhline(0.5, color="gray", ls="--", lw=1, alpha=0.7)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
plt.xlabel(r"Ugao rotacije $\theta$")
plt.ylabel("Verovatnoća")
plt.title(r"Verovatnoća ishoda kao funkcija rotacije $R_y(\theta)$ na $|+\rangle$")
plt.ylim(0, 1.05); plt.grid(alpha=0.2); plt.legend()
plt.tight_layout()
plt.show()
```

```{figure} ../images/rotacija_verovatnoca.png
:label: fig:rotacija_verovatnoca
:alt: verovatnoca kao funkcija ugla rotacije
:width: 560px
:align: center

Rotacijom biramo verovatnoću ishoda. Na $\theta = 0$ smo u polaznom $\ket{+}$ (50–50); na $\theta = -\pi/2$ dobijamo $100\%$ $\ket{0}$, a na $\theta = +\pi/2$ dobijamo $100\%$ $\ket{1}$.
```


Merenje jednog kola daje jedan bit, ali **koliko je taj bit nepredvidiv zavisi od baze**. Isto stanje $\ket{+}$ je nasumično u računskoj bazi, a savršeno predvidivo u $\{\ket{+}, \ket{-}\}$ bazi. Primeniti kapije pre merenja u računskoj bazi je zato isto što i **meriti u zarotiranoj bazi**.


:::{important} Zaključak
:class: simple
Kvantna mehanika nije „nasumična tek tako". Stanje je potpuno određeno: verovatnoće se pojavljuju tek kada ga projektujemo na izabranu bazu! 

**Kad bazu poravnamo sa stanjem, nasumičnost nestaje!**
:::

## Merenje kao projekcija: projektori i kolaps

Do sada smo merenje opisivali preko *verovatnoća* ishoda. Sada formalizujemo merenje na malo drugačiji način: šta se sa stanjem dešava **posle** merenja, tj. onaj „kolaps" koji smo gore samo pomenuli. Ključni alat je **projektor**.

Svakom ishodu $b \in \{0, 1\}$ u računskoj bazi pridružujemo projektor na odgovarajuće bazno stanje,

```{math}
:label: eq:projektor
\Pi_0 = \dyad{0}{0} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad
\Pi_1 = \dyad{1}{1} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.
```

Projektori su **ermitski** ($\Pi_b^\dagger = \Pi_b$) i **idempotentni** ($\Pi_b^2 = \Pi_b$) tj. primena istg projektora dvaput isto je što i primeniti ga jednom. Uz to važi **relacija potpunosti** (eng. completeness relation) definisana kao

```{math}
:label: eq:potpunost
\Pi_0 + \Pi_1 = I.
```

**Verovatnoća** ishoda $b$ tada se zapisuje kao

```{math}
:label: eq:born-projektor
p(b) = \bra{\psi}\Pi_b^\dagger \Pi_b \ket{\psi} = \bra{\psi}\Pi_b\ket{\psi} = |\braket{b}{\psi}|^2,
```

gde smo iskoristili $\Pi_b^\dagger \Pi_b = \Pi_b^2 = \Pi_b$. 

Za stanje $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$ ovo daje $p(0) = |\alpha|^2$ i $p(1) = |\beta|^2$: dakle isto kao do sada, samo zapisano preko projektora.

Ono što je **novo** jeste stanje *posle* merenja. Ako izmerimo ishod $b$, stanje se „kolabira" u

```{math}
:label: eq:kolaps
\ket{\psi'_b} = \frac{\Pi_b \ket{\psi}}{\sqrt{p(b)}},
```

gde deljenje sa $\sqrt{p(b)}$ služi da novo stanje ostane **normirano**. Za jedan kubit u računskoj bazi je $\Pi_0\ket{\psi} = \alpha\ket{0}$, pa je

```{math}
\ket{\psi'_0} = \frac{\alpha}{|\alpha|}\,\ket{0} \;\equiv\; \ket{0}, 
```

(faktor $\alpha/|\alpha|$ je samo nebitna globalna faza). 

Merenje, dakle, **deterministički** obara na $\ket{0}$ ili $\ket{1}$ i to predstavlja precizan smisao „kolapsa" superpozicije.

:::{important} Merenje je ponovljivo
:class: simple
Pošto je $\Pi_b^2 = \Pi_b$, čim stanje jednom kolabira u $\ket{b}$, ponovno merenje u istoj bazi daje **isti** ishod sa sigurnošću: $p(b) = \bra{b}\Pi_b\ket{b} = 1$. Kvantno merenje je zato **stabilno** jer drugo merenje ne „pokvari" i ne menja ništa!
:::

:::{note} Merenje u proizvoljnoj bazi (klik)
:class: dropdown
Projektorski zapis ne zavisi od baze. Merenje u bilo kojoj ortonormiranoj bazi $\{\ket{u_0}, \ket{u_1}\}$ koristi projektore $\Pi_{u} = \dyad{u}{u}$. Na primer, merenje u $X$-bazi koristi $\Pi_{+} = \dyad{+}{+}$ i $\Pi_{-} = \dyad{-}{-}$ — a to je upravo „projektorska" verzija trika *zarotiraj-pa-izmeri-u-$Z$* iz narednog odeljka.
:::


## Vežbe

:::{admonition} Vežba 1
:class: tip
Kubit je pripremljen u stanju $\ket{\psi} = \tfrac{\sqrt{3}}{2}\ket{0} + \tfrac{1}{2}\ket{1}$. Izračunaj Bornove verovatnoće $p(0)$ i $p(1)$, pa proveri uzorkovanjem ($1000$ uzoraka) da se relativne učestanosti približavaju tim vrednostima.
:::

:::{admonition} Rešenje
:class: dropdown
Po Bornovom pravilu je $p(0) = |\tfrac{\sqrt{3}}{2}|^2 = \tfrac{3}{4}$ i $p(1) = |\tfrac{1}{2}|^2 = \tfrac{1}{4}$. Pošto je stanje fiksno, verovatnoće su tačne; uzorkovanjem dobijamo *procenu* koja se sa više shots-a stabilizuje oko $0.75$ i $0.25$.

```python
import numpy as np

# stanje |psi> = (sqrt(3)/2)|0> + (1/2)|1>
amplitudes = np.array([np.sqrt(3)/2, 1/2], dtype=complex)

# Bornove verovatnoće
probs = np.abs(amplitudes) ** 2
print("p(0), p(1):", np.round(probs, 3))   # [0.75 0.25]

# uzorkovanje 1000 puta
shots = 1000
outcomes = np.random.choice([0, 1], size=shots, p=probs)
counts = np.bincount(outcomes, minlength=2)
print("Ishodi 1000 merenja:", counts)              # ~ [750, 250]
print("Relativne učestanosti:", np.round(counts/shots, 3))  # ~ [0.75, 0.25]
```
:::

:::{admonition} Vežba 2
:class: tip
Polazimo od stanja $\ket{+}$ i primenjujemo rotaciju $R_y(\theta)$ pre merenja u računskoj bazi. Nađi ugao $\theta$ za koji verovatnoća ishoda $0$ iznosi $p(0) = 0.85$. (Podsetnik: $p(0) = \tfrac{1 - \sin\theta}{2}$.) Proveri rezultat numerički.
:::

:::{admonition} Rešenje
:class: dropdown
Iz $p(0) = \tfrac{1 - \sin\theta}{2}$ sledi $\sin\theta = 1 - 2p(0) = 1 - 1.7 = -0.7$, pa je $\theta = \arcsin(-0.7) \approx -0.775\ \text{rad} \approx -44.4^\circ$. Uvrštavanjem u $R_y(\theta)\ket{+}$ i kvadriranjem gornje amplitude dobijamo tačno $p(0) = 0.85$.

```python
import numpy as np

def Ry(theta):
    c, s = np.cos(theta/2), np.sin(theta/2)
    return np.array([[c, -s],
                     [s,  c]], dtype=complex)

plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)

# traženi ugao iz p(0) = (1 - sin(theta))/2
p0_cilj = 0.85
theta = np.arcsin(1 - 2*p0_cilj)
print("theta:", round(theta, 4), "rad  =", round(np.degrees(theta), 2), "stepeni")  # ~ -0.775 rad, -44.43°

# provera: p(0) posle rotacije
psi = Ry(theta) @ plus
p0 = np.abs(psi[0]) ** 2
print("Postignuto p(0):", round(float(p0), 3))   # 0.85
```
:::

:::{admonition} Vežba 3
:class: tip
Za stanje $\ket{\psi} = \cos\tfrac{\pi}{6}\ket{0} + \sin\tfrac{\pi}{6}\ket{1}$ i projektore $\Pi_0, \Pi_1$: (a) proveri relaciju potpunosti $\Pi_0 + \Pi_1 = I$ i idempotentnost $\Pi_0^2 = \Pi_0$, (b) izračunaj $p(0) = \bra{\psi}\Pi_0\ket{\psi}$, i (c) nađi stanje posle izmerenog ishoda $0$.
:::

:::{admonition} Rešenje
:class: dropdown
Projektori su $\Pi_0 = \dyad{0}{0}$ i $\Pi_1 = \dyad{1}{1}$, pa je $\Pi_0 + \Pi_1 = I$ i $\Pi_0^2 = \Pi_0$. Verovatnoća je $p(0) = \bra{\psi}\Pi_0\ket{\psi} = \cos^2\tfrac{\pi}{6} = \tfrac{3}{4}$. Posle ishoda $0$ stanje se kolabira u $\ket{\psi'_0} = \tfrac{\Pi_0\ket{\psi}}{\sqrt{p(0)}} = \ket{0}$.

```python
import numpy as np

P0 = np.array([[1, 0], [0, 0]], dtype=complex)   # |0><0|
P1 = np.array([[0, 0], [0, 1]], dtype=complex)   # |1><1|

# (a) potpunost i idempotentnost
print("P0 + P1 = I ?  ", np.allclose(P0 + P1, np.eye(2)))
print("P0^2 = P0 ?    ", np.allclose(P0 @ P0, P0))

# (b) verovatnoća ishoda 0
psi = np.array([np.cos(np.pi/6), np.sin(np.pi/6)], dtype=complex)
p0 = (psi.conj() @ P0 @ psi).real
print("p(0) = <psi|P0|psi>:", round(float(p0), 3))   # 0.75

# (c) stanje posle merenja ishoda 0
psi_kolaps = (P0 @ psi) / np.sqrt(p0)
print("Stanje posle merenja:", np.round(psi_kolaps, 3))   # [1, 0] = |0>
```
:::

:::{admonition} Vežba 4 (teža)
:class: tip
Do sada smo merili u računskoj ($Z$) bazi. Sada merimo u $X$-bazi $\{\ket{+}, \ket{-}\}$. Za stanje $\ket{\psi} = \cos\tfrac{\pi}{8}\ket{0} + \sin\tfrac{\pi}{8}\ket{1}$ nađi verovatnoće ishoda $p(+)$ i $p(-)$ na **tri načina** i pokaži da se svi slažu:

1. preko projektora $\Pi_{+} = \dyad{+}{+}$ i $\Pi_{-} = \dyad{-}{-}$;
2. trikom *„zarotiraj pa izmeri u $Z$"*. Primeni $H$ pre merenja u računskoj bazi (jer $H\ket{+} = \ket{0}$, $H\ket{-} = \ket{1}$);
3. u **Qiskit**-u, pripremom stanja pomoću $R_y(\pi/4)$ i merenjem posle $H$.
:::

:::{admonition} Rešenje
:class: dropdown
**1. Projektori.** Kako je $\braket{+}{\psi} = \tfrac{1}{\sqrt2}(\cos\tfrac{\pi}{8} + \sin\tfrac{\pi}{8})$, dobijamo
```{math}
p(+) = |\braket{+}{\psi}|^2 = \tfrac{1}{2}\big(\cos\tfrac{\pi}{8} + \sin\tfrac{\pi}{8}\big)^2 = \frac{1 + \sin\frac{\pi}{4}}{2} \approx 0.854,
```
gde smo iskoristili $2\sin\theta\cos\theta = \sin 2\theta$. Slično je $p(-) = \tfrac{1 - \sin(\pi/4)}{2} \approx 0.146$.

**2. Zarotiraj pa izmeri.** Merenje u $X$-bazi je isto što i primena $H$ (koji dovodi $X$-bazu u $Z$-bazu) pa merenje u računskoj bazi: ishod $0$ posle $H$ odgovara $\ket{+}$, a ishod $1$ odgovara $\ket{-}$. Zato je $p(0)_{\text{posle }H} = p(+)$.


```python
import numpy as np

# stanje |psi> = cos(pi/8)|0> + sin(pi/8)|1>
th = np.pi/8
psi = np.array([np.cos(th), np.sin(th)], dtype=complex)

# X-bazna stanja i projektori
plus  = np.array([1,  1], dtype=complex)/np.sqrt(2)
minus = np.array([1, -1], dtype=complex)/np.sqrt(2)
Pp = np.outer(plus,  plus.conj())    # |+><+|
Pm = np.outer(minus, minus.conj())   # |-><-|

# (1) preko projektora
p_plus  = (psi.conj() @ Pp @ psi).real
p_minus = (psi.conj() @ Pm @ psi).real
print("(1) projektori   p(+), p(-):", np.round([p_plus, p_minus], 4))   # [0.854 0.146]

# (2) zarotiraj (H) pa izmeri u Z-bazi
H = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]], dtype=complex)
phi = H @ psi
print("(2) H pa Z-baza  p(0), p(1):", np.round(np.abs(phi)**2, 4))       # [0.854 0.146]
```

**3. Qiskit.** Stanje $\ket{\psi}$ pripremimo sa $R_y(\pi/4)$ (jer $R_y(\theta)\ket{0} = \cos\tfrac{\theta}{2}\ket{0} + \sin\tfrac{\theta}{2}\ket{1}$, pa je $\theta = \pi/4$), dodamo $H$ za prelazak u $X$-bazu, i merimo.

```python
# (3) Qiskit: priprema Ry(pi/4), rotacija H u X-bazu, pa merenje
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler

sampler = StatevectorSampler()

prep = QuantumCircuit(1)
prep.ry(np.pi/4, 0)   # priprema |psi>
prep.h(0)             # prelazak u X-bazu
print("(3) Qiskit tačne p(+), p(-):", np.round(Statevector(prep).probabilities(), 4))  # [0.854 0.146]

qc = QuantumCircuit(1, 1)
qc.ry(np.pi/4, 0)
qc.h(0)
qc.measure(0, 0)      # ishod 0 <-> |+>, ishod 1 <-> |->
counts = sampler.run([qc], shots=2000).result()[0].data.c.get_counts()
print("(3) 2000 merenja:", counts)   # ~ {'0': 1707, '1': 293}
```

Sva tri načina daju isto: $p(+) \approx 0.854$, $p(-) \approx 0.146$. Poenta: **merenje u drugoj bazi je samo rotacija pre merenja u računskoj bazi** — upravo „projektorska" ideja sa kraja lekcije.
:::
