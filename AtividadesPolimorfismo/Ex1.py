class Transporte:
    def __init__(self, nome):
        self.nome = nome

    def viajar(self):
        print("Viajando.....")

class Aviao(Transporte):
    def viajar(self):
        print(f"{self.nome} está voando")

class Navio(Transporte):
    def viajar(self):
        print(f"{self.nome} está navegando")

class Trem(Transporte):
    def viajar(self):
        print(f"{self.nome} está andando pelos trilhos")

def iniciar_viajem(Transporte):
    Transporte.viajar()

transportes = [Aviao("GG"), Navio("KK"), Trem("WW")]

for transporte in transportes:
    iniciar_viajem(transporte)
