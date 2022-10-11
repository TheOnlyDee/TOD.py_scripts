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

latticini = input("Scegli fra i latticini nella lista: \n"+ "1- Latte \n2- Yogurt Greco \n3- Burro \n4- Parmigiano Reggiano." + "\n" )

time.sleep(1.2)

if [latticini in list("1- Latte \n2- Yogurt Greco \n3- Burro \n4- Parmigiano Reggiano.")  ]:
  print ("Bene, abbiamo "+ latticini + ".")
else:
  print("Non abbiamo " + latticini + ".")


#Reparto della carne

time.sleep(1.3)

print("Siamo nel reparto della carne.")

time.sleep(0.9)

list("1- Hamburger \n2- Maiale \n3- Agnello \n4-  Bistecca \n5- Cavallo.")

meat = input("Che cosa prendi in questo reparto?\n Hamburger, Maiale, Agnello, Bistecca, Cavallo \n" )

time.sleep(1)

if [ meat in list("1- Hamburger \n2- Maiale \n3- Agnello \n4-  Bistecca \n5- Cavallo.") ]:
  print("Bene, prendiamo " + meat )
else: 
  print("No c'è " + meat)