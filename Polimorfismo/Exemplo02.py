class Forma:
    def __init__(self, nome = "Forma Genérica"):
        self.nome = nome

    def calcular_area(self):
        return 0

    def descricao(self):
        return self.nome

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__("Circulo")
        self.raio = raio

    def calcular_area(self):
        return 3.1415 * self.raio ** 2

    def descricao(self):
        return f"{self.nome} (raio = {self.raio})"

class Retangulo(Forma):
    def __init__(self, largura, altura):
        super().__init__("Retangulo")
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def descricao(self):
        return f"{self.nome}({self.largura} X {self.altura})"

def exibir_area(Forma):
    print(f"{Forma.descricao()} - Area = {Forma.calcular_area()}")

formas = [Circulo(5), Retangulo(3, 5), Circulo(7), Retangulo(6, 7), Circulo(8), Retangulo(9, 8)]

for forma in formas:
    exibir_area(forma)