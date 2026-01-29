"""
Scrivi uno script che:Crei una lista chiamata spesa
 contenente almeno 5 prodotti (es: "Pane", "Latte", "Uova", ecc.).
 Usi un ciclo for per stampare ogni prodotto della lista.Per rendere
   l'output più carino, ogni riga deve essere stampata così: Prodotto 
   da acquistare: [nome del prodotto].
Bonus per chi finisce prima: Aggiungi un messaggio finale che stampi
 il numero totale di oggetti da comprare usando la funzione len().
"""

lista_spesa = ["Pane", "Latte", "Frutta", "Carne", "Coca-cola" ]

for prodotto in lista_spesa:
    print(f"Prodotto da acquistare: {prodotto}")

print(f"Numero toale di prodotti da acquistare: {len(lista_spesa)}")