---
title: "Višekubitna stanja"
short_title: "Višekubitna stanja"
description: Merenje i kolaps višekjubitnog registra — Bornovo pravilo preko projektora, sa primerima.
---




# Zašto samo jedan kubit do sada?
Videli smo do sada šta sve jedan kubit podrazumeva. Na jednom kubitu gradimo intuiciju i tehničke alate koji su na potrebni kasnije u slučaju višekubita. Treba napomenuti da neki od intuitivnih stvari poput Blohove sfere ne može da se iskoristi u sistemima višekubita. 

Ono gde zapravo kvantni računari su od koristi jeste slučaj kad ih je više i kad oni mogu da deluju jedan na drugog i podležu kvantnim kapijama ne-lokalnog dejstvar (dva, tri i itd kvantne kapije). Svi kvantni algoritmi uključuju više od jednog kubita. 



Treba isto navesti nedavni primer korisnosti jednog kubit sistema u procesuiranju klasičnih signala:
- https://ishaan-kannan.github.io/blog/2026/08/17/bringing-quantum-advantage-to-todays-classical-world/
- sa pratećim radom na https://arxiv.org/pdf/2608.13521

Što govori da već ovo što smo do sad obradili može biti osnova naučnog delovanja u odgovarajućem kontekstu. 



## Višekubitna računska baza

Registar od $N$ kubita živi u prostoru dimenzije $2^N$, sa računskom bazom 

```{math}
:label: eq:mq-def
\ket{\Psi} = \ket{b_1} \otimes \ket{b_2} \otimes \ket{b_1} \otimes \cdots \otimes \ket{b_N} \equiv  \ket{b_1 b_2 \cdots b_N} , \quad b_i \in \{0,1\}. 
```
Gde koristimo operaciju tenzorskog proizvod $\otimes$. Šta precizno tenzorski proizvod između dva vektora ili dve matrice čini možemo videti kroz račun ispod. 


:::{note} Prikaži račun (klik)
:class: dropdown

```{figure} ../images/zoperator.png
:label: fig:zoperator
:alt: purity
:width: 520px
:align: center

```
:::

Koristeći Python takvu operaciju možemo koristiti na sledeći način:

```python
import numpy as np

# Primer 1: tenzorski proizvod vektora |0> i |1>
ket0 = np.array([1, 0])
ket1 = np.array([0, 1])
vektor = np.kron(ket0, ket1)
print("|0> ⊗ |1> =", vektor)          # [0 1 0 0]
print("oblik vektora:", vektor.shape)  # (4,)

# Primer 2: tenzorski proizvod dve matrice
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
matrica = np.kron(X, Z)
print("X ⊗ Z =\n", matrica)
print("oblik matrice:", matrica.shape)  # (4, 4)
```



### Koliko memorije treba za $N$ kubita?

Iz gornjih primera vidimo ključnu osobinu tenzorskog proizvoda: on **množi**, a ne sabira dimenzije. Jedan kubit živi u prostoru dimenzije $2$; kad dodamo još jedan, dimenzija ne postaje $2+2=4$ nego $2\times 2 = 4$. Svaki novi kubit **udvostručuje** broj koeficijenata (amplituda) koje moramo da pamtimo, pa broj brojeva raste kao

```{math}
:label: eq:mem-scaling
\underbrace{2\times 2 \times \cdots \times 2}_{N \text{ puta}} = 2^{N}.
```

Odatle sledi da za registar od $N$ kubita treba:

- **vektor stanja** sa $2^{N}$ kompleksnih amplituda (jedan broj po baznom stanju), i
- **operator/matricu** (npr. kvantnu kapiju na svih $N$ kubita) sa $2^{N}\times 2^{N} = 4^{N}$ kompleksnih elemenata.

Dodavanje **jednog** kubita udvostručuje dužinu vektora, a **učetvorostručuje** broj elemenata matrice. To je suština „eksponencijalnog zida": pomak od $N$ do $N+10$ kubita znači $2^{10}\approx 1000$ puta veći vektor i $4^{10}\approx 10^6$ puta veću matricu.

U numeričkim simulacijama kompleksnu amplitudu čuvamo kao par realnih brojeva (realni i imaginarni deo):

- **jednostruka preciznost** (dva `float32`): $2\times 4 = 8$ bajtova po amplitudi,
- **dvostruka preciznost** (dva `float64`): $2\times 8 = 16$ bajtova po amplitudi.

Potrebna memorija je onda prosto broj elemenata puta broj bajtova po elementu:

