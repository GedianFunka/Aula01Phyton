import random

numero = random.randint(0,100)
tentativas = 5

while tentativas > 0:
    palpites = int(input("Digite um numero entre 0 e 100: "))

    if palpites == numero:
        print("Parabens, voce acertou o numero!")
        break

    elif palpites < numero:
        print("O numero é maior que o seu palpite.")
        tentativas = tentativas - 1
        print(f"tentativas restantes: {tentativas}")
    else:
        print("O numero é menor que o seu palpite.")
        tentativas = tentativas - 1
        print(f"tentativas restantes: {tentativas}")

else:
        print("Suas tentativas acabaram.")
        print(f"O numero correto era {numero}.")