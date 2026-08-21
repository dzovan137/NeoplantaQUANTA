---
title: O ovom kursu
description: Dobrodošli!
---

# Dobrodošli!  👋

```{figure} images/dva.jpg
:alt: Uvodna slika za kurs kvantne informatike
:width: 88%
:align: center

Izvor slike: [QTLab — ICSC QC1 Quantum Computing Center](https://www.qtlab.unina.it/labs/icsc-qc1-quantum-computing-ccenter/)
Na slici: Carlo Cosenza, Univerzitet u Napulju Federico II.
```

Dobrodošli na interaktivni kurs **Uvod u kvantnu informatiku**. Kurs je osmišljen sa ciljem da približi osnovne ideje savremenog polja
kvantne informatike. Kroz kurs uvešćemo i definisaćemo neke od ključnih pojmova kao što su: 
- kubit,
- kvantna superpozicija,
- kvantno merenje,
- spletenost,
- itd ...

U ovom kursu poseban naglasak stavljamo na <u>praktične vežbe u programskom okruženju Python</u>, kroz Jupyter notebook, koji zahvaljujući svojoj fleksibilnosti
i jednostavnosti igra veoma važnu ulogu u savremenoj fizici i računarstvu. 


 Kurs je hostovan na adresi: https://github.com/dzovan137/NeoplantaQUANTA ,gde je moguće direktno pristupi sadržaju koji će sa svakim poglabvljem se širiti. 


:::{note} Kako koristiti ovu stranicu? <span style="font-size: 1.45em;">📘💻</span>
:class: simple
Ova stranica je zamišljena kao vodič za učenje, dok se kod izvršava u vašem **Jupyter notebook-u**.  

Princip rada:
- predstavljanje osnovnih teorijskih aspekata,
- praktični rad kroz primere.

U okviru Jupiter notebook obruženja na vama je da:
- kopirajte svaki primer koda sa stranice u svoj notebook,
- pokrenite kod i proverite rezultat,
- dodajte sopstvene beleške i male izmene kako biste bolje razumeli šta se dešava.

Kodovi se ne izvršavaju direktno na ovoj stranici, jer je cilj da ih prolazite korak po korak,
razumete svaku liniju i usput usvajate osnove programiranja u Python-u.  
:::

:::{note} Google Colab  
:class: simple

```{image} images/google-colab.png
:alt: Google Colab ikonica
:width: 56px
```

