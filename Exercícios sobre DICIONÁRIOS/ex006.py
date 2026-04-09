"""
Aprimore o ex004 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogadores = []
jogador = {}
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
    gols = []
    for c in range (0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols ele marcou na {c + 1}ª partida?')))
    jogador['gols'] = gols
    jogador['total_gols'] = sum(gols)
    jogadores.append(jogador.copy())
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Opção inválida. Digite [S] ou [N]. ')).upper().strip()[0]
    if op == 'N':
        break

print(f"{'ID':>4} {'Nome':<15} {'Gols':<20} {'Total':>5}")
print('-'*50)

for i, dados in enumerate(jogadores):
    gols_str = ', '.join(map(str, dados['gols']))
    print(f"{i:>4} {dados['nome']:<15} {gols_str:<20} {dados['total_gols']:>5}")

print('-'*50)

while True:
    i = int(input('Deseja mostrar os dados de qual jogador? (999 para sair) '))
    while i >= len(jogadores) and i != 999:
        i = int(input(f'Não existe jogador com o ID {i}, tente novamente. '))
    if i == 999:
        break
    print(f"--- LEVANTAMENTO DO JOGADOR {jogadores[i]['nome']}:")
    for c, gol in enumerate(jogadores[i]['gols']):
        print(f"No jogo {c + 1}, fez {gol} gols.")
print('< ENCERRANDO... >')