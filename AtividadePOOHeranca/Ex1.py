class Veiculo:
    def __init__(self, ano, marca, modelo):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print("-"*20)
        print(f"Ano: {self.ano}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        super().__init__(marca, modelo, ano)
        self.numero_portas = numero_portas

    def exibir_info(self):
        super().exibir_info()
        print(f"Número de portas: {self.numero_portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_info(self):
        super().exibir_info()
        print(f"Cilindradas: {self.cilindradas}")

c = Carro("Volkswagen","Golf", "2020", "4")
m = Moto("Honda","CRF", "2025", "250")
        
c.exibir_info()
m.exibir_info()

