---
title: "Merenje više kubita"
short_title: "Merenje više kubita"
description: Merenje i kolaps u slučaju više kubita
---



## Merenje više kubita istovremeno

Ako merimo $L$ kjubita $\{j_1, \dots, j_L\}$ odjednom, projektor zadržava bazna stanja koja se slažu sa **svim** izmerenim ishodima:

```{math}
:label: eq:proj-multi
\Pi_{\{b_{j_1}, \dots, b_{j_L}\}} = \sum_{\mathbf{x}\,:\, x_{j_1}=b_{j_1},\,\dots,\, x_{j_L}=b_{j_L}} \dyad{\mathbf{x}}{\mathbf{x}},
```

a verovatnoća

```{math}
:label: eq:born-multi1
p(b_{j_1},\dots,b_{j_L}) = \bra{\Psi}\Pi_{\{b_{j_1},\dots,b_{j_L}\}}\ket{\Psi}, 
```
i kolaps su opet istog oblika

```{math}
:label: eq:born-multi2
\ket{\Psi'} = \frac{\Pi_{\{b_{j_1},\dots,b_{j_L}\}}\ket{\Psi}}{\sqrt{p(b_{j_1},\dots,b_{j_L})}}
```

### Primer 1
Hajde da se skoncentrišemo na primer $N = 3$ kubita. Merimo prvi i drugi kubit stanja {eq}`eq:ex-stanje`. Četiri moguća ishoda daju projektore

```{math}
:label: eq:ex2-proj
\begin{aligned}
\Pi_{\{0_1, 0_2\}} &= \dyad{{\color{red}00}0}{{\color{red}00}0} + \dyad{{\color{red}00}1}{{\color{red}00}1}, \\
\Pi_{\{0_1, 1_2\}} &= \dyad{{\color{red}01}0}{{\color{red}01}0} + \dyad{{\color{red}01}1}{{\color{red}01}1}, \\
\Pi_{\{1_1, 0_2\}} &= \dyad{{\color{red}10}0}{{\color{red}10}0} + \dyad{{\color{red}10}1}{{\color{red}10}1}, \\
\Pi_{\{1_1, 1_2\}} &= \dyad{{\color{red}11}0}{{\color{red}11}0} + \dyad{{\color{red}11}1}{{\color{red}11}1}.
\end{aligned}
```

Uzimamo za primer generalno stanje 3 kubita i to:
```{math}
:label: eq:n3ponovo
\ket{\Psi} = a_0\ket{000} + a_1\ket{001} + a_2\ket{010} + a_3\ket{011} + a_4\ket{100} + a_5\ket{101} + a_6\ket{110} + a_7\ket{111},
```

Evo svih mogućih kolapsa i odgovarajućih stanja za sve četiri moguće kombinacije ishoda prvog i drugog kubita:

```{math}
:label: eq:ex2-post
\begin{aligned}
\ket{\Psi'_{\{0_1, 0_2\}}} &= \frac{a_0\ket{000} + a_1\ket{001}}{\sqrt{|a_0|^2 + |a_1|^2}}, \\
\ket{\Psi'_{\{0_1, 1_2\}}} &= \frac{a_2\ket{010} + a_3\ket{011}}{\sqrt{|a_2|^2 + |a_3|^2}}, \\
\ket{\Psi'_{\{1_1, 0_2\}}} &= \frac{a_4\ket{100} + a_5\ket{101}}{\sqrt{|a_4|^2 + |a_5|^2}}, \\
\ket{\Psi'_{\{1_1, 1_2\}}} &= \frac{a_6\ket{110} + a_7\ket{111}}{\sqrt{|a_6|^2 + |a_7|^2}}.
\end{aligned}
```

Pošto smo fiksirali prva dva kjubita, samo **treći** kubit ostaje u superpoziciji. Možemo primetiti da ova stanja možemo zapisati i kao
```{math}
:label: eq:ex3-post
\begin{aligned}
\ket{\Psi'_{\{0_1, 0_2\}}} &= \frac{\ket{00}}{\sqrt{|a_0|^2 + |a_1|^2}} \otimes \left( a_0 \ket{0} + a_1 \ket{1} \right), \\
\ket{\Psi'_{\{0_1, 1_2\}}} &= \frac{\ket{01}}{\sqrt{|a_2|^2 + |a_3|^2}} \otimes \left( a_2 \ket{0} + a_3 \ket{1} \right), \\
\ket{\Psi'_{\{1_1, 0_2\}}} &= \frac{\ket{10}}{\sqrt{|a_4|^2 + |a_5|^2}} \otimes \left( a_4 \ket{0} + a_5 \ket{1} \right), \\
\ket{\Psi'_{\{1_1, 1_2\}}} &= \frac{\ket{11}}{\sqrt{|a_6|^2 + |a_7|^2}} \otimes \left( a_6 \ket{0} + a_7 \ket{1} \right).
\end{aligned}
```

