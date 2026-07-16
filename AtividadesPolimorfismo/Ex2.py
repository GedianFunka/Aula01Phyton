class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        print(f"O meu nome é: {self.nome}")

class Recepcionista(Funcionario):
    def __init__(self, nome):
            self.nome = nome

    def cumprimentar(self):
        print(f"Bem vindo! Meu nome é {self.nome}, posso ajudar?")

class Gerente(Funcionario):
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        print(f"Olá! Sou {self.nome}, gerente dessa unidade.")

class Tecnico(Funcionario):
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        print(f"Oi, meu nome é {self.nome}, do suporte técnico.")

def comprimentar(funcionario):
    funcionario.cumprimentar()

funcionarios = [Recepcionista("Kauã"), Gerente("Weslley"), Tecnico("Gedian"), Recepcionista("Willian"), Gerente("Guilherme"), Tecnico("Felipe")]

for funcionario in funcionarios:
    comprimentar(funcionario)
