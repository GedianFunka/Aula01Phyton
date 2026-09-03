class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir(self):
        print((f"Nome: {self.nome}, Email: {self.email}, telefone: {self.telefone}"))

    def converter_tupla(self):
        return (self.nome, self.email, self.telefone)

    @staticmethod
    def reverte_tupla(tupla):
        cliente = Cliente(
            nome = tupla[1],
            email = tupla[2],
            telefone = tupla[3]
        )

        cliente.id = tupla[0]
        return cliente

c1 = Cliente("Gedian" , "gediangabrielf@gmail.com", "(47) 992165428")
c2 = Cliente("Kauã", "Kaua_miguel@gmail.com", "(47) 991544034")

c1.exibir()
c2.exibir()

c3 = Cliente.reverte_tupla((5, "Weslley", "weslley.@gmail.com", "(47) 991544034"))
c3.exibir()