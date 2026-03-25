from random import randint
quant = int(input('Quantos jogos serão gerados? '))
jogos = []
numeros = []
for count in range (0, quant): #Faz o jogo de 0 até a quantidade escolhida
    while len(numeros) < 6: #Enquanto o tamanho da lista "numeros" for menor que 6:
        num = randint(1, 61) #Gera um número inteiro de 1 a 60
        if num not in numeros: #Se o número gerado não estiver na lista "numeros":
            numeros.append(num) #Adicionar o número gerado na lista "numeros"
    jogos.append(numeros[:]) #Adicionar os numeros na lista "jogos"
    numeros.clear() #Limpar a lista numeros para iniciar novamente o laço.
for c in range (0, quant):
    print(f'Jogo {c+1}: {sorted(jogos[c])}')