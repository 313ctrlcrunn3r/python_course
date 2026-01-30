# lol
#print("Inserisci frase da colorare:")
RESET = "\x1b[0m"
#frase = input()
# \x1b[38;2;200;200m] lilla
LILLA = "\x1b[38;2;221;160;221m"
GIALLO_BG="\x1b[48;2;229;190;1m"
ROSSO = "\x1b[38;2;255;0;0m"      # Rosso
VERDE = "\x1b[38;2;0;255;0m"       # Verde
BLU = "\x1b[38;2;0;0;255m"         # Blu
GIALLO = "\x1b[38;2;255;255;0m"    # Giallo
CIANO = "\x1b[38;2;0;255;255m"     # Ciano
MAGENTA = "\x1b[38;2;255;0;255m"   # Magenta
ARANCIONE = "\x1b[38;2;255;165;0m" # Arancione
VERDE_LIMONE = "\x1b[38;2;204;255;0m"  # Verde Limone
GRIGIO = "\x1b[38;2;128;128;128m"  # Grigio
#print("\x1b[32m" + "\n" +frase)
#print(lilla + "\n" +frase)
#print(f"{GIALLO_BG}\n{frase} {RESET}{LILLA}{frase} no colore")
print("inserisci il primo numero:")
a = input("primo numero: ")
print(f"Il primo numero è: {ROSSO}{a}{RESET}")
print("inserisci il secondo numero:")
b = input("secondo numero: ")
print(f"Il secondo numero è: {CIANO}{b}{RESET}")
somma = int(a) + int(b)
print(f"La somma dei numeri è: {MAGENTA}{somma}")
