from random import choice, randint
from time import sleep
from utilidades_daniel import mensagem


def jokenpô():
    mensagem('\033[1;36m', 'VAMOS JOGAR JOKENPÔ/PEDRA, PAPEL E TESOURA!', '~')
    nome = int(input(mensagem('\033[1;33m', 'Como você chama o jogo? \n1 = JOKENPÔ, \n2 = PEDRA PAPEL TESOURA')))
    n_jogos = int(input('\033[1;34mQuantas partidas? \033[m'))
    print(' ')
    vitoria = 0
    derrota = 0
    e = 0
    f = False
    for a in range(n_jogos):
        jogadas = [1, 2, 3]
        jogada_jogador = int(
            input(mensagem('\033[1;35m', 'Qual seu lance? \n1 para pedra, 2 para papel e 3 para tesoura: ')))
        jogada_computador = choice(jogadas)
        if nome == 1:
            print('\033[1;31mJO')
            sleep(1)
            print('\033[1;33mKEN')
            sleep(1)
            print('\033[1;32mPÔ!')
            sleep(1)
        elif nome == 2:
            mensagem('\033[1;31m', 'PEDRA')
            sleep(1)
            mensagem('\033[1;33m', 'PAPEL')
            sleep(1)
            mensagem('\033[1;32m', 'TESOURA!')
            sleep(1)
        else:
            sleep(1)
        if jogada_jogador == 1 and jogada_computador == 1 or jogada_jogador == 2 and jogada_computador == 2 or jogada_jogador == 3 and jogada_computador == 3:
            mensagem('\033[1;33m', 'EMPATE!!! Você tirou pedra e o computador também!', '-=')
            e = e + 1
        elif jogada_jogador == 1 and jogada_computador == 2 or jogada_jogador == 2 and jogada_computador == 3 or jogada_jogador == 3 and jogada_computador == 1:
            mensagem('\033[1;31m', 'O COMPUTADOR GANHOU!!! Você tirou pedra e o computador tirou papel!', '-=')
            derrota = derrota + 1
        elif jogada_jogador == 1 and jogada_computador == 3 or jogada_jogador == 2 and jogada_computador == 1 or jogada_jogador == 3 and jogada_computador == 2:
            mensagem('\033[1;32m-=', 'VOCÊ GANHOU!!! Você tirou pedra e o computador tirou tesoura!', '-=')
            vitoria = vitoria + 1
        elif jogada_jogador < 1 or jogada_jogador > 3:
            mensagem('\033[1;31m', 'Ei! Essa jogada não vale!', '-=')
            f = True
        print(' ')
    mensagem('\033[1;33m', 'PROCESSANDO RESULTADO...')
    sleep(3)
    if f is True:
        print(' ')
    elif vitoria > derrota:
        mensagem('\033[1;32m', f'VOCÊ VENCEU O COMPUTADOR COM {vitoria} VITÓRIAS, {e} EMPATES E {derrota} DERROTAS!!! Continue jogando assim!\033[m', '~')
    elif derrota > vitoria:
        mensagem('\033[1;31m', f'VOCÊ PERDEU DO COMPUTADOR COM {vitoria} VITÓRIAS, {e} EMPATES E {derrota} DERROTAS!!! \nTente de novo!\033[m', '~')
    else:
        mensagem(
            '\033[1;33m', f'VOCÊ EMPATOU COM O COMPUTADOR COM {vitoria} VITÓRIAS, {e} EMPATES E {derrota} DERROTAS!!! \nJogue de novo, e que vença o melhor!\033[m', '~')


