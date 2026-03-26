"""
Crie um programa que leia uma nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo média de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente
Minha resolução:
"""


alunos = []
dados = []
while True:
    nome = str(input('Qual é o nome do aluno? '))
    nota1 = float(input('Qual foi a primeira nota? '))
    nota2 = float(input('Qual foi a segunda nota? '))
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    alunos.append(dados[:])
    dados.clear()
    op = input('Você deseja continuar? [S]/[N] ').upper().strip()[0]
    while op not in 'SN':
        op = input('Opção inválida. Você deseja continuar? [S]/[N]').upper().strip()[0]
        if op in 'SN':
            break
        else:
            continue
    if op == 'S':
        continue
    else:
        break
texto = 'MEDIA DOS ALUNOS'
medias = []
print('-=' * 20)
print(f'{texto:^40}')
print('-='*20)
for i, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f'Aluno {i:<3}: {aluno[0]:<20} {media:>5.1f}')
while True:
    op = int(input('Digite o número do aluno que você deseja ver a nota ou 999 para cancelar. '))
    if op == 999:
        print('Saindo...')
        break
    if op >= 0 and op < len(alunos):
        print(f'Notas de {alunos[op][0]} são {alunos[op][1]} e {alunos[op][2]}')
    else:
        print(f'Erro! Não existe aluno com o código {op}. Tente novamente.')