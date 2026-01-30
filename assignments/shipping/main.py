from logistica import *
from colorama import Fore, Back, Style, init


def main():
    print(f"{Fore.CYAN}Benvenuto nel sistema di spedizioni Python!")
    while True:
        print(f"{Fore.GREEN}1. Crea etichetta")
        print(f"{Fore.RED}2. Esci")
        scelta = int(input("Scegli l'operazione:\n"))

        if scelta == 1:
            nome = input("Inserisci nome del destinatario:\n")
            city = input("Inserisci la città di destinazione:\n")
            prezzo_ordine = float(input("Inserisci il prezzo dell'ordine:\n"))
            peso = float(input("Inserisci il peso del pacco:\n"))
            prezzo = calcola_spedizione(prezzo_ordine, peso)
            etichetta = crea_etichetta(nome, city, prezzo, peso)
            print(f"Ecco il riepilogo della spedizione!")
            print(f"{Fore.RED}Prezzo della spedizione: {prezzo}")
            print(f"{Fore.MAGENTA}Etichetta:\n{etichetta}\n")

        elif scelta == 2:
            print(f"{Back.RED}Esco dal programma, arrivederci!")
            break

if __name__ == "__main__":
    main()