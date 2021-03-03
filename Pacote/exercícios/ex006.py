n1 = int(input('digite um número: '))
print('dobro: \033[7;30m{}\033[m \ntriplo: \033[7;31m{}\033[m \nraiz quadrada: \033[7;32m{:.2f}\033[m'.format(n1*2, n1*3, n1**(1/2)))
