---
title: "Korišćenje pravog kvatnog računara"
short_title: Korišćenje pravog kvatnog računara
description: Kako koristimo pravi kvantni računar?
---

# Kako da pustimo prvi kvantni račun

Hajde da vidimo kako možemo da koristimo pravi kvantni računar koristeći programsko okruženje QisKit. 

Prvo pristupimo: https://resonance.iqm.tech i ulogujemo se.

Nakon prijave otvara se **kontrolna tabla** (*Dashboard*). Na njoj vidimo dostupne kvantne računare: IQM Emerald, IQM Garnet i IQM Sirius. Zajedno sa brojem kubita, statusom (da li su trenutno dostupni) i dužinom reda čekanja. Ispod se nalaze kalendar dostupnosti i lista naših poslednjih poslova (*jobs*), sa vremenom izvršavanja i statusom.

```{figure} ../images/step1.png
:label: fig:iqm-dashboard
:alt: IQM Resonance kontrolna tabla sa dostupnim kvantnim računarima i listom poslova
:width: 720px
:align: center

Kontrolna tabla IQM Resonance okruženja: dostupni kvantni računari (Emerald, Garnet, Sirius), kalendar dostupnosti i pregled poslednjih poslova.
```

Klikom na pojedinačni kvantni računar otvaraju se njegove **tehničke specifikacije**. Za IQM Garnet vidimo da je reč o procesoru sa 20 superprovodnih transmon kubita raspoređenih u kvadratnu rešetku. Prikazani su cena po sekundi i po satu, topologija (CRYSTAL 20), najveći dozvoljeni broj uzorkovanja i kola, kao i ključni pokazatelji kvaliteta: prosečna vernost PRX kapije (99.93%), vernost CZ kapije (99.38%) i vremena koherencije $T_1$ i $T_2$. Na mapi je prikazan raspored svih kubita (QB1–QB20) i njihove veze, obojeni prema greškama kapija.

```{figure} ../images/step2.png
:label: fig:iqm-garnet-specs
:alt: Tehničke specifikacije i mapa kubita procesora IQM Garnet
:width: 720px
:align: center

Tehnička specifikacija procesora IQM Garnet: parametri kvaliteta kapija, vremena koherencije i mapa povezanosti 20 kubita.
```

Primer detaljne tehničke specifikacije za IQM Garnet procesor možete pronaći i u naučnom radu: https://arxiv.org/abs/2408.12433

Da bismo pokrenuli sopstveni račun, potreban nam je **pristupni token**. Idemo na karticu **Account** (*Nalog*). Tu vidimo naš nalog, izabrani plan (Starter) i broj dostupnih **kredita** (na slici 320.00), koji se troše prilikom izvršavanja kvantnih kola na kvantnom računaru.

```{figure} ../images/step3.png
:label: fig:iqm-account
:alt: Stranica naloga (Account) sa pregledom dostupnih kredita
:width: 720px
:align: center

Stranica **Account**: pregled naloga, dostupnih kredita i vremenskih termina (*timeslots*).
```

Zatim otvaramo **podešavanja profila** (*Profile settings*), gde se nalaze osnovne informacije o nalogu.

```{figure} ../images/step4.png
:label: fig:iqm-profile
:alt: Stranica podešavanja profila (Profile settings)
:width: 720px
:align: center

Podešavanja profila (*Profile settings*) je polazna tačka za kreiranje pristupnog tokena.
```

Na dnu stranice profila nalazi se odeljak **Access tokens** (*Pristupni tokeni*). Klikom na dugme **Create new token** kreiramo novi token sa opsegom *Job execution*. Dobijeni niz znakova je naš token. Kopiramo ga i unosimo u promenljivu `my_token` u kodu ispod. Token je poput lozinke, pa ga ne treba deliti javno niti ostavljati u kodu koji delimo sa drugima.

```{figure} ../images/step5.png
:label: fig:iqm-tokens
:alt: Odeljak Access tokens sa dugmetom Create new token
:width: 720px
:align: center

Odeljak **Access tokens**. Ovde dugmetom *Create new token* kreiramo novi token sa opsegom *Job execution*.
```

Kada ste kreirali svoj token možemo započeti naš prvi račun na pravom kvantnom računaru! 

Koraci:

- instaliraj potrebne pakete
```python
!pip install qiskit 
!pip install pylatexenc
!pip install iqm-client[qiskit]
```

