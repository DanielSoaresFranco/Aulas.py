from random import randint
from time import sleep

print('\033[1;34mVAMOS JOGAR O JOGO DA ADIVINHAÇÃO!!!')
print(' ')
print('\033[1;33mTENTE ADIVINHAR O NÚMERO QUE EU PENSAR ENTRE 0 E 10!')
print(' ')

palpite = int(input('AQUI VAI O SEU PALPITE: \033[m'))
número = randint(0, 10)

print(' ')

a = 0

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

print('\033[1;32mVOCÊ ACERTOU COM APENAS {} TENTATIVAS!!! PARABÉNS!!!\033[m'.format(a + 1))