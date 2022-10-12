##########provo a fare uno script da solo

print ("Ciao, benvenuti nel Minimarket digitale di TOD!!!")

import time

time.sleep (0.9)

print ("Siete fortunati, oggi non ho clienti, posso guidarvi nell'acquisto di cosa cercate.")

time.sleep (1.3)

nome = input ("Qual'e il vostro nome? \n")

time.sleep (1.2)

dom_uno = input  ("Bene, " + nome + " ,  cosa stai cercando?\n")

time.sleep (0.9)

if ( dom_uno == "la figa" ):
  print ("Scusa " + nome + " non credo che la puoi trovare qui, almeno oggi, ma sul retro posso venderti un manichino sensuale... ")
  exit ()
else:
  print ("Ok, seguimi.\n \n \n ")

#entriamo nel primo reparto del minimarket (la frutta)

lista_uno = "Pomodori, Limoni, Mele, Carote, Ravanelli"

print ("Allora, siamo nel reparto degli ortaggi e della frutta.")

time.sleep (1.5)

politics = " \n 1- Non chiedere cose che non sono nella lista del reparto. \n 2- Puoi prendere solo una cosa a reparto "

frutta_o_verdura_uno = input (". \n Dimmi cosa vuoi prendere , rispettando le regole:" + politics + "\n Scegli fra cosa abbiamo oggi \n" + lista_uno + " \n")
time.sleep(0.8)

time.sleep (2)

if ( frutta_o_verdura_uno == "Pomodori" ) or (frutta_o_verdura_uno == "Limoni") or (frutta_o_verdura_uno  == "Mele") or (frutta_o_verdura_uno == "Ravanelli") or (frutta_o_verdura_uno == "Carote"):
  print("Ok")
#elif (frutta_o_verdura_uno == "Limoni"):
#  print("Ok")
#elif (frutta_o_verdura_uno  == "Mele"):
#  print("ok")
#elif (frutta_o_verdura_uno == "Mele"):
#  print("ok")
#elif (frutta_o_verdura_uno == "Ravanelli"):
#  print("ok")
#elif (frutta_o_verdura_uno == "Carote"):
#  print("ok")
else :
  print("non abbiamo " + frutta_o_verdura_uno + " in questo reparto, se non e frutta o verdura nella lista non protrai essere accontentato.")

time.sleep(2)

#Entriamo nel secondo reparto, il reparto dei latticini

print ("Andiamo nel reparto dei latticini.")

time.sleep(1.5)

list("1- Latte \n2- Yogurt Greco \n3- Burro \n4- Parmigiano Reggiano.")

latticini = input("Scegli fra i latticini nella lista: \n Latte, Yogurt Greco, Burro, Parmigiano Reggiano.\n ")

time.sleep(1.2)

if (latticini == "Latte" ) or (latticini == "Yogurt Greco") or (latticini == "Burro") or (latticini == "Parmigiano Reggiano"):
  print ("Bene, abbiamo "+ latticini + ".")
else:
  print("Non abbiamo " + latticini + ".")


#Reparto della carne

time.sleep(1.3)

print("Siamo nel reparto della carne. \n \n")

time.sleep(0.9)

carne = ["Hamburger", "Maiale", "Angello", "Bistecca", "Cavallo"]

#list("1- Hamburger \n2- Maiale \n3- Agnello \n4-  Bistecca \n5- Cavallo.")

# meat = input("Che cosa prendi in questo reparto?\n Hamburger, Maiale, Agnello, Bistecca, Cavallo \n" )

print("Gli alimenti nel reparto sono: ")

time.sleep(0.65)

for cibo in carne:
    print(cibo)

time.sleep(0.6)

meat = input("Che cosa prendi nel reparto? \n")

time.sleep(0.9)

if ( meat == "Hamburger") or ( meat   == "Maiale") or (meat == "Agnello") or (meat == "Bistecca") or (meat == "Cavallo"):
  print("Ok, prendiamo " + meat + ".")
elif (meat == "niente"):
  print("Ok, Passiamo ad un altro reparto")
else:
  print("Non abbiamo " + meat + "." )
  
#if [ meat in list("1- Hamburger \n2- Maiale \n3- Agnello \n4-  Bistecca \n5- Cavallo.") ]:
#  print("Bene, prendiamo " + meat )
#else: 
#  print("No c'è " + meat )



#ENTRIAMO IN UN NUOVO REPARTO: LA PANETTERIA

time.sleep(1.2)

print("Entriamo nel reparto della panetteria")

time.sleep(0.5)

panetteria = [ "Pane 00", "Pane 0", "Pane Integrale", "Pane Nero", "Baguette",]

print("Le Opzioni sono:")

time.sleep(0.3)

for pane in panetteria:
  print(pane)

time.sleep(0.6)

bread = input("Cosa prendi? \n")

time.sleep(0.4)

if (bread == "Pane 00") or (bread == "Pane 0") or (bread == "Pane Integrale") or (bread == "Pane Nero") or (meat == "Baguette"):
  print("Prendiamo " + bread + ".")
elif (bread == "niente"):
  print("Ok, passiamo al prossimo reparto")
else:
  print( str(bread) +" non è nella lista.")


#ENTRIAMO NEL REPARTO DEGLI ALCOLICI, MA PRIMA CHIEDIAMO L'ETA' DEL CLIENTE

time.sleep(2)

eta = input("Quanti anni hai? \n")

time.sleep(0.6)

if (int(eta) > 17):
  print("Siamo nel reparto degli alcolici, visto che sei maggiorenne puoi comprare qualcosa qui." )
  
  time.sleep(0.6)

  alcolici = ["Vino Chianti", "Birra Moretti", "Spumante", "Vodka Base"]

  for alcolico in alcolici:
    print(alcolico)
  
  time.sleep(0.5)
  
  alc = input("Che cosa prendi? \n")

  if ( alc == "Vino Chianti") or (alc == "Birra Moretti") or (alc == "Spumante") or (alc == "Vodka Base"):
    print("Bene, Prendiamo " + alc + ".")
  elif (alc == "niente"):
    print("Va bene, " + nome + " non prendiamo alcol.")
  else:
    print("Non Abbiamo " + alc + ".")
else:
  print( "\n")


