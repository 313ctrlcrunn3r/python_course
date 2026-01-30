from colorama import Fore, Back, Style, init
init(autoreset=True)


def calcola_spedizione(prezzo, peso):
    if prezzo > 100:
        return 0
    elif peso < 5:
        return 5
    else:
        return 10
    
def crea_etichetta(nome, citta, prezzo, peso):
    return Fore.BLUE + "DESTINATARIO: " + nome.upper() + ", CITTÀ: " + citta.upper() + "\nPeso del pacco: " + str(peso) + " kg, prezzo della spedizone: €" + str(prezzo)