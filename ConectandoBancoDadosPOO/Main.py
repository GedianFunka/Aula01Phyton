import Produtos
from Models import Produto

def exibir_lista(lista):
    if lista:
        for produto in lista:
            produto.exibir()
    else:
        print("Nenhum produto encontrado")

def menu():
    while True:
        print("\n ===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar preço")
        print("5 - Excluir produto")
        print("0 - SAIR")

        opcao = input("Opcao: ")

        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preco: "))
            quantidade = int(input("Quantidade: "))
            categoria = input("Categoria: ")

            novo_produto = Produto(nome, preco, quantidade, categoria)
            Produtos.cadastrar_produto(novo_produto)

        elif opcao == "2":
            exibir_lista(Produtos.listar_produto())

        elif opcao == "3":
            termo = input("Buscar nome: ")
            exibir_lista(Produtos.buscar_produto(termo))

        elif opcao == "4":
            pid = int(input("ID produto:"))
            novo = float(input("Novo preco:"))
            Produtos.atualizar_preco(pid, novo)

        elif opcao == "5":
            pid = int(input("ID produto:"))
            Produtos.excluir_produto(pid)

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

menu()