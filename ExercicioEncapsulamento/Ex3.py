class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

    #Getter
    def get_senha(self):
        return self.__senha

    def set_senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
        else:
            print("Senha inválida! A senha deve ter pelo menos 6 caracteres.")

    def verificar_senha(self, senha_check):
        if senha_check == self.__senha:
            print("Senha correta!")
        else:
            print("Senha incorreta!")

    def exibir_perfil(self):
        print("=" *30)
        print("Nome:", self.nome)
        print("Email:", self.email)
        print("Senha:", "*" * len(self.__senha))

u1 = Usuario("Gedian", "gedian@email.com", "123456")
u1.set_senha("12345")
u1.exibir_perfil()
u1.verificar_senha("123456")

u2 = Usuario("Kauã", "kaua@email.com", "654321")
u2.set_senha("665485468468")
u2.exibir_perfil()
u2.verificar_senha("6654854684")