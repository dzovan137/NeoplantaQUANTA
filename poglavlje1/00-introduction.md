---
title: "Zašto kvantni računari?"
short_title: Zašto kvantni računari?
description: Motivacija — kada i zašto nam kvantni računari zaista donose korist.
---

:::{margin}
![Napredak kursa: korak 1 od 8 — put ka pravom kvantnom računaru](../images/progress/progress-00.svg)
:::

Pre nego što se upustimo u kubite, kvantne kapije i kola, vredi zastati na jednom naizgled prostom pitanju: **zašto uopšte graditi kvantne računare?**

 
Odgovor nije „zato što su brži“!


Za veliku većinu svakodnevnih zadataka oni to nisu, niti će biti. Već zato što postoji uska, ali izuzetno <u>vredna klasa problema</u> za koje verujemo da ih klasični računari nikada neće rešavati efikasno.




:::{admonition} Motivacija
:class: note

Kvantni računar vredi graditi onda kada nam omogućava da rešimo problem čija vrednost nadilazi cenu resursa koje u njega uložimo.
:::

## Vrednost mora da nadmaši cenu

Ključna reč je **korist**. Kvantni računar je skup i osetljiv uređaj, pa ćemo ga upotrebiti samo tamo gde nam donosi nešto što drugačije ne bismo mogli, ili ne bismo mogli dovoljno brzo i dovoljno jeftino.

Najdirektniji primer (makar za fizičare i hemičare) takve koristi jeste **simulacija materije ili dinamičkih procesa na kvantnom nivou**: predviđanje ponašanja novih molekula, katalizatora, lekova i materijala. 

U praksi razlika ume da bude dramatična: simulacija koja bi na <u>klasičnom superračunaru koštala milione evra i trajala mesecima</u> mogla bi na odgovarajućem kvantnom računaru da se svede na <u>hiljade evra i nekoliko sati</u>!


Upravo tu gde ušteda u vremenu i novcu opravdava uloženo leži prava motivacija za kvantno računarstvo.

## Šta znači „praktična“ kvantna prednost

Nije, međutim, dovoljno da kvantni računar bude tek *asimptotski* brži. Da bi prednost bila stvarna, ona mora da nastupi za probleme realne veličine i unutar razumnog vremena: reda dana ili nedelja, a ne vekova.

```{figure} ../images/MatTroyer.png
:label: fig:troyer
:alt: Vreme rešavanja u zavisnosti od veličine problema za klasične i kvantne računare
:width: 560px
:align: center

Praktična kvantna prednost: vreme rešavanja u zavisnosti od veličine problema $N$, za klasične (plava kriva) i kvantne (tamna linija) računare. Cilj je da „tačka preseka“, od koje kvantni računar postaje isplativiji, nastupi u roku od nekoliko nedelja. Izvor: Matthias Troyer, [Simons Institute for the Theory of Computing — Berkeley, 24.07.2026.](https://www.youtube.com/live/5uDPnvgElY8?si=MIjdGMEkVzj-8zQO)

Interesantna stvar o kojoj se priča u ovom predavanju jeste činjenica da kvantni računari trebaju da pomognu u rešavanju problema za koji neki praktični dataset ne postoji i samim tim kvantnih računari bi bili generatori vrednih i veoma teško realizujićih seta podataka. Zatim koristeći izlaze računa sa kvantog računara ti podaci bi se koristili kao 'trening podaci' za mašinsko učenje koje bi trebalo da efikasnije i jeftinije rešenje nego kvantni računari. 

```

