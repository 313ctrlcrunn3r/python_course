"""
Creare un programma che blocchi l'accesso finché l'utente non inserisce la parola magica.

Scrivi uno script che:Definisca una variabile password_corretta (es: "python123").
Usi un ciclo while per continuare a chiedere all'utente: "Inserisci la password per entrare:".
Se la password è sbagliata, deve stampare "Accesso negato! Riprova.".
Il ciclo deve interrompersi solo quando la password inserita è corretta.
Alla fine, fuori dal ciclo, deve stampare "Benvenuto nel sistema!".
"""
correct_password = "esempio_password1234$"

while True:
    password_in = input("Inserisci password: ")

    if password_in == correct_password:
        break
    else:
        print("Password errata! inserisci la pssword corretta per entrare")

print("Benvenuto nel sistema!")