Joao = 0
Ana = 0
Pedro = 0
voto = 0

while voto != 4:
    print("Escolha um dos candidatos : 1 - Joao; 2 - Ana; 3 - Pedro; 4 - Encerrar")
    voto = int(input("Digite seu voto: "))
    if voto == 1:
        Joao = Joao + 1
    elif voto == 2:
        Ana = Ana + 1
    elif voto == 3:
        Pedro = Pedro + 1
    elif voto == 4:
        print("\nVotacao encerrada")

print("Resultado da eleição:")
print("Voto: ",Joao)
print("Voto: ",Ana)
print("Voto: ",Pedro)
print("Total de votos: ",Joao + Ana + Pedro)

if Joao > Ana and Joao > Pedro:
    print("O vencedor é Joao")
elif Ana > Joao and Ana > Pedro:
    print("O vencedor é Ana")
elif Pedro > Joao and Pedro > Ana:
    print("O vencedor é Pedro")

