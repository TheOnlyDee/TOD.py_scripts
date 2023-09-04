#!/usr/bin/python
def conta_parole(testo):
    parole = testo.lower().split()
    conteggio_parole = {}
    
    for parola in parole:
        if parola in conteggio_parole:
            conteggio_parole[parola] += 1
        else:
            conteggio_parole[parola] = 1
    
    return conteggio_parole

def parole_piu_frequenti(conteggio_parole, num_parole):
    parole_frequenti = sorted(conteggio_parole, key=conteggio_parole.get, reverse=True)[:num_parole]
    return parole_frequenti

# Input del testo da parte dell'utente
testo = input("Inserisci un testo: ")

# Conteggio delle parole
conteggio = conta_parole(testo)

# Numero di parole più frequenti da visualizzare
num_parole_frequenti = 5

# Identificazione delle parole più frequenti
parole_frequenti = parole_piu_frequenti(conteggio, num_parole_frequenti)

# Stampa delle parole più frequenti
print("Parole più frequenti nel testo:")
for parola in parole_frequenti:
    print(parola, "-", conteggio[parola], "occorrenze")