Ako želite da radite u Jupyter okruženju bez lokalne instalacije i dodatnog podešavanja, preporuka je da koristite **Google Colab**. Otvorite platformu ovde: [Google Colab](https://colab.research.google.com), napravite novi notebook i direktno pokrenite kodove iz lekcija.



Prednosti korišćenja Google Colab-a:
- nije potrebna instalacija Python-a i dodatnih paketa na vašem računaru,
- notebook možete otvoriti sa bilo kog uređaja koji ima internet,
- jednostavno deljenje rada sa kolegama putem linka.

**Nužno je potrebno imati gmail email nalog!** 


Takođe koristo je prebaciti ⚙️ Settings/Editor/Editor Colorization --> **GitHub** gde se podudara sa bojama i stilom koda u lekcijama.
:::


## Potrebno predznanje

- osnove programskog jezika Python,  
- osnove linearne algebre (vektori, matrice, ...), 
- LaTeX ispisivanje formula (ukoliko želite da upotpunite Jupiter notebook beleške).




## Šta ćeš naučiti? 

:::{admonition} Tvoj put kroz kurs
:class: tip outcomes-hero

```{figure} /images/progress-start.png
:label: fig:mapa
:alt: mapa
:width: 420px
:align: center

Od teorije do eksperimentalne prakse. Sa svakim korakom se približavamo cilju a to je da pustite svoj prvi izračun na kvantnom računaru. 

<u>Sa svakom lekcijom bliže smo direktnom radu sa pravim kvantnim računarem! </u>
```


:::


## Cilj ovog kursa jeste da spoznaš i razumeš

::::{grid} 1 1 2 2

:::{card} 🔹 Kvantno stanja kubita
- matematički zapišeš i protumačiš stanje jednog kjubita,
- vizuelizuješ stanje kjubita na Blohovoj sferi.
:::

:::{card} 🔹 Kvantna notacija i merenje
- koristiš Dirakovu bra-ket notaciju u osnovnim primerima,
- izračunaš verovatnoće merenja
:::

:::{card} 🔹 Python i Qiskit praksa
- pratiš svaki korak računa kroz Python kod i proveriš rezultat,
- koristiš QisKit* za kreiranje i pokretanje jednostavnih kvantnih kola.

*programski paket za programiranje superprovodnih kvantnih računara
:::

:::{card} 🔹 Rad na stvarnom kvantnom hardveru
- pokreneš osnovne primere na stvarnom kvantnom računaru na daljinu.
:::


::::


## Osnovni matematički objekti




Linearna algebra sa matematičkim objektima poput vektora i matrica i pridruženim operacijama predstavlja nužni matematički okvir za kvantnu mehaniku. Sami objekti nad kojima pravila linearne algebre su zastupljenja  (i koji se pojavljuju u kvantnoj teoriji) prikazani su na slici [](#fig:DifferentMathObjects), poređani po složenosti.


```{figure} /images/DifferentMathObjects.png
:label: fig:DifferentMathObjects
:alt: Skalar, vektor, matrica i tenzor kao tenzori ranga 0, 1, 2 i 3
:width: 620px
:align: center

Skalar, vektor, matrica i tenzor, iliti tenzori **ranga** (reda) $0$, $1$, $2$ i $3$ koji zajedno sa svojom dijagramatičkom reprezentacijom. Broj „nogu“ (spoljašnjih linija) koje izlaze iz svakog objekta jednak je broju indeksa potrebnih da se imenuje jedan njegov element; taj broj upravo i jeste rang. Za ovaj kurs dovoljna su prva tri objekta (skalar, vektor i matrica), dok tenzori višeg ranga pripadaju naprednijem nivou.
```

Pogledajmo ih redom, onako kako su označeni na slici:

- **Skalar** ($A$): običan broj, tenzor **ranga 0**. Nema nijedan indeks (nijednu „nogu“), jer je potpuno određen jednom jedinom vrednošću. Kod nas će skalari najčešće biti kompleksne amplitude i verovatnoće merenja.
- **Vektor** ($B$): uređena kolona brojeva $B_i$, tenzor **ranga 1**. Potreban je **jedan** indeks $i$ da bismo izdvojili pojedinačni element. Stanje jednog kubita upravo ćemo zapisivati kao vektor.
- **Matrica** ($C$): pravougaona tablica brojeva $C_{ij}$, tenzor **ranga 2**. Potrebna su **dva** indeksa: $i$ (red) i $j$ (kolona). Kvantne kapije, tj. operacije nad kubitima, jesu matrice.
- **Tenzor** ($D$): uopštenje sa **tri** ili više indeksa, $D_{ijk}$, tenzor **ranga 3** (i višeg). Tenzori se prirodno pojavljuju kada više kubita spajamo u jedan sistem.

Tenzori igraju veoma važnu ulogu u kvantnoj informatici, kao i u drugim oblastima fizike, ali u ovom kursu nećemo ulaziti u detalje njihove reprezentacije i zašto je bitna. Koristićemo prve tri konstrukcije — skalare, vektore i matrice. Uostalom, nije slučajno što se kvantna mehanika naziva i **matričnom mehanikom**: njenu prvu potpunu formulaciju dao je Heisenberg 1925. godine (a nedugo zatim razvijena je i u saradnji sa Bornom i Jordanom).

% TODO: dodati referencu za matričnu mehaniku — Pantić, <naslov knjige>


## Praktični detalji
- 3 x 45 min + 2 x 15 pauze
- online and offline
- možete postavljati pitanja u svakom trenutku
- ukoliko vam kod u Python-u ne funkcioniše, slobodno prijavite
- ovaj vebsajt će biti nadopunjen sa svakom novom lekcijom



:::{note} Mala napomena
:class: simple
Ovaj kurs je napravljen kao uvod koji bi trebao da predstavlja osnove a ne kao kompletan pregled celog polja. 
:::



