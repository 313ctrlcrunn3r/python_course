from vehicles import *

def main():
    print(f"{Fore.BLUE}Benvenuto nel selezionatore di veicoli\n")
    while True:
        print(f"{Fore.GREEN}1. Crea auto e leggi la scheda tecnica")
        print(f"{Fore.RED}2. Esci")
        scelta = int(input("Scegli l'operazione:\n"))
        if scelta == 1:
            print(f"{Fore.CYAN}1. Benzina")
            print(f"{Fore.CYAN}2. Diesel")
            print(f"{Fore.CYAN}3. GPL")
            print(f"{Fore.CYAN}4. Elettrico")

            scelta = int(input("Scegli la tipologia di motore:\n"))
            if scelta == 1:
                marca = input("Inserisci la marca:\n")
                modello = input("Inserisci il modello:\n")
                auto = VeicoloBenzina(marca, modello)
                print(auto.descrivi())
            if scelta == 2:
                marca = input("Inserisci la marca:\n")
                modello = input("Inserisci il modello:\n")
                auto = VeicoloDiesel(marca, modello)
                print(auto.descrivi())
            if scelta == 3:
                marca = input("Inserisci la marca:\n")
                modello = input("Inserisci il modello:\n")
                auto = VeicoloGPL(marca, modello)
                print(auto.descrivi())
            if scelta == 4:
                marca = input("Inserisci la marca:\n")
                modello = input("Inserisci il modello:\n")
                auto = VeicoloElettrico(marca, modello)
                print(auto.descrivi())


        elif scelta == 2:
            print(f"{Back.RED}Esco dal programma, arrivederci!")
            break

if __name__== "__main__":
    main()

