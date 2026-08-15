---
title: "Realni kvantni računar"
short_title: Realni kvantni računar
description: Kako šum utiče na jedan kubit i kako ga vidimo na Blohovoj sferi?
---

# Realni kvantni računar (noisy hardware)

Do sada smo računali kao da je sve **savršeno**: kapije deluju tačno, stanje se ne kvari, a merenje daje čiste Bornove verovatnoće. Pravi kvantni računari su, međutim, **bučni** (eng. *noisy*). Kubit stalno „curi" informaciju u okolinu, kapije nisu idealne, a što je kolo dublje, to je greška veća. Ova era računara zove se **NISQ** (eng. *Noisy Intermediate-Scale Quantum*).

U ovoj lekciji uzimamo **najjednostavniji** model šuma za jedan kubit — **depolarizacioni kanal** — i korak po korak vidimo šta on radi stanju. Cilj je da steknemo osećaj: *kako šum menja stanje, verovatnoće merenja, i kako to izgleda na Blohovoj sferi.*

:::{important} Ključna ideja
:class: simple
Idealna kapija **rotira** Blohov vektor (dužina ostaje $1$). Šum ga **skuplja ka centru** (dužina se smanjuje). Dovoljno šuma i vektor padne u centar — stanje postane potpuno nasumično, „zaboravljeno".
:::

## Čista i mešana stanja: matrica gustine

Da bismo uopšte opisali „pokvareno" stanje, čist vektor $\ket{\psi}$ nam više nije dovoljan. Uvodimo **matricu gustine** $\rho$.

Za čisto stanje $\ket{\psi}$ ona je prosto projektor na to stanje:

```{math}
:label: eq:rho-pure
\rho = \dyad{\psi}{\psi}.
```

Na primer, za $\ket{0}$ je $\rho = \dyad{0}{0} = \left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)$.

Svako stanje jednog kubita (i čisto i „pokvareno") može se zapisati preko **Blohovog vektora** $\mathbf{r} = (r_x, r_y, r_z)$:

```{math}
:label: eq:rho-bloch
\rho = \tfrac{1}{2}\big(I + r_x X + r_y Y + r_z Z\big), \qquad
\mathbf{r} = \big(\langle X\rangle, \langle Y\rangle, \langle Z\rangle\big) = \big(\Tr(\rho X),\, \Tr(\rho Y),\, \Tr(\rho Z)\big).
```

Geometrija je jednostavna i lepa:

- $|\mathbf{r}| = 1$ (**na površini** sfere) $\Rightarrow$ **čisto** stanje, baš kao u prethodnim lekcijama.
- $|\mathbf{r}| < 1$ (**unutar** sfere) $\Rightarrow$ **mešano** stanje — mešavina više mogućnosti.
- $\mathbf{r} = 0$ (**centar**) $\Rightarrow$ **maksimalno mešano** stanje $\rho = I/2$ — potpuno nasumičan kubit.

Koliko je stanje „čisto" meri **čistoća** (eng. *purity*):

```{math}
:label: eq:purity
\Tr(\rho^2) = \tfrac{1}{2}\big(1 + |\mathbf{r}|^2\big),
```

koja ide od $1$ (čisto, na površini) do $\tfrac{1}{2}$ (maksimalno mešano, u centru).

```python
import numpy as np

# Paulijeve matrice i baza (kao u prethodnim lekcijama)
I2 = np.eye(2, dtype=complex)
X  = np.array([[0, 1], [1, 0]], dtype=complex)
Y  = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z  = np.array([[1, 0], [0, -1]], dtype=complex)
ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)

def rho_iz_stanja(psi):
    """Matrica gustine rho = |psi><psi| za čisto stanje."""
    psi = psi.reshape(2, 1)
    return psi @ psi.conj().T

def blohov_vektor(rho):
    """Blohov vektor r = (Tr(rho X), Tr(rho Y), Tr(rho Z))."""
    return np.array([np.trace(rho @ X).real,
                     np.trace(rho @ Y).real,
                     np.trace(rho @ Z).real])

def cistoca(rho):
    return np.trace(rho @ rho).real

# provera: |0> je čisto, na severnom polu (0,0,1)
rho0 = rho_iz_stanja(ket0)
print("r(|0>)  =", np.round(blohov_vektor(rho0), 3))   # [0 0 1]
print("čistoća =", round(cistoca(rho0), 3))            # 1.0
```

## Depolarizacioni kanal

Najjednostavniji model šuma kaže: **sa verovatnoćom $p$ nešto krene po zlu i kubit se zameni potpuno nasumičnim stanjem $I/2$**, a sa verovatnoćom $1-p$ ostane netaknut. Matematički:

```{math}
:label: eq:depol
\mathcal{E}(\rho) = (1-p)\,\rho + p\,\frac{I}{2}, \qquad p \in [0, 1].
```

Parametar $p$ je **jačina šuma**: $p=0$ je savršen kubit, $p=1$ je potpuno izbrisan kubit.

### Računica korak po korak (ulaz $\ket{0}$)

Uzmimo $\rho = \dyad{0}{0} = \left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)$ i pustimo ga kroz kanal {eq}`eq:depol`:

