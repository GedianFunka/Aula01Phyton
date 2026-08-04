class Carro:

    def __init__(self, marca, modelo, ano, velocidade = 0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def Acelerar(self, valor):
        if (valor > 0):
            self.velocidade += valor
            print(f'Acelerando {valor} km/h')
        else:
            print(f'Valor de aceleração inválido')

    def Frear(self, valorDi):
        if (self.velocidade > 0 and valorDi <= self.velocidade):
            self.velocidade -= valorDi
            print(f'Freando {valorDi} km/h')
        else:
            print(f'Velocidade invalida ou valor de frenagem inválido')

    def ExibirInfo(self):
        print(f'Carro: {self.marca} {self.modelo} ({self.ano}) | Velocidade atual: {self.velocidade} km/h')
        print("-" * 32)

c1 = Carro('Honda', 'Civic' , '2020')
c2 = Carro('Volkswagem', 'Saveiro', '2026')

c1.Acelerar(100)
c1.Frear(80)
c1.ExibirInfo()

c2.Acelerar(100)
c2.Frear(110)
c2.ExibirInfo()