print("**********************************")
print("Bem vindo ao jogo de adivinhação")
print("**********************************")

numero_secreto = 42
tentativas = 3
rodada = 1

while(rodada <= tentativas):
    print("Tentativa {} de {}".format(rodada,tentativas))
    numero_usuario = int(input("Digite o número secreto: "))
    acertou = numero_secreto == numero_usuario
    maior = numero_usuario > numero_secreto
    menor = numero_usuario < numero_secreto

    if (acertou):
        print("Você acertou o número da máquina: ",numero_secreto)
    elif (maior):
        print("Você errou, seu número é maior que o número secreto")
    else:
        print("Você errou, seu número é menor que o número secreto")

    rodada = rodada + 1

print("Fim de jogo")

