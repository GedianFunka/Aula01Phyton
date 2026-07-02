class Calculadora:
    def __init__(self):
        self.lista = []

    def somar(self, num1, num2):
        resultado = num1 + num2
        print(f'O resultado da soma de {num1} + {num2} = {resultado}')
        self.lista.append(f'{num1} + {num2} = {resultado}')
        print("-" * 32)
        return resultado

    def subtrair(self, num1, num2):
        resultado = num1 - num2
        print(f'O resultado da subtração de {num1} - {num2} = {resultado}')
        self.lista.append(f'{num1} - {num2} = {resultado}')
        print("-" * 32)
        return resultado

    def multiplicar(self, num1, num2):
        resultado = num1 * num2
        print(f'O resultado da multiplicação de {num1} * {num2} = {resultado}')
        self.lista.append(f'{num1} * {num2} = {resultado}')
        print("-" * 32)
        return resultado

    def dividir(self, num1, num2):
        if num2 == 0:
            aviso = f'Dividido por zero : {num1} / {num2}'
            self.lista.append(aviso)
            print("Não é possível dividir por zero")
            print("-" * 32)
            return None
        else:
            resultado = num1 / num2
            print(f'O resultado da divisão de {num1} / {num2} = {resultado}')
            self.lista.append(f'{num1} / {num2} = {resultado}')
            print("-" * 32)
            return resultado

    def ExibirHistorico(self):
        print(f'--Histórico--')
        if not self.lista:
            print(f'Lista vazia')
        else:
            for historico in self.lista:
                print(historico)
        print("-" *32)

Calculadora = Calculadora()
Calculadora.somar(2, 3)
Calculadora.somar(4, 5)

Calculadora.subtrair(3, 2)
Calculadora.subtrair(5, 4)

Calculadora.multiplicar(2, 2)
Calculadora.multiplicar(5, 4)

Calculadora.dividir(2, 0)
Calculadora.dividir(10, 5)

Calculadora.ExibirHistorico()