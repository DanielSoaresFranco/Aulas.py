from random import randint
from time import sleep

print('\033[1;36mTENTE ADIVINHAR O NÚMERO QUE EU PENSAR ENTRE 0 E 5!!!\033[m')  # Graça
n1 = randint(0, 5)  # Número do computador
n2 = int(input('\033[1;35mAQUI VAI O SEU PALPITE: \033[m'))  # Número do jogador
print('\033[1;33mPROCESSANDO...\033[m')
sleep(3)
if n2 == n1:
    print('\033[1;32mACERTOU!!! PARABÉNS!!!\033[m')
elif n2 < 0 or n2 > 5:
    print('\033[1;31mEi! Essa jogada não vale!\033[m')
else:
    print('\033[1;31mERROU!!! TENTE NOVAMENTE!!!\033[m')
    print('\033[31mO NÚMERO ERA {} E NÃO {}\033[m'.format(n1, n2))
