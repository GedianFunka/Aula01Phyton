agenda = {}

while True:
    print("\n1- Cadastrar")
    print("2- Consultar")
    print("3- Listar contatos")
    print("4- Sair")

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
        print("Sair")
        break