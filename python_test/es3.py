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

print("inserisci il primo numero:")
a = int(input("primo numero: "))
if a%2==0:
    color_a = ROSSO
else:
    color_a = BLU
print(f"il primo numero è: {color_a}{a}{RESET}")
print("inserisci il secondo numero:")

b = int(input("secondo numero: "))
if b%2==0:
    color_b = VERDE
else:
    color_b = GIALLO
print(f"il secondo numero è: {color_b}{b}{RESET}")
somma=a+b
if somma%2==0:
    color_somma=MAGENTA
else:
    color_somma=CIANO
print(f"La somma dei numeri è: {color_somma}{a+b}{RESET}")