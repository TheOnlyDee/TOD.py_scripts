#primo progetto python (pagina 118) del libro "CODING: Guida Facile Per Principianti" (apogeonline.com)
#messo in pratica da TOD (https://github.com/TheOnlyDee)

import random

import time

time.sleep(1)

print("Benvenuto su Team Allocator!!")

players = ["Martin", "Craig", "Sue", "Claire", "Dave", "Alice", "Sonakshi", "Harry", "Jack", "Rose", "Lexi", "Maria", "Thomas", "James", "William", "Ada", "Grace", "Jean", "Merissa", "Alan"]

time.sleep(1)

while True:

    random.shuffle(players)

    response = input("E' uno sport di scuadra o induviduale? \n Digita s o i:\n")

    if response == "s":

        team1 = players[:len(players)//2]

        print("\n \nCapitano team 1: " + random.choice(team1))

        time.sleep(0.9)

        print("\nTeam 1:")

        time.sleep(0.8)

        for player in team1:
            time.sleep(0.7)
            print(player)

        time.sleep(1)

        team2 = players[len(players)//2:]

        print("\n \nCapitano team 2: " + random.choice(team2))

        time.sleep(1)

        print("\nTeam 2:")

        for player in team2:
            time.sleep(0.7)
            print(player)

        response = input("\nRiselezionare le squadre? Digita s o n: \n")

        if response == "n":
            print("Arresto selettore...")
            time.sleep(1)
            break
    else:
        for i in range(0, 20, 2):
            
            time.sleep(1.3)
            
            print(players[i] + " vs " + players[i+1] + "\n")

            start = random.randrange(i, i+2)

            time.sleep(0.5)

            print("Comincia " + players[start] + " \n \n")
        response = input("Riselsezionare gli sfidandi? s/n \n")
        if response == "n":
            print("Arresto Selettore....")
            time.sleep(1)
            break