def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = "python"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False
    
    print("A palavra secreta contem {} letras".format(len(letras_acertadas)))
    print(letras_acertadas)
    
    while (not enforcou and not acertou ):
        
        chute = input ("Qual a letra?: ")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
                   
        
        
        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()