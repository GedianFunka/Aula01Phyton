class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def CalcularArea(self):
        return self.largura * self.altura

    def CalcularPerimetro(self):
        return 2 * (self.largura + self.altura)

    def ExibirInfo(self):
        print(f'A largura do retângulo é: {self.largura}')
        print(f'A altura do retângulo é: {self.altura}')
        print(f'O valor da área é: {self.CalcularArea()}')
        print(f'O valor do perímetro é: {self.CalcularPerimetro()}')
        print("-" * 32)

R1 = Retangulo(10, 20)
R2 = Retangulo(20, 20)

R1.ExibirInfo()
R2.ExibirInfo()