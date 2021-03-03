aprov = {
    'nome': str(input('Digite o nome do jogador: ')),
    'jogos': int(input('Quantos jogos ele jogou? ')),
    'gols no campeonato': 0,
    'gols_jogos': [],
    'aproveitamento': 0
}
firula = '-=' * 40
for c in range(0, aprov['jogos']):
    aprov['gols_jogos'].append(int(input(f'Quantos gols no jogo {c + 1}? ')))
    aprov['gols no campeonato'] += aprov['gols_jogos'][c]
aprov['aproveitamento'] = aprov['gols no campeonato'] / aprov['jogos']
print(f"""{firula}
{aprov}
{firula}
O nome é {aprov['nome']}.
os gols são {aprov['gols_jogos']}
foi um total de {aprov['gols no campeonato']},
sendo aproximadamente {aprov['aproveitamento']} gols por partida
{firula}
O jogador {aprov['nome']} jogou {aprov['jogos']} partidas.""")
c = 1
for g in aprov['gols_jogos']:
    print(f'Na partida {c} ele fez {g} gols')
    c += 1
print(f'Foi um total de {aprov["gols no campeonato"]} gols')
