from random import choice
from time import sleep

jogadas = [1, 2, 3]
print('\033[1;36mVAMOS JOGAR JOKENPÔ/PEDRA, PAPEL E TESOURA!\033[m')
nome = int(input('\033[1;33mComo você chama o jogo? \n1 = JOKENPÔ, \n2 = PEDRA PAPEL TESOURA \033[m'))

jogada_jogador = int(input('\033[1;35mQual seu lance? \n1 para pedra, 2 para papel e 3 para tesoura: \033[m'))
jogada_computador = choice(jogadas)

if nome == 1:
    print('\033[1;31mJO\033[m')
    sleep(1)
    print('\033[1;33mKEN\033[m')
    sleep(1)
    print('\033[1;32mPÔ!\033[m')
    sleep(1)
elif nome == 2:
    print('\033[1;31mPEDRA\033[m')
    sleep(1)
    print('\033[1;33mPAPEL\033[m')
    sleep(1)
    print('\033[1;32mTESOURA!\033[m')
    sleep(1)
else:
    sleep(1)

if jogada_jogador == 1 and jogada_computador == 1:
    print('\033[1;33m-=' * 20, '-')
    print('EMPATE!!! você tirou pedra e o computador também!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 1 and jogada_computador == 2:
    print('\033[1;31m-=' * 20, '-')
    print('O COMPUTADOR GANHOU!!! Você tirou pedra e o computador tirou papel!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 1 and jogada_computador == 3:
    print('\033[1;32m-=' * 20, '-')
    print('VOCÊ GANHOU!!! Você tirou pedra e o computador tirou tesoura!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 2 and jogada_computador == 1:
    print('\033[1;32m-=' * 20, '-')
    print('VOCÊ GANHOU!!! Você tirou papel e o computador tirou pedra!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 2 and jogada_computador == 2:
    print('\033[1;33m-=' * 20, '-')
    print('EMPATE!!! Você tirou papel e o computador também!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 2 and jogada_computador == 3:
    print('\033[1;31m-=' * 20, '-')
    print('O COMPUTADOR GANHOU!!! Você tirou papel e o computador tirou tesoura!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 3 and jogada_computador == 1:
    print('\033[1;31m-=' * 20, '-')
    print('O COMPUTADOR GANHOU!!! Você tirou tesoura e o computador jogou pedra!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 3 and jogada_computador == 2:
    print('\033[1;32m-=' * 20, '-')
    print('VOCÊ GANHOU!!! Você tirou tesoura e o computador tirou papel!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador == 3 and jogada_computador == 3:
    print('\033[1;33m-=' * 20, '-')
    print('EMPATE!!! Você tirou tesoura e o computador também!')
    print('-=' * 20, '-\033[m')
elif jogada_jogador < 1 or jogada_jogador > 3:
    print('\033[1;31m-=' * 20, '-')
    print('Ei! Essa jogada não vale!')
    print('-=' * 20, '-\033[m')