Grafički, u reprezentaciji **kvantnog kola**, ovakvo merenje možemo predstaviti na sledeći način.

## Kolo koje izvodi projektivno merenje

Kolo čitamo s leva na desno: prvo pripremimo registar u nekom stanju $\ket{\Psi}$ (blok $\ket{\Psi}$ obuhvata sva tri kubita), a zatim na kubit $1$ i kubit $2$ postavimo **simbol merenja**. Svaki takav simbol „ispiše" izmereni bit u klasični registar $c$ (dvostruka linija = klasična žica). Ono što je ovde ključno: **kubit $3$ ne merimo**. Njegova žica se nastavlja bez prekida, pa on ostaje u superpoziciji.

```{figure} ../images/kolo-merenje-2q.png
:label: fig:kolo-merenje-2q
:alt: Kolo od tri kubita: blok pripreme stanja Psi, zatim merenje prvog i drugog kubita u dvobitni klasični registar, dok treći kubit ostaje nemeren.
:width: 480px
:align: center

Projektivno merenje kubita $1$ i $2$ registra od tri kubita. Blok $\ket{\Psi}$ priprema proizvoljno stanje {eq}`eq:n3ponovo`; dva simbola merenja odgovaraju projektorima $\Pi_{\{b_1, b_2\}}$ i beleže ishode $b_1, b_2$ u klasične bitove $c_0, c_1$. Kubit $3$ (žica $q_2$) ostaje nemeren i time u superpoziciji. Kolo je **recept**, a ne rezultat: opisuje operaciju koja *može* dati četiri ishoda, ali svaki put kad ga pokrenemo dobijemo **tačno jedan** od njih.
```

Isto kolo napravimo i nacrtamo u Qiskit-u. Kubite čitamo odozgo naniže kao kubit $1, 2, 3$ (tj. $q_0, q_1, q_2$). Blok pripreme je ovde tek „rezervisano mesto" (placeholder) za proizvoljno stanje $\ket{\Psi}$ — u praksi bi tu stajao konkretan niz kapija:

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Gate

q = QuantumRegister(3, "q")     # q0=kubit 1, q1=kubit 2, q2=kubit 3
c = ClassicalRegister(2, "c")   # dva klasična bita za dva ishoda
qc = QuantumCircuit(q, c)

# priprema proizvoljnog stanja |Psi> (placeholder blok preko sva tri kubita)
qc.append(Gate(name=r"$|\Psi\rangle$", num_qubits=3, params=[]), [q[0], q[1], q[2]])
qc.barrier()

qc.measure(q[0], c[0])          # izmeri kubit 1 -> bit c0
qc.measure(q[1], c[1])          # izmeri kubit 2 -> bit c1
# kubit 3 (q2) NE merimo -> ostaje u superpoziciji

