---
title: "Korišćenje pravog kvatnog računara"
short_title: Korišćenje pravog kvatnog računara
description: Kako koristimo pravi kvantni računar?
---

# Kako da pustimo prvi kvantni računa

Hajde da vidimo kako možemo da koristimo pravi kvantni računar koristeći programsko okruženje QisKit. 

Prvo pristupimo: https://resonance.iqm.tech i ulogujemo se. 
Onog što bi trebali da vidimo je sledeće 

- step1.

- step2. 

Primer tehničke specificacije na: https://arxiv.org/abs/2408.12433

- step3

- step4

- step5

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


Pokušaj da dodaš još jednu H operaciju. 