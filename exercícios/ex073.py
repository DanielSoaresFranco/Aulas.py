times = (' ', 'Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense',
         'Palmeiras', 'Grêmio', 'Corinthians', 'Red Bull Bragantino', 'Athletico',
         'Santos', 'Ceará', 'Atlético-GO', 'Fortaleza', 'Vasco',
         'Bahia', 'Sport', 'Goiás', 'Coritiba', 'Botafogo')
print('Times do brasileirão: ')
for t in times:
    print(t)
print(' ')
print(f'Os 5 primeiros times são {times[1]}, {times[2]}, {times[3]}, {times[4]} e {times[5]}.')
print(f'Os 4 últimos colocados são {times[-4]}, {times[-3]}, {times[-2]} e {times[-1]}.')
print(f'Times em ordem alfabética: {sorted(times)}')
print('A Chapecoense está na série B.')
