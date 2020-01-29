print('********* Forca!! *********')
forca = 'banana'
palavra = list(forca)
resultado = {}
erros = []
total_acertos = 0
acertos = ['_'] * len(palavra)
for i in palavra:  # loop na quantidade de perguntas por letra na palavra
    chute = input('advinhe uma letra\n')[0:1]  # filtra só uma letra do que for inputado
    if palavra.count(chute) == 0:  # verifica se o chute existe
        erros.extend(chute)  # adiciona o chute errado a lista de erros
        print(f'Letra {chute} nao existe\n')  # avisa do chute errado
        print(f'Letras erradas: {erros}\n')  # exibe lista com os chutes errados
    else:
        print(f'A letra {chute} existe!\n')  # confirma exibiçao de chute certo
        total_acertos = total_acertos + palavra.count(chute)  # adiciona a quantidade de letras acertadas
        for indice, letra in enumerate(palavra):
            if chute == palavra[indice]:
                acertos[indice] = letra
        if total_acertos == len(palavra):  # se acertou todas as letras, exibe a palvra por inteiro
            print(f'Você acertou!! A palavra é {palavra}')
            break
        else:
            print(acertos)
