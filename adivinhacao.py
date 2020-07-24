import random
def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("**********************************")



    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('1 - Fácil\n2 - Médio\n3 - Difícil')

    print (numero_secreto) #mostrando o número random

    nivel = int(input('Escolha o nível de dificuldade: '))

    if(nivel == 1):
        tentativas = 20
    elif(nivel ==2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada,tentativas))
        numero_usuario = int(input("Digite o número entre 1 e 100: "))
    
        if (numero_usuario < 1 or numero_usuario > 100):
            print('NUMERO INVALIDO, Favor digitar um número entre 1 e 100')
            continue
    
        acertou = numero_secreto == numero_usuario
        maior = numero_usuario > numero_secreto
        menor = numero_usuario < numero_secreto

        if (acertou):
            print("Você acertou, o numero é {} e fez {} pontos: ".format(numero_secreto,pontos))
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o número secreto')
            elif(menor):
                print('Você erro! O seu chute foi menor que o número secreto')
            pontos_perdidos = abs(numero_secreto - numero_usuario)
            pontos = pontos_perdidos

    print("Fim de jogo")