```{math}
\mathcal{E}(\rho) = (1-p)\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}
+ \frac{p}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
= \begin{pmatrix} 1 - \tfrac{p}{2} & 0 \\[4pt] 0 & \tfrac{p}{2} \end{pmatrix}.
```

Dijagonala matrice gustine su upravo **verovatnoće merenja** u računskoj bazi:

```{math}
:label: eq:depol-probs
p(0) = 1 - \frac{p}{2}, \qquad p(1) = \frac{p}{2}.
```

Iako smo pripremili čisto $\ket{0}$ (koje bi *uvek* dalo $0$), sada sa verovatnoćom $p/2$ dobijamo pogrešan ishod $1$! To je „greška merenja" koju uvodi šum.

A Blohov vektor? Bio je $\mathbf{r} = (0,0,1)$, a sada je

```{math}
r_z = \Tr(\rho Z) = \Big(1 - \tfrac{p}{2}\Big) - \tfrac{p}{2} = 1 - p,
```

tj. $\mathbf{r} = (0, 0, 1-p)$. **Skratio se za faktor $(1-p)$.**

### Opšte pravilo: vektor se skuplja

Ovo nije slučajno baš za $\ket{0}$. Ako umetnemo $\rho = \tfrac12(I + \mathbf{r}\cdot\boldsymbol\sigma)$ iz {eq}`eq:rho-bloch` u kanal {eq}`eq:depol`, dobijamo

```{math}
:label: eq:depol-bloch
\mathcal{E}(\rho) = \tfrac{1}{2}\Big(I + (1-p)\,\mathbf{r}\cdot\boldsymbol\sigma\Big)
\quad\Longrightarrow\quad
\boxed{\;\mathbf{r} \;\longmapsto\; (1-p)\,\mathbf{r}\;}
```

Dakle depolarizacija **skuplja ceo Blohov vektor ka centru za faktor $(1-p)$**, ne menjajući mu pravac. Stanje ostaje na istom „meridijanu", samo klizi ka centru — postaje sve više mešano.

```python
def depolarizacija(rho, p):
    """Depolarizacioni kanal: E(rho) = (1-p) rho + p I/2."""
    return (1 - p) * rho + p * I2 / 2

p = 0.3
rho_in  = rho_iz_stanja(ket0)          # čisto |0>
rho_out = depolarizacija(rho_in, p)

print("E(|0><0|) =\n", np.round(rho_out, 3))
print("p(0), p(1)      :", np.round(np.diag(rho_out).real, 3))   # [0.85 0.15]
print("Blohov vektor   :", np.round(blohov_vektor(rho_out), 3))  # [0 0 0.7] = (1-p)
print("dužina |r|      :", round(np.linalg.norm(blohov_vektor(rho_out)), 3))  # 0.7
print("čistoća Tr(ρ²)  :", round(cistoca(rho_out), 3))           # 0.745
```

