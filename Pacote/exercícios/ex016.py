from math import trunc
n1 = float(input('digite um número decimal(com ponto): '))
print('a porção inteira de \033[1;34m{}\033[m é \033[1;36m{}\033[m.'.format(n1, trunc(n1)))
