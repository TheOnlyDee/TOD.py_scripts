#QUESTO SCRIPT CONTIENE LE INFORMAZIONI IMPARATE DAL LIBRO (apogeonline.com)

print("Ciao a tutti!!! \n")

import time

time.sleep(0.65)

#variabile + input

nome = input("Come Ti Chiami? \n")

time.sleep(0.65)

print( nome )

time.sleep(0.65)

#funzione len

print(int(len(nome)))

uno = 1

cinque = 5

tre = 3

time.sleep(0.65)

print( uno * cinque)

time.sleep(0.65)

print(uno + cinque)

time.sleep(0.65)

if uno < cinque:
    print("La matematica non è cambiata!!")
else:
    print("Addio Mondo")

time.sleep(0.65)

if  ( cinque + tre == 8 ):
    print("La matematica non è cambiata!!")
else:
    print("Addio Mondo")

#CICLI E LISTE

time.sleep(1)

#ciclo for

gatti = ["Tigro", "Lea"]

for gatto in gatti:
    print(gatto)

time.sleep(1)

#ciclo  while

rispostaI = input("Vuoi far esplodere un petardo? s/n \n")

while rispostaI == "s":
    print("Accensione...")
    time.sleep(0.7)
    print("....")
    time.sleep(0.7)
    print("lancio...")
    time.sleep(0.7)
    print("....")
    time.sleep(0.7)
    print("ESPLOSIONE!!!")
    time.sleep(2)
    print("Mamma mia che potenza!!")
    time.sleep(1)
    rispostaI = input("Ne vuoi far esplodere un altro? s/n \n")

time.sleep(3)

# cicli annidati

rispostaII = input("Lancire un razzo? s/n \n")

while rispostaII == "s":
    for count in range(10, 0 -1):
        time.sleep(0.7)
        print(count)
    print("DECOLLO!!")
    rispostaII = input("Lancire un altro razzo? s/n \n")

#liste di liste

#periferiche = [ [ "INPUT", "Tastiera", "Mouse", "Elgato"], ["AUDIO", "Microfono", "Cuffie", "Casse" ], ["VIDEO", "Schermo", "Tivù", "Scheda Di Acquisizione"]]

#for perif in periferiche:
#    time.sleep(2)
#    for periferica  in perif:
#       time.sleep(2)
#    print( perif)
#    print("\n")

#FUNZIONI

#definire una funzione

def saluto():
    print("Ciao!")

saluto()

time.sleep(3)

#funzioni integrate
    
num_I = 1/7

time.sleep(1)

print(num_I)

time.sleep(1)

#round(num_I, 2)

print(round(num_I, 2))

time.sleep(1)

#metodi

città = "Firenze"

print(città.upper())

time.sleep(1)

list_a = [1, 2, 3, 4]

list_a.append("cinque") 

print(list_a)

time.sleep(1)

#creare funzioni

numeroI = input("Dimmi un numero \n")

time.sleep(1)

numeroII = input("Un altro numero \n")

time.sleep(2)



time.sleep(0.76)

def add(numeroI: int, numeroII: int):
    #mette insieme due numeri
    numeroIII = int(numeroI) + int(numeroII)
    return numeroIII

print(add(numeroI, numeroII))

time.sleep(1)

def count_letter_e(word):
    total_e = 0
    for letter in word:
        if letter == "e":
            total_letter = total_e + 1
            return total_letter
    total_letter_e = total_letter 
nick = input("il tuo nickname? \n")

total_es_in_nick = count_letter_e(nick)

time.sleep(1)

print("Nel tuo nickname ci sono " + str(total_es_in_nick) + " E.")

time.sleep(1)