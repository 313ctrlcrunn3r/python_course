from colorama import Fore, Back, Style, init
init(autoreset=True)

class Veicolo:
    tipo_carburante = "generico"
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def descrivi(self):
        return "Marca: " + self.marca + ";\nModello: " + self.modello + ";\ntipo di carburante: " + self.tipo_carburante

class VeicoloBenzina(Veicolo):
    tipo_carburante = "Benzina"
    def __init__(self, marca, modello):
        super().__init__(marca, modello)

class VeicoloDiesel(Veicolo):
    tipo_carburante = "Diesel"
    def __init__(self, marca, modello):
        super().__init__(marca, modello)

class VeicoloGPL(Veicolo):
    tipo_carburante = "GPL"
    def __init__(self, marca, modello):
        super().__init__(marca, modello)

class VeicoloElettrico(Veicolo):
    tipo_carburante = "Elettrico"
    def __init__(self, marca, modello):
        super().__init__(marca, modello)

    def descrivi(self):
        return super().descrivi() + "\n"+Fore.GREEN+ "Complimenti per la scelta ecologica!"

