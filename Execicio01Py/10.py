loginCerto = "Gedian"
senhaCerto = "1234"

tentativas = 5

while tentativas > 0:
    login = str(input("Login: "))
    senha = str(input("Senha: "))

    if login == loginCerto and senha == senhaCerto:
        print("Acesso concedido.")
        break
    else:
        tentativas = tentativas - 1
        print("Login ou senha incorretos. Tente novamente.")
        print(tentativas)
else:
    print("\nNúmero máximo de tentativas excedido.")