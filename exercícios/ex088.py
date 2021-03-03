from random import randint
from time import sleep
palpites = []
palpite = []
print('=' * 40)
print(f'{"< Simulador mega sena >":-^40}')
print('=' * 40)
num_palpites = int(input('Quantos jogos eu devo sortear? '))
print('\n', '=' * 10, f' SORTEANDO {num_palpites} JOGOS ', '=' * 10)
for c in range(0, num_palpites):
    palpite.clear()
    while True:
        n = randint(1, 60)
        if n not in palpites:
            palpite.append(n)
        if len(palpite) == 6:
            palpites.append(palpite[:])
            break
    palpite.sort()
    sleep(1)
    print(f'Jogo {c + 1}: {palpite}')
sleep(1)
print(f'{" < BOA SORTE! > ":=^40}')