- definiši kvantno kolo
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

```

Definisano kolo možemo i da nacrtamo pozivom `qc.draw()` gde dobijamo jedan kubit `q` na koji deluje Hadamardova kapija **H**, a zatim sledi merenje čiji se rezultat upisuje u klasični registar `meas`.

```{figure} ../images/step6.png
:label: fig:iqm-circuit
:alt: Dijagram kvantnog kola sa jednom Hadamardovom kapijom i merenjem
:width: 320px
:align: center

Nacrtano kvantno kolo: Hadamardova kapija na kubitu `q`, praćena merenjem u klasični registar `meas`.
```

- pokreni račun
```python
# potrebni alati
from qiskit import transpile
from iqm.qiskit_iqm import IQMProvider


# Definisanje konekcije to IQM 
iqm_server_url = "https://resonance.iqm.tech"
my_token = "97tntBkqWiVm4idfd+tZQDn3iUgcXCLeGJA/Dtf9JNgBn6nbIVt9AZbOx3VojD9s"

# Instantiate the IQMProvider directly with the URL, token, and quantum_computer
provider = IQMProvider(url=iqm_server_url, token=my_token, quantum_computer='garnet')

# Get the 'sirius' backend from the provider. This step will now correctly use the configured provider.
qiskit_iqm_backend = provider.get_backend("garnet")

transpiled_circuit = transpile(qc, backend=qiskit_iqm_backend)
job = qiskit_iqm_backend.run(transpiled_circuit, shots=1000)

result = job.result()
counts = result.get_counts() # Removed transpiled_circuit argument
print("Measurement counts:", counts)
```
- vizuelizacija
```python
import matplotlib.pyplot as plt

probabilities = [counts['0']/broj_uzorkovanja, counts['1']/broj_uzorkovanja]

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


Ukoliko pokušamo da dodamo još jedanu kapiju $H$ dobijamo početno stanje nazad! Proveri to!


Ukoliko recimo ponovimo taj korak više puta, možemo da vidimo kako 'kvalitet' rezultata opada!
Primer koda:

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)

for i in range(0,100):
  qc.h(0)
  qc.barrier()
  qc.h(0)
  qc.barrier()


qc.measure_all()
```

Nacrtajmo ovo kolo pomoću `qc.draw()`. Dobijamo dugačak niz Hadamardovih kapija: sto puta ponovljen par `H`–`H`, razdvojenih barijerama koje sprečavaju prevodilac da ih uprosti. Idealno, svaki par `H`–`H` se poništava u identitet, pa bi kubit trebalo da ostane u stanju $\ket{0}$.

```{figure} ../images/step7.png
:label: fig:iqm-circuit-repeated
:alt: Kolo sa velikim brojem uzastopnih Hadamardovih kapija razdvojenih barijerama, praćeno merenjem
:width: 600px
:align: center

Kolo dobijeno stostrukim ponavljanjem para `H`–`H` (ukupno 200 kapija), razdvojenih barijerama i praćeno merenjem.
```

Kada ovo kolo pokrenemo na pravom kvantnom računaru, umesto idealnog rezultata (100% ishoda "0") javlja se i pogrešan ishod "1". Svaka kapija unosi malu grešku, a kroz veliki broj kapija te greške se nagomilavaju, pa kvalitet rezultata opada.

```{figure} ../images/step8.png
:label: fig:iqm-histogram-noise
:alt: Histogram izmerenih verovatnoća sa oko 90 procenata ishoda 0 i 10 procenata ishoda 1
:width: 640px
:align: center

Izmereni histogram nakon 200 kapija: umesto idealnih 100% za "0", zbog šuma i grešaka kapija oko 10% merenja daje "1". Nagomilavanje grešaka smanjuje pouzdanost rezultata.
```



## Merenje u drugim bazama i očekivane vrednosti

Merenje u računskoj bazi zapravo meri **operator $Z$**: ishodi $0$ i $1$ odgovaraju njegovim svojstvenim vrednostima $+1$ i $-1$. Prosečna izmerena vrednost je **očekivana vrednost**

```{math}
:label: eq:expectation-z
\langle Z \rangle = p(0) - p(1) = \dfrac{N_{0} - N_{1}}{N},
```
gde smo sa $N_0$ označili broj uzorkovanja u stanju $\ket{0}$ tj. merenja registra u $0$ dok $N_1$ broj uzorkovanja u stanju $\ket{1}$, iliti registar u vrednosti $1$. 

:::{note} Prikaži račun (klik)
:class: dropdown

```{figure} ../images/zoperator.png
:label: fig:zoperator
:alt: purity
:width: 520px
:align: center

