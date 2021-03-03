s = c = 0
n = int(input('Digite um número (Digite 999 para parar): '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número (Digite 999 para parar): '))
print('A soma dos {} números digitados é {}'.format(c, s))
