---
title: "Kjubit"
short_title: Kjubit
description: The state of a single qubit, the Bloch sphere, and first steps in Python.
---

# Qubit (Kjubit)

**Qubit** is osnovna jedinica građe i funkcije kvatne informatike, i i predstavlja
analogon klasičnim bit-ovima. Klasični bitovi mogu da imaju vrednosti $0$ i $1$, qubit može biti u linearnoj superpoziciji ova dva stanja!

Šta mislim pod linearnim? U najjednostavnijem smislu ukoliko imamo funkciju $f(a \vec{x} + b \vec{y}) = a f(\vec{x}) + b f(\vec{y})$ gde x i y mogu biti bilo koji od sledećih matematičkih objekata


```{figure} ../images/DifferentMathObjects.png
:label: fig:DifferentMathObjects
:alt: The Bloch sphere with the state psi drawn as a unit vector.
:width: 620px
:align: center

Različiti tipovi matematičkih funkcija i njihova dijagramatička representacija. 
```

Tenzori igraju veoma važnu ulogu u kvantnoj informatici ali i u ostalim poljima fizike, ali u ovom kursu nećemo ulaziti u detalje ove reprezentacije i zašto je bitna. 
Dok prve tre konstrukcije će biti korišćene. Kvantna mehaniku nazivaju i matrično mehanikom koju je Heisenberg prvi formulisao [citat iz Panticeve knjige]




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


Do na globalnu fazu ili parameter, svako jedno kjubitno stanje se može zapisati pomoću
sledeća dva parametra ugla 
- $\theta$: polarni ugao, $\theta \in [0,\pi]$
- $\varphi$: azimutalni ugao, $\varphi \in [0,2\pi)$

Gde jednokjubitno stanje poprima oblik

