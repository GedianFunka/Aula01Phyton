numero = int(input("Digite um numero para saber se ele e primo: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores = divisores + 1

if divisores == 2:
        print(f"O numero {numero} é primo")
else:
        print(f"O numero {numero} não é primo")