```{math}
:label: eq:mem-formula
M_{\text{vektor}} = 2^{N}\cdot b, \qquad M_{\text{matrica}} = 4^{N}\cdot b, \qquad b \in \{8,\ 16\}\ \text{bajtova}.
```

Sledeća tabela daje memoriju potrebnu za čuvanje **jednog vektora stanja** od $N$ kubita (koristimo binarne jedinice: $1\,\text{KiB}=1024$ B, $1\,\text{MiB}=1024$ KiB, itd.):

| $N$ (kubita) | dimenzija $2^N$ | vektor, `complex64` (8 B) | vektor, `complex128` (16 B) |
|---:|---:|---:|---:|
| 1  | 2                 | 16 B    | 32 B    |
| 10 | 1 024             | 8 KiB   | 16 KiB  |
| 20 | ~$10^6$           | 8 MiB   | 16 MiB  |
| 26 | ~$6.7\times10^7$  | 512 MiB | 1 GiB   |
| 30 | ~$10^9$           | 8 GiB   | 16 GiB  |
| 34 | ~$1.7\times10^{10}$ | 128 GiB | 256 GiB |
| 40 | ~$10^{12}$        | 8 TiB   | 16 TiB  |
| 45 | ~$3.5\times10^{13}$ | 256 TiB | 512 TiB |
| 50 | ~$10^{15}$        | 8 PiB   | 16 PiB  |

Za **matricu** ($2^N\times 2^N$ elemenata) je slika još drastičnija — ona „potroši" istu memoriju kao vektor sa **dvostruko više** kubita, jer $4^N = 2^{2N}$:

| $N$ (kubita) | elemenata $4^N$ | matrica, `complex64` (8 B) | matrica, `complex128` (16 B) |
|---:|---:|---:|---:|
| 1  | 4                 | 32 B   | 64 B   |
| 5  | 1 024             | 8 KiB  | 16 KiB |
| 10 | ~$10^6$           | 8 MiB  | 16 MiB |
| 15 | ~$10^9$           | 8 GiB  | 16 GiB |
| 20 | ~$10^{12}$        | 8 TiB  | 16 TiB |
| 25 | ~$10^{15}$        | 8 PiB  | 16 PiB |
| 30 | ~$10^{18}$        | 8 EiB  | 16 EiB |

Nekoliko orijentira da brojevi dobiju smisao:
- tipičan laptop sa $16\,\text{GiB}$ RAM-a u dvostrukoj preciznosti staje do otprilike $N \approx 30$ kubita za **sam vektor stanja** (a u praksi manje, jer i sistem i međurezultati troše memoriju),
- već oko $N \approx 45$–$50$ kubita ulazimo u domen najjačih svetskih superračunara, gde vektor meri stotine terabajta do petabajta. 
- kod $N = 300$ kubita broj amplituda $2^{300}$ premašuje procenjeni broj atoma u vidljivom svemiru, tj. takvo stanje je nemoguće ispisati, a kamoli sačuvati, ni na jednom klasičnom računaru





:::{important} Suština! 
:class: simple
**Klasična simulacija kvantnog registra je eksponencijalno skupa po memoriju.** 

Upravo tu leži razlika prema pravom kvantnom računaru, tj. on stanje od $2^N$ amplituda ne „skladišti" u memoriji, već ga fizički nosi $N$ kubita, pa dodavanje kubita ne udvostručuje potrošnju resursa.
:::
 

Opšte stanje je superpozicija svih $2^N$ baznih stanja,

```{math}
:label: eq:mq-stanje
\ket{\Psi} = \sum_{\mathbf{x}} a_{\mathbf{x}} \ket{\mathbf{x}}, \qquad {\rm normalizacija} \rightarrow \qquad \sum_{\mathbf{x}} |a_{\mathbf{x}}|^2 = 1,
```

gde $\mathbf{x} = b_1 b_2 \cdots b_N$ prolazi kroz svih $2^N$ mogućih binarnih bitova sastavljenih od $0$ i $1$. 

Eksplicitno:
- $N = 2$
```{math}
:label: eq:n2
\ket{\Psi} = b_1 \ket{00} + b_2 \ket{01} + b_3 \ket{10} + b_4 \ket{11}. 
```

- $N = 3$

```{math}
:label: eq:ex-stanje
\ket{\Psi} = b_1\ket{000} + b_2\ket{001} + b_3\ket{010} + b_4\ket{011} + b_5\ket{100} + b_6\ket{101} + b_7\ket{110} + b_8\ket{111},
```
