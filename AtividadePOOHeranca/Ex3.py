class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcularsalario(self):
        return self.salario_base

    def exibir_info(self):
        print(f"Funcionário {self.nome}, tem o salário de: {self.salario_base}")

class Horista(Funcionario):
    def __init__(self, nome, salario_base, horas, valor_horas):
        super().__init__(nome, salario_base)
        self.horas = horas
        self.valor_horas = valor_horas

    def calcularsalario(self):
        return  super().calcularsalario() +  (self.valor_horas * self.horas)

    def exibir_info(self):
        print(f"Funcionario {self.nome}")
        print(f"Horas trabalhadas: {self.horas}")
        print(f"Valor de horas trabalhadas: {self.valor_horas}")
        print(f"Salario total: R${self.calcularsalario():.2f}")
        print("-"*20)

class Mensalista(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcularsalario(self):
        return self.salario_base

    def exibir_info(self):
        print(f"Funcionario: {self.nome}")
        print(f"Salário: {self.calcularsalario()}")
        print("-"*20)

h = Horista("Gedian", 0, 80, 10)
h.exibir_info()

m = Mensalista("Kauã",30000)
m.exibir_info()