import random
import time

# Metto 64 nomi da usare per gli amici


nomi = [
    "Pippo", "Topolino", "Paperino", "Paperina", "Zio Paperone", "Archimede", "Minnie",
    "Ciccio", "Pluto", "Bruto", "Clarabella", "Minnie", "Orazio", "Ugo", "Gastone", "Daisy",
    "Nonna Papera", "Amelia", "Paperon de' Paperoni", "Gedeone", "Basettoni", "Macchia Nera",
    "Nonno Bassotto", "Bisnonno Paperone", "Zio Paperino", "Banda Bassotti", "Rocky",
    "Battista", "Beniamino", "Carabiniere", "Silvestro", "Lorenzo", "Giulio", "Riccio",
    "Duccio", "Bisio", "Arturo", "Ubaldo", "Ernesto", "Filiberto", "Pasquale", "Lino",
    "Oronzo", "Nino", "Edoardo", "Bruno", "Giacomo", "Rinaldo", "Ennio", "Nicolò", "Vittorio",
    "Olindo", "Vinicio", "Tullio", "Ruggero", "Osvaldo", "Eusebio", "Nando", "Tino",
    "Prudenzio", "Alfredo", "Arbuscello", "Rugantino", "Ruffino", "Tito"
]

# Scelgo casualmente due nomi dalla lista
nome_1 = random.choice(nomi)
nome_2 = random.choice(nomi)

while nome_1 == nome_2:
    nome_2 = random.choice(nomi)

# Spiego il gioco tra i due amici

print("Ci sono due amici al tavolo:", nome_1, "e", nome_2)

time.sleep(2)

print(nome_1, "e", nome_2, "stanno giocando ad un gioco")

time.sleep(2)

print("Questo gioco consiste nel pescare due carte da un mazzo di 50 carte")

time.sleep(2)

print("Chi pesca la carta maggiore ha vinto")

time.sleep(2)

#mescolamento finto delle carte

def print_schermata_caricamento():
    print("Mescolamento carte in corso")
    print("[                    ] 0%")

    for i in range(1, 11):
        time.sleep(0.5)  
        print("[{}{}] {}%".format("=" * i, " " * (10 - i), i * 10))

    print(" Mescolamento completato!")

print_schermata_caricamento()

#due numeri da uno a 50

time.sleep(2)

print( nome_1, "e ", nome_2, " pescano le carte...")

time.sleep(1.5)

print( nome_1, "e ", nome_2, " pescano le carte......")

time.sleep(1.5)

print( nome_1, "e ", nome_2, " pescano le carte...")

time.sleep(2)

print("Pescate!")

time.sleep(2)

def confronta_valori():
    
    time.sleep(2)

    valore_a1 = random.randint(1, 50)
    valore_a2 = random.randint(1, 50)
    
    while valore_a1 == valore_a2: 
        valore_a2 = random.randint(1, 50)


    if valore_a1 > valore_a2:
        print("Ha vinto", nome_1)
    elif valore_a1 < valore_a2:
        print("Ha vinto", nome_2)
    else:
        print("I valori sono uguali")

# Funzione per l'input del tasto
def tasto():
    tasto = input("Premi 'M' per confrontare i valori: ")

    if tasto == "M" or tasto == "m":
        confronta_valori()
    else:
        print("Tasto non valido")

tasto()
