import Banco
import Produtos
import Relatorio

Banco.criar_tabela()

def menu():
    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar preço")
        print("5 - Excluir produto")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            cat = input("Categoria: ")
            Produtos.cadastrar_produto(nome, preco, qtd, cat)
        elif opcao == "2":
            Produtos.listar_produtos()
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            Produtos.buscar_produto(termo)
        elif opcao == "4":
            pid = int(input("ID do produto: "))
            novo = float(input("Novo preço: "))
            Produtos.atualizar_preco(pid, novo)
        elif opcao == "5":
            pid = int(input("ID do produto: "))
            Produtos.excluir_produto(pid)
        elif opcao == "6":
            Relatorio.total_produtos()
        elif opcao == "7":
            Relatorio.valor_total_estoque()
        elif opcao == "8":
            Relatorio.produto_mais_caro()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

#--- Chamado das funções ---
#criar_tabela()          #executar uma unica vez

menu()                   #executa de modo recorrente