```
:::



Šta ako želimo $\langle X \rangle$ ili $\langle Y \rangle$? Hardver ume da meri samo u $Z$-bazi, pa željenu osu prvo **zarotiramo u $Z$-osu**, izmerimo, i pročitamo isti izraz $p(0)-p(1)$. Iz [](03-one-qubit-gates.md) znamo prave rotacije: 

- $X$ je dovoljan $H$ --> jer $H^{\dagger} X H = Z$,
- $Y$ kombinacija $S^\dagger$ pa $H$ --> $  (H S^{\dagger})^{\dagger} Z ( H S^{\dagger}) =  (S H) Z (H S^{\dagger}) = Y$ (proveri račun!).



:::{note} Prikaži račun (klik)
:class: dropdown

```{figure} ../images/rotiranje_Y.png
:label: fig:yoperator
:alt: purity
:width: 520px
:align: center

```
:::


```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Pauli
from qiskit.primitives import StatevectorSampler

# lokalni "simulator"; kasnije ga menjamo pravim hardverom
sampler = StatevectorSampler()   

def izmeri_ocekivanu(prep, osa, shots=1000):
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

Ove tri očekivane vrednosti nisu ništa drugo do **koordinate Blohovog vektora** $\mathbf{r} = (\langle X\rangle, \langle Y\rangle, \langle Z\rangle)$ koji smo uveli u prethodnim lekcijama! 

## Kvantna tomografija

Ako izmerimo sve tri komponente $\langle X\rangle, \langle Y\rangle, \langle Z\rangle$, možemo da **rekonstruišemo** Blohov vektor, tj. celo (nepoznato) jednokubitno stanje. To je najprostiji primer **kvantne tomografije**.