Za $p = 0.3$: verovatnoća greške je $p(1) = 0.15$, vektor se skratio na $0.7$, a čistoća pala sa $1$ na $0.745$. Sve tri brojke govore istu priču — **stanje više nije savršeno**.

## Vizuelizacija na Blohovoj sferi

Pošto svako jednokubitno stanje živi na (ili u) Blohovoj sferi, šum je najlakše „videti" upravo tu. Koristimo istu pomoćnu funkciju `nacrtaj_sferu` kao u lekciji o kapijama, samo sada crtamo vektor **pre** i **posle** delovanja šuma.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

%matplotlib inline

def nacrtaj_sferu(ax):
    # providna sferična mreža
    u = np.linspace(0, 2*np.pi, 60)
    v = np.linspace(0, np.pi,   60)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(xs, ys, zs, color="black", alpha=0.06,
                    linewidth=0, rstride=2, cstride=2, antialiased=True, shade=False)
    circ = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(circ), np.sin(circ), 0, color="#555555", lw=0.8, alpha=0.5)
    for d, col in [((1,0,0), "#c0392b"), ((0,1,0), "#27ae60"), ((0,0,1), "#34495e")]:
        dx, dy, dz = d
        ax.quiver(0,0,0,  1.3*dx,  1.3*dy,  1.3*dz, color=col, lw=1.2, arrow_length_ratio=0.05)
        ax.quiver(0,0,0, -1.3*dx, -1.3*dy, -1.3*dz, color=col, lw=1.2, arrow_length_ratio=0.05)
    ax.text(1.45, 0, 0, r"$x$", color="#c0392b")
    ax.text(0, 1.42, 0, r"$y$", color="#27ae60")
    ax.text(0, 0, 1.45, r"$z$", color="#34495e")
    ax.set_box_aspect([1,1,1])
    ax.set_xlim(-1.1,1.1); ax.set_ylim(-1.1,1.1); ax.set_zlim(-1.1,1.1)
    ax.set_axis_off()

# --- stanje pod uglom (da se lepo vidi), pa depolarizacija ---
def stanje(theta, phi):
    return np.array([[np.cos(theta/2)],
                     [np.exp(1j*phi)*np.sin(theta/2)]], dtype=complex)

p = 0.3
rho_in  = rho_iz_stanja(stanje(np.radians(55), np.radians(50)))
rho_out = depolarizacija(rho_in, p)
r_pre   = blohov_vektor(rho_in)
r_posle = blohov_vektor(rho_out)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")
nacrtaj_sferu(ax)
ax.plot(*zip(r_posle, r_pre), color="gray", ls=":", lw=1.3)   # skupljanje
ax.quiver(0,0,0, *r_pre,   color="#8e44ad", lw=3, arrow_length_ratio=0.12)
ax.text(*(1.15*r_pre), r"pre (čisto)", color="#8e44ad", fontsize=13)
ax.quiver(0,0,0, *r_posle, color="#e67e22", lw=3, arrow_length_ratio=0.17)
ax.text(*(1.15*r_posle), r"posle", color="#e67e22", fontsize=13)
ax.scatter([0],[0],[0], color="black", s=15)
ax.set_title(r"Depolarizacija skuplja Blohov vektor: $\mathbf{r}\to(1-p)\,\mathbf{r}$")
ax.view_init(elev=22, azim=40)
plt.tight_layout()
plt.savefig("sum_depolarizacija.png", dpi=300, bbox_inches="tight")
plt.show()
```

```{figure} ../images/sum_depolarizacija.png
:label: fig:sum_depolarizacija
:alt: Blohov vektor se skuplja ka centru posle depolarizacije
:width: 460px
:align: center

