import requests

# Numero di volte da visitare il sito
num_visite = 10

# URL del sito da visitare
url = "https://wiby.me/surprise"

# File in cui registrare gli URL
file_output = "urls.txt"

# Ciclo per visitare il sito e registrare i domini
for _ in range(num_visite):
    response = requests.get(url)
    
    # Estrae l'URL dal testo di output
    start_index = response.text.find("URL='") + len("URL='")
    end_index = response.text.find("'", start_index)
    redirect_url = response.text[start_index:end_index]
    
    if redirect_url:
        with open(file_output, "a") as file:
            file.write(redirect_url + "\n")
        
        print("URL registrato:", redirect_url)
    else:
        print("Nessun reindirizzamento trovato.")

print("Le visite sono state completate e gli URL sono stati registrati in", file_output)
