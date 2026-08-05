---
title: "Lekcija 0 — Uvod u kvantno računarstvo"
short_title: Uvod
description: Motivacija i cilj. 
---



:::{admonition} Motivacija
:class: note

Rešiti probleme čija vrednost nadilazi cenu resursa koje smo uložili. 
:::

Primer problema: simulacije novih jedinjenja i hemijskih procesa košta milion eura ili hiljadu eura je velika razlika, što je potrebno koristiti modalitete računice koji će nam omogućiti tu uštedu. 


::::{admonition} Veličina problema i vreme potrebno za njegovo rešavanje 
:class: note

:::{figure} ../images/MatTroyer.png
:alt: Matthias Troyer
:width: 450px
:align: center

Matthias Troyer [Simons Institute for the Theory of Computing - Berkeley 24.07.2026](https://www.youtube.com/live/5uDPnvgElY8?si=MIjdGMEkVzj-8zQO).
:::

::::


::::{admonition} Klase problema i teorijski aspekti kompleksnosti
:class: note

```{figure} ../images/ProblemClassesQC.png
:alt: Problem Classes Quantum Computing
:width: 450px
:align: center

Olivia Lanes [Quantum computing in practice - IBM](https://quantum.cloud.ibm.com/learning/en/courses/quantum-computing-in-practice/applications-of-qc).

Example of a problem that fall into the BQP class: https://www.pnas.org/doi/full/10.1073/pnas.2006103117
and https://arxiv.org/pdf/2603.15608
```
::::

HERE WE NEED TO PUT THE RELEVANT REFERENCES:
- SCOTT AARONSON LECTURE NOTES
- Nielsen and Chuang


Ovaj kurs neće ulaziti u kategorizaciju problem i teorijske aspekte nego pokušati približiti celo polje putem praktičnih vežbi i rada. 
Videćemo konkretno trenutak u kome kvantni računari zapravo trebali bi da budu od pomoći u simulacijama kvantih sistema i probblem (a ne Shor/ov algoritam ili Grover). 
Kroz minimalne primere i račun pokušaćemo približiti 

Recimo najnovija interacija Solvay konferencije: https://www.jovanodavic.com/post/solvay2022/
Gde vidimo da kvanti računari bi trebali da igraju jednu od ključnih uloga u napredku fizike 21 veka. 


Ovde bi sad mogao da ubacim sta je pocetak, sta je kraj celog kursa. 

Zatim mi mogao da objasnim kako i sta su kvatna kola. 

Fali mi ovde one slike od Mattijasa Troyer gde pokazuje gde smo trenutno. Tipa da smo negde između prvog i drugog nivoa. TechnologicalDevelopment.png and SOTA.png

Treba da ubacim i sliku kvantnog računara iz Napulja i kako ja dodirujem taj računar. 

Mislim da bi mogli da radimo Bell ineqality konkretno da bi onda posle toga napravili referencu za knjigu 'hypster guide to quantum computing'. 

Verovatno bi mogli da se bavimo kvantnom teleportacijom, derivacija i da napravimo circuit koji ce to da raunije. 

https://spectrum.ieee.org/ibm-verifiable-quantum-advantage

Quantum information theory builds on Shannon's foundations [@shannon1948], with the
modern reference being Nielsen & Chuang [@nielsen2010]. The no-cloning theorem is due to
Wootters and Zurek [@wootters1982].[^history]

[^history]: Footnotes are great for asides that would interrupt the flow.
