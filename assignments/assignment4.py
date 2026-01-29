"""
Obiettivo: Gestire una lista di persone che cercano di entrare, controllando l'età e la presenza in una "Blacklist".La Consegna
Scrivi uno script che segua questi passaggi:La Blacklist: Crea una lista chiamata blacklist con 3 nomi (es: "Mario", "Lara", "Luca").Il Ciclo Infinito: 
Usa un while True per continuare a chiedere nomi all'ingresso. (Il ciclo si deve fermare solo se scrivi "esci").Controlli (IF/ELIF/ELSE):

    Se il nome è nella blacklist, stampa: "Accesso negato: sei in lista nera!".
    Altrimenti, chiedi l'età:
    Se l'età è minore di 18, stampa: "Accesso negato: sei troppo giovane!".
    Se l'età è 18 o più, stampa: "Benvenuto nel club, [nome]!".
"""

blacklist=["Luigi", "Peach", "Toad"]

while True:
    comando = input("Controlla nome: ")
    if comando.lower() == 'esci' :
        print("Esco dal programma.")
        break

    if comando in blacklist:
        print(f"Accesso negato: sei in lista nera!")
    else:
        try:
            age=int(input("Inserisci l'età: "))
            if age < 18:
                print("Accesso negato: sei troppo giovane!")
            else: 
                print(f"Benvenuto nel club, {comando}")
        except ValueError:
            print("Inserisci valore corretto.")