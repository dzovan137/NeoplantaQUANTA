---
title: "MyST Feature Gallery"
short_title: Feature Gallery
description: A reference page demonstrating every authoring feature used in this course.
---

# MyST Feature Gallery

This page is a **living cheat-sheet**: every block below shows a MyST feature *and* the
result. Copy any snippet into your own pages. View the raw source of this file next to the
rendered page to see exactly how each is written.

## 1. Admonitions (callouts)

:::{note}
A `note` for neutral information.
:::

:::{tip}
A `tip` for helpful advice.
:::

:::{warning}
A `warning` for things that can bite you.
:::

:::{danger}
A `danger` box for the most serious pitfalls.
:::

:::{note} Click to expand
:class: dropdown
This is a **collapsible** admonition (`:class: dropdown`). Great for hints and solutions.
:::

## 2. Dropdowns

:::{dropdown} Show the extra detail
Dropdowns use the native HTML `<details>` element, so they work even without JavaScript.
:::

## 3. Tabs

Use tabs to show the same idea in different representations:

::::{tab-set}
:::{tab-item} Dirac notation
$\ket{+} = \tfrac{1}{\sqrt2}\big(\ket{0} + \ket{1}\big)$
:::
:::{tab-item} Column vector
$\ket{+} = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$
:::
:::{tab-item} Python
```python
import numpy as np
plus = (1/np.sqrt(2)) * np.array([[1],[1]], dtype=complex)
```
:::
::::

## 4. Cards and grids

::::{grid} 1 1 2 3

:::{card} 🧮 NumPy
Everything in this course runs on plain NumPy arrays.
:::
:::{card} 🎯 Dirac notation
Bra–ket macros make the math read like a textbook.
:::
:::{card} 🌐 Bloch sphere
A geometric picture of a single qubit.
:::

::::

You can also make a whole card a link, or drop in a {button}`Visit MyST <https://mystmd.org>`.

## 5. Math and equations

A labelled display equation using our macros:

```{math}
:label: eq:bell
\ket{\Phi^+} = \frac{1}{\sqrt{2}}\big(\ket{00} + \ket{11}\big)
```

Cross-reference it as [](#eq:bell), or with the equation role: {eq}`eq:bell`.

Aligned multi-line math with an AMS environment:

$$
\begin{align}
H\ket{0} &= \ket{+} = \tfrac{1}{\sqrt2}(\ket{0}+\ket{1}) \\
H\ket{1} &= \ket{-} = \tfrac{1}{\sqrt2}(\ket{0}-\ket{1})
\end{align}
$$

A matrix (the Hadamard gate):

$$
H = \frac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

## 6. Figures and images

An `image` (no caption, no number):

```{image} ../images/bloch-sphere.png
:alt: Bloch sphere
:width: 260px
:align: center
```

A `figure` is numbered and cross-referenceable — see [](#fig:bloch2):

```{figure} ../images/bloch-sphere.png
:label: fig:bloch2
:width: 300px
:align: center

A qubit on the Bloch sphere.
```

## 7. Code presentation

A plain fenced block is syntax-highlighted with a copy button (not executed):

```python
def dagger(A):
    "Conjugate transpose (Hermitian adjoint)."
    return A.conj().T
```

A `code` directive can add a **filename**, **caption**, line numbers, and highlighting:

```{code} python
:filename: measure.py
:caption: Born-rule probability of an outcome
:linenos:
:emphasize-lines: 3
import numpy as np
def prob(ket_k, psi):
    return abs((ket_k.conj().T @ psi).item())**2   # |<k|psi>|^2
```

## 8. Theorems and proofs

:::{prf:theorem} No-cloning theorem
:label: thm:nocloning
There is no unitary $U$ that copies an arbitrary unknown quantum state, i.e. such that
$U\big(\ket{\psi}\otimes\ket{0}\big) = \ket{\psi}\otimes\ket{\psi}$ for all $\ket{\psi}$.
:::

:::{prf:proof}
:class: dropdown
Suppose such a $U$ exists for two states $\ket{\psi}$ and $\ket{\phi}$. Taking inner
products of $U(\ket{\psi}\ket{0})=\ket{\psi}\ket{\psi}$ and
$U(\ket{\phi}\ket{0})=\ket{\phi}\ket{\phi}$ and using unitarity gives
$\braket{\psi}{\phi} = \braket{\psi}{\phi}^2$, so the overlap is $0$ or $1$. Hence cloning
is impossible for non-orthogonal states. $\;\square$
:::

:::{prf:definition} Fidelity
:label: def:fidelity
For pure states the **fidelity** is $F(\psi,\phi) = |\braket{\psi}{\phi}|^2$.
:::

## 9. Exercises and solutions

:::{exercise}
:label: ex:hadamard
Show that $H^2 = I$, i.e. applying the Hadamard gate twice returns the original state.
:::

:::{solution} ex:hadamard
:class: dropdown
Direct multiplication of the matrix in §5 gives
$H^2 = \tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
= \begin{pmatrix}1&0\\0&1\end{pmatrix} = I.$
:::

## 10. Citations and footnotes

Quantum information theory builds on Shannon's foundations [@shannon1948], with the
modern reference being Nielsen & Chuang [@nielsen2010]. The no-cloning theorem is due to
Wootters and Zurek [@wootters1982].[^history]

[^history]: Footnotes are great for asides that would interrupt the flow.

## 11. Margin notes

:::{aside}
Margin content (an `aside`) floats beside the text — handy for definitions, side remarks,
or historical notes.
:::

## 12. Diagrams (Mermaid)

Quantum teleportation as a flowchart, rendered from text:

```{mermaid}
flowchart LR
    A[Alice: |psi>] -->|entangled pair| B(Bell measurement)
    B -->|2 classical bits| C[Bob]
    C -->|apply correction| D[Bob: |psi>]
```

## 13. Tables

```{list-table} Single-qubit gates
:header-rows: 1
:label: tbl:gates

* - Gate
  - Symbol
  - Action on $\ket{0}$
* - Pauli-X
  - $X$
  - $\ket{1}$
* - Hadamard
  - $H$
  - $\ket{+}$
* - Phase
  - $S$
  - $\ket{0}$
```

See [](#tbl:gates) for the numbered table.

## 14. Glossary and terms

:::{glossary}
qubit
: The basic unit of quantum information; a normalised vector in $\CC^2$.

superposition
: A linear combination of basis states, as in {eq}`eq:bell`.
:::

Reference a defined term inline, like {term}`qubit` or {term}`superposition`.

## 15. Cross-page references

Because everything is labelled, you can link across the whole book: jump back to
[Lesson 1](../content/01-qubits.md), to a section like [](#sec:state), or to a result like
[](#thm:nocloning).

<!-- This is a MyST comment: it will not appear in the output. -->
