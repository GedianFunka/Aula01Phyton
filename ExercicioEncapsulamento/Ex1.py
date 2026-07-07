class Cofre:
    def __init__(self, dono, valor):
        self.dono = dono
        self.__valor = valor

    #Setter
    def set_valor(self, novo_valor):
        if novo_valor >= 0:
            self.__valor = novo_valor
        else:
            print("Valor invalido! O valor deve ser maior ou igual a zero.")

    def depositar(self, valor_deposito):
        if valor_deposito >= 0:
            self.__valor += valor_deposito
        else:
            print("Valor deve ser maior ou igual a zero.")

    def retirar(self, valor_retirado):
        if valor_retirado >= 0 and valor_retirado <= self.__valor:
            self.__valor -= valor_retirado
        else:
            print("Valor invalido! O valor deve ser maior ou igual a zero e menor ou igual ao saldo disponivel.")

    # Getter
    def get_valor(self):
        return self.__valor

    def exibir_saldo(self):
        print("=" * 30)
        print(f"Dono: {self.dono}")
        print(f"Valor: {self.__valor}")
        print("=" * 30)

c1 = Cofre("Gedian", 500)
c1.depositar(100)
c1.retirar(50)
c1.exibir_saldo()

c2 = Cofre("Kauã", 2000)
c2.depositar(100)
c2.retirar(200)
c2.exibir_saldo()