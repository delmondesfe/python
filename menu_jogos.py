import forca
import adivinhacao

print('Escolho o seu jogo: ')

print('1 - Adivinhação\n2 - Forca')

jogo = int(input('Escolha o jogo: '))

if(jogo ==1):
    print('Jogando adivinhação')
    adivinhacao.jogar()
elif(jogo ==2):
    print('Jogando Forca')
    forca.jogar()