class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    #Getter
    def get_estoque(self):
        return self.__estoque

    def adiciona_estoque(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            print(f"{quantidade} unidades adicionadas ao estoque.")
        else:
            print("Quantidade inválida para ser adicionada no estoque. A quantidade deve ser maior que zero.")

    def vender_estoque(self, quantidadeVendido):
        if quantidadeVendido > 0 and quantidadeVendido <= self.__estoque:
            self.__estoque -= quantidadeVendido
            print(f"{quantidadeVendido} unidades vendidas.")
        else:
            print("Quantidade inválida para ser vendida. Verifique o estoque disponível.")

    def exibir_info(self):
        print("=" * 30)
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Estoque: {self.get_estoque()} unidades")
        print("=" * 30)

p1 = Produto("Notebook", 3500.00, 10)
p1.adiciona_estoque(-5)
p1.vender_estoque(3)
p1.exibir_info()

p2 = Produto("Mouse", 100.00, 20)
p2.adiciona_estoque(10)
p2.vender_estoque(32)
p2.exibir_info()