:::{important} Zašto treba mnogo kopija?
:class: simple
Jedno merenje daje samo jedan bit i **uništi** stanje. Zato za tomografiju moramo iznova da pripremimo isto stanje mnogo puta i podelimo merenja na tri grupe (po jednu za $X$, $Y$ i $Z$ osu). Kopiranje nepoznatog stanja nije rešenje: to zabranjuje teorema o nekloniranju (https://en.wikipedia.org/wiki/No-cloning_theorem)!
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

Vektor treba da leži (do na statističku grešku) na **površini** Blohove sfere, $|\mathbf{r}| = 1$, jer je stanje čisto. Više urokovanja (`shots`) daje precizniju procenu vrednosti ovih korelatora! Pokušaj da promeniš broj uzorkovanja! 

## Izvršenje na pravom kvantnom računaru

Do sada je `sampler` bio lokalni simulator. Lepota Qiskit-ovih **primitiva** je što se isto kolo pokreće na **pravom** kvantnom računaru promenom svega nekoliko linija — kolo, `measure` i „shots" ostaju isti. Na IBM-ovom hardveru (uz besplatan nalog na [IBM Quantum](https://quantum.ibm.com)) obrazac je:

```python
# ============================================================
#  1-qubit tomografija na IQM hardveru (Sirius)
# ============================================================
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector, Pauli
from iqm.qiskit_iqm import IQMProvider

# ---------- Konekcija ka IQM ----------
iqm_server_url   = "https://resonance.iqm.tech"
my_token         = "97tntBkqWiVm4idfd+tZQDn3iUgcXCLeGJA/Dtf9JNgBn6nbIVt9AZbOx3VojD9s"
broj_uzorkovanja = 1000

provider = IQMProvider(url=iqm_server_url, token=my_token, quantum_computer='sirius')
qiskit_iqm_backend = provider.get_backend("sirius")


# ---------- Merenje jednog Bloh vektora (X, Y, Z u JEDNOM poslatom job-u) ----------
def blohov_vektor_hardver(prep, shots=broj_uzorkovanja):
    """Proceni Blohov vektor [<X>,<Y>,<Z>] merenjem pripremljenog stanja na hardveru."""
    ose = ['X', 'Y', 'Z']
    krugovi = []
    for osa in ose:
        qc = QuantumCircuit(1, 1)
        qc.compose(prep, inplace=True)      # 1) pripremi stanje
        if osa == 'X':
            qc.h(0)                         # 2) X-baza -> Z-baza
        elif osa == 'Y':
            qc.sdg(0); qc.h(0)              #    Y-baza -> Z-baza
        qc.measure(0, 0)                    # 3) izmeri u Z-bazi
        krugovi.append(qc)

    tqc = transpile(krugovi, backend=qiskit_iqm_backend)
    result = qiskit_iqm_backend.run(tqc, shots=shots).result()

    r = []
    for i in range(len(ose)):
        c = result.get_counts(i)
        p0 = c.get('0', 0) / shots
        p1 = c.get('1', 0) / shots
        r.append(p0 - p1)                   # <P> = p(0) - p(1)
    return np.array(r)

print("PRIMER 1")
# ---------- Primer 1: <X>, <Y>, <Z> za jednostavno stanje ----------
prep1 = QuantumCircuit(1)
prep1.ry(0.7, 0)                            # neko stanje na Blohovoj sferi

r1 = blohov_vektor_hardver(prep1)
print("<X>, <Y>, <Z> =", list(np.round(r1, 2)))

print(30*'-')

print("PRIMER 2")
# ---------- Primer 2: rekonstrukcija "nepoznatog" stanja ----------
prep2 = QuantumCircuit(1)
prep2.ry(0.7, 0)
prep2.rz(1.1, 0)                            # "nepoznato" stanje koje rekonstruišemo

r_est = blohov_vektor_hardver(prep2)
print("Procenjen Blohov vektor:", np.round(r_est, 2))

# tačan (idealni) Blohov vektor iz statevektora (za proveru):
sv = Statevector(prep2)
r_true = np.array([sv.expectation_value(Pauli(P)).real for P in ['X', 'Y', 'Z']])
print("Tačan (idealni) Blohov vektor:", np.round(r_true, 2))
print("|r| (na hardveru < 1 zbog šuma):", round(float(np.linalg.norm(r_est)), 3))
```

## Vizuelizacija izmerenog vektora

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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


# --- vektori iz tomografije (iz prethodne ćelije) ---
# r_true  = idealni Blohov vektor (|r| = 1, na površini sfere)
# r_est   = izmereni na hardveru  (|r| < 1 zbog šuma)
r_ideal = np.asarray(r_true, dtype=float)
r_hw    = np.asarray(r_est,  dtype=float)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")
nacrtaj_sferu(ax)

# linija skupljanja: od izmerenog do idealnog vrha
ax.plot(*zip(r_hw, r_ideal), color="gray", ls=":", lw=1.3)

# idealni vektor (čisto stanje)
#ax.quiver(0,0,0, *r_ideal, color="#8e44ad", lw=3, arrow_length_ratio=0.12)
#ax.text(*(1.15*r_ideal), r"idealni (čisto)", color="#8e44ad", fontsize=13)

# izmereni na hardveru
ax.quiver(0,0,0, *r_hw, color="#e67e22", lw=3, arrow_length_ratio=0.17)
ax.text(*(1.15*r_hw), r"izmerena vrednost (hardver)", color="#e67e22", fontsize=13)

ax.scatter([0],[0],[0], color="black", s=15)

nr = float(np.linalg.norm(r_hw))
ax.set_title(r"Šum na hardveru skuplja Blohov vektor:  $|\mathbf{r}|=%.2f<1$" % nr)
ax.view_init(elev=22, azim=40)
plt.tight_layout()
plt.savefig("tomografija_hardver.png", dpi=300, bbox_inches="tight")
plt.show()
```
```{figure} ../images/eksperiment_bloh.png
:label: fig:bloh_eksperiment
:alt: purity
:width: 520px
:align: center

```

## Rekonstrukcija matrice gustoće


### 2D vizuelizacija
```python
def reconstruct_rho_from_data(pauli_expectations):
    example_key = next(iter(pauli_expectations))
    num_qubits = len(example_key)

    out = np.zeros((2**num_qubits, 2**num_qubits), dtype=complex)

    for P, expval in pauli_expectations.items():
        out += expval * pauli_string_to_matrix(P)

    return out/2**num_qubits




def plot_density_matrixEXPERIMENT(rho, title=r'$\rho_{\rm experiment}$',
                        order='computational',      # <-- the toggle
                        max_labels=16,
                        show_weight_blocks=True):
    n   = int(round(np.log2(rho.shape[0])))
    dim = rho.shape[0]

    if order == 'hamming':
        perm, sorted_weights = hamming_order(n)
        rho = rho[np.ix_(perm, perm)]           # symmetric permutation
        labels = [format(k, f'0{n}b') for k in perm]
        order_note = 'Hamming-weight ordered'
    elif order == 'computational':
        sorted_weights = None
        labels = [format(k, f'0{n}b') for k in range(dim)]
        order_note = 'computational order'
    else:
        raise ValueError("order must be 'computational' or 'hamming'")

    vmax, vmin = np.abs(rho).max(), -np.abs(rho).max()

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), constrained_layout=True)

    for ax, data, lab in zip(axes, [rho.real, rho.imag],
                             [r'Re$(\rho)$', r'Im$(\rho)$']):
        im = ax.imshow(data, cmap='RdBu_r', vmin=vmin, vmax=vmax,
                       interpolation='nearest')
        ax.set_title(lab, pad=10)

        if dim <= max_labels:
            ax.set_xticks(range(dim)); ax.set_yticks(range(dim))
            ax.set_xticklabels(labels, rotation=90, fontsize=7, family='monospace')
            ax.set_yticklabels(labels, fontsize=7, family='monospace')
        ax.tick_params(top=False, labeltop=False, bottom=True, labelbottom=True)

        ax.set_xticks(np.arange(-.5, dim, 1), minor=True)
        ax.set_yticks(np.arange(-.5, dim, 1), minor=True)
        ax.grid(which='minor', color='w', linewidth=0.4)
        ax.tick_params(which='minor', length=0)

        # black lines separating the Hamming-weight sectors
        if order == 'hamming' and show_weight_blocks:
            for b in np.flatnonzero(np.diff(sorted_weights)) + 0.5:
                ax.axhline(b, color='k', lw=1.1)
                ax.axvline(b, color='k', lw=1.1)

    cbar = fig.colorbar(im, ax=axes, shrink=0.85, pad=0.02)
    cbar.set_label('matrix element', rotation=270, labelpad=14)
    fig.suptitle(f'{title}   ($n={n}$, {dim}×{dim}, {order_note})', fontsize=12)
    return fig