qc.draw("mpl")
```

## Jedan pokret kola: jedan ishod, jedno stanje trećeg kubita

Ovo je mesto gde je lako pogrešno zamisliti šta se dešava. **Ne** dešavaju se sva četiri ishoda odjednom. Svaki put kada kolo zaista pokrenemo (jedan „pokret", engl. *run* ili *shot*), dva simbola merenja vrate **tačno jedan** par bitova $(b_1, b_2)$. I baš taj jedan ishod trenutno fiksira stanje trećeg kubita — potpuno u skladu sa tvojom intuicijom.

Uzmimo konkretno taj slučaj koji si i sam izdvojio. Ako u nekom pokretu izmerimo **$0$ na kubitu $1$ i $0$ na kubitu $2$**, onda je, po faktorisanom obliku {eq}`eq:ex3-post`, ceo registar posle tog pokreta

```{math}
:label: eq:jedan-run-00
\ket{\Psi'_{\{0_1, 0_2\}}} = \underbrace{\ket{0}_1 \ket{0}_2}_{\text{fiksirano ishodom}} \otimes \underbrace{\frac{a_0\ket{0} + a_1\ket{1}}{\sqrt{|a_0|^2 + |a_1|^2}}}_{\text{stanje kubita }3}.
```

Prva dva kubita su sada čvrsto $\ket{0}$; **sva** preostala superpozicija je „sabijena" u treći kubit. Grafički, registar posle tog jednog pokreta izgleda ovako (žice počinju od $\ket{0}$; blok $R_3$ znači da kubit $3$ nosi rezidualnu superpoziciju $\tfrac{a_0\ket{0}+a_1\ket{1}}{\sqrt{|a_0|^2+|a_1|^2}}$):

```{figure} ../images/kolo-merenje-jedan-run.png
:label: fig:kolo-merenje-jedan-run
:alt: Registar od tri kubita posle jednog pokreta sa ishodom 0,0: prva dva kubita su u stanju |0>, treci kubit nosi rezidualnu superpoziciju.
:width: 320px
:align: center

Stanje registra posle **jednog** pokreta kod kog je ishod bio $\{0_1, 0_2\}$. Kubiti $1$ i $2$ su kolabirali u $\ket{0}$, a kubit $3$ nosi rezidualnu superpoziciju $R_3\ket{0} = (a_0\ket{0}+a_1\ket{1})/\sqrt{|a_0|^2+|a_1|^2}$. To je jedan jedini, određen ishod — ne sva četiri.
```

**A ostali ishodi?** Drugi pokret istog kola može dati drugačiji par $(b_1, b_2)$, i tada bi treći kubit završio u drugom stanju. Sve mogućnosti staju u jednu tabelu — ali obavezno je čitaj ovako: *u jednom pokretu ostvari se tačno jedan red*, a koji, odlučuje slučaj (Bornovo pravilo):

| ishod $(b_1, b_2)$ | verovatnoća $p(b_1, b_2)$ | stanje kubita $3$ posle **tog** pokreta |
|:--:|:--:|:--:|
| $\{0_1, 0_2\}$ | $\lvert a_0\rvert^2 + \lvert a_1\rvert^2$ | $\dfrac{a_0\ket{0} + a_1\ket{1}}{\sqrt{\lvert a_0\rvert^2 + \lvert a_1\rvert^2}}$ |
| $\{0_1, 1_2\}$ | $\lvert a_2\rvert^2 + \lvert a_3\rvert^2$ | $\dfrac{a_2\ket{0} + a_3\ket{1}}{\sqrt{\lvert a_2\rvert^2 + \lvert a_3\rvert^2}}$ |
| $\{1_1, 0_2\}$ | $\lvert a_4\rvert^2 + \lvert a_5\rvert^2$ | $\dfrac{a_4\ket{0} + a_5\ket{1}}{\sqrt{\lvert a_4\rvert^2 + \lvert a_5\rvert^2}}$ |
| $\{1_1, 1_2\}$ | $\lvert a_6\rvert^2 + \lvert a_7\rvert^2$ | $\dfrac{a_6\ket{0} + a_7\ket{1}}{\sqrt{\lvert a_6\rvert^2 + \lvert a_7\rvert^2}}$ |

Zbir sve četiri verovatnoće je tačno $1$ (relacija potpunosti $\sum_{b_1, b_2} \Pi_{\{b_1, b_2\}} = I$) — što i mora, jer se u svakom pokretu ostvari jedan i samo jedan red.

### Isprobajmo „pokret po pokret" (numerički)

Da se ova slika učvrsti, uzmimo konkretno (slučajno, normirano) stanje $\ket{\Psi}$ i **simulirajmo pojedinačne pokrete**. Koristimo konvenciju $\ket{b_1 b_2 b_3}$, gde je indeks amplitude $i = 4b_1 + 2b_2 + b_3$, pa ishod $(b_1, b_2)$ zadržava baš amplitude sa indeksima $\text{baza}$ i $\text{baza}+1$, uz $\text{baza} = 4b_1 + 2b_2$:

```python
import numpy as np

# konkretno (slučajno) normirano stanje 3 kubita: a[i] = amplituda uz |i>, i = b1 b2 b3
rng = np.random.default_rng(7)
a = rng.normal(size=8) + 1j*rng.normal(size=8)
a /= np.linalg.norm(a)

def ishodi(a):
    """Za SVAKI mogući ishod (b1,b2): njegova verovatnoća i rezidualno stanje kubita 3."""
    tab = {}
    for b1 in (0, 1):
        for b2 in (0, 1):
            baza = 4*b1 + 2*b2                       # preživeli indeksi: baza, baza+1
            p = np.sum(np.abs(a[[baza, baza + 1]])**2)
            psi3 = a[[baza, baza + 1]] / np.sqrt(p)  # (a_baza|0> + a_baza+1|1>)/sqrt(p)
            tab[(b1, b2)] = (p, psi3)
    return tab

# ovo je tabela odozgo — SVE mogućnosti, ne jedan pokret:
for (b1, b2), (p, psi3) in ishodi(a).items():
    print(f"{{ {b1}_1, {b2}_2 }}:  p = {p:.4f}   kubit 3 -> {np.round(psi3, 3)}")
```

Sada napravimo **jedan pokret**: slučajno izaberemo ishod po njegovoj verovatnoći, i vratimo pripadno (jedno!) stanje trećeg kubita:

```python
def jedan_pokret(a, rng):
    tab = ishodi(a)
    ishod_lista = list(tab.keys())
    verovatnoce = [tab[k][0] for k in ishod_lista]
    k = rng.choice(len(ishod_lista), p=verovatnoce)   # <-- slučajnost JEDNOG pokreta
    b1, b2 = ishod_lista[k]
    p, psi3 = tab[(b1, b2)]
    return (b1, b2), psi3

print("pet nezavisnih pokreta istog kola:")
for _ in range(5):
    (b1, b2), psi3 = jedan_pokret(a, rng)
    print(f"  ishod = ({b1},{b2})  ->  kubit 3 = {np.round(psi3, 3)}")
```

Svaki red ispisa je jedan pokret: dobijemo **jedan** par $(b_1, b_2)$ i **jedno** stanje trećeg kubita. Različiti pokreti daju različite ishode — a tek kada pokret ponovimo mnogo puta, učestanosti ishoda teže verovatnoćama $p(b_1, b_2)$ iz tabele.

:::{note} Qiskit i redosled kubita (klik)
:class: dropdown
Ako isto proveravamo Qiskit-ovim `Statevector.measure` (koji upravo i vrati jedan slučajan ishod i pripadno kolabirano stanje), treba imati na umu da Qiskit numeriše kubite **obrnuto** (little-endian): kubit $q_0$ je *krajnje desni* bit izlazne niske, pa se niska `'b_{q_1} b_{q_0}'` čita unatrag u odnosu na našu konvenciju $\ket{b_1 b_2 b_3}$. Da bismo isto stanje $a[i]$ preneli u Qiskit, amplitudu sa indeksa $i = b_1 b_2 b_3$ smeštamo na Qiskit-ov indeks $b_3 b_2 b_1$ (obrnuti bitovi). Zbog tog zamešateljstva gore smo, kao i u lekciji o teleportaciji, ostali na `numpy`-ju gde redosled sami držimo pod kontrolom.
:::

:::{important} Šta pamtimo iz ove lekcije
:class: simple
Kolo koje meri kubit $1$ i kubit $2$ crtamo kao dva simbola merenja koji upisuju ishode u klasični registar; **nemereni kubit $3$ zadrži svoju žicu** i ostaje u superpoziciji. To jedno kolo je *recept* sa četiri moguća ishoda — ali u **jednom pokretu** ostvari se tačno jedan. Taj jedan ishod $(b_1, b_2)$ trenutno fiksira i stanje trećeg kubita: registar postaje $\ket{b_1}_1\ket{b_2}_2 \otimes \ket{\varphi_3}$, gde $\ket{\varphi_3}$ nosi celu preostalu superpoziciju (npr. za ishod $\{0_1,0_2\}$ to je $(a_0\ket{0}+a_1\ket{1})/\sqrt{|a_0|^2+|a_1|^2}$). Koji ishod će pasti odlučuje slučaj, sa verovatnoćom jednakom zbiru $|a_{\mathbf{x}}|^2$ preživelih amplituda; ponavljanjem mnogo pokreta učestanosti teže tim verovatnoćama.
:::

