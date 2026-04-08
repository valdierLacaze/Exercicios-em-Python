"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
dados = {}
dados['nome'] = str(input('Digite o nome do jogador: '))
dados['partidas'] = int(input('Quantas partidas ele jogou? '))
gols = []
for c in range (0, dados['partidas']):
    gols.append(int(input(f'Quantos gols ele marcou na {c + 1}ª partida?')))
dados['gols'] = gols
dados['total_gols'] = sum(gols)

print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas.")
for i, gol in enumerate(gols):
    print(f"Na {i + 1}ª partida, {dados['nome']} fez {gol} gols.")
print(f"O total de gols feito por {dados['nome']} foi {dados['total_gols']}.")