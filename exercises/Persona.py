class Persona:
    specie = "Homo Sapiens"
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

pers =  Persona("Franco", 31)
print(f"Abbiamo qui con noi {pers.nome}, che ha {pers.eta} anni!")