def adivinhação():
    print(' ')
    print('\033[1;34mVAMOS JOGAR O JOGO DA ADIVINHAÇÃO!!!')
    print(' ')
    n_jogos = int(input('\033[1;34mQuantas partidas? '))
    print(' ')
    min_num = int(input('QUAL O VALOR MÍNIMO? '))
    max_num = int(input('QUAL O VALOR MÁXIMO? \033[m'))
    print(' ')
    a = 0

    for c in range(n_jogos):
        print('\033[1;33mTENTE ADIVINHAR O NÚMERO QUE EU PENSAR ENTRE {} E {}!'.format(min_num, max_num))
        print(' ')
        palpite = int(input('AQUI VAI O SEU PALPITE: \033[m'))
        número = randint(min_num, max_num)
        print(' ')
        while palpite != número:

            sleep(2)
            if palpite > número:
                print('\033[1;31mEsse número é muito grande. Pense em um menor.\033[m')
                print(' ')
                palpite = int(input('\033[1;33mNOVO VALOR: \033[m'))
                print(' ')
            elif palpite < número:
                print('\033[1;31mEsse número é muito pequeno. Pense em um maior.')
                print(' ')
                palpite = int(input('\033[1;33mNOVO VALOR: \033[m'))
                print(' ')
            a += 1
        sleep(2)
        print('\033[1;32mVOCÊ ACERTOU em apenas {} tentativas!!! PARABÉNS!!!\033[m'.format(a + 1))
        print(' ')
        a = 0


def par_impar():
    v = 0
    d = 0
    numero_jogos = int(input('\033[1;36mQuantas partidas? \033[m'))
    while numero_jogos > 0:
        numero_jogos -= 1
        print('\033[1;36mVAMOS JOGAR PAR OU ÍMPAR!!!\033[m')
        jog_jog = int(input('\033[1;33mDigite um número: \033[m'))
        par_jog = int(input('\033[1;33mPar ou ímpar? (1 = par, 2 = ímpar) \033[m'))
        jog_comp = randint(1, 10)
        print(f'\033[1;34mO computador jogou {jog_comp}\033[m')
        ver = jog_jog + jog_comp
        if par_jog == 1:
            if ver % 2 == 1:
                print(f'\033[1;31mVocê perdeu! {jog_jog} + {jog_comp} = {ver}\033[m')
                d += 1
            else:
                print(f'\033[1;32mVocê ganhou! {jog_jog} + {jog_comp} = {ver}\033[m')
                v += 1
        elif par_jog == 2:
            if ver % 2 == 0:
                print(f'\033[1;31mVocê perdeu! {jog_jog} + {jog_comp} = {ver}\033[m')
                d += 1
            else:
                print(f'\033[1;32mVocê ganhou! {jog_jog} + {jog_comp} = {ver}\033[m')
                v += 1
        else:
            print('\033[1;31mCódigo inválido.\033[m')
        print(' ')
        if numero_jogos == 0:
            break
    if v > d:
        print(f'\033[1;32mParabéns! Você ganhou {v} partidas, contra {d} vitórias da máquina!\033[m')
    elif v == d:
        print(f'\033[1;33mEmpate! Você ganhou {v} partidas, e o computador também.\033[m')
    else:
        print(f'\033[1;31mQue pena! Você ganhou {v} partidas e o computador ganhou {d}.\033[m')


while True:
    jogo = int(input(mensagem('\033[1;35m', 'Que jogo você quer jogar? Digite:\n1 = jokenpô/pedra papel tesoura, \n2 = jogo da adivinhação ou \n3 = par ou ímpar? ', '-=')))
    if jogo < 1:
        mensagem('\033[1;31m', 'Código inválido.')

    if jogo == 1:
        jogo = 'jokenpô'
    elif jogo == 2:
        jogo = 'adivinhação'
    elif jogo == 3:
        jogo = 'par/ímpar'

    if jogo == 'jokenpô':
        jokenpô()
    elif jogo == 'adivinhação':
        adivinhação()
    elif jogo == 'par/ímpar':
        par_impar()
    else:
        print('\033[1;33mAinda não temos esse jogo.\033[m')
    print('\033[1;32mEm breve teremos mais jogos!\033[m')
    print(' ')
    jog_nov = str(input('\033[1;33mQue tal jogar novamente? (s/n) \033[m')).strip().lower()[0]
    if jog_nov == 'n':
        print('\033[1;32mTudo bem. \nAté a próxima!\033[m')
        break
