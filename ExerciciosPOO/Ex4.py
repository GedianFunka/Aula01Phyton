class Turma:

    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def Matricular(self, nome_aluno):
        if nome_aluno in self.alunos:
            print("-" * 32)
            print(f'O nome {nome_aluno} já existe na lista de alunos')
        else:
            self.alunos.append(nome_aluno)

    def RemoverAluno(self, nome_aluno):
        if nome_aluno in self.alunos:
            self.alunos.remove(nome_aluno)
        else:
            print(f'O nome {nome_aluno}, não existe na lista de alunos')
        print("-" * 32)

    def ListarAlunos(self):
        contador = 0
        for alunos in sorted(self.alunos):
            print(alunos)
            contador += 1
        print(f'Total de alunos na lista de alunos: {contador}')

    def EstaMatruculado(self, nome_aluno):
        print("-" * 32)
        if nome_aluno in self.alunos:
            print(f'TRUE, o nome {nome_aluno} está na lista de alunos')
        else:
            print(f'FALSE, o nome {nome_aluno} não existe na lista de alunos')
turma1 = Turma("DS")
print(f'Listando os nomes da turma de {turma1.nome}')
turma1.Matricular("Gedian")
turma1.Matricular("Gedian")
turma1.Matricular("Kauã")
turma1.Matricular("Weslley")
turma1.Matricular("Willian")

print("-" * 32)

turma1.ListarAlunos()

turma1.RemoverAluno("Kauã")

turma1.ListarAlunos()

turma1.EstaMatruculado("Kauã")
