agenda = {}

while True:
    print("\n1- Cadastrar")
    print("2- Consultar")
    print("3- Listar contatos")
    print("4- Pesquisar por letra")
    print("5- Excluir contato")
    print("6- Sair")

    opcao = (input("Digite uma opcao: "))

    if opcao == "1":
        nome = input("\nDigite o nome: ")
        if nome in agenda:
            print("O nome já está na agenda")
        else:
            while True:
                telefone = input("Digite o telefone: ")
                if telefone != "":
                        break
                print("Telefone Obrigatorio")
            agenda[nome] = telefone
            print("Contato cadastrado")

    elif opcao == "2":
        nome = input("Digite o nome para ser buscado: ")
        if nome in agenda:
            print("\nTelefone", agenda[nome])
        else:
            print("Contato não encontrado")

    elif opcao == "3":
        if len(agenda) == 0:
            print("Agenda Vazia")
        else:
            print("\nContatos cadastrados")
            contador = 1
            #For que percorre dois argumentos
            for nome, telefone in agenda.items():
                print(f"{contador} - {nome}: {telefone}")
                contador += 1

    elif opcao == "4":
        letra = input("Digite a letra inicial: ").upper()
        encontrou = False

        for nome, telefone in agenda.items():
            if nome.upper().startswith(letra):
                print(f"{nome} - {telefone}")
                encontrou = True
        if not encontrou:
            print("Nenhum contato encontrado com a letra inicial informada")

    elif opcao == "5":
        nomeex = input("\nDigite o nome: ")

        if nomeex in agenda:
            del agenda[nomeex]
            print("Contato excluído")
        else:
            print("Contato não encontrado")

    elif opcao == "6":
        print("Sair")
        break