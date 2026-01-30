class Libro:
    def __init__(self, autore, titolo, anno = None, casa_editrice = None):
        self.autore = autore
        self.titolo = titolo
        self.anno = int(anno)
        self.casa_editrice = casa_editrice
    
    def stampa_informazioni(self):
        print("Informazioni sul libro:")
        print(f"    - Autore del libro: {self.autore};")
        print(f"    - Titolo del libro: {self.titolo};")
        print(f"    - Anno di uscita: {self.anno};")
        print(f"    - Casa editrice: {self.casa_editrice}")


libro = Libro("George Orwell", "1984", "1967")
libro2 = Libro("Ernest Hemingway", "Per chi suona la campana", 1937, "Einaudi")
libro.stampa_informazioni()
libro2.stampa_informazioni()


