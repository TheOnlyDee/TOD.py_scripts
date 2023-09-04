def calcola_media():
    numeri = []  # Inizializza una lista vuota per i numeri

    # Input dei dati
    while True:
        input_numero = input("Inserisci un numero (invio per uscire): ")
        
        # Esci se l'utente preme solo invio
        if input_numero == "":
            break
        
        try:
            numero = float(input_numero)  # Converti l'input in un numero float
            numeri.append(numero)  # Aggiungi il numero alla lista
        except ValueError:
            print("Inserisci un numero valido.")

    # Elaborazione dei dati
    somma = sum(numeri)
    numero_totale = len(numeri)

    # Calcolo della media
    if numero_totale > 0:
        media = somma / numero_totale
        print("La media dei numeri inseriti è", media)
    else:
        print("Nessun numero inserito.")

if __name__ == "__main__":
    calcola_media()