[](#fig:troyer) tu ideju prikazuje slikovito. Vreme potrebno za rešavanje raste sa veličinom problema $N$: kod klasičnog računara ono raste eksponencijalno (strma plava kriva), dok kod kvantnog raste znatno blaže (tamna linija). Tačka u kojoj se dve krive seku jeste trenutak od kojeg kvantni računar postaje isplativiji; cilj nije samo da ta tačka *postoji*, već da nastupi dovoljno rano i da odgovarajuće „vreme preseka“ (engl. *crossover time*) bude reda nekoliko nedelja, a ne astronomsko. Tek tada govorimo o *praktičnoj*, a ne samo teorijskoj kvantnoj prednosti.

Vredi imati na umu i da se trenutno nalazimo u tzv. NISQ eri (engl. *Noisy Intermediate-Scale Quantum*), tj. dobu uređaja srednje veličine i kojima je prisutan šum, u kojem tu tačku preseka tek pomeramo ka sve korisnijim problemima [@Preskill_2018].

## Gde leži kvantna prednost: klase problema

Prirodno se nameće pitanje: koje probleme kvantni računar zapravo može da ubrza? Odgovor nije tako jednostavan kao što što se često pretpostavlja. Teorija kompleksnosti probleme razvrstava u **klase** prema resursima (vremenu i memoriji) koji su potrebni za njihovo rešavanje.

```{figure} ../images/ProblemClassesQC.png
:label: fig:bqp
:alt: Odnos klasa problema P, NP, NP-kompletnih, PSPACE i BQP
:width: 480px
:align: center

Klase problema i mesto koje među njima zauzima **BQP** (bounded-error quantum polynomial time) skup problema koje kvantni računar rešava efikasno u odnosu na klasi;ni. BQP obuhvata celu klasu P i deo klase NP, ali (verovatno) ne i najteže, NP-kompletne probleme. Izvor: Olivia Lanes, [Quantum computing in practice — IBM](https://quantum.cloud.ibm.com/learning/en/courses/quantum-computing-in-practice/applications-of-qc). Primeri problema iz klase BQP: [PNAS (2020)](https://www.pnas.org/doi/full/10.1073/pnas.2006103117) i [arXiv:2603.15608](https://arxiv.org/pdf/2603.15608).
```

Probleme koje kvantni računar rešava efikasno teorija svrstava u klasu **BQP** (engl. *Bounded-error Quantum Polynomial time*). Kao što slika [](#fig:bqp) pokazuje, BQP sadrži sve probleme klase **P** — one koje i klasični računar rešava lako — i deo klase **NP**, ali se veruje da **ne** obuhvata najteže, tzv. **NP-kompletne** probleme. Drugim rečima, kvantni računar *nije* čarobni uređaj koji efikasno rešava baš svaki težak problem; njegova moć je usmerena i specifična. Najuverljiviju prednost očekujemo baš tamo gde je i sama priroda problema kvantna — poput već pomenutih simulacija.

## Pejzaž kvantnih algoritama

Kroz decenije istraživanja razvijen je čitav niz **kvantnih algoritama**, koje je zgodno grupisati prema oblasti primene.

```{figure} ../images/different_algoritms.jpeg
:label: fig:algoritmi
:alt: Pregled poznatih kvantnih algoritama grupisanih po oblastima primene
:width: 520px
:align: center

Izbor poznatih **kvantnih algoritama**, grupisanih po oblasti primene: temeljni algoritmi, kriptografija, optimizacija, mašinsko učenje, simulacija i komunikacija. Ilustrativni pregled.
```

% TODO: pronaći i dodati originalni izvor slike „Key Quantum Algorithms“ (trenutno neatribuirano).

Neki od ovih algoritama postali su čuveni — Šorov (*Shor*) algoritam za faktorizaciju velikih brojeva (a time i za probijanje RSA enkripcije) ili Groverov (*Grover*) algoritam za brzu pretragu. Njih ćemo u ovom kursu tek uzgred pominjati. Naš fokus biće na grani koja je danas najbliža stvarnoj koristi — **simulaciji kvantnih sistema** — i na tome da celu priču približimo kroz konkretne, praktične primere.


## REST
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



Veoma vredan resurs: https://quantum.cloud.ibm.com/learning/en



## Fizički vs. logički kubiti

```{figure} ../images/lukin.png
:alt: Lukin
:width: 660px
:align: center

https://www.youtube.com/watch?v=hRuC89L5T9U
```

[^history]: Footnotes are great for asides that would interrupt the flow.
