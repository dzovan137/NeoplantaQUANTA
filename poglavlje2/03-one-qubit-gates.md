---
title: "Kvantne kapije"
short_title: Kvantne kapije
description: Šta su to kvantne kapije?
---

# Kvantne kapije (quantum gates)

Kako to možemo da utičemo na kvantna stanja? Videli smo da kvantna stanja definišemo pomoću vektora, dok da bismo menjali te vektore zapravo koristimo matrice.

Naime, promenu kvantnog stanja (u slučaju jednog kjubita to je rotacija na Blohovoj sferi) zapisujemo kao

```{math}
:label: eq:evolution
\ket{\psi^{\rm novo}} = U \ket{\psi^{\rm staro}},
```
gde je veličina matrice $d^N \times d^N$, pri čemu je za kubite lokalna dimenzija $d = 2$, a $N$ broj kubita.
U slučaju jednog kjubita $N = 1$, pa je operator $U$ zapravo dimenzije $2 \times 2$.

:::{important} Kvantne kapije su unitarni operatori
:class: simple
Da bi transformacija [](#eq:evolution) sačuvala normu stanja (ukupnu verovatnoću iz [](#eq:norm)), matrica $U$ mora biti **unitarna**:
```{math}
:label: eq:unitary
U^\dagger U = U U^\dagger = I,
```
gde je $U^\dagger = (U^{*})^{\top}$ **konjugovano-transponovana** (hermitski adjungovana) matrica. Unitarnost povlači da je svaka kvantna kapija **reverzibilna**: inverz kapije $U$ je prosto $U^{-1} = U^\dagger$, pa svako kvantno kolo možemo „pustiti unazad".
:::

Među najpoznatijim kvantnim kapijama su zapravo Paulijeve matrice definisane kao

```{math}
:label: eq:paulimatrices
\begin{aligned}
I &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \\
X &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \\
Y &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \\
Z &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
\end{aligned}
```
Interesantna stvar je da su vektori $\{ \ket{0}, \ket{1} \}$ svojstveni vektori $Z$ operatora.

## Paulijeve kapije

Pogledajmo šta svaka od Paulijevih kapija radi kada deluje na računsku bazu $\{\ket{0}, \ket{1}\}$.

Kapija $X$ je **kvantni NOT** (obrtanje bita): ona zamenjuje amplitude uz $\ket{0}$ i $\ket{1}$,
```{math}
:label: eq:xaction
X\ket{0} = \ket{1}, \qquad X\ket{1} = \ket{0}.
```
Kapija $Z$ je **obrtanje faze** (phase flip): ostavlja $\ket{0}$ na miru, a stanju $\ket{1}$ dodaje znak minus,
```{math}
:label: eq:zaction
Z\ket{0} = \ket{0}, \qquad Z\ket{1} = -\ket{1}.
```
Kapija $Y$ istovremeno obrće i bit i fazu (do na imaginarnu jedinicu), $Y = iXZ$:
```{math}
:label: eq:yaction
Y\ket{0} = i\ket{1}, \qquad Y\ket{1} = -i\ket{0}.
```

Sve tri Paulijeve matrice dele nekoliko važnih svojstava. One su istovremeno **hermitske** ($P = P^\dagger$) i **unitarne** ($P^\dagger P = I$), a pošto su same sebi inverz, kvadrat svake je jedinična matrica,
```{math}
:label: eq:involution
X^2 = Y^2 = Z^2 = I.
```
Dodatno, Paulijeve matrice **antikomutiraju** i zadovoljavaju ciklične relacije
```{math}
:label: eq:paulialgebra
XY = iZ, \qquad YZ = iX, \qquad ZX = iY,
```
odakle sledi, na primer, $\{X, Z\} = XZ + ZX = 0$.

:::{note} Geometrijsko značenje na Blohovoj sferi (klik)
:class: dropdown
Svaka jednokjubitna kapija odgovara nekoj **rotaciji Blohove sfere**. Paulijeve kapije su rotacije za ugao $\pi$ oko odgovarajuće koordinatne ose:
- $X$ — rotacija za $180^\circ$ oko $x$-ose,
- $Y$ — rotacija za $180^\circ$ oko $y$-ose,
- $Z$ — rotacija za $180^\circ$ oko $z$-ose.

Na primer, $Z$ obrne stanje $\ket{+}$ (na pozitivnoj $x$-osi) u $\ket{-}$ (na negativnoj $x$-osi). 


```{figure} ../images/BlohovaSfera.png
:label: fig:blochagain
:alt: Bloh
:width: 420px
:align: center

Prethodna vizuelizacija ponovo iskrošćena. 

```

:::

## Hadamardova kapija

Najvažnija kapija koja **pravi superpoziciju** iz stanja računske baze je **Hadamardova kapija**

```{math}
:label: eq:hadamard
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.
```
Njeno dejstvo na bazna stanja daje upravo stanja $\ket{+}$ i $\ket{-}$ sa Blohovog ekvatora (vidi tabelu specijalnih stanja u [](../dan1/02-qubits.md)):
```{math}
:label: eq:hadaction
H\ket{0} = \frac{1}{\sqrt{2}}\big(\ket{0} + \ket{1}\big) = \ket{+}, \qquad
H\ket{1} = \frac{1}{\sqrt{2}}\big(\ket{0} - \ket{1}\big) = \ket{-}.
```
Hadamardova kapija je i hermitska i unitarna, pa je sama sebi inverz, $H^2 = I$.


## Fazne kapije: $S$ i $T$

Pored $Z$, često nam trebaju „blaže" rotacije faze, koje stanju $\ket{1}$ dodaju fazu manju od $\pi$. Uopšteno, **fazna kapija** $P(\lambda)$ deluje kao

```{math}
:label: eq:phase
P(\lambda) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\lambda} \end{pmatrix},
\qquad P(\lambda)\ket{0} = \ket{0}, \quad P(\lambda)\ket{1} = e^{i\lambda}\ket{1}.
```
Tri posebna slučaja imaju svoja imena:
```{math}
:label: eq:stz
Z = P(\pi), \qquad S = P\!\left(\tfrac{\pi}{2}\right) = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix},
\qquad T = P\!\left(\tfrac{\pi}{4}\right) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}.
```
Kapija $S$ je „kvadratni koren" iz $Z$, a $T$ je koren iz $S$:
```{math}
:label: eq:roots
S^2 = Z, \qquad T^2 = S, \qquad T^4 = Z.
```
Za razliku od Paulijevih kapija i Hadamarda, kapije $S$ i $T$ **nisu** same sebi inverz ($S^\dagger = S^3$, $T^\dagger = T^7$); one su prve u nizu kapija koje ćemo koristiti da bismo dosegli **proizvoljno** stanje na sferi. Na Blohovoj sferi $P(\lambda)$ je prosto rotacija za ugao $\lambda$ oko $z$-ose, pa $S$ i $T$ „kližu" tačku duž paralela (linija konstantne visine).

:::{warning} $T$ kapija i „magično" stanje
:class: simple
Primenom $T$ na $\ket{+}$ dobijamo tačno **magično stanje** $\ket{T} = T\ket{+}$ sa uglovima $\theta = \arccos\tfrac{1}{\sqrt3}$, $\varphi = \tfrac{\pi}{4}$, koje smo sreli u tabeli specijalnih stanja u [](../dan1/02-qubits.md). Upravo $T$ kapija „izbacuje" računanje iz skupa kapija koje klasičan računar može lako da simulira ([Klifordova grupa](https://en.wikipedia.org/wiki/Clifford_group)), pa je ključna za kvantnu prednost.
:::

## Rotacione kapije

Najprirodniji način da napravimo rotaciju za **proizvoljan** ugao je da eksponenciramo Paulijevu matricu. Za $P \in \{X, Y, Z\}$ definišemo **rotacionu kapiju**

```{math}
:label: eq:rotdef
R_P(\theta) = e^{-i\frac{\theta}{2} P}.
```
Pošto je $P^2 = I$ (iz [](#eq:involution)), razvoj eksponencijalne funkcije se „lomi" na paran i neparan deo i sažima u zatvorenu formu

```{math}
:label: eq:euler-op
e^{-i\frac{\theta}{2} P} = \cos{\left( \!\frac{\theta}{2}\right)} I - i\sin{\left( \!\frac{\theta}{2} \right)} P,
```
što je operatorska verzija Ojlerove formule.

:::{note} Prikaži izvođenje (klik)
:class: dropdown
Krenimo od definicije eksponencijalne funkcije operatora preko stepenog (Tejlorovog) reda:
```{math}
e^{-i\frac{\theta}{2} P} = \sum_{n=0}^{\infty} \frac{1}{n!}\left(-i\frac{\theta}{2}\,P\right)^{n} = \sum_{n=0}^{\infty} \frac{1}{n!}\left(-i\frac{\theta}{2}\right)^{n} P^{\,n}.
```
Ključno svojstvo je $P^2 = I$ (iz [](#eq:involution)): stepeni operatora $P$ smenjuju se u samo dve vrednosti,
```{math}
P^{0}=I,\quad P^{1}=P,\quad P^{2}=I,\quad P^{3}=P,\ \dots \qquad\Longrightarrow\qquad P^{2k}=I,\quad P^{2k+1}=P.
```
Zato red razdvajamo na **parne** ($n=2k$) i **neparne** ($n=2k+1$) članove — parni skupljaju $I$, a neparni $P$:
```{math}
e^{-i\frac{\theta}{2} P} = \underbrace{\left(\sum_{k=0}^{\infty} \frac{1}{(2k)!}\left(-i\frac{\theta}{2}\right)^{2k}\right)}_{\text{uz } I}\, I \;+\; \underbrace{\left(\sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\left(-i\frac{\theta}{2}\right)^{2k+1}\right)}_{\text{uz } P}\, P.
```
Pošto je $(-i)^2=-1$, sledi $(-i)^{2k}=(-1)^k$ i $(-i)^{2k+1}=-i\,(-1)^k$, pa se dva koeficijenta svode na poznate Tejlorove redove kosinusa i sinusa (argumenta $\theta/2$):
```{math}
\sum_{k=0}^{\infty} \frac{(-1)^{k}}{(2k)!}\left(\frac{\theta}{2}\right)^{2k} = \cos{\left( \!\frac{\theta}{2}\right)}, \qquad -i\sum_{k=0}^{\infty} \frac{(-1)^{k}}{(2k+1)!}\left(\frac{\theta}{2}\right)^{2k+1} = -i\sin{\left( \!\frac{\theta}{2} \right)}.
```
Uvrštavanjem nazad dobijamo zatvorenu formu
```{math}
e^{-i\frac{\theta}{2} P} = \cos{\left( \!\frac{\theta}{2}\right)} I - i\sin{\left( \!\frac{\theta}{2} \right)} P,
```
što je upravo [](#eq:euler-op). Izvođenje počiva jedino na $P^2=I$, pa važi jednoobrazno za $P\in\{X,Y,Z\}$ i odmah daje matrice $R_x,R_y,R_z$ iz [](#eq:rotations).
:::

Uvrštavanjem $P = X, Y, Z$ dobijamo tri standardne rotacione kapije

```{math}
:label: eq:rotations
\begin{aligned}
R_x(\theta) &= e^{-i\frac{\theta}{2}X}
= \begin{pmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}, \\[6pt]
R_y(\theta) &= e^{-i\frac{\theta}{2}Y}
= \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}, \\[6pt]
R_z(\theta) &= e^{-i\frac{\theta}{2}Z}
= \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}.
\end{aligned}
```


:::{note} Veza sa Paulijevim kapijama (klik)
:class: dropdown
Za $\theta = \pi$ rotacione kapije se poklapaju sa Paulijevim kapijama **do na globalnu fazu** $-i$:
```{math}
R_x(\pi) = -iX, \qquad R_y(\pi) = -iY, \qquad R_z(\pi) = -iZ.
```
Pošto globalna faza ne utiče na verovatnoće merenja (Vežba 8 iz [](../dan1/02-qubits.md)), $R_P(\pi)$ i $P$ opisuju isto fizičko dejstvo na stanje.
:::

## Opšta parametrizovana kapija $U(\theta, \phi, \lambda)$

Sve prethodne kapije su specijalni slučajevi **jedne** opšte jednokubitne kapije. U [Qiskit](https://www.ibm.com/quantum/qiskit) okruženju najopštija jednokjubitna kapija se definiše (do na nebitnu globalnu fazu) sa tri realna ugla $\theta, \phi, \lambda$ kao

```{math}
:label: eq:ugate
U(\theta, \phi, \lambda) = \begin{pmatrix}
\cos{(\theta/2)} & - e^{i \lambda} \sin{(\theta/2)} \\
e^{i \phi} \sin{ (\theta/2)} & e^{i (\phi + \lambda)} \cos{ (\theta/2)}
\end{pmatrix}.
```
Broj parametara se lepo slaže sa geometrijom: matrica $U \in SU(2)$ ([specijalna unitarna grupa](https://en.wikipedia.org/wiki/Special_unitary_group)) ima tačno **tri** realna slobodna parametra, a $U(\theta,\phi,\lambda)$ zapravo nije ništa drugo do Ojlerova dekompozicija na tri rotacije, $U(\theta,\phi,\lambda) = R_z(\phi)\,R_y(\theta)\,R_z(\lambda)$ (do na globalnu fazu).

Sada je lako proveriti da su **sve** dosadašnje kapije samo posebni izbori uglova. Paulijeve matrice se dobijaju kao

```{math}
:label: eq:pauli-from-u
\begin{aligned}
X &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = U(\pi,\, 0,\, \pi), \\[4pt]
Y &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = U\!\left(\pi,\, \tfrac{\pi}{2},\, \tfrac{\pi}{2}\right), \\[4pt]
Z &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = U(0,\, 0,\, \pi),
\end{aligned}
```
dok se rotacione kapije zapisuju kao

```{math}
:label: eq:rot-from-u
\begin{aligned}
R_x(\theta) &= U\!\left(\theta,\, -\tfrac{\pi}{2},\, \tfrac{\pi}{2}\right), \\[4pt]
R_y(\theta) &= U(\theta,\, 0,\, 0), \\[4pt]
R_z(\theta) &= e^{-i\theta/2}\, U(0,\, 0,\, \theta).
\end{aligned}
```
Preostale kapije iz lekcije popunjavaju istu tabelu (fazna kapija $P(\lambda) = U(0,0,\lambda)$, pa otud $Z = U(0,0,\pi)$, $S = U(0,0,\tfrac{\pi}{2})$, $T = U(0,0,\tfrac{\pi}{4})$, a Hadamard $H = U(\tfrac{\pi}{2}, 0, \pi)$):

| Kapija | Matrica | Kao $U(\theta,\phi,\lambda)$ |
|---|---|---|
| $I$ | $\left(\begin{smallmatrix} 1 & 0 \\ 0 & 1 \end{smallmatrix}\right)$ | $U(0,\,0,\,0)$ |
| $X$ | $\left(\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\right)$ | $U(\pi,\,0,\,\pi)$ |
| $Y$ | $\left(\begin{smallmatrix} 0 & -i \\ i & 0 \end{smallmatrix}\right)$ | $U(\pi,\,\tfrac{\pi}{2},\,\tfrac{\pi}{2})$ |
| $Z$ | $\left(\begin{smallmatrix} 1 & 0 \\ 0 & -1 \end{smallmatrix}\right)$ | $U(0,\,0,\,\pi)$ |
| $H$ | $\tfrac{1}{\sqrt2}\left(\begin{smallmatrix} 1 & 1 \\ 1 & -1 \end{smallmatrix}\right)$ | $U(\tfrac{\pi}{2},\,0,\,\pi)$ |
| $S$ | $\left(\begin{smallmatrix} 1 & 0 \\ 0 & i \end{smallmatrix}\right)$ | $U(0,\,0,\,\tfrac{\pi}{2})$ |
| $T$ | $\left(\begin{smallmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{smallmatrix}\right)$ | $U(0,\,0,\,\tfrac{\pi}{4})$ |
| $R_x(\theta)$ | $\left(\begin{smallmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{smallmatrix}\right)$ | $U(\theta,\,-\tfrac{\pi}{2},\,\tfrac{\pi}{2})$ |
| $R_y(\theta)$ | $\left(\begin{smallmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{smallmatrix}\right)$ | $U(\theta,\,0,\,0)$ |
| $R_z(\theta)$ | $\left(\begin{smallmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{smallmatrix}\right)$ | $e^{-i\theta/2}\,U(0,\,0,\,\theta)$ |

## Vaš kvantni kod: kapije u Python-u

Kao i u prošloj lekciji, sve možemo direktno da proverimo u nekoliko linija koda. Prvo definišemo Paulijeve matrice i osnovne kapije.



```python
import numpy as np

# Računska baza |0> i |1> (vektori kolone)
ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)

# --- Paulijeve matrice i osnovne kapije ---
I2 = np.eye(2, dtype=complex)
X  = np.array([[0, 1], [1, 0]], dtype=complex)
Y  = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z  = np.array([[1, 0], [0, -1]], dtype=complex)
H  = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
S  = np.array([[1, 0], [0, 1j]], dtype=complex)
T  = np.array([[1, 0], [0, np.exp(1j*np.pi/4)]], dtype=complex)

# dejstvo kapija na baznim stanjima
print("X|0> =\n", X @ ket0)      # -> |1>
print("Z|1> =\n", Z @ ket1)      # -> -|1>
print("H|0> =\n", H @ ket0)      # -> |+>
```

Proverimo ključna algebarska svojstva iz lekcije — unitarnost, involutivnost i to da su $S$ i $T$ koreni iz $Z$:

```python
# unitarnost: U^dagger U = I (npr. za Hadamard)
print("H unitarno? ", np.allclose(H.conj().T @ H, I2))

# involutivnost Paulijevih kapija i Hadamarda: P^2 = I
print("X^2 = I? ", np.allclose(X @ X, I2))
print("H^2 = I? ", np.allclose(H @ H, I2))

# koreni: S^2 = Z i T^2 = S
print("S^2 = Z? ", np.allclose(S @ S, Z))
print("T^2 = S? ", np.allclose(T @ T, S))

# Hadamard kao (X + Z)/sqrt(2)
print("H = (X+Z)/sqrt(2)? ", np.allclose(H, (X + Z)/np.sqrt(2)))
```

Rotacione kapije i opštu $U(\theta,\phi,\lambda)$ kapiju najlakše je zapisati kao funkcije uglova:

```python
def Rx(theta):
    return np.array([[np.cos(theta/2), -1j*np.sin(theta/2)],
                     [-1j*np.sin(theta/2), np.cos(theta/2)]], dtype=complex)

def Ry(theta):
    return np.array([[np.cos(theta/2), -np.sin(theta/2)],
                     [np.sin(theta/2),  np.cos(theta/2)]], dtype=complex)

def Rz(theta):
    return np.array([[np.exp(-1j*theta/2), 0],
                     [0, np.exp(1j*theta/2)]], dtype=complex)

def U(theta, phi, lam):
    return np.array([
        [np.cos(theta/2),               -np.exp(1j*lam)*np.sin(theta/2)],
        [np.exp(1j*phi)*np.sin(theta/2), np.exp(1j*(phi+lam))*np.cos(theta/2)]
    ], dtype=complex)

# svaka poznata kapija je specijalan slučaj opšte U(theta, phi, lam):
print("X = U(pi,0,pi)?        ", np.allclose(X, U(np.pi, 0, np.pi)))
print("Y = U(pi,pi/2,pi/2)?   ", np.allclose(Y, U(np.pi, np.pi/2, np.pi/2)))
print("Z = U(0,0,pi)?         ", np.allclose(Z, U(0, 0, np.pi)))
print("H = U(pi/2,0,pi)?      ", np.allclose(H, U(np.pi/2, 0, np.pi)))
print("S = U(0,0,pi/2)?       ", np.allclose(S, U(0, 0, np.pi/2)))
print("T = U(0,0,pi/4)?       ", np.allclose(T, U(0, 0, np.pi/4)))
print("Rx = U(t,-pi/2,pi/2)?  ", np.allclose(Rx(0.7), U(0.7, -np.pi/2, np.pi/2)))
print("Ry = U(t,0,0)?         ", np.allclose(Ry(0.7), U(0.7, 0, 0)))
print("Rz = e^{-it/2}U(0,0,t)?", np.allclose(Rz(0.7), np.exp(-1j*0.7/2)*U(0, 0, 0.7)))
```

## Vizuelizacija dejstva kapija na Blohovoj sferi

Pošto svaka jednokjubitna kapija odgovara rotaciji Blohove sfere, najbolji način da je „osetimo" jeste da nacrtamo stanje **pre** i **posle** dejstva kapije. Prvo nam treba funkcija koja iz vektora stanja $\ket{\psi}$ računa Blohov vektor $\mathbf{r} = (\langle X\rangle, \langle Y\rangle, \langle Z\rangle)$:

```python
def bloch_vector(psi):
    """Blohov vektor r = (<X>, <Y>, <Z>) za stanje jednog kjubita."""
    psi = psi.reshape(2, 1)
    rx = (psi.conj().T @ X @ psi).item().real
    ry = (psi.conj().T @ Y @ psi).item().real
    rz = (psi.conj().T @ Z @ psi).item().real
    return np.array([rx, ry, rz])

# provera: |0> je na severnom polu (0,0,1), |+> na +x osi (1,0,0)
print("r(|0>) =", np.round(bloch_vector(ket0), 3))          # [0 0 1]
print("r(H|0>) =", np.round(bloch_vector(H @ ket0), 3))     # [1 0 0]  -> |+>
```

Sledeći blok crta providnu sferu sa koordinatnim osama (pomoćna funkcija), a zatim iscrtava stanje pre (ljubičasto) i posle (narandžasto) delovanja izabrane kapije:

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D     # 3D projekcija

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
    # ekvator
    circ = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(circ), np.sin(circ), 0, color="#555555", lw=0.8, alpha=0.5)
    # tri ose (oba smera)
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

# --- IZABERI kapiju i početno stanje ---
kapija = H                     # probaj i X, Z, S, T, Rx(np.pi/2), Ry(np.pi/3) ...
psi_pre   = ket0               # početno stanje
psi_posle = kapija @ psi_pre   # stanje posle dejstva kapije

r_pre   = bloch_vector(psi_pre)
r_posle = bloch_vector(psi_posle)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")
nacrtaj_sferu(ax)

ax.quiver(0,0,0, *r_pre,   color="#8e44ad", lw=3, arrow_length_ratio=0.12)
ax.text(*(1.15*r_pre),   r"pre", color="#8e44ad", fontsize=13)
ax.quiver(0,0,0, *r_posle, color="#e67e22", lw=3, arrow_length_ratio=0.12)
ax.text(*(1.15*r_posle), r"posle", color="#e67e22", fontsize=13)

ax.set_title("Dejstvo kapije na Blohovoj sferi", fontsize=13, pad=8)
ax.view_init(elev=18, azim=35)
plt.tight_layout()
plt.savefig("dejstvo_kapije.png", dpi=300, bbox_inches="tight")
plt.show()
```

Menjajući promenljivu `kapija` (na primer u `X`, `Z`, `S`, `T`, `Rx(np.pi/2)`, `Ry(np.pi/3)`) i početno stanje `psi_pre`, možeš da vidiš kako svaka kapija **rotira** Blohov vektor: Paulijeve i Hadamardova za ugao $\pi$, a rotacione za proizvoljan ugao koji sam biraš.

## Univerzalnost: $H$, $S$ i $T$

Prirodno pitanje je: **koliko kapija nam zaista treba** da bismo mogli da izvedemo bilo koje kvantno računanje? Neće nam trebati beskonačna riznica kapija — dovoljan je mali, konačan skup.

Za jedan kjubit, opšta kapija $U(\theta,\phi,\lambda)$ pokriva **sve** rotacije, ali na pravom hardveru ne možemo da podesimo uglove savršeno precizno. Zato tražimo **konačan** (diskretan) skup kapija čijim kombinovanjem možemo da se **proizvoljno blizu** približimo svakoj željenoj kapiji. Ključne su dve grupe:

- **Klifordove kapije** $\{H, S\}$ (i $\mathrm{CNOT}$ za više kjubita) — generišu takozvanu [Klifordovu grupu](https://en.wikipedia.org/wiki/Clifford_group). One su moćne, ali ih klasičan računar može efikasno simulirati (Gotesman–Nilova teorema [@gottesman1998]; vidi i [@nielsen2010], odeljak 10.5.4), pa **same po sebi** ne daju kvantnu prednost.
- **$T$ kapija** — dodavanje jedne jedine ne-Klifordove kapije $T$ skupu $\{H, S\}$ daje skup $\{H, S, T\}$ (odnosno $\{H, T\}$ za jedan kjubit) koji je **univerzalan**: njime se svaka jednokjubitna kapija može aproksimirati do proizvoljne tačnosti.

Da ta aproksimacija bude i **efikasna**, garantuje **[Solovej–Kitajeva teorema](https://en.wikipedia.org/wiki/Solovay%E2%80%93Kitaev_theorem)**: svaku željenu jednokjubitnu kapiju možemo aproksimirati sa greškom $\varepsilon$ koristeći samo $\mathcal{O}\!\big(\log^{c}(1/\varepsilon)\big)$ kapija iz skupa $\{H, T\}$ (uz malu konstantu $c$). Drugim rečima, cena veće preciznosti raste tek **poli-logaritamski**, što je izuzetno povoljno.

## Vežbe




:::{admonition} Vežba 1
:class: tip
Izračunaj $X\ket{0}$ i $X\ket{1}$ i objasni zašto se $X$ zove „kvantni NOT" (obrtanje bita).
:::

:::{admonition} Rešenje
:class: dropdown
Množenjem matrice i vektora dobijamo $X\ket{0} = \left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\left(\begin{smallmatrix}1\\0\end{smallmatrix}\right) = \left(\begin{smallmatrix}0\\1\end{smallmatrix}\right) = \ket{1}$ i slično $X\ket{1} = \ket{0}$. Kapija $X$ zamenjuje ulogu stanja $\ket{0}$ i $\ket{1}$, baš kao klasična NOT operacija nad bitom.

```python
print("X|0> =\n", X @ ket0)   # |1>
print("X|1> =\n", X @ ket1)   # |0>
```
:::

:::{admonition} Vežba 2
:class: tip
Pokaži da $Z$ ostavlja $\ket{+}$ i pretvara ga u $\ket{-}$, tj. $Z\ket{+} = \ket{-}$. Šta to znači na Blohovoj sferi?
:::

:::{admonition} Rešenje
:class: dropdown
$Z\ket{+} = \tfrac{1}{\sqrt2}Z(\ket{0}+\ket{1}) = \tfrac{1}{\sqrt2}(\ket{0}-\ket{1}) = \ket{-}$. Na Blohovoj sferi $Z$ je rotacija za $\pi$ oko $z$-ose; ona šalje $x \mapsto -x$, pa tačku $\ket{+}$ (na $+x$) prebacuje u $\ket{-}$ (na $-x$).

```python
plus  = (ket0 + ket1)/np.sqrt(2)
minus = (ket0 - ket1)/np.sqrt(2)
print("Z|+> = |-> ? ", np.allclose(Z @ plus, minus))
```
:::

:::{admonition} Vežba 3
:class: tip
Proveri direktnim množenjem matrica da važi $H^2 = I$, $S^2 = Z$ i $T^2 = S$.
:::

:::{admonition} Rešenje
:class: dropdown
Za Hadamard: $H^2 = \tfrac{1}{2}\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right) = \tfrac{1}{2}\left(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\right) = I$. Za faznu kapiju: $S^2 = \left(\begin{smallmatrix}1&0\\0&i\end{smallmatrix}\right)^2 = \left(\begin{smallmatrix}1&0\\0&i^2\end{smallmatrix}\right) = \left(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\right) = Z$, i analogno $T^2 = \left(\begin{smallmatrix}1&0\\0&e^{i\pi/2}\end{smallmatrix}\right) = S$.

```python
print("H^2 = I? ", np.allclose(H @ H, I2))
print("S^2 = Z? ", np.allclose(S @ S, Z))
print("T^2 = S? ", np.allclose(T @ T, S))
```
:::

:::{admonition} Vežba 4
:class: tip
Pokaži da Paulijeve matrice zadovoljavaju $XY = iZ$. Da li $X$ i $Y$ komutiraju?
:::

:::{admonition} Rešenje
:class: dropdown
$XY = \left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\left(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\right) = \left(\begin{smallmatrix}i&0\\0&-i\end{smallmatrix}\right) = i\left(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\right) = iZ$. Slično je $YX = -iZ$, pa je $XY \neq YX$ — Paulijeve matrice **ne komutiraju** (zapravo antikomutiraju, $XY + YX = 0$).

```python
print("XY = iZ? ", np.allclose(X @ Y, 1j*Z))
print("YX = -iZ? ", np.allclose(Y @ X, -1j*Z))
```
:::



:::{admonition} Vežba 5
:class: tip
Proveri da je $H = U(\tfrac{\pi}{2}, 0, \pi)$ zamenom uglova u opštu kapiju {eq}`eq:ugate`.
:::

:::{admonition} Rešenje
:class: dropdown
Za $\theta = \tfrac{\pi}{2}$ je $\cos\tfrac{\theta}{2} = \sin\tfrac{\theta}{2} = \tfrac{1}{\sqrt2}$. Uz $\phi = 0$, $\lambda = \pi$ dobijamo
$U(\tfrac{\pi}{2},0,\pi) = \left(\begin{smallmatrix}\tfrac{1}{\sqrt2} & -e^{i\pi}\tfrac{1}{\sqrt2} \\ e^{i0}\tfrac{1}{\sqrt2} & e^{i\pi}\tfrac{1}{\sqrt2}\end{smallmatrix}\right) = \tfrac{1}{\sqrt2}\left(\begin{smallmatrix}1 & 1 \\ 1 & -1\end{smallmatrix}\right) = H,$
jer je $e^{i\pi} = -1$.

```python
print("H = U(pi/2, 0, pi)? ", np.allclose(H, U(np.pi/2, 0, np.pi)))
```
:::

:::{admonition} Vežba 6
:class: tip
**Univerzalnost u praksi.** Zadata je ciljna kapija $R_z(\tfrac{\pi}{4})$. Pokaži da se ona poklapa sa $T$ (do na globalnu fazu), koristeći $R_z(\theta) = e^{-i\theta/2}U(0,0,\theta)$ i $T = U(0,0,\tfrac{\pi}{4})$.
:::

:::{admonition} Rešenje
:class: dropdown
Iz {eq}`eq:rot-from-u` je $R_z(\tfrac{\pi}{4}) = e^{-i\pi/8}\,U(0,0,\tfrac{\pi}{4}) = e^{-i\pi/8}\,T$. Dakle $R_z(\tfrac{\pi}{4})$ i $T$ se razlikuju samo za globalnu fazu $e^{-i\pi/8}$, pa daju identično fizičko dejstvo. Ovo je najprostiji primer principa iz Solovej–Kitajeve teoreme: „egzotičnu" rotaciju smo zamenili jednom kapijom iz univerzalnog skupa $\{H, S, T\}$.

```python
lhs = Rz(np.pi/4)
rhs = np.exp(-1j*np.pi/8) * T
print("Rz(pi/4) = e^{-i pi/8} T? ", np.allclose(lhs, rhs))
```
:::
