"""
prova colorama o altre librerie
"""
from colorama import Fore, Back, Style, init
from rich import print
from colora_testo import colora_testo

init(autoreset=True)

while True:
    testo = input("Inserisci del testo: ")
    if testo.lower() == "esci":
        #print(Back.RED + "Esco dal programma!")
        print("[on red]Esco dal programma[/]")
        break
    if len(testo)%2:
        #print(f"Il testo colorato: \n {Fore.CYAN}{Style.BRIGHT}{testo}")
        print(colora_testo(testo))
    else:
        #print(f"Il testo colorato: \n {Back.GREEN}{Fore.RED}{testo}")
        print(colora_testo(testo))