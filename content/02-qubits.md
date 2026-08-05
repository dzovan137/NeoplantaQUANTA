---
title: "Lesson 1 — The Qubit"
short_title: The Qubit
description: The state of a single qubit, the Bloch sphere, and first steps in Python.
---

# Qubit (Kjubit)

**Qubit** is osnovna jedinica građe i funkcije kvatne informatike, i i predstavlja
analogon klasičnim bit-ovima. Klasični bitovi mogu da imaju vrednosti $0$ i $1$, qubit može biti u linearnoj superpoziciji ova dva stanja!

Šta mislim pod linearnim? U najjednostavnijem smislu ukoliko imamo funkciju $f(a \vec{x} + b \vec{y}) = a f(\vec{x}) + b f(\vec{y})$ gde x i y mogu biti bilo koji od sledećih matematičkih objekata


```{figure} ../images/DifferentMathObjects.png
:label: fig:DifferentMathObjects
:alt: The Bloch sphere with the state psi drawn as a unit vector.
:width: 420px
:align: center

Različiti tipovi matematičkih funkcija i njihova dijagramatička representacija. 
```

Tenzori igraju veoma važnu ulogu u kvantnoj informatici ali i u ostalim poljima fizike, ali u ovom kursu nećemo ulaziti u detalje ove reprezentacije i zašto je bitna. 
Dok prve tre konstrukcije će biti korišćene. Kvantna mehaniku nazivaju i matrično mehanikom koju je Heisenberg prvi formulisao [citat iz Panticeve knjige]




(sec:state)=
## Kvantno stanje - qubit

A qubit lives in a two-dimensional complex Hilbert space $\Hilb = \CC^2$, spanned by the
**computational basis** states $\ket{0}$ and $\ket{1}$. A general pure state is

```{math}
:label: eq:qubit
\ket{\psi} = \alpha \ket{0} + \beta \ket{1},
\qquad \alpha, \beta \in \CC,
```

where the amplitudes obey the **normalisation condition**

```{math}
:label: eq:norm
\braket{\psi}{\psi} = |\alpha|^2 + |\beta|^2 = 1 .
```

Inline notation works too: the overlap of two states is written $\braket{\phi}{\psi}$, and
a projector onto $\ket{0}$ is the outer product $\dyad{0}{0}$. These come from the
`\ket`, `\bra`, `\braket`, and `\dyad` macros defined once in `myst.yml` — see
[](#eq:qubit) and [](#eq:norm) for the numbered equations.

## The Bloch sphere

Up to a global phase, any single-qubit pure state can be written with two real angles
$\theta \in [0,\pi]$ and $\varphi \in [0,2\pi)$,

```{math}
:label: eq:bloch
\ket{\psi} = \cos\tfrac{\theta}{2}\,\ket{0} + e^{i\varphi}\sin\tfrac{\theta}{2}\,\ket{1},
```

so that the state maps to a point on the unit sphere, as shown in [](#fig:bloch).

```{figure} ../images/bloch-sphere.png
:label: fig:bloch
:alt: The Bloch sphere with the state psi drawn as a unit vector.
:width: 420px
:align: center

The **Bloch sphere**. The north and south poles are $\ket{0}$ and $\ket{1}$; the state
$\ket{\psi}$ of {eq}`eq:bloch` is the red unit vector at angles $(\theta,\varphi)$.
```

## Your first quantum code

Let's build these states in Python. We only need NumPy.

:::{tip} Copy me into your notebook
:class: simple
Paste each block below into a cell of your **own** Jupyter notebook and run it there.
The blocks are self-contained and run top-to-bottom.
:::

```python
import numpy as np

# The computational basis states |0> and |1> as column vectors.
ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)

# A superposition: the |+> state = (|0> + |1>)/sqrt(2)
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
