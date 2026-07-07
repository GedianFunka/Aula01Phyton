class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota
        self.set_nota(nota)

    #Getter
    def get_nota(self):
        return self.__nota

    #Setter
    def set_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Nota invalida! A nota deve estar entre 0 e 10.")

    def situacao(self):
        if self.__nota >= 6:
            return "Aprovado"

        elif self.__nota >= 4:
            return "Recuperação"

        else:
            return "Reprovado"

    def exibir_info(self):
        print("=" * 30)
        print(f"Aluno: {self.nome}")
        print(f"Nota: {self.get_nota()}")
        print(f"Situação: {self.situacao()}")

a1 = Aluno("Weslley", 10.0)
a1.exibir_info()

a2= Aluno("Jullya", 5.0)
a2.exibir_info()

a3= Aluno("Kauã", 3.0)
a3.exibir_info()