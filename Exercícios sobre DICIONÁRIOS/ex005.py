"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
"""

galera = []
pessoa = {}

while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  pessoa['sexo'] = str(input('Sexo: [M/F] ' )).strip().upper()[0]
  pessoa['idade'] = int(input('Idade: '))
  galera.append(pessoa.copy())
  op = input('Deseja continuar? [S/N] ').strip().upper()[0]
  while op not in 'SN':
    op = input('Opção inválida. Digite [S/N]').strip().upper()[0]
    if op == 'S':
      break
  if op == 'N':
    break

idade = []
for i in galera:
  idade.append(i['idade'])
media = sum(idade) / len(idade)
mulheres = []
idadeMaior = []

for i in galera:
  if i['idade'] > media:
    idadeMaior.append(i['nome'])
  elif i['sexo'] == 'F':
    mulheres.append(i['nome'])

print('=-'*15)
print(f'{len(galera)} pessoas foram cadastradas.')
print(f'A média de idade é {media}')
print(f'As mulheres cadastradas foram: ', end = '')
for i, mulher in enumerate(mulheres):
    if i < len(mulheres) - 1:
        print(mulher, end=", ")
    else:
        print(mulher)
print(f'Idades acima da média: ', end = '')
for i, nome in enumerate(idadeMaior):
    if i < len(idadeMaior) - 1:
        print(nome, end=", ")
    else:
        print(nome)