# ---------- helper koji nedostaje: Pauli string -> matrica ----------
def pauli_string_to_matrix(P):
    """Tenzorski proizvod 1-kubitnih Pauli matrica za string kao 'X', 'ZZ', 'XIZ'..."""
    single = {
        'I': np.array([[1, 0], [0,  1]], dtype=complex),
        'X': np.array([[0, 1], [1,  0]], dtype=complex),
        'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
        'Z': np.array([[1, 0], [0, -1]], dtype=complex),
    }
    M = np.array([[1]], dtype=complex)
    for ch in P:
        M = np.kron(M, single[ch])
    return M


# ---------- sklopi ρ iz izmerenih očekivanih vrednosti ----------
# r_est = [<X>, <Y>, <Z>] sa hardvera;  <I> = Tr(ρ) = 1
pauli_exp_hw = {'I': 1.0, 'X': r_est[0], 'Y': r_est[1], 'Z': r_est[2]}
rho_hw = reconstruct_rho_from_data(pauli_exp_hw)

print("ρ (hardver):")
print(np.round(rho_hw, 3))
print("Tr(ρ) =", round(float(np.trace(rho_hw).real), 3))
print("Svojstvene vrednosti:", np.round(np.linalg.eigvalsh(rho_hw), 3))
print("Čistoća Tr(ρ²) =", round(float(np.trace(rho_hw @ rho_hw).real), 3))

# ---------- prikaz ----------
fig = plot_density_matrixEXPERIMENT(rho_hw,
                                    title=r'$\rho_{\rm hardver}$',
                                    order='computational')
plt.show()
```

```{figure} ../images/2D.png
:label: fig:2D
:alt: purity
:width: 520px
:align: center

