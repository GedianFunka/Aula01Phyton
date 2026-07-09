class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome}, emite um som.")

    def mover(self):
        print(f"{self.nome}, se move")

    def exibir_info(self):
        print(f"Animal {self.nome} | Idade: {self.idade} anos")
        print("-" * 20)

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print(f"{self.nome}, late")

    def mover(self):
        print(f"{self.nome}, corre em 4 patas")

    def exibir_info(self):
        super().exibir_info()
        print(f"Raça: {self.raca}")
        print("-" * 20)

class Passaro(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def emitir_som(self):
        print(f"{self.nome}, canta")

    def mover(self):
        if(self.pode_voar):
            print(f"{self.nome}, voa no céu")
        else:
            print(f"{self.nome}, anda no chão")

    def exibir_info(self):
        super().exibir_info()
        print(f"Voa: {'SIM' if self.pode_voar else 'NÃO'}")
        print("-" * 20)

#Uso
c = Cachorro("Rex", 4, "Pastor alemão")
p1 = Passaro("Lorota", 5, "True")
p2 = Passaro("Storlax", 6, "False")

c.emitir_som()
c.mover()
c.exibir_info()

p1.emitir_som()
p1.mover()
p1.exibir_info()

p2.emitir_som()
p2.mover()
p2.exibir_info()