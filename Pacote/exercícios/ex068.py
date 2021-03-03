from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(1, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I]')).strip().upper()
    print(f'O computador jogou {computador}')
    if escolha == 'P':
        if total % 2 == 1:
            print(f'Você perdeu! {jogador} + {computador} = {total}')
            break
        else:
            print(f'Você ganhou! {jogador} + {computador} = {total}')
            v += 1
    elif escolha == 'I':
        if total % 2 == 0:
            print(f'Você perdeu! {jogador} + {computador} = {total}')
            break
        else:
            print(f'Você ganhou! {jogador} + {computador} = {total}')
            v += 1

    else:
        print('Código inválido.')
    print(' ')
print(f'Parabéns! Você ganhou {v} partidas!')
