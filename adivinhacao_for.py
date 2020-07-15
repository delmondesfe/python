print("**********************************")
print("Bem vindo ao jogo de adivinhação")
print("**********************************")

numero_secreto = 42
tentativas = 3

for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodada,tentativas))
    numero_usuario = int(input("Digite o número entre 1 e 100: "))
    acertou = numero_secreto == numero_usuario
    maior = numero_usuario > numero_secreto
    menor = numero_usuario < numero_secreto

    if (acertou):
        print("Você acertou o número da máquina: ",numero_secreto)
        break
    elif (maior):
        print("Você errou, seu número é maior que o número secreto")
    else:
        print("Você errou, seu número é menor que o número secreto")

print("Fim de jogo")

