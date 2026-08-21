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

Klase problema i mesto koje među njima zauzima **BQP** (bounded-error quantum polynomial time) skup problema koje kvantni računar rešava efikasno u odnosu na klasični. BQP obuhvata celu klasu P i deo klase NP, ali (verovatno) ne i najteže, NP-kompletne probleme. Izvor: Olivia Lanes, [Quantum computing in practice — IBM](https://quantum.cloud.ibm.com/learning/en/courses/quantum-computing-in-practice/applications-of-qc).


Neki primeri problema po klasama:
- P  --> sortiranje liste
- NP  --> faktorizacija celih brojeva
- NP complete --> problem putujućeg prodavca


 Primeri problema iz klase BQP i primene u fizici: [PNAS (2020)](https://www.pnas.org/doi/full/10.1073/pnas.2006103117) i [arXiv:2603.15608](https://arxiv.org/pdf/2603.15608).
```

Probleme koje kvantni računar rešava efikasno teorija svrstava u klasu **BQP** (engl. *Bounded-error Quantum Polynomial time*). Kao što slika [](#fig:bqp) pokazuje, BQP sadrži sve probleme klase **P**, one koje i klasični računar rešava lako, i deo klase **NP**, ali se veruje da **ne** obuhvata najteže, tzv. **NP-kompletne** probleme. 



:::{danger} Napomena (klik)
:class: dropdown
Drugim rečima, <u> kvantni računar *nije* čarobni uređaj koji efikasno rešava baš svaki težak problem</u>; njegova moć je usmerena i specifična. 

:::



## Pejzaž kvantnih algoritama

Kroz decenije istraživanja (počev od '90) razvijen je čitav niz **kvantnih algoritama**, koje je zgodno grupisati prema oblasti primene:

```{figure} ../images/different_algoritms.jpeg
:label: fig:algoritmi
:alt: Pregled poznatih kvantnih algoritama grupisanih po oblastima primene
:width: 520px
:align: center

Izbor poznatih **kvantnih algoritama**, grupisanih po oblasti primene: temeljni algoritmi, kriptografija, optimizacija, mašinsko učenje, simulacija i komunikacija. Ilustrativni pregled.
```


Neki od ovih algoritama postali su čuveni, npr.
- [Šorov algoritam](https://en.wikipedia.org/wiki/Shor%27s_algorithm) (eng. *Shor*) za faktorizaciju velikih brojeva (a time i za probijanje RSA enkripcije) ili
- [Groverov algoritham](https://en.wikipedia.org/wiki/Grover%27s_algorithm) (eng. *Grover*) za brzu pretragu. 

Njih ćemo u ovom kursu nećemo direktno obrađivati.

Naš fokus biće na grani koja je danas najbliža stvarnoj koristi: **simulaciji kvantnih sistema** i na tome da celu priču približimo kroz konkretne, praktične primere. 

```{figure} ../images/simulation_cost.png
:label: fig:simulation_cost
:alt: simulation cost
:width: 520px
:align: center

Jako korelisani sistemi imaju problem klasične simulacije. Spletenost (eng. "entanglement") je jedan vid korelacija .  Preuzeto iz Shaw, A.L., Chen, Z., Choi, J. *et al.* Benchmarking highly entangled states on a 60-atom analogue quantum simulator. *Nature* **628**, 71–77 (2024). [https://doi.org/10.1038/s41586-024-07173-x](https://doi.org/10.1038/s41586-024-07173-x)
```


Nešto malo više o razlozima zašto baš simulacije kvantnih sistema predstavljaju prvu pravu primenu i to u nauci možete pročitati [Ovde](https://www.jovanodavic.com/post/solvay2022/). 


## Nomenklatura

Polje kvantnog računarstva ima svoj rečnik. Pre nego što zaronimo u matematičke delje vezane za same kubite i kvantna algoritme, vredi usvojiti nekoliko pojmova koji se stalno ponavljaju, jer nam oni govore koliko je neki kvantni računar zaista „odmakao“ i zaista može da ponudi korisnu primenu. 

### Fizički i logički kubiti

Najvažnija razlika u celoj priči jeste ona između **fizičkog** i **logičkog** kubita.

**Fizički kubit** je stvarni uređaj u laboratoriji, na primer 
- elektično kolo sa superprovodnim elementima
- jedan zarobljeni jon ili jedan atom, 
koji nosi kvantnu informaciju, ali su krhki i podložni šumu i greškama. 


**Logički kubit** je skoro pa „idealan“ kubit koji zapravo želimo da koristimo u pravom računu. Njega ne gradimo direktno, već ga *kodiramo* redundantno preko mnoštva fizičkih kubita, uz stalnu **kvantnu korekciju grešaka** (engl. *quantum error correction*).


:::{admonition} Razlika u odnosu na klasično računarstvo
:class: note
Suština priče o potrebi za logičkim kubitima leži u [no-cloning teoremi](https://en.wikipedia.org/wiki/No-cloning_theorem), koja zabranjuje kopiranje kvantnih stanja. U klasičnim računarima korekcija grešaka u bitovima može se napraviti tako što se napravi kopija informacije, a zatim se ona paralelno proverava i, ako se uoči razlika, detektuje greška. U kvantnoj mehanici, zbog no-cloning teoreme, to nije moguće. 

To čini zapravo kvantne računare i njihovu nesmetanu operaciju veoma kompleksnim problemom. 

Za uvod u ovo trenutno veoma bitno polje u kvantnoj informaciji možete pogledati [https://arxiv.org/abs/2605.29137](https://arxiv.org/abs/2605.29137)

:::

```{figure} ../images/lukin.png
:label: fig:logicki-kubit
:alt: Logički kubit kodiran preko mreže fizičkih kubita, sa označenim rastojanjem koda d
:width: 660px
:align: center

Jedan **logički kubit** raspoređen je preko čitave mreže **fizičkih** kubita. Otpornost na greške raste sa tzv. **rastojanjem koda** (engl. *code distance*) $d$: što je $d$ veće, to je više fizičkih kubita i koraka korekcije potrebno po jednom logičkom kubitu. Izvor: predavanje M. Lukina (Mikhail Lukin), [YouTube](https://www.youtube.com/watch?v=hRuC89L5T9U).
```

Cena ove izvršenja algoritama tolerantnim na grešku je visoka: za jedan pouzdan logički kubit danas je potrebno na desetine, pa i na stotine fizičkih.

<u>Zato je „broj kubita“ varljiv podatak, jer uvek se mora znati da li se govori o **fizičkim** ili o **logičkim** kubitima.</u>

### Tri nivoa razvoja

Da bi se govorilo o 'kvalitetu' nekog kvantnog računara, ustalila se podela na:

```{figure} ../images/TechnologicalDevelopment.png
:label: fig:nivoi
:alt: Tri nivoa razvoja kvantnog računarstva — temeljni, otporni i skaliranje
:width: 700px
:align: center

Tri nivoa implementacije kvantnog računarstva:
- **Nivo 1:  temeljni** (engl. *Foundational*): fizički kubiti, NISQ era, eksperimentalno računanje. 
- **Nivo 2: otporni** (engl. *Resilient*): logički kubiti i prva prednost nad klasičnim računarima na problemima male dubine (spletena stanja, uzorkovanje slučajnih kola),
- **Nivo 3: skaliranje** (engl. *Scale*): 1000+ logičkih kubita i industrijska kvantna prednost (hemija, kataliza, nauka o materijalima). 

Izvor: Matthias Troyer, [Simons Institute for the Theory of Computing — Berkeley, 24.07.2026.](https://www.youtube.com/live/5uDPnvgElY8?si=MIjdGMEkVzj-8zQO)
```



:::{admonition} Gde smo trenutno?
:class: tip

Danas se nalazimo na prelazu sa **Nivoa 1 na Nivo 2**: prvi logički kubiti već delimično demonstrirani, ali smo još daleko od hiljada koje su potrebne za primene koje zaista menjanju stvari. 
:::

### Trka za logičkim kubitima

Koliko brzo se taj prelaz odvija? Poslednjih godina napredak u broju **logičkih** kubita je izuzetno brz:

```{figure} ../images/SOTA.png
:label: fig:sota
:alt: Vremenska linija rasta broja logičkih kubita od 2024. do 2026.
:width: 720px
:align: center

Rast broja **logičkih** kubita kroz vreme: 
- 4 (april 2024, Quantinuum)
- 12 (septembar 2024, Quantinuum) 
- 24 (novembar 2024, neutralni atomi, Atom Computing) 
- cilj 50 (2026). 


Za manje od dve godine broj logičkih kubita višestruko je porastao. Izvor: Matthias Troyer, [Simons Institute for the Theory of Computing — Berkeley, 24.07.2026.](https://www.youtube.com/live/5uDPnvgElY8?si=MIjdGMEkVzj-8zQO)
```

Brojevi su još uvek skromni, ali važan je trend. Upravo ovaj sve brži prelazak sa fizičkih na logičke kubite pomera polje ka „tački preseka“ o kojoj smo govorili (v. [](#fig:troyer)) i ka trenutku kada će se kvantni računari zaista isplatiti.

## Uđžbenici i korisni resursi

- Nielsen & Chuang [@nielsen2010].
- Scott Aaronson, [Introduction to Quantum Information Science — beleške s predavanja](https://scottaaronson.blog/?p=3943): besplatne i pristupačno napisane beleške s njegovog uvodnog kursa na Univerzitetu u Teksasu, koje kvantnu informatiku prirodno povezuju s teorijom računske složenosti.
- Scott Aaronson, [Introduction to Quantum Information Science II — beleške s predavanja](https://scottaaronson.blog/?p=6685): nastavak prethodnog kursa koji zalazi dublje u napredne teme, poput kvantne složenosti, kriptografije i korekcije grešaka.
- [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en): interaktivna platforma s kursevima i praktičnim primerima za učenje kvantnog računarstva i programiranja u Qiskit-u.



## Ko sve gradi kvantne računare?
U sledećem poglavlju videćemo ko se sve bavi izradom i izgradnjom kvantnih računara danas. 