"""
Faça uma matriz 3x3 com inputs e listas;
Mostre a soma dos números pares da matriz, a soma dos valores da terceira coluna e o maior
valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range (0, 3):
    for c in range (0, 3):
        if c == 2:
            print(f'[{matriz[l][c]:^5}]')
        else:
            print(f'[{matriz[l][c]:^5}]', end = '')

soma = 0
soma3 = 0
maior2Linha = max(matriz[1])
for l in range (0, 3):
    for c in range (0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
print(f'A soma dos números pares na matriz é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior2Linha}')