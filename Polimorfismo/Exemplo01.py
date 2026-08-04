class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} emite um som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} Late")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} Mia")

def fazer_barulho(animal):
    animal.emitir_som()

animais = [Cachorro("Tobi"), Gato("Morto"), Cachorro("Tayler"), Gato("Morto2")]

for animal in animais:
    fazer_barulho(animal)