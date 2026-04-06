"""
Faça um programa que leia o nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'O nome do aluno é {aluno['nome']}.')
print(f'A média de {aluno['nome']} é {aluno['media']}.')
print(f'A situação do aluno é {aluno['situacao']}.')