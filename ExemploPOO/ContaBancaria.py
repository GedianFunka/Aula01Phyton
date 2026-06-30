class ContaBancaria:

    def __init__(self, titular, numero, saldo_inicial = 0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo_inicial

    #Depositar
    #Sacar
    #Fazer extrato

    #Depositar
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R$:{valor:.2f} realizado com sucesso")
        else:
            print("Valor de deposito invalido")

    #Sacar
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque invalido")
        elif valor >= self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque no valor de R${valor:.2f} realizado com sucesso")

    #Fazer extrato
    def extrato(self):
        print("="*20)
        print(f"Titular: {self.titular}")
        print(f"Conta: {self.numero}")
        print(f"Saldo: R${self.saldo:.2f}")
        print("="*20)

conta1 = ContaBancaria("Gedian","12469-9",10000.00)
conta1.depositar(300.00)
conta1.sacar(100.00)
conta1.extrato()

conta2 = ContaBancaria("Kaua","15869-0",1000.00)
conta2.depositar(3000000.00)
conta2.sacar(1000000.00)
conta2.extrato()


