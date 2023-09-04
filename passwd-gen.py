import random
import string
import time

lunghezza_password = int(input("Di quanti caratteri vuoi che sia la password? "))

caratteri_validi= string.ascii_letters + string.digits + string.punctuation

def genera_password(lunghezza):
    password = ''.join(random.choice(caratteri_validi) for carattere in range(lunghezza))
    return password

password = genera_password(lunghezza_password)

time.sleep(2)

print("la tua password è:", password)