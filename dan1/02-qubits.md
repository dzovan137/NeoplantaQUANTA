---
title: "Kjubit"
short_title: Kjubit
description: Stanje jednog kubita. 
---

# Qubit (Kjubit)

**Qubit** je osnovna jedinica građe i funkcije kvantne informatike i predstavlja
analogon klasičnim bit-ovima. Klasični bitovi mogu da imaju vrednosti $0$ i $1$, qubit može biti u linearnoj superpoziciji ova dva stanja!




(sec:state)=
## Kvantno stanje kjubita

Kjubit predstavlja vektor u dvodimenzionalnom kompleksnom Hilbertovom prostoru $\Hilb = \CC^2$.
Ovaj Hilbertov prostor je razapet **ortonormiranom računskom bazom** $\ket{0}$ i $\ket{1}$. Ove vektore zapisujemo kao
```{math}
:label: eq:basis-vectors
\ket{0} = \begin{pmatrix}1\\0\end{pmatrix},
\qquad
\ket{1} = \begin{pmatrix}0\\1\end{pmatrix}.
```

Generalno, stanje kjubita (ket vektor) možemo zapisati kao

```{math}
:label: eq:qubit
\ket{\psi} = \alpha \ket{0} + \beta \ket{1},
\qquad \alpha, \beta \in \CC,
```
gde kompleksne amplitude zadovoljavaju uslov **normalizacije**
```{math}
:label: eq:norm
\braket{\psi}{\psi} = |\alpha|^2 + |\beta|^2 = 1 .
```
Gde smo već koristili i uveli Dirakovu bra-ket notaciju. 

