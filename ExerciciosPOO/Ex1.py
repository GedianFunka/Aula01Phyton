class Pessoa:

    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def Apresentar(self):
        print(f'Olá! Meu nome é: {self.nome}, tenho {self.idade} anos e moro em {self.cidade}')

p1 = Pessoa("Gedian", 17, "Corupá")
p2 = Pessoa("Fernando", 18, "Corupá")
p3 = Pessoa("Cenoura", 24, "Pomerode")

p1.Apresentar()
p2.Apresentar()
p3.Apresentar()