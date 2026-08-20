---
title: "Teleportacija"
short_title: Teleportacija
description: Osnove višekubitnih sistema    
---

# Ovde ćemo da stavimo osnove
- Više kubitni sistemi se dobijaju tenzorskim proizvodom
- Neke osnove. Dvokubitni primeri --> Bellova stanja
- Računanje zapletenosti
- Osnove kako se entanglement definished
- Born-ovo pravilo za merenje, primeri računice
- Kolo za kvantu teleportaciju, numericki i graficko objasnjenje
- Bellova nejednakost, tenutak kada kvantna mehanika ulazi u igra i velika razlika sa klasičnom fizikom
- full state multiqubit tomography




## Kod: Bornovo pravilo i kolaps za registar

Napravimo mali alat koji za proizvoljno stanje registra gradi projektor {eq}`eq:proj-multi`, računa verovatnoću i kolaps, pa njime proverimo oba primera. Projektor je (radi nastave) prosto dijagonalna matrica sa jedinicama na baznim stanjima koja prežive:

```python
import numpy as np
from itertools import product

N = 3
baza = [''.join(bits) for bits in product('01', repeat=N)]   # '000','001',...,'111'

def slucajno_stanje(N=3, seed=0):
    rng = np.random.default_rng(seed)
    a = rng.normal(size=2**N) + 1j*rng.normal(size=2**N)
    return a/np.linalg.norm(a)                                # normirano stanje

def projektor(mereni, ishodi, N=3):
    """Dijagonalni projektor: zadrži bazna stanja gde su 'mereni' kjubiti = 'ishodi'.
    mereni: 1-indeksirani kjubiti; ishodi: pripadni bitovi."""
    diag = [1.0 if all(int(s[q-1]) == b for q, b in zip(mereni, ishodi)) else 0.0
            for s in baza]
    return np.diag(diag).astype(complex)

def izmeri(psi, mereni, ishodi):
    P = projektor(mereni, ishodi)
    p = (psi.conj() @ P @ psi).real                          # p = <psi|P|psi>
    psi_post = (P @ psi)/np.sqrt(p)                          # kolaps + normiranje
    return p, psi_post
```

**Primer 1** — merimo prvi kjubit (ishod $0$), pa drugi kjubit (ishod $1$):

```python
psi = slucajno_stanje(seed=1)
a = psi                                    # a[i] je amplituda uz |i>  (i = 0..7)

# --- prvi kjubit = 0  (prežive |000>,|001>,|010>,|011>, tj. indeksi 0,1,2,3) ---
p, post = izmeri(psi, mereni=[1], ishodi=[0])
print("p(0_1) =", round(p, 4), " (rucno:", round(np.sum(np.abs(a[[0, 1, 2, 3]])**2), 4), ")")

ocek = np.zeros(8, complex); ocek[[0, 1, 2, 3]] = a[[0, 1, 2, 3]]
ocek /= np.linalg.norm(ocek)
print("kolaps = ocekivano stanje? ", np.allclose(post, ocek))

# --- drugi kjubit = 1  (prežive |010>,|011>,|110>,|111>, indeksi 2,3,6,7) ---
p2, post2 = izmeri(psi, mereni=[2], ishodi=[1])
print("p(1_2) =", round(p2, 4), " (rucno:", round(np.sum(np.abs(a[[2, 3, 6, 7]])**2), 4), ")")
```

**Primer 2** — merimo prva dva kjubita, ishod $\{1_1, 1_2\}$ (prežive samo $\ket{110}, \ket{111}$):

```python
p11, post11 = izmeri(psi, mereni=[1, 2], ishodi=[1, 1])
print("p(1_1,1_2) =", round(p11, 4), " (rucno:", round(np.sum(np.abs(a[[6, 7]])**2), 4), ")")

ocek11 = np.zeros(8, complex); ocek11[[6, 7]] = a[[6, 7]]
ocek11 /= np.linalg.norm(ocek11)
print("kolaps na {|110>, |111>}? ", np.allclose(post11, ocek11))

# relacija potpunosti: zbir verovatnoća svih ishoda na kjubitu 1 je 1
print("p(0_1) + p(1_1) =", round(izmeri(psi, [1], [0])[0] + izmeri(psi, [1], [1])[0], 6))
```

:::{note} Qiskit i redosled kjubita (klik)
:class: dropdown
Isto se može uraditi i u Qiskit-u sa `Statevector(psi).measure([j])`, ali oprez: Qiskit numeriše kjubite **obrnuto** (little-endian, kjubit $0$ je krajnje desni bit), pa se indeksi i niske razlikuju od konvencije $\ket{b_1 b_2 b_3}$ koju ovde koristimo. Zbog jasnoće smo gore ostali na `numpy`-ju, gde sami držimo redosled pod kontrolom.
:::

:::{important} Šta pamtimo iz ove lekcije
:class: simple
Bornovo pravilo i kolaps za registar imaju **isti oblik** kao za jedan kjubit; samo je projektor $\Pi = \sum_{\mathbf{x}} \dyad{\mathbf{x}}{\mathbf{x}}$ zbir po baznim stanjima koja se slažu sa izmerenim ishodima: $p = \bra{\Psi}\Pi\ket{\Psi}$ i $\ket{\Psi'} = \Pi\ket{\Psi}/\sqrt{p}$. Verovatnoća je zbir $|a_{\mathbf{x}}|^2$ preživelih amplituda, a stanje se posle merenja normira istim tim korenom. Kada izmerimo samo deo registra, **preostali kjubiti ostaju u superpoziciji** — to je polazna tačka za spletenost i teleportaciju.
:::
