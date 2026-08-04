class Lampada:
    def __init__(self, marca):
        self.marca = marca

    def acender(self):
        print(f"Lampada da marca {self.marca} acendendo.")

class LampadaIncandescente(Lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        print(f"{self.marca} luz quente e amarelada acessa.")

class LampadaFlourescente(Lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        print(f"{self.marca} luz branca  fria acesa.")

class LampadaLed(Lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        print(f"{self.marca} luz LED de baixo consumo acessa.")

def ligar_lampadas(Lampada):
    Lampada.acender()

lampadas = [LampadaIncandescente("Phillips"), LampadaFlourescente("WOM"), LampadaLed("Sansung"), LampadaIncandescente("Elgin"), LampadaFlourescente("G-light"), LampadaLed("Ourolux")]

for lampada in lampadas:
    ligar_lampadas(lampada)