```


### 3D vizuelizacija



```python
from matplotlib import colors, cm  
def plot_density_matrix_3d(rho,
                           title=r'$\rho_{\rm simu}$',
                           order='computational',   # 'computational' | 'hamming'
                           parts=('real', 'imag'),  # any of 'real','imag','abs'
                           color_by='value',        # 'value' | 'phase'
                           max_labels=16,
                           bar_width=0.75,
                           elev=28, azim=-58,
                           cmap_name='RdBu_r'):
    """3D 'cityscape' bar plot of a density matrix."""
    n   = int(round(np.log2(rho.shape[0])))
    dim = rho.shape[0]

    # --- optional Hamming-weight reordering (reuses hamming_order from before)
    if order == 'hamming':
        perm, _ = hamming_order(n)
        rho = rho[np.ix_(perm, perm)]
        labels = [format(k, f'0{n}b') for k in perm]
        order_note = 'Hamming-weight ordered'
    elif order == 'computational':
        labels = [format(k, f'0{n}b') for k in range(dim)]
        order_note = 'computational order'
    else:
        raise ValueError("order must be 'computational' or 'hamming'")

    part_data  = {'real': rho.real, 'imag': rho.imag, 'abs': np.abs(rho)}
    part_label = {'real': r'Re$(\rho)$', 'imag': r'Im$(\rho)$', 'abs': r'$|\rho|$'}

    vmax = np.abs(rho).max()
    if color_by == 'value':
        norm = colors.TwoSlopeNorm(vmin=-vmax, vcenter=0.0, vmax=vmax)
        cmap = plt.get_cmap(cmap_name)
        cbar_label = 'matrix element'
    elif color_by == 'phase':
        norm = colors.Normalize(vmin=-np.pi, vmax=np.pi)
        cmap = plt.get_cmap('hsv')
        cbar_label = r'phase  arg$(\rho_{jk})$'
    else:
        raise ValueError("color_by must be 'value' or 'phase'")

    # --- bar base grid
    xs, ys = np.meshgrid(np.arange(dim), np.arange(dim), indexing='ij')
    xpos = xs.ravel() - bar_width / 2
    ypos = ys.ravel() - bar_width / 2
    zpos = np.zeros_like(xpos, dtype=float)
    dx = dy = np.full_like(xpos, bar_width, dtype=float)
    phase = np.angle(rho).ravel()

    fig = plt.figure(figsize=(6.4 * len(parts) + 1.4, 5.6))

    for a, p in enumerate(parts):
        ax = fig.add_subplot(1, len(parts), a + 1, projection='3d')
        dz = part_data[p].ravel().astype(float)

        facecolors = cmap(norm(phase if color_by == 'phase' else dz))
        dz_plot = np.where(np.abs(dz) < 1e-12, 1e-12, dz)   # avoid zero-height artefacts

        ax.bar3d(xpos, ypos, zpos, dx, dy, dz_plot,
                 color=facecolors, edgecolor=(0, 0, 0, 0.25),
                 linewidth=0.25, shade=True, zsort='max')

        ax.set_title(part_label[p], pad=16)
        ax.set_zlim(min(-vmax, dz.min()) * 1.05, vmax * 1.05)
        ax.view_init(elev=elev, azim=azim)

        if dim <= max_labels:
            ax.set_xticks(np.arange(dim)); ax.set_yticks(np.arange(dim))
            ax.set_xticklabels(labels, rotation=90, fontsize=6,
                               family='monospace', va='center', ha='right')
            ax.set_yticklabels(labels, fontsize=6, family='monospace',
                               va='center', ha='left')
        else:
            ax.set_xticks([]); ax.set_yticks([])

        ax.tick_params(axis='z', labelsize=7)
        ax.set_box_aspect((1, 1, 0.55))
        ax.grid(False)
        for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
            axis.pane.set_alpha(0.06)

    mappable = cm.ScalarMappable(cmap=cmap, norm=norm)
    mappable.set_array([])
    cbar = fig.colorbar(mappable, ax=fig.axes, shrink=0.6, pad=0.02, aspect=18)
    cbar.set_label(cbar_label, rotation=270, labelpad=16)

    fig.suptitle(f'{title}   ($n={n}$, {dim}×{dim}, {order_note})', fontsize=12, y=0.97)
    return fig


# 3D "cityscape" prikaz rekonstruisane matrice gustine sa hardvera
fig = plot_density_matrix_3d(rho_hw,
                             title=r'$\rho_{\rm hardver}$',
                             order='computational',
                             parts=('real', 'imag'),
                             color_by='value')
plt.savefig("rho_hardver_3d.png", dpi=300, bbox_inches="tight")
plt.show()
```

```{figure} ../images/3D.png
:label: fig:3D
:alt: purity
:width: 520px
:align: center

```
