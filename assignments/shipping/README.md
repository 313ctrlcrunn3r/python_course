1. Crea il file logistica.py (Il Modulo)
In questo file scriverai le funzioni di calcolo. Attenzione: usa return per restituire i risultati, non usare input o print qui dentro.

- calcola_spedizione(prezzo_ordine, peso):
- Se l'ordine supera i 100€, la spedizione è Gratis (0€).
- Altrimenti: costa 5€ se il pacco pesa meno di 5kg, oppure 10€ se pesa 5kg o più.

crea_etichetta(nome, citta): Restituisce una stringa con i dati formattati (es: "DESTINATARIO: MARCO - CITTÀ: ROMA").

2. Crea il file main.py (Il Programma)
In questo file gestirai l'interazione con l'utente:

-  Importa il modulo logistica.
-   Chiedi all'utente: Nome, Città, Totale spesa (€) e Peso del pacco (kg).
-   Richiama le funzioni dal file logistica.py per ottenere il costo di spedizione e l'etichetta.
-   Stampa il riepilogo finale e il Totale Complessivo (Spesa + Spedizioni).

3. Debug (Prova Pratica)

-   Inserisci un breakpoint nel main.py sulla riga dove chiami la funzione calcola_spedizione.
-   Avvia il debug e usa il tasto "Step Into" (F11): osserva come il computer "salta" da un file all'altro per eseguire il calcolo.

Carica entrambi i file (logistica.py e main.py).