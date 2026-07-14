class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def exibir_info(self):
        print("-"*20)
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_rendimento):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def render(self):
        self.saldo = self.saldo * (1+self.taxa_rendimento)

    def exibir_info(self):
        print("-" * 20)
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print(f"Taxa de rendimento: {self.taxa_rendimento * 100}%")

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def depositar(self, valor):
        if valor < 0:
            print("Valor de de depósito inválido")
        else:
            self.saldo = self.saldo + valor

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            print("-" * 20)
            print("Valor de saldo insuficiente")
        else:
            self.saldo = self.saldo - valor

    def exibir_info(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print(f"Limite: {self.limite}")


cp = ContaPoupanca("Gedian", 1000, 0.10)
cp.render()
cp.exibir_info()

cc = ContaCorrente("Kauã", 2000, 500)
cc.depositar(100)
cc.sacar(2700)
cc.exibir_info()
