from operation import *
from colorama import Fore, Back, Style, init

init(autoreset=True)


print(f"{Fore.CYAN}Calcolatrice Python")
while True:
    try:
        print(f"{Fore.GREEN}1. Somma di due numeri")
        print(f"{Fore.GREEN}2. Sottrazione di due numeri")
        print(f"{Fore.GREEN}3. Moltiplicazione di due numeri")
        print(f"{Fore.GREEN}4. Divisione di due numeri")
        print(f"{Fore.BLUE}0. Esci dalla Calcolatrice")

        scelta = int(input("Inserisci il numero dell'operazione (0-4): "))

        if scelta == 1:
            n1 = float(input("Inserisci il primo termine: "))
            n2 = float(input("Inserisci il secondo termine: "))
            print(f"Il risultato è: {sum(n1, n2)}")
        
        elif scelta == 2:
            n1 = float(input("Inserisci il primo termine: "))
            n2 = float(input("Inserisci il secondo termine: "))
            print(f"Il risultato è: {sub(n1, n2)}")

        elif scelta == 3:
            n1 = float(input("Inserisci il primo termine: "))
            n2 = float(input("Inserisci il secondo termine: "))
            print(f"Il risultato è: {mul(n1, n2)}")

        elif scelta == 4:
            try:
                n1 = float(input("Inserisci il primo termine: "))
                n2 = float(input("Inserisci il secondo termine: "))
                print(f"Il risultato è: {div(n1, n2)}")
            except ValueError as e:
                print(f"{Back.RED}Errore: {e}")
        elif scelta == 0:
            print(f"{Back.RED} Esco dal programma, arrivederci!")
            break

    except ValueError:
        print(f"{Back.RED}Errore: Inserisci numeri validi!")