Depolarizacija ne menja **pravac** Blohovog vektora — samo mu skraćuje **dužinu** za faktor $(1-p)$. Čisto stanje (ljubičasto, na površini) klizi ka centru u mešano stanje (narandžasto).
```

## Šum koji se ponavlja: put ka centru

Na pravom hardveru šum ne deluje jednom, već **posle svake kapije** i tokom svakog čekanja. Ako isti kanal primenimo $n$ puta, faktori se množe:

```{math}
:label: eq:depol-n
\mathbf{r} \;\longmapsto\; (1-p)^n\,\mathbf{r}.
```

Pošto je $0 \le 1-p \le 1$, dužina **eksponencijalno opada** ka nuli: što je kolo dublje, to je stanje bliže centru sfere, tj. sve nasumičnije. Tako izgleda **dekoherencija** — postepeni gubitak kvantne informacije.

```python
p = 0.3
rho = rho_iz_stanja(ket0)
print("n   r_z=(1-p)^n   čistoća   p(1)")
for n in range(6):
    r  = blohov_vektor(rho)
    print(f"{n}      {r[2]:.3f}       {cistoca(rho):.3f}    {rho[1,1].real:.3f}")
    rho = depolarizacija(rho, p)   # još jedan „udarac" šuma
```

```{figure} ../images/sum_opadanje.png
:label: fig:sum_opadanje
:alt: ponavljanje depolarizacije skuplja vektor ka centru sfere
:width: 460px
:align: center

Ponavljanjem šuma ($p=0.3$) Blohov vektor stanja $\ket{0}$ se sve više skuplja: $r_z = (1-p)^n = 1,\,0.7,\,0.49,\dots \to 0$. U granici stanje padne u centar — potpuno nasumičan, „mrtav" kubit.
```

Verovatnoća pogrešnog ishoda pritom raste ka $0.5$ (čist bacač novčića):

```{math}
:label: eq:depol-n-probs
p(1) = \frac{1 - (1-p)^n}{2} \;\xrightarrow[n\to\infty]{}\; \frac{1}{2}.
```

Sledeći grafik sažima **sva tri lica** istog šuma kao funkciju jačine $p$: dužinu vektora, čistoću i grešku merenja.

```python
import numpy as np
import matplotlib.pyplot as plt

pp = np.linspace(0, 1, 200)
plt.figure(figsize=(12, 6))
plt.plot(pp, 1 - pp,                 color="#8e44ad", lw=2.4, label=r"dužina $|\mathbf{r}| = 1-p$")
plt.plot(pp, 0.5*(1 + (1-pp)**2),    color="#e67e22", lw=2.4, label=r"čistoća $\mathrm{Tr}(\rho^2)$")
plt.plot(pp, pp/2,                   color="#2980b9", lw=2.4, label=r"greška merenja $p(1)=p/2$")
plt.axhline(0.5, color="gray", ls="--", lw=1, alpha=0.7)
plt.xlabel("Jačina šuma $p$"); plt.ylabel("Vrednost")
plt.xlim(0, 1); plt.ylim(0, 1.02)
plt.title("Uticaj depolarizacionog šuma na jedan kubit")
plt.grid(alpha=0.2); plt.legend()
plt.tight_layout()
plt.savefig("sum_verovatnoca.png", dpi=300, bbox_inches="tight")
plt.show()
```

```{figure} ../images/sum_verovatnoca.png
:label: fig:sum_verovatnoca
:alt: dužina vektora, čistoća i greška merenja kao funkcije jačine šuma
:width: 560px
:align: center

Tri načina da se vidi isti šum. Kako $p$ raste: dužina vektora i čistoća opadaju ka mešanom stanju, a greška merenja raste ka $50\%$. Na $p=1$ kubit je potpuno nasumičan.
```

## Ekvivalent na pravom hardveru (Qiskit)

U Qiskit-u šum ubacujemo preko **modela šuma** (`NoiseModel`). Ovde svakoj `id` operaciji (jedno „čekanje" kubita) dodeljujemo depolarizacionu grešku, pripremimo $\ket{0}$, pustimo ga da čeka $n$ koraka, i izmerimo. Rezultat prati našu formulu $p(1) = \tfrac{1-(1-p)^n}{2}$.

```python
# instalacija dodatka za simulaciju šuma
!pip install qiskit qiskit-aer
```

```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

