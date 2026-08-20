---
title: "Spletenost"
short_title: Spletenost
description: Osnove višekubitnih sistema    
---


## Proizvodna nasuprot spregnutim stanjima

Tenzorski proizvod nam omogućava da od stanja pojedinačnih kubita **sagradimo** stanje registra: 

```{math}
:label: eq:examp
\ket{\psi_1}\otimes\ket{\psi_2}\otimes\cdots \otimes \ket{\psi_N}

```

Takva stanja zovemo **proizvodna** (eng. "product state") ili **separabilna** (eng. "separable"). 

:::{important} Ključna osobina koja čini višekubitne sisteme interesantnim! 
:class: simple

Ključno zapažanje koje leži u srce kvantne mehanike i kvantnog računarstva: **ne može svako** stanje registra da se zapisati ili "rastaviti" na ovaj način! Vektor ima $2^N$ elemenata, a proizvodnih stanja ima „premalo" da ga popune; ostatak su **spregnuta** (eng. "entangled") stanja.
:::

- Hajde da vidimo to na sledećem primeru! 

Za dva kubita, opšte proizvodno stanje je
```{math}
:label: eq:prod-2q
(\alpha\ket0 + \beta\ket1)\otimes(\gamma\ket0 + \delta\ket1)
= \alpha\gamma\ket{00} + \alpha\delta\ket{01} + \beta\gamma\ket{10} + \beta\delta\ket{11}.
```
Odatle su amplitude $a_{00}=\alpha\gamma,\ a_{01}=\alpha\delta,\ a_{10}=\beta\gamma,\ a_{11}=\beta\delta$. Postoji jednostavan i elegantan način da proverimo da li ovo stanje može da se razloži u tenzorski produkt. Složimo četiri amplitude u **matricu** čiji red bira prvi, a kolona drugi kubit:

```{math}
:label: eq:coef-matrix
C = \begin{pmatrix} a_{00} & a_{01} \\ a_{10} & a_{11} \end{pmatrix} = \begin{pmatrix}\alpha\gamma & \alpha\delta \\ \beta\gamma & \beta\delta\end{pmatrix}.
```

Sa sledećim preciznim uslovom:

```{math}
:label: eq:sep-crit
\text{separabilno} \;\Longleftrightarrow\;  \det C = a_{00}a_{11} - a_{01}a_{10} = 0.
```

Ako je determinanta različita od nule, stanje je **spregnuto** i nema rastavljanja na „prvi kubit puta drugi kubit"!

Hajde da kroz primere pokažemo kako funkcioniše ovaj uslov i kako se koristimo Python-om u ovom slučaju.  
(a) Napiši $\ket0\otimes\ket{+}$ eksplicitno kao vektor u $\mathbb{C}^4$ i potvrdi `np.kron`-om. \
(b) Prekroji amplitude u matricu $C$ iz {eq}`eq:coef-matrix` i pomoću determinantei i odredi da li je stanje proizvodno. \
(c) Testiraj uslov separabilnosti na $\ket0\otimes\ket{+}$ (očekivano separabilno) i na Bell stanju $\tfrac{1}{\sqrt2}(\ket{00}+\ket{11})$ (očekivano spregnuto).


:::{admonition} Rešenje
:class: dropdown
(a) $\ket{+} = \tfrac{1}{\sqrt2}(\ket0+\ket1)$, pa je $\ket0\otimes\ket{+} = \tfrac{1}{\sqrt2}(\ket{00}+\ket{01}) = \tfrac{1}{\sqrt2}(1,1,0,0)^{\mathsf T}$.

(b) Za $\ket0\otimes\ket{+}$ je $C = \tfrac{1}{\sqrt2}\left(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\right)$, rang $1$, $\det C = 0$ → separabilno. Za Bell stanje je $C = \tfrac{1}{\sqrt2}\left(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\right)$, rang $2$, $\det C = \tfrac12 \neq 0$ → spregnuto.