```{math}
:label: eq:bloch
\ket{\psi} = \cos\tfrac{\theta}{2}\,\ket{0} + e^{i\varphi}\sin\tfrac{\theta}{2}\,\ket{1},
```
gde svako moguće stanje i odabrani ugao pokazuje na površinu sfere radijusa 1. Kao što je prikazano na slici [](#fig:bloch). 


```{figure} ../images/BlohovaSfera.png
:label: fig:bloch
:alt: Bloh
:width: 420px
:align: center

**Blohova sfera** sa severnim i južnim polom $\ket{0}$ i $\ket{1}$, pritom gde je jednokjubitno stanje $\ket{\psi}$ iz jednačine {eq}`eq:bloch` prikazano sa ljubičastom bojom sa primerom dva ugla $(\theta, \varphi)$. 
```

## Vaš prvi kod u Python-u! 

Hajde da generišemo jednokjubitna stanja, kao i napravimo vizuelizaciju Blohove sfere. 


:::{tip} Kopiraj me u svoj Jupiter Notebook! 
:class: simple
Kopiraj svaku liniju koda iz obeleženog kodnog bloka u svoj Jupiter Notebook na [Google Colab](https://colab.research.google.com) i pokreni koristeći **Shift+Enter**!
Svaki blok i linija koda sadrže objašnjene o funkciji i ulozi koju igraju u kodu.

:::

```python
# za numeričku manipulaciju nizova, vektori, matrice, tenzori
import numpy as np             

# Računska baza |0> and |1> kao ket vektori (vektori kolone)
ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)

# prikaži definicije stanja 
print("Stanje nula: ", ket0)
print("Stanje jedan: ", ket1)
```

Kada definišeš vektor pomoću `np.array`, parametar `dtype` određuje tip elemenata u nizu. Najčešće mogućnosti su:

- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int</span> za cele brojeve
- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">float</span> za realne brojeve
- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">complex</span> za kompleksne brojeve, što je ovde najkorisnije
- dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">bool</span> za logičke vrednosti, Tačno/Netačno (True/False) 


Kod dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int</span>, NumPy obično bira celobrojni tip koji odgovara platformi: na 64-bit sistemima to je najčešće <span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int64</span>, a na 32-bit sistemima <span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int32</span>. Ako želiš potpuno fiksnu širinu, koristi dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">np.int32</span> ili dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">np.int64</span>.


U ovom primeru koristimo dtype=<span style="color: #8250df; font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;">int</span> zato što amplituda kvantnog stanja može da bude kompleksna!

Hajde sad da definišemo stanje plus $\ket{+}$ kao: $\theta = \frac{\pi}{2}$ i $\varphi = 0$ i to
```{math}
:label: eq:plus
\ket{+} = \dfrac{1}{\sqrt{2}} ( \ket{0} + \ket{1} ), 
```

```python
# Linearna superpozicija stanja: |+> state = (|0> + |1>)/sqrt(2)
alpha = 1/np.sqrt(2)
beta  = 1/np.sqrt(2)
psi = alpha * ket0 + beta * ket1

print("|psi> =")
print(psi)
```


We can check normalisation from {eq}`eq:norm` by computing $\braket{\psi}{\psi}$, which is
`psi.conj().T @ psi`:

```python
# <psi|psi> should equal 1
norm = (psi.conj().T @ psi).item().real
print("norm =", round(norm, 6))
```

Finally, the **Born rule** says the probability of measuring outcome $k$ is
$p(k) = |\braket{k}{\psi}|^2$:

```python
# Measurement probabilities in the computational basis
p0 = abs((ket0.conj().T @ psi).item())**2
p1 = abs((ket1.conj().T @ psi).item())**2
print("p(0) =", round(p0, 3), " p(1) =", round(p1, 3))
```

:::{note} What you should see
For the $\ket{+}$ state both outcomes are equally likely: $p(0) = p(1) = 0.5$.
:::

## Practice

:::{exercise}
:label: ex:minus
Write down the amplitudes $\alpha, \beta$ for the state
$\ket{-} = \tfrac{1}{\sqrt 2}\big(\ket{0} - \ket{1}\big)$, and predict $p(0)$ and $p(1)$.
Then modify the code above to check your answer.
:::

:::{solution} ex:minus
:class: dropdown
Here $\alpha = \tfrac{1}{\sqrt2}$ and $\beta = -\tfrac{1}{\sqrt2}$. Since
$|\alpha|^2 = |\beta|^2 = \tfrac12$, we again get $p(0) = p(1) = 0.5$ — the minus sign is a
*relative phase* that does not affect measurement in the computational basis.

```python
beta = -1/np.sqrt(2)
psi_minus = (1/np.sqrt(2)) * ket0 + beta * ket1
p0 = abs((ket0.conj().T @ psi_minus).item())**2
print("p(0) =", round(p0, 3))
```
:::

:::{important} Key points
- A qubit state is a normalised vector in $\CC^2$ — {eq}`eq:qubit` and {eq}`eq:norm`.
- Pure states live on the surface of the Bloch sphere — {eq}`eq:bloch`.
- Measurement outcomes follow the Born rule $p(k) = |\braket{k}{\psi}|^2$.
:::





```python
import numpy as np                          
import matplotlib.pyplot as plt             # vizuelizacija
from mpl_toolkits.mplot3d import Axes3D     # vizuelizacija za 3D 

%matplotlib inline                          # pomoćna funckija za vizuelizaciju unutar Jupiter notebook okruženja

```


```python
# --- The two knobs: change these and re-run ----------------------------
THETA = np.radians(45)   # polar angle:   0 -> |0>,  180 deg -> |1>
PHI   = np.radians(45)   # azimuthal angle around z

# --- Angles -> Bloch vector  r = (sin th cos ph, sin th sin ph, cos th) -
x = np.sin(THETA) * np.cos(PHI)
y = np.sin(THETA) * np.sin(PHI)
z = np.cos(THETA)
r = np.array([x, y, z])

print("Bloch vector r =", np.round(r, 3))
print("length |r|     =", round(float(np.linalg.norm(r)), 3), " (= 1 for a pure state)")


```

```python
# --- Sphere surface mesh ----------------------------------------------
u = np.linspace(0, 2*np.pi, 60)     # azimuthal grid
v = np.linspace(0, np.pi,   60)     # polar grid
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))

# --- A circle we reuse for the equator + two meridians ----------------
circ = np.linspace(0, 2*np.pi, 200)
```



```python

fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_subplot(111, projection="3d")

# --- translucent GRAY sphere (black at low opacity) -------------------
ax.plot_surface(xs, ys, zs, color="black", alpha=0.08,
                linewidth=0, rstride=2, cstride=2, antialiased=True, shade=False)

# --- faint guide circles: equator + two meridians ---------------------
ax.plot(np.cos(circ), np.sin(circ), 0, color="#555555", lw=0.8, alpha=0.6)   # equator
ax.plot(np.cos(circ), 0*circ, np.sin(circ), color="#bbbbbb", lw=0.6)         # xz meridian
ax.plot(0*circ, np.cos(circ), np.sin(circ), color="#bbbbbb", lw=0.6)         # yz meridian

# --- three axes, BOTH directions (arrowheads at each end) --------------
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

# --- the six intersection points + eigenstate labels ------------------
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

# --- the state vector -------------------------------------------------
ax.quiver(0,0,0, r[0], r[1], r[2], color="#8e44ad", lw=3.0, arrow_length_ratio=0.12, zorder=6)
ax.scatter(*r, color="#8e44ad", s=45, zorder=6)
ax.text(r[0]*1.12, r[1]*1.12, r[2]*1.12+0.06, r"$|\psi\rangle$", color="#8e44ad", fontsize=14)

# --- dotted projection lines (to xy-plane, then to origin) ------------
ax.plot([r[0], r[0]], [r[1], r[1]], [0, r[2]], color="#8e44ad", ls=":", lw=1)
ax.plot([0, r[0]], [0, r[1]], [0, 0], color="#8e44ad", ls=":", lw=1.2)

# --- angle arcs -------------------------------------------------------
ARC = "#e67e22"
nx, ny = np.cos(PHI), np.sin(PHI)            # xy-plane direction of the projection

# phi: arc in the xy-plane from +x to the projection direction
tp = np.linspace(0, PHI, 40)
ax.plot(0.32*np.cos(tp), 0.32*np.sin(tp), 0, color=ARC, lw=1.8)
ax.text(0.46*np.cos(PHI/2), 0.46*np.sin(PHI/2), 0.0, r"$\varphi$",
        color=ARC, fontsize=14, ha="center")

# theta: arc from +z down to the vector, in the plane spanned by z and the projection
tt = np.linspace(0, THETA, 40)
ax.plot(0.40*np.sin(tt)*nx, 0.40*np.sin(tt)*ny, 0.40*np.cos(tt), color=ARC, lw=1.8)
tm = THETA/2
ax.text(0.52*np.sin(tm)*nx, 0.52*np.sin(tm)*ny, 0.52*np.cos(tm), r"$\theta$",
        color=ARC, fontsize=14, ha="center")

# --- title with the exact state ---------------------------------------
a, b = np.cos(THETA/2), np.sin(THETA/2)
ax.set_title(rf"$|\psi\rangle = {a:.2f}\,|0\rangle + e^{{i\,{PHI:.2f}}}\,{b:.2f}\,|1\rangle$"
             + f"\n$\\theta={np.degrees(THETA):.0f}^\\circ,\\ \\varphi={np.degrees(PHI):.0f}^\\circ$",
             fontsize=13, pad=8)

# --- cosmetics --------------------------------------------------------
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_zlim(-1.1, 1.1)
ax.set_axis_off()
ax.view_init(elev=18, azim=35)

plt.tight_layout()
plt.show()
```



```python

from mpl_toolkits.mplot3d.art3d import Poly3DCollection   # add to Cell 1 if you prefer

fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_subplot(111, projection="3d")

# --- translucent GRAY sphere ------------------------------------------
ax.plot_surface(xs, ys, zs, color="black", alpha=0.06,
                linewidth=0, rstride=2, cstride=2, antialiased=True, shade=False)

# --- faint guide circles ----------------------------------------------
ax.plot(np.cos(circ), np.sin(circ), 0, color="#555555", lw=0.8, alpha=0.5)   # equator
ax.plot(np.cos(circ), 0*circ, np.sin(circ), color="#bbbbbb", lw=0.6)         # xz meridian
ax.plot(0*circ, np.cos(circ), np.sin(circ), color="#bbbbbb", lw=0.6)         # yz meridian

# --- three axes, both directions --------------------------------------
L = 1.3
axis_kw = dict(lw=1.3, arrow_length_ratio=0.05)
for d, col in [((1,0,0), "#c0392b"), ((0,1,0), "#27ae60"), ((0,0,1), "#34495e")]:
    dx, dy, dz = d
    ax.quiver(0,0,0,  L*dx,  L*dy,  L*dz, color=col, **axis_kw)
    ax.quiver(0,0,0, -L*dx, -L*dy, -L*dz, color=col, **axis_kw)
ax.text(1.45, 0, 0, r"$x$", color="#c0392b", fontsize=11, alpha=0.7)
ax.text(0, 1.42, 0, r"$y$", color="#27ae60", fontsize=11, alpha=0.7)
ax.text(0, 0, 1.45, r"$z$", color="#34495e", fontsize=11, alpha=0.7)

# --- OCTAHEDRON: 8 triangular faces (one pole from each axis) ----------
faces = [[(sx,0,0), (0,sy,0), (0,0,sz)]
         for sx in (1,-1) for sy in (1,-1) for sz in (1,-1)]
ax.add_collection3d(Poly3DCollection(faces, facecolor="#2980b9",
                                     edgecolor="none", alpha=0.16))

# --- OCTAHEDRON edges = the three coordinate-plane squares -------------
for sq in [[(1,0,0), (0,1,0), (-1,0,0), (0,-1,0), (1,0,0)],   # xy square
           [(1,0,0), (0,0,1), (-1,0,0), (0,0,-1), (1,0,0)],   # xz square
           [(0,1,0), (0,0,1), (0,-1,0), (0,0,-1), (0,1,0)]]:  # yz square
    a = np.array(sq)
    ax.plot(a[:,0], a[:,1], a[:,2], color="#1f5f8b", lw=1.6)

# --- the six vertices + eigenstate labels -----------------------------
poles = [
    (( 0, 0, 1), r"$|0\rangle$",    "#34495e", ( 0.16, -0.16,  0.10)),
    (( 0, 0,-1), r"$|1\rangle$",    "#34495e", ( 0.16, -0.16, -0.12)),
    (( 1, 0, 0), r"$|{+}\rangle$",  "#c0392b", ( 0.14, -0.02,  0.10)),
    ((-1, 0, 0), r"$|{-}\rangle$",  "#c0392b", (-0.30,  0.00,  0.10)),
    (( 0, 1, 0), r"$|{+}i\rangle$", "#27ae60", ( 0.02,  0.14,  0.10)),
    (( 0,-1, 0), r"$|{-}i\rangle$", "#27ae60", ( 0.02, -0.28,  0.10)),
]
for (px,py,pz), lab, col, (ox,oy,oz) in poles:
    ax.scatter(px, py, pz, color=col, s=55, edgecolors="white", linewidths=0.8, zorder=5)
    ax.text(px+ox, py+oy, pz+oz, lab, color=col, fontsize=13, ha="center")

# --- cosmetics --------------------------------------------------------
ax.set_title("Octahedron of the six eigenstates inscribed in the Bloch sphere",
             fontsize=12, pad=8)
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_zlim(-1.1, 1.1)
ax.set_axis_off()
ax.view_init(elev=25, azim=35)

plt.tight_layout()
plt.show()
```