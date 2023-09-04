import webbrowser

# Percorso del file "urls.txt"
file_path = "urls.txt"

# Leggi i link dal file e apri ognuno di essi in schede separate
with open(file_path, "r") as file:
    for line in file:
        url = line.strip()
        webbrowser.open_new_tab(url)
