"""
Scrivi uno script che:Chieda all'utente la sua età (usando input e trasformandolo in int).Applichi le seguenti regole con if, elif ed else:

    Sotto i 5 anni: Il biglietto è Gratis (0€).
    Dai 5 ai 17 anni: Il biglietto è Ridotto (7€).
    Dai 18 ai 64 anni: Il biglietto è Intero (10€).
    Dai 65 anni in su: Il biglietto è Senior (6€).

Stampi un messaggio finale con il prezzo da pagare.
"""

age =int(input("Inserisci l'età: "))
if age < 5:
    print(f"Biglietto gratis ({age} anni)")
elif age >= 5 and age < 18:
    print(f"Biglietto ridotto ({age} anni): €5")
elif age >= 18 and age < 65:
    print(f"Biglietto intero ({age} anni): €10")
else:
    print(f"Biglietto senior ({age} anni): €6")