p = 0.3
noise = NoiseModel()
noise.add_all_qubit_quantum_error(depolarizing_error(p, 1), ['id'])  # šum na "čekanje"
sim = AerSimulator(noise_model=noise)

for n in [1, 3, 5]:
    qc = QuantumCircuit(1, 1)
    for _ in range(n):
        qc.id(0)          # svaki korak čekanja -> jedan "udarac" šuma
    qc.measure(0, 0)
    counts = sim.run(qc, shots=50000).result().get_counts()
    p1 = counts.get('1', 0) / 50000
    print(f"n={n}:  p(1) izmereno = {p1:.3f}   teorija = {(1-(1-p)**n)/2:.3f}")
# n=1: ~0.150   n=3: ~0.329   n=5: ~0.417  -> raste ka 0.5
```

:::{danger} U slučaju greške pri izvršenju (klik)
:class: dropdown
U slučaju greške pri puštanju koda, potrebno je restart-ovati 'Runtime session' vašeg Jupiter notebook-a (i proveriti da je paket `qiskit-aer` instaliran).
:::

:::{note} Šum je više od depolarizacije (klik)
:class: dropdown
Depolarizacioni kanal je najjednostavniji, „simetričan" model — skuplja vektor podjednako u svim pravcima. Pravi hardver ima i **usmerene** kanale: *amplitude damping* ($T_1$, opuštanje ka $\ket{0}$) i *phase damping* ($T_2$, gubitak faze, spljošti sferu ka $z$-osi). Svi oni imaju istu geometrijsku poruku: **stanje klizi sa površine ka unutrašnjosti** Blohove sfere.
:::

:::{important} Zaključak
:class: simple
Idealna kapija je **rotacija** (dužina vektora $=1$). Šum je **skupljanje** ($\mathbf{r}\to(1-p)\mathbf{r}$). Zato je borba za kvantni računar borba da vektor **ostane blizu površine** što duže — bilo boljim hardverom, bilo **kvantnom korekcijom grešaka**.
:::

## Vežbe

:::{admonition} Vežba 1
:class: tip
Kroz depolarizacioni kanal jačine $p = 0.2$ propusti čisto stanje $\ket{1}$. Izračunaj $\mathcal{E}(\rho)$, verovatnoće $p(0)$ i $p(1)$, i novi Blohov vektor. Za koliko se skratio?
:::

:::{admonition} Rešenje
:class: dropdown
$\rho = \dyad{1}{1} = \left(\begin{smallmatrix}0&0\\0&1\end{smallmatrix}\right)$, pa je $\mathcal{E}(\rho) = 0.8\left(\begin{smallmatrix}0&0\\0&1\end{smallmatrix}\right) + 0.1\left(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\right) = \left(\begin{smallmatrix}0.1&0\\0&0.9\end{smallmatrix}\right)$. Dakle $p(0) = p/2 = 0.1$, $p(1) = 1 - p/2 = 0.9$. Blohov vektor je bio $(0,0,-1)$, a sada $r_z = 0.1 - 0.9 = -0.8 = -(1-p)$, tj. skratio se za faktor $1-p = 0.8$.

```python
p = 0.2
rho_out = depolarizacija(rho_iz_stanja(ket1), p)
print("E(|1><1|) =\n", np.round(rho_out, 3))
print("p(0), p(1):", np.round(np.diag(rho_out).real, 3))     # [0.1 0.9]
print("Blohov vektor:", np.round(blohov_vektor(rho_out), 3)) # [0 0 -0.8]
```
:::

:::{admonition} Vežba 2
:class: tip
Pokaži da depolarizacija **ne menja** maksimalno mešano stanje $\rho = I/2$ (centar sfere). Objasni zašto to ima smisla.
:::

:::{admonition} Rešenje
:class: dropdown
Njegov Blohov vektor je $\mathbf{r} = 0$, a pravilo $\mathbf{r}\to(1-p)\mathbf{r}$ daje opet $0$. Direktno: $\mathcal{E}(I/2) = (1-p)\tfrac{I}{2} + p\tfrac{I}{2} = \tfrac{I}{2}$. Ima smisla jer je $I/2$ već „potpuno nasumično" — nema više informacije koju bi šum mogao da pokvari. To je **fiksna tačka** kanala.

```python
rho_mix = I2 / 2
print("E(I/2) = I/2 ? ", np.allclose(depolarizacija(rho_mix, 0.4), rho_mix))
```
:::

:::{admonition} Vežba 3
:class: tip
Za $p = 0.25$ i početno stanje $\ket{+}$, koliko puta $n$ treba primeniti šum da dužina Blohovog vektora padne ispod $0.1$? Reši i „na papiru" (preko $(1-p)^n$) i kodom.
:::

:::{admonition} Rešenje
:class: dropdown
Tražimo najmanje $n$ za koje je $(1-p)^n = 0.75^n < 0.1$. Logaritmovanjem: $n > \dfrac{\ln 0.1}{\ln 0.75} \approx \dfrac{-2.302}{-0.288} \approx 8.0$, pa je $n = 9$ (jer je $0.75^8 = 0.100$, tek malo iznad, a $0.75^9 = 0.075$).

```python
p = 0.25
n = 0
duzina = 1.0
while duzina >= 0.1:
    duzina *= (1 - p)
    n += 1