Sledeće pokušajmo sada da izvedemo jednačinu [](#eq:norm) direktno. 

:::{note} Prikaži računicu (klik)
:class: dropdown
Dobijanje jednačine [](#eq:norm) koristeći Dirakov zapis i osnovne definicije. 

```{figure} ../images/normalizacija.png
:label: fig:state-derivation-placeholder
:alt: Privremena slika ručne računice za stanje kjubita.
:width: 520px
:align: center

```
:::


## Blohova sfera


Prirodno pitanje je *odakle* dva realna ugla, kad opšte stanje [](#eq:qubit) ima dva
**kompleksna** koeficijenta. Kratak odgovor je prebrojavanje parametara: dve kompleksne
amplitude nose četiri realna broja (dva modula i dve faze); uslov normalizacije [](#eq:norm)
oduzima jedan, a sloboda izbora **globalne faze** još jedan — ostaju tačno **dva** slobodna
parametra. Njih biramo kao dva ugla:
- $\theta$: polarni ugao, $\theta \in [0,\pi]$
- $\varphi$: azimutalni ugao (relativna faza), $\varphi \in [0,2\pi)$

Uz taj izbor, svako jednokjubitno stanje se **do na globalnu fazu** može zapisati u obliku

```{math}
:label: eq:bloch
\ket{\psi} = \cos{\left( \tfrac{\theta}{2} \right)} \,\ket{0} + e^{i\varphi}\sin{ \left( \tfrac{\theta}{2} \right)}\,\ket{1},
```

:::{note} Prikaži izvođenje (klik)
:class: dropdown
Kako iz opšteg stanja [](#eq:qubit) dolazimo do oblika [](#eq:bloch).

Napišimo amplitude u polarnom obliku, $\alpha = r_0\,e^{i\gamma_0}$ i $\beta = r_1\,e^{i\gamma_1}$,
gde su $r_0, r_1 \ge 0$ moduli, a $\gamma_0, \gamma_1$ faze:
```{math}
\ket{\psi} = r_0\,e^{i\gamma_0}\ket{0} + r_1\,e^{i\gamma_1}\ket{1}.
```
Izvučemo zajedničku (globalnu) fazu $e^{i\gamma_0}$ ispred zagrade:
```{math}
\ket{\psi} = e^{i\gamma_0}\left( r_0\ket{0} + r_1\,e^{i(\gamma_1 - \gamma_0)}\ket{1} \right).
```
Globalna faza $e^{i\gamma_0}$ ne utiče ni na jednu verovatnoću merenja (to formalno pokazujemo
u **Vežbi 8** na kraju lekcije), pa je slobodno odbacujemo. Uvedimo **relativnu fazu**
$\varphi \equiv \gamma_1 - \gamma_0$:
```{math}
\ket{\psi} = r_0\ket{0} + r_1\,e^{i\varphi}\ket{1}.
```
Normalizacija [](#eq:norm) daje $r_0^2 + r_1^2 = 1$ uz $r_0, r_1 \ge 0$. Takve tačke leže na
jediničnoj kružnici u prvom kvadrantu, pa ih prirodno parametrizujemo **jednim** uglom:
```{math}
r_0 = \cos\tfrac{\theta}{2}, \qquad r_1 = \sin\tfrac{\theta}{2}, \qquad \theta \in [0,\pi],
```
jer za $\tfrac{\theta}{2} \in [0, \tfrac{\pi}{2}]$ i kosinus i sinus prolaze sve nenegativne
vrednosti i zadovoljavaju $\cos^2\tfrac{\theta}{2} + \sin^2\tfrac{\theta}{2} = 1$. Time smo
dobili [](#eq:bloch). Polovina ugla ($\theta/2$, a ne $\theta$) osigurava da $\theta$ pređe
ceo opseg $[0,\pi]$ dok stanje putuje od severnog pola $\ket{0}$ ($\theta = 0$) do južnog pola
$\ket{1}$ ($\theta = \pi$).
:::

gde svako moguće stanje i odabrani ugao pokazuje na površinu sfere radijusa 1. Kao što je prikazano na slici [](#fig:bloch). 


```{figure} ../images/BlohovaSfera.png
:label: fig:bloch
:alt: Bloh
:width: 420px
:align: center

**Blohova sfera** sa severnim i južnim polom $\ket{0}$ i $\ket{1}$, pritom gde je jednokjubitno stanje $\ket{\psi}$ iz jednačine {eq}`eq:bloch` prikazano sa ljubičastom bojom sa primerom dva ugla $(\theta, \varphi)$. 
Ostale relevantne tačke na sferi poput $\ket{\pm}$ i $\ket{\pm i}$ su takođe date. Za ukazane vrednosti uglova potrebno je konvertovati vrednosti uglova koristeći $\frac{\pi}{180}$, i to za dati primer $\cos{(\frac{45^{\circ}}{2})} = \cos{(\frac{45 \frac{\pi}{180}}{2})} = 0.92388$, $\varphi = 45^{\circ} = 45 \frac{pi}{180} = 0.785398$, i $\sin{(\frac{45^{\circ}}{2})} = 0.382683$.
```

## Vaš prvi 'kvantni' kod u Python-u! 

Hajde da generišemo jednokjubitna stanja, kao i napravimo vizuelizaciju Blohove sfere. 


:::{tip} Kopiraj u svoj Jupyter Notebook! 
:class: simple
Kopiraj svaku liniju koda iz obeleženog kodnog bloka u svoj Jupyter Notebook na [Google Colab](https://colab.research.google.com) i pokreni koristeći **Shift+Enter**!
Svaki blok i linija koda sadrže objašnjenje o funkciji i ulozi koju igraju u kodu.

:::

```python
# za numeričku manipulaciju nizova, vektori, matrice, tenzori
import numpy as np             

# Računska baza |0> and |1> kao ket vektori (vektori kolone)
ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)

# prikaži definicije stanja 
print("Stanje nula: ")
print(ket0)
print("Stanje jedan: ")
print(ket1)
```

:::{note} Različite opcije pri definisanju



Kada definišeš vektor pomoću `np.array`, parametar `dtype` određuje tip elemenata u nizu. Najčešće mogućnosti su:

- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int</span> za cele brojeve
- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">float</span> za realne brojeve
- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">complex</span> za kompleksne brojeve, što je ovde najkorisnije
- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">bool</span> za logičke vrednosti, Tačno/Netačno (True/False) 


Kod dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int</span>, NumPy obično bira celobrojni tip koji odgovara platformi: na 64-bit sistemima to je najčešće <span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int64</span>, a na 32-bit sistemima <span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int32</span>. Ako želiš potpuno fiksnu širinu, koristi dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">np.int32</span> ili dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">np.int64</span>.


U ovom primeru koristimo dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">complex</span> zato što amplituda kvantnog stanja može da bude kompleksna!

:::

Hajde sad da definišemo stanje plus $\ket{+}$ kao: $\theta = \frac{\pi}{2}$ i $\varphi = 0$ (vidi [](#fig:bloch)) i to
```{math}
:label: eq:plus
\ket{+} = \dfrac{1}{\sqrt{2}} ( \ket{0} + \ket{1} ), 
```
stanje koje možemo da definišemo u Python-u kao
```python
# Definisanje linearna superpozicija stanja: |+> = (|0> + |1>)/sqrt(2)
alpha = 1/np.sqrt(2)
beta  = 1/np.sqrt(2)
psi = alpha * ket0 + beta * ket1

# prikaži definiciju stanja
print("|psi> =")
print(psi)
```

Sada možemo da proverimo normalizaciju vektora {eq}`eq:norm` za ovaj primer direktno 
izračunajući $\braket{\psi}{\psi}$ što je u kodu:
`psi.conj().T @ psi`:

```python
# <psi|psi> što bi trebalo da nam da 1
norm = (psi.conj().T @ psi).item().real
print("norm =", round(norm, 6))
```

## Kod za vizuelizaciju Blohove sfere
Sada ćemo predstaviti kod koji vizualizuje različite vektore na Blohovoj sferi i generiše samu [](#fig:bloch).
Kod se sastoji od više elemenata i sledećih:



```python
import numpy as np                          
import matplotlib.pyplot as plt             # vizuelizacija
from mpl_toolkits.mplot3d import Axes3D     # vizuelizacija za 3D 

%matplotlib inline                          # pomoćna funkcija za vizuelizaciju unutar Jupyter notebook okruženja

```


Moguće je automatski uraditi konverziju uglova iz stepeni u radijane i to:

```python
# Biranje parametara ugla: po promeni potrebno je promeniti i ponoviti egzekuciju ovog i sledećih blokova 
THETA = np.radians(45)   # polarni ugao:   0 -> |0>,  180 deg -> |1>
PHI   = np.radians(45)   # azimutalni ugao oko z ose

# --- Uglovi -> Blohov vektor  r = (sin th cos ph, sin th sin ph, cos th) -
x = np.sin(THETA) * np.cos(PHI)
y = np.sin(THETA) * np.sin(PHI)
z = np.cos(THETA)
r = np.array([x, y, z])

# prikaži vrednosti
print("Blohov Vektor r =", np.round(r, 3))
print("Dužina |r|      =", round(float(np.linalg.norm(r)), 3), " (= 1 za čista stanja)")


```

Grafičke konverzije u cilju iscrtavanja:

```python
# Grafično generisanje sferične mreže 
u = np.linspace(0, 2*np.pi, 60)     # azimutalna mreža
v = np.linspace(0, np.pi,   60)     # polarna mreža

xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))

# Kružnica za Ekvator i dva meridijana
circ = np.linspace(0, 2*np.pi, 200)
```

Poslednji blok koji generiše sliku:


```python
# krajnje generisanje grafika (celokupan kod je dosta tehnički i nije neophodno razumeti ga u detalje za ovaj kurs)

fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(xs, ys, zs, color="black", alpha=0.08,
                linewidth=0, rstride=2, cstride=2, antialiased=True, shade=False)


ax.plot(np.cos(circ), np.sin(circ), 0, color="#555555", lw=0.8, alpha=0.6)   # equator
ax.plot(np.cos(circ), 0*circ, np.sin(circ), color="#bbbbbb", lw=0.6)         # xz meridian
ax.plot(0*circ, np.cos(circ), np.sin(circ), color="#bbbbbb", lw=0.6)         # yz meridian


L = 1.3
axis_kw = dict(lw=1.3, arrow_length_ratio=0.05)
for d, col in [((1,0,0), "#c0392b"), ((0,1,0), "#27ae60"), ((0,0,1), "#34495e")]:
    dx, dy, dz = d
    ax.quiver(0,0,0,  L*dx,  L*dy,  L*dz, color=col, **axis_kw)   # positive
    ax.quiver(0,0,0, -L*dx, -L*dy, -L*dz, color=col, **axis_kw)   # negative
# small axis letters at the positive tips
ax.text(1.45, 0, 0, r"$x$", color="#c0392b", fontsize=11, alpha=0.7)
ax.text(0, 1.42, 0, r"$y$", color="#27ae60", fontsize=11, alpha=0.7)
ax.text(0, 0, 1.45, r"$z$", color="#34495e", fontsize=11, alpha=0.7)


poles = [
    (( 0, 0, 1), r"$|0\rangle$",    "#34495e", ( 0.1, -0.1,  0.10)),
    (( 0, 0,-1), r"$|1\rangle$",    "#34495e", ( 0.1, -0.1, -0.12)),
    (( 1, 0, 0), r"$|{+}\rangle$",  "#c0392b", (0.14,-0.02,  0.10)),
    ((-1, 0, 0), r"$|{-}\rangle$",  "#c0392b", (-0.30,0.00,  0.10)),
    (( 0, 1, 0), r"$|{+}i\rangle$", "#27ae60", (0.02, 0.14,  0.10)),
    (( 0,-1, 0), r"$|{-}i\rangle$", "#27ae60", (0.02,-0.28,  0.10)),
]
for (px,py,pz), lab, col, (ox,oy,oz) in poles:
    ax.scatter(px, py, pz, color=col, s=55, edgecolors="white", linewidths=0.8, zorder=5)
    ax.text(px+ox, py+oy, pz+oz, lab, color=col, fontsize=13, ha="center")


ax.quiver(0,0,0, r[0], r[1], r[2], color="#8e44ad", lw=3.0, arrow_length_ratio=0.12, zorder=6)
ax.scatter(*r, color="#8e44ad", s=45, zorder=6)
ax.text(r[0]*1.12, r[1]*1.12, r[2]*1.12+0.06, r"$|\psi\rangle$", color="#8e44ad", fontsize=14)


ax.plot([r[0], r[0]], [r[1], r[1]], [0, r[2]], color="#8e44ad", ls=":", lw=1)
ax.plot([0, r[0]], [0, r[1]], [0, 0], color="#8e44ad", ls=":", lw=1.2)


ARC = "#e67e22"
nx, ny = np.cos(PHI), np.sin(PHI)            # xy-plane direction of the projection


tp = np.linspace(0, PHI, 40)
ax.plot(0.32*np.cos(tp), 0.32*np.sin(tp), 0, color=ARC, lw=1.8)
ax.text(0.46*np.cos(PHI/2), 0.46*np.sin(PHI/2), 0.0, r"$\varphi$",
        color=ARC, fontsize=14, ha="center")


tt = np.linspace(0, THETA, 40)
ax.plot(0.40*np.sin(tt)*nx, 0.40*np.sin(tt)*ny, 0.40*np.cos(tt), color=ARC, lw=1.8)
tm = THETA/2
ax.text(0.52*np.sin(tm)*nx, 0.52*np.sin(tm)*ny, 0.52*np.cos(tm), r"$\theta$",
        color=ARC, fontsize=14, ha="center")


a, b = np.cos(THETA/2), np.sin(THETA/2)
ax.set_title(rf"$|\psi\rangle = {a:.2f}\,|0\rangle + e^{{i\,{PHI:.2f}}}\,{b:.2f}\,|1\rangle$"
             + f"\n$\\theta={np.degrees(THETA):.0f}^\\circ,\\ \\varphi={np.degrees(PHI):.0f}^\\circ$",
             fontsize=13, pad=8)


ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_zlim(-1.1, 1.1)
ax.set_axis_off()
ax.view_init(elev=18, azim=35)

plt.tight_layout()
plt.savefig("blohova_sfera.png", dpi=300, bbox_inches="tight")
plt.show()
```
Izlaz ova 4 bloka koda je zapravo [](#fig:bloch). 


## Specijalna stanja na Blohovoj sferi

Najčešće izdvajamo šest posebnih čistih stanja koja leže na koordinatnim osama Blohove sfere (plus magično $\ket{T}$ stanje duž dijagonale $(1,1,1)$, između ekvatora i pola):

| Stanje | Definicija | $\theta$ | $\varphi$ |
|---|---|---:|---:|
| $\ket{0}$ | severni pol | $0$ | bilo koje |
| $\ket{1}$ | južni pol | $\pi$ | bilo koje |
| $\ket{+}$ | $\dfrac{1}{\sqrt 2}(\ket{0}+\ket{1})$ | $\dfrac{\pi}{2}$ | $0$ |
| $\ket{-}$ | $\dfrac{1}{\sqrt 2}(\ket{0}-\ket{1})$ | $\dfrac{\pi}{2}$ | $\pi$ |
| $\ket{+i}$ | $\dfrac{1}{\sqrt 2}(\ket{0}+i\ket{1})$ | $\dfrac{\pi}{2}$ | $\dfrac{\pi}{2}$ |
| $\ket{-i}$ | $\dfrac{1}{\sqrt 2}(\ket{0}-i\ket{1})$ | $\dfrac{\pi}{2}$ | $\dfrac{3\pi}{2}$ |
| $\ket{T}$ | $\approx 0.888\,\ket{0} + e^{i\pi/4}\,0.460\,\ket{1}$ | $\arccos\tfrac{1}{\sqrt3}\approx 54.7^\circ$ | $\dfrac{\pi}{4}$ |

Za polarne tačke $\ket{0}$ i $\ket{1}$ izbor za $\varphi$ je proizvoljan, jer svi azimutalni uglovi opisuju isti pol.

## Interpretacija stanja kao verovatnoća

Naposletku, hajde da damo definiciju koja daje verovatnoću nekog ishoda $k$ 
```{math}
:label: eq:bornrule
p(k) = |\braket{k}{\psi}|^2,
```
kao kvadrat modula kompleksnog skalarnog broja 

Za recimo:
- $k = 0$ da stanje se pronađe u stanju $\vert 0 \rangle$,
- $k = 1$ da stanje se pronađe u stanju $\vert 1 \rangle$.

Izračunajmo primer za stanje $\ket{+}$. 

:::{note} Prikaži računicu (klik)
:class: dropdown

```{figure} ../images/verovatnoca.png
:label: fig:verovatnoca
:alt: Verovatnoća račun
:width: 520px
:align: center

```
:::

Pomoću sledećeg koda možemo uraditi račun numerički:


```python
# Računska baza |0> and |1> kao ket vektori (vektori kolone)
ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)

# Definisanje linearna superpozicija stanja: |+> = (|0> + |1>)/sqrt(2)
alpha = 1/np.sqrt(2)
beta  = 1/np.sqrt(2)
psi = alpha * ket0 + beta * ket1

# Verovatnoća da izmerimo ishod k u računskoj bazi
p0 = abs((ket0.conj().T @ psi).item())**2
p1 = abs((ket1.conj().T @ psi).item())**2
print("p(0) =", round(p0, 3))
print("p(1) =", round(p1, 3))
```

Očekivani rezultat bi trebalo da bude $1/2$ i $1/2$ za oba slučaja. Ukoliko saberemo ove verovatnoće, one bi trebalo da izađu na $0.5 + 0.5 = 1$. 


Kao što vidimo, kvantna mehanika je u stvari neka vrsta **generalizovane teorije verovatnoće** sa posebnim pravilima gde kvadrati koeficijenata linearne superpozicije svi treba da se saberu na 1, što predstavlja zakon očuvanja ukupne verovatnoće.   

## Vežbe

Reši sledeće zadatke koristeći **samo** gradivo iz ove lekcije: definiciju kjubita i
normalizaciju {eq}`eq:norm`, Dirakovu bra-ket notaciju, Blohovu sferu {eq}`eq:bloch`,
tabelu specijalnih stanja i Bornovo pravilo {eq}`eq:bornrule`.

:::{tip} Kako da radiš zadatke
:class: simple
Prvo pokušaj sam na papiru, pa klikni na **Rešenje** da otvoriš analitičko rešenje
(LaTeX) i proveru u Python-u (kod). U kodu pretpostavljamo da su `numpy`, `ket0` i `ket1`
već definisani kao u lekciji:

```python
import numpy as np
ket0 = np.array([[1], [0]], dtype=complex)   # |0>
ket1 = np.array([[0], [1]], dtype=complex)   # |1>
```
:::

### Zagrevanje: normalizacija i verovatnoće

:::{admonition} Vežba 1
:class: tip
Dato je stanje $\ket{\psi} = \tfrac{1}{2}\ket{0} + \beta\ket{1}$, gde je $\beta$ **realan i
pozitivan** broj. Odredi $\beta$ tako da stanje bude normirano.
:::

:::{admonition} Rešenje
:class: dropdown
Uslov normalizacije {eq}`eq:norm` daje $|\alpha|^2 + |\beta|^2 = 1$, tj.
$\left(\tfrac{1}{2}\right)^2 + \beta^2 = 1 \Rightarrow \beta^2 = \tfrac{3}{4}
\Rightarrow \beta = \tfrac{\sqrt{3}}{2} \approx 0.866.$

```python
alpha = 0.5
beta  = np.sqrt(3)/2
psi = alpha*ket0 + beta*ket1
norm = (psi.conj().T @ psi).item().real
print("beta =", round(beta, 4), " |psi|^2 =", round(norm, 6))   # 0.866  1.0
```
:::

:::{admonition} Vežba 2
:class: tip
Za normirano stanje $\ket{\psi} = \tfrac{1}{2}\ket{0} + \tfrac{\sqrt{3}}{2}\ket{1}$
izračunaj verovatnoće ishoda $p(0)$ i $p(1)$ pri merenju u računskoj bazi.
:::

:::{admonition} Rešenje
:class: dropdown
Po Bornovom pravilu {eq}`eq:bornrule` je
$p(0) = |\braket{0}{\psi}|^2 = \left|\tfrac{1}{2}\right|^2 = \tfrac{1}{4} = 0.25$ i
$p(1) = |\braket{1}{\psi}|^2 = \left|\tfrac{\sqrt{3}}{2}\right|^2 = \tfrac{3}{4} = 0.75$.
Zbir je $0.25 + 0.75 = 1$, kao što i treba.

```python
psi = 0.5*ket0 + (np.sqrt(3)/2)*ket1
p0 = abs((ket0.conj().T @ psi).item())**2
p1 = abs((ket1.conj().T @ psi).item())**2
print("p(0) =", round(p0, 3), " p(1) =", round(p1, 3))   # 0.25  0.75
```
:::

:::{admonition} Vežba 3
:class: tip
Zapiši amplitude $\alpha$ i $\beta$ za stanje
$\ket{-} = \tfrac{1}{\sqrt{2}}\big(\ket{0} - \ket{1}\big)$ i predvidi $p(0)$ i $p(1)$.
:::

:::{admonition} Rešenje
:class: dropdown
Ovde je $\alpha = \tfrac{1}{\sqrt{2}}$ i $\beta = -\tfrac{1}{\sqrt{2}}$. Pošto je
$|\alpha|^2 = |\beta|^2 = \tfrac{1}{2}$, dobijamo $p(0) = p(1) = 0.5$. Znak minus je
**relativna faza** i ne utiče na merenje u računskoj bazi.

```python
psi = (1/np.sqrt(2))*ket0 - (1/np.sqrt(2))*ket1
p0 = abs((ket0.conj().T @ psi).item())**2
p1 = abs((ket1.conj().T @ psi).item())**2
print("p(0) =", round(p0, 3), " p(1) =", round(p1, 3))   # 0.5  0.5
```
:::

:::{admonition} Vežba 4
:class: tip
Stanje $\ket{+i} = \tfrac{1}{\sqrt{2}}\big(\ket{0} + i\ket{1}\big)$ ima **kompleksnu**
amplitudu. Pokaži da je normirano i izračunaj $p(0)$ i $p(1)$.
:::

:::{admonition} Rešenje
:class: dropdown
Pošto je $|i|^2 = 1$, sledi
$\left|\tfrac{1}{\sqrt2}\right|^2 + \left|\tfrac{i}{\sqrt2}\right|^2
= \tfrac{1}{2} + \tfrac{1}{2} = 1$, pa je stanje normirano. Dalje je
$p(0) = \left|\tfrac{1}{\sqrt2}\right|^2 = \tfrac{1}{2}$ i
$p(1) = \left|\tfrac{i}{\sqrt2}\right|^2 = \tfrac{1}{2}$. Kvadrat modula „pojede“ fazu $i$.

```python
psi = (1/np.sqrt(2))*ket0 + (1j/np.sqrt(2))*ket1   # 1j je imaginarna jedinica
norm = (psi.conj().T @ psi).item().real
p0 = abs((ket0.conj().T @ psi).item())**2
p1 = abs((ket1.conj().T @ psi).item())**2
print("|psi|^2 =", round(norm, 6), " p(0) =", round(p0, 3), " p(1) =", round(p1, 3))
```
:::

### Blohova sfera: uglovi, vektori, stanja

:::{admonition} Vežba 5
:class: tip
Za uglove $\theta = 90^\circ$ i $\varphi = 90^\circ$ izračunaj Blohov vektor
$\mathbf{r} = (\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)$.
Koje specijalno stanje iz tabele dobijaš?
:::

:::{admonition} Rešenje
:class: dropdown
$\mathbf{r} = (\sin 90^\circ\cos 90^\circ,\ \sin 90^\circ\sin 90^\circ,\ \cos 90^\circ)
= (0,\ 1,\ 0)$ — vrh na pozitivnoj $y$-osi, što odgovara stanju $\ket{+i}$.

```python
THETA = np.radians(90)
PHI   = np.radians(90)
r = np.array([np.sin(THETA)*np.cos(PHI),
              np.sin(THETA)*np.sin(PHI),
              np.cos(THETA)])
print("r =", np.round(r, 3))   # [0. 1. 0.]  ->  |+i>
```
:::

:::{admonition} Vežba 6
:class: tip
Magično $\ket{T}$ stanje ima uglove $\theta = \arccos\tfrac{1}{\sqrt3}$ i $\varphi = \tfrac{\pi}{4}$.
(a) Izračunaj njegov Blohov vektor i uveri se da je jednak $\tfrac{1}{\sqrt3}(1,1,1)$.
(b) Izračunaj $p(0)$ i $p(1)$ i uporedi ih sa ekvatorskim stanjem $T\ket{+}$.
:::

:::{admonition} Rešenje
:class: dropdown
**(a)** $\mathbf{r} = (\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)$. Pošto je
$\cos\theta = \tfrac{1}{\sqrt3}$, sledi $\sin\theta = \sqrt{1-\tfrac13} = \sqrt{\tfrac23}$, a
$\cos\varphi = \sin\varphi = \tfrac{1}{\sqrt2}$. Onda je
$r_x = r_y = \sqrt{\tfrac23}\cdot\tfrac{1}{\sqrt2} = \tfrac{1}{\sqrt3}$ i $r_z = \tfrac{1}{\sqrt3}$,
tj. $\mathbf r = \tfrac{1}{\sqrt3}(1,1,1)$. ✓

**(b)** $p(0) = \cos^2\tfrac{\theta}{2} = \tfrac{1+\cos\theta}{2} = \tfrac12\big(1+\tfrac{1}{\sqrt3}\big) \approx 0.789$
i $p(1) = \tfrac{1-\cos\theta}{2} \approx 0.211$. Za razliku od $T\ket{+}$ (na ekvatoru,
$p(0)=p(1)=\tfrac12$), magično stanje je nagnuto ka $\ket{0}$, pa je $p(0) > p(1)$.

```python
THETA = np.arccos(1/np.sqrt(3))   # ~54.74 stepeni, između ekvatora i pola
PHI   = np.radians(45)
r = np.array([np.sin(THETA)*np.cos(PHI),
              np.sin(THETA)*np.sin(PHI),
              np.cos(THETA)])
print("r =", np.round(r, 3))                          # [0.577 0.577 0.577] = (1,1,1)/sqrt(3)

p0 = np.cos(THETA/2)**2
p1 = np.sin(THETA/2)**2
print("p(0) =", round(p0, 4), " p(1) =", round(p1, 4))   # 0.7887  0.2113
```
:::

:::{admonition} Vežba 7
:class: tip
**Inverzni problem.** Dato je stanje $\ket{\psi} = \tfrac{\sqrt3}{2}\ket{0} + \tfrac{1}{2}\ket{1}$
(amplitude realne i pozitivne). Odredi uglove $\theta$ i $\varphi$ na Blohovoj sferi.
:::

:::{admonition} Rešenje
:class: dropdown
Iz $\ket{\psi} = \cos\tfrac{\theta}{2}\ket{0} + e^{i\varphi}\sin\tfrac{\theta}{2}\ket{1}$
i realnih, pozitivnih amplituda sledi $\varphi = 0$ i
$\cos\tfrac{\theta}{2} = \tfrac{\sqrt3}{2} \Rightarrow \tfrac{\theta}{2} = 30^\circ
\Rightarrow \theta = 60^\circ$. Provera: $\sin 30^\circ = \tfrac{1}{2}$. ✓

```python
theta = 2*np.arccos(np.sqrt(3)/2)
print("theta =", round(np.degrees(theta), 1), "stepeni,  phi = 0")   # 60.0
print("provera sin(theta/2) =", round(np.sin(theta/2), 3))           # 0.5
```
:::

### Faze, geometrija i opšte formule

:::{admonition} Vežba 8
:class: tip
**Globalna faza.** Pokaži da stanja $\ket{\psi}$ i $e^{i\gamma}\ket{\psi}$ daju **iste**
verovatnoće $p(k)$ za bilo koje $\gamma$. Zato kažemo da je stanje određeno „do na globalnu fazu“.
:::

:::{admonition} Rešenje
:class: dropdown
$p(k) = \big|\braket{k}{e^{i\gamma}\psi}\big|^2 = \big|e^{i\gamma}\big|^2\,\big|\braket{k}{\psi}\big|^2
= \big|\braket{k}{\psi}\big|^2$, jer je $|e^{i\gamma}| = 1$. Globalna faza nestaje pri kvadriranju modula.

```python
psi   = 0.5*ket0 + (np.sqrt(3)/2)*ket1
gamma = 1.234
psi_g = np.exp(1j*gamma) * psi            # ista fizika, druga globalna faza
p0   = abs((ket0.conj().T @ psi  ).item())**2
p0_g = abs((ket0.conj().T @ psi_g).item())**2
print("p(0) bez faze =", round(p0, 6), " sa fazom =", round(p0_g, 6))   # isto
```
:::

:::{admonition} Vežba 9
:class: tip
**Opšta formula.** Za proizvoljno stanje na Blohovoj sferi
$\ket{\psi} = \cos\tfrac{\theta}{2}\ket{0} + e^{i\varphi}\sin\tfrac{\theta}{2}\ket{1}$
izvedi $p(0)$ i $p(1)$ i pokaži da **ne zavise** od $\varphi$.
:::

:::{admonition} Rešenje
:class: dropdown
$p(0) = |\braket{0}{\psi}|^2 = \cos^2\tfrac{\theta}{2}$ i
$p(1) = |\braket{1}{\psi}|^2 = \big|e^{i\varphi}\big|^2 \sin^2\tfrac{\theta}{2} = \sin^2\tfrac{\theta}{2}$.
Pošto je $|e^{i\varphi}| = 1$, verovatnoće zavise samo od polarnog ugla $\theta$.
Provera: $\cos^2\tfrac{\theta}{2} + \sin^2\tfrac{\theta}{2} = 1$.

```python
theta = np.radians(60)
for phi_deg in [0, 30, 90, 200]:          # menjamo samo phi
    phi = np.radians(phi_deg)
    psi = np.cos(theta/2)*ket0 + np.exp(1j*phi)*np.sin(theta/2)*ket1
    p0 = abs((ket0.conj().T @ psi).item())**2
    p1 = abs((ket1.conj().T @ psi).item())**2
    print("phi =", phi_deg, " p0,p1 =", round(p0,4), round(p1,4))
# uvek 0.75  0.25  ->  cos^2(30) = 0.75
```
:::