```python
import numpy as np
ket0 = np.array([1, 0], dtype=complex); ket1 = np.array([0, 1], dtype=complex)
plus = (ket0 + ket1)/np.sqrt(2)

def je_separabilno(psi, tol=1e-9):
    C = psi.reshape(2, 2)                              # amplitude -> 2x2 matrica
    return np.linalg.matrix_rank(C, tol=tol) == 1     # rang 1 <=> proizvodno

prod = np.kron(ket0, plus)
bell = (np.kron(ket0, ket0) + np.kron(ket1, ket1))/np.sqrt(2)
print("|0>|+> =", np.round(prod, 3))
print("|0>|+> separabilno? ", je_separabilno(prod))   # True
print("Bell separabilno?   ", je_separabilno(bell))   # False

# ista provera preko determinante (samo za 2x2):
for ime, psi in [("|0>|+>", prod), ("Bell", bell)]:
    C = psi.reshape(2, 2)
    print(f"det C ({ime}) =", round(abs(np.linalg.det(C)), 3))
```
:::

## Bell-ova stanja 
Za sistem od dva kubita postoji poseban skup stanja koja su, prema ranije predstavljenoj definiciji, istorijski i praktično veoma važna u kvantnoj mehanici. Ta stanja nazivamo Bell-ovim stanjima ([Bell state](https://en.wikipedia.org/wiki/Bell_state)). 

Ona su definisana kao:

1. $\ket{\Phi^{+}} = \dfrac{1}{\sqrt{2}} \left( \ket{00} + \ket{11} \right)$,
2. $\ket{\Phi^{-}} = \dfrac{1}{\sqrt{2}} \left( \ket{00} - \ket{11} \right)$,
3. $\ket{\Psi^{+}} = \dfrac{1}{\sqrt{2}} \left( \ket{01} + \ket{10} \right)$,
4. $\ket{\Psi^{-}} = \dfrac{1}{\sqrt{2}} \left( \ket{01} - \ket{10} \right)$,

Ova stanja igraju veoma važnu ulogu u kvantnom mehanici i u konteksku Bellovih nejednakosti. Time ćemo se baviti u nekim narednim poglavljima.  

## Kapije na delu registra

Kada kapiju primenjujemo na **jedan** kubit unutar registra, na ostale kubite deluje jedinična matrica $I$. Delovanje na kubit $j$ dobijamo tenzorskim proizvodom u kom je na mestu $j$ tražena kapija, a svuda drugde $I$. Na primer, $H$ samo na srednjem od tri kubita je $I\otimes H\otimes I$ (matrica $8\times 8$). Tako svaki simulator zapravo „diže" jednokubitne kapije na ceo prostor.

:::{admonition} Vežba 3 — Hadamard na srednjem kubitu
:class: tip
Sastavi $8\times 8$ matricu $I\otimes H\otimes I$ i primeni je na $\ket{000}$. Uveri se da rezultat pravi superpoziciju **samo** po srednjem bitu, tj. daje $\ket0\otimes\ket{+}\otimes\ket0$.
:::

:::{admonition} Rešenje
:class: dropdown
```python
import numpy as np
ket0 = np.array([1, 0], dtype=complex); ket1 = np.array([0, 1], dtype=complex)
plus = (ket0 + ket1)/np.sqrt(2)
I = np.eye(2); H = np.array([[1, 1], [1, -1]])/np.sqrt(2)

op = np.kron(np.kron(I, H), I)                 # I ⊗ H ⊗ I  (8x8)
out = op @ np.kron(np.kron(ket0, ket0), ket0)  # deluje na |000>
exp = np.kron(np.kron(ket0, plus), ket0)       # očekivano |0>|+>|0>
print("I⊗H⊗I |000> == |0>|+>|0> ? ", np.allclose(out, exp))
```
:::



## Normiranje i broj parametara

Amplitude opšteg stanja nisu proizvoljne — moraju biti **normirane**, $\sum_{\mathbf x}|a_{\mathbf x}|^2 = 1$. Uz to, globalna faza nije fizička (stanja $\ket\Psi$ i $e^{i\varphi}\ket\Psi$ su ista). Prebrojavanje slobodnih parametara pokazuje koliko je „veliko" $N$-kubitno stanje.

:::{admonition} Vežba 4 — normiraj i prebroj parametre
:class: tip
Generiši slučajan kompleksan vektor dužine $2^N$, normiraj ga i numerički potvrdi $\sum_{\mathbf x}|a_{\mathbf x}|^2 = 1$. Zatim prebroj: koliko realnih parametara ima **nenormiran** vektor, a koliko fizičko stanje (posle normiranja i uklanjanja globalne faze)?
:::

:::{admonition} Rešenje
:class: dropdown
Kompleksan vektor dužine $2^N$ ima $2\cdot 2^N$ realnih brojeva. Normiranost uklanja jedan ($\sum|a|^2=1$), a globalna faza još jedan, pa fizičko stanje ima $2\cdot 2^N - 2 = 2^{N+1}-2$ realnih parametara. Za $N=3$ to je $14$ (naspram $2N=6$ koliko bi imalo $N$ nezavisnih Blohovih sfera — razlika je spregnutost).

```python
import numpy as np
rng = np.random.default_rng(0); N = 3
a = rng.normal(size=2**N) + 1j*rng.normal(size=2**N)
a /= np.linalg.norm(a)                          # normiranje
print("sum |a|^2 =", round(np.sum(np.abs(a)**2), 12))   # 1.0
print("fizickih realnih parametara:", 2**(N+1) - 2)     # 14 za N=3
```
:::



## Prva spregnuta kapija: CNOT i Bell stanje

Proizvodna stanja gradimo tenzorskim proizvodom, ali da bismo **napravili** spregnutost treba nam kapija koja povezuje dva kubita. Najvažnija je **CNOT** (kontrolisano-NE): ako je kontrolni kubit $\ket1$, ona obrne ciljni kubit; ako je $\ket0$, ne radi ništa. U računskoj bazi $\{\ket{00},\ket{01},\ket{10},\ket{11}\}$ (kontrola = prvi kubit) njena matrica je

```{math}
:label: eq:cnot
\mathrm{CNOT} =
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0
\end{pmatrix}.
```

Primenimo li $H$ na prvi kubit, pa CNOT, iz $\ket{00}$ dobijamo čuveno **Bell stanje** — proizvodni ulaz, a spregnuti izlaz.

:::{admonition} Vežba 5 — napravi Bell stanje
:class: tip
Primeni CNOT na $(H\otimes I)\ket{00}$ i pokaži da dobiješ $\tfrac{1}{\sqrt2}(\ket{00}+\ket{11})$. Iskoristi test faktorabilnosti iz Vežbe 2 da potvrdiš da izlaz **nije** proizvodno stanje, iako je ulaz bio.
:::

:::{admonition} Rešenje
:class: dropdown
$(H\otimes I)\ket{00} = \tfrac{1}{\sqrt2}(\ket{00}+\ket{10})$; CNOT obrne ciljni kubit tamo gde je kontrola $\ket1$, pa $\ket{10}\to\ket{11}$, čime dobijamo $\tfrac{1}{\sqrt2}(\ket{00}+\ket{11})$.

```python
import numpy as np
ket0 = np.array([1, 0], dtype=complex); ket1 = np.array([0, 1], dtype=complex)
H = np.array([[1, 1], [1, -1]])/np.sqrt(2); I = np.eye(2)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)

psi  = np.kron(H @ ket0, ket0)                  # (H⊗I)|00>
out  = CNOT @ psi
bell = (np.kron(ket0, ket0) + np.kron(ket1, ket1))/np.sqrt(2)
print("izlaz == Bell? ", np.allclose(out, bell))

def faktorabilno(psi, tol=1e-9):
    a = psi.reshape(4); return abs(a[0]*a[3] - a[1]*a[2]) < tol
print("izlaz faktorabilan? ", faktorabilno(out))   # False -> spregnuto
```

Spregnuta stanja, koja ne možemo razložiti na „prvi kubit puta drugi kubit", srce su kvantne prednosti — njima se detaljno bavimo u [](../poglavlje3/09-entanglement.md).
:::



## Vežbe: memorija i skaliranje

:::{admonition} Vežba 6 — koliko kubita staje u RAM?
:class: tip
Koliko **najviše** kubita staje u $32\,\text{GiB}$ RAM-a ako čuvamo samo vektor stanja? Reši za dvostruku ($16$ B) i za jednostruku ($8$ B) preciznost, koristeći {eq}`eq:mem-formula`. Šta primećuješ o „dobitku" od prelaska na nižu preciznost?
:::

:::{admonition} Rešenje
:class: dropdown
Iz $2^N\cdot b \le M$ sledi $N \le \log_2(M/b)$. Za $M = 32\,\text{GiB}$: dvostruka preciznost daje $N = 31$, a jednostruka $N = 32$. Prepolovljavanje memorije po amplitudi kupuje **tačno jedan** dodatni kubit — jer je zavisnost od $N$ eksponencijalna, a od preciznosti tek linearna.

```python
import numpy as np
M = 32 * 1024**3
for b in (16, 8):
    N = int(np.floor(np.log2(M / b)))
    print(f"b = {b} B  ->  max N = {N}")
```
:::

:::{admonition} Vežba 7 — faktor rasta po kubitu
:class: tip
Za koliko se **poveća** potrebna memorija kada pređeš sa $N$ na $N+1$ kubita — posebno za vektor, a posebno za matricu? Objasni zašto matrica za $N$ kubita troši istu memoriju kao vektor za $2N$ kubita.
:::

:::{admonition} Rešenje
:class: dropdown
Vektor: $M_{\text{vektor}}(N+1)/M_{\text{vektor}}(N) = 2^{N+1}/2^{N} = 2$ — udvostruči se. Matrica: $4^{N+1}/4^{N} = 4$ — učetvorostruči se. Kako je $4^{N} = 2^{2N}$, matrica za $N$ kubita ima isto elemenata kao vektor za $2N$ kubita, pa i istu memoriju (uz istu preciznost).
:::







# Ovde ćemo da stavimo osnove
- Više kubitni sistemi se dobijaju tenzorskim proizvodom
- Neke osnove. Dvokubitni primeri --> Bellova stanja
- Računanje zapletenosti
- Osnove kako se entanglement definished
- Born-ovo pravilo za merenje, primeri računice
- Kolo za kvantu teleportaciju, numericki i graficko objasnjenje
- Bellova nejednakost, tenutak kada kvantna mehanika ulazi u igra i velika razlika sa klasičnom fizikom
- full state multiqubit tomography



### test


Kada je kubit deo **registra** od više kjubita, isti projektor deluje kao $\Pi_b \otimes I$ na ostatak: zadržava samo one delove superpozicije koji su u skladu sa izmerenim ishodom, dok **preostali kjubiti ostaju u superpoziciji** (i mogu ostati međusobno spregnuti). Taj, bogatiji slučaj radimo kasnije, kada uvedemo višekjubitne registre u [](../poglavlje3/06-multiqubit.md).

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

# Zašto samo jedan kubit do sada?
Videli smo do sada šta sve jedan kubit podrazumeva. Na jednom kubitu gradimo intuiciju i tehničke alate koji su na potrebni kasnije. 
Kao primer korisnosti jednog kubit sistema u merenju klasičnih signala pogledajte:
- https://ishaan-kannan.github.io/blog/2026/08/17/bringing-quantum-advantage-to-todays-classical-world/
- sa pratećim radom na https://arxiv.org/pdf/2608.13521


### Napomena
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


