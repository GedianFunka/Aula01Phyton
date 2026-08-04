class Forma:
    def __init__(self, cor):
        self.cor = cor

    def calcular_area(self):
        return 0

    def exibir_info(self):
        print("-"*20)
        print(f"Cor: {self.cor}")

class Circulo(Forma):
    def __init__(self, raio, cor):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self):
        return 3.1415 * self.raio ** 2

    def exibir_info(self):
        super().exibir_info()
        print(f"Raio: {self.raio}")
        print(f"Area: {self.calcular_area()}")

class Retangulo(Forma):
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def exibir_info(self):
        super().exibir_info()
        print(f"Largura: {self.largura}")
        print(f"Altura: {self.altura}")
        print(f"Area: {self.calcular_area()}")

class Triangulo(Forma):
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return (self.largura * self.altura) / 2

    def exibir_info(self):
        super().exibir_info()
        print(f"Largura: {self.largura}")
        print(f"Altura: {self.altura}")
        print(f"Area: {self.calcular_area()}")

c = Circulo(5, "Azul")
c.exibir_info()

r = Retangulo("Verde", 6, 5)
r.exibir_info()

t = Triangulo("Vermelho", 7, 5)
t.exibir_info()