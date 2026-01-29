"""
esempio di funzione
"""
from rich import print

def colora_testo(testo):
    if len(testo)%2:
        print(f"Il testo colorato: \n[cyan]{testo}[/]")
    else:
        print(f"Il testo colorato: \n[on green][red]{testo}[/]")

while True:
    testo = input("Inserisci del testo: ")
    if testo.lower() == "esci":
        #print(Back.RED + "Esco dal programma!")
        print("[on red]Esco dal programma[/]")
        break
    colora_testo(testo)