print("Potrebno koraka n =", n, " -> dužina =", round(duzina, 3))   # n = 9
```
:::

:::{admonition} Vežba 4 (teža)
:class: tip
**Vernost** (eng. *fidelity*) meri koliko izlazno stanje liči na ulazno čisto $\ket{\psi}$: $F = \bra{\psi}\mathcal{E}(\rho)\ket{\psi}$. (a) Pokaži da za depolarizaciju **ne zavisi** od izbora $\ket{\psi}$ i iznosi $F = 1 - \tfrac{p}{2}$. (b) Kolika sme biti jačina šuma $p$ da vernost jedne operacije bude bar $99\%$ (tipičan cilj za dobar hardver)? Proveri kodom na nekoliko nasumičnih stanja.
:::

:::{admonition} Rešenje
:class: dropdown
(a) Kako je $\mathcal{E}(\rho) = (1-p)\dyad{\psi}{\psi} + p\tfrac{I}{2}$, dobijamo
$F = (1-p)\,|\braket{\psi}{\psi}|^2 + p\,\bra{\psi}\tfrac{I}{2}\ket{\psi} = (1-p)\cdot 1 + p\cdot\tfrac12 = 1 - \tfrac{p}{2}$,
gde smo iskoristili $\braket{\psi}{\psi} = 1$. Rezultat **ne zavisi** od $\ket{\psi}$ — depolarizacija je „ravnomerna" po celoj sferi.

(b) $F \ge 0.99 \Rightarrow 1 - \tfrac{p}{2} \ge 0.99 \Rightarrow p \le 0.02$. Dakle šum mora biti ispod $2\%$ po operaciji.

```python
def vernost(psi, p):
    psi = psi.reshape(2, 1)
    rho_out = depolarizacija(rho_iz_stanja(psi), p)
    return (psi.conj().T @ rho_out @ psi).item().real

p = 0.02
for _ in range(4):
    a = np.random.randn(2) + 1j*np.random.randn(2)
    psi = a / np.linalg.norm(a)          # nasumično čisto stanje
    print("F =", round(vernost(psi, p), 4), " (teorija 1 - p/2 =", 1 - p/2, ")")
```
:::
