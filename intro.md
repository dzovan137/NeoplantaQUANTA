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

Dobrodošli na interaktivni kurs **Kvantne informatike**. Kurs je osmišljen da približi osnovne ideje savremenog polja
kvantne informatike. Uvešćemo ključne pojmove kao što su: kjubit, superpozicija, merenje i spletenost. Poseban naglasak
stavljamo na praktične vežbe u programskom okruženju Python, kroz Jupyter notebook, koji zahvaljujući svojoj fleksibilnosti
ima veoma važnu ulogu u savremenoj fizici i informatici.


:::{note} Kako koristiti ovu stranicu? <span style="font-size: 1.45em;">📘💻</span>
:class: simple
Ova stranica je zamišljena kao vodič za učenje <span style="font-size: 1.35em;">📘</span>, dok se kod izvršava u vašem **Jupyter notebook-u** <span style="font-size: 1.35em;">💻</span>.  

Kako da radite:
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
- jednostavno deljenje rada sa kolegama i nastavnicima putem linka,

**Nužno je potrebno imati gmail email nalog!** 

:::


## Potrebno predznanje

- Osnove linearne algebre, 
- LaTeX ispisivanje formula (ukoliko želite da upotpunite Jupiter notebook beleške),
- osnove programskog jezika Python. 



## Šta ćeš naučiti? 

:::{admonition} Tvoj put kroz kurs
:class: tip outcomes-hero
Od teorije do prakse: svaki korak povezuje matematičku intuiciju, Python kod i rad na pravom kvantnom uređaju.
:::

::::{grid} 1 1 2 2

:::{card} 🔹 Osnove stanja kjubita
- matematički zapišeš i protumačiš stanje jednog kjubita,
- vizuelizuješ stanje kjubita na Blohovoj sferi.
:::

:::{card} 🔹 Kvantna notacija i merenje
- koristiš Dirakovu bra-ket notaciju u osnovnim primerima,
- izračunaš verovatnoće merenja
:::

:::{card} 🔹 Python i Qiskit praksa
- pratiš svaki korak računa kroz Python kod i proveriš rezultat,
- koristiš Qiskit za kreiranje i pokretanje jednostavnih kvantnih kola.
:::

:::{card} 🔹 Rad na stvarnom hardveru
- pokreneš osnovne primere na stvarnom kvantnom računaru na daljinu.
:::

::::



## Praktični detalji
- 3 x 45 min + 2 x 15 pauze
- nije opšti kurs iz kvatne informatike, nego osnove koje se mogu nadograditi u budućnosti



## Neke potrebne matematičke osnove


Šta mislim pod linearnim? U najjednostavnijem smislu ukoliko imamo funkciju $f(a \vec{x} + b \vec{y}) = a f(\vec{x}) + b f(\vec{y})$ gde x i y mogu biti bilo koji od sledećih matematičkih objekata


```{figure} /images/DifferentMathObjects.png
:label: fig:DifferentMathObjects
:alt: razlici matematicki objekti
:width: 620px
:align: center

Različiti tipovi matematičkih funkcija i njihova dijagramatička reprezentacija. 
```

Tenzori igraju veoma važnu ulogu u kvantnoj informatici ali i u ostalim poljima fizike, ali u ovom kursu nećemo ulaziti u detalje ove reprezentacije i zašto je bitna. 
Dok će prve tri konstrukcije biti korišćene. Kvantnu mehaniku nazivaju i matričnom mehanikom koju je Heisenberg prvi formulisao [citat iz Panticeve knjige]
