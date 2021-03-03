num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número {}...'.format(num))
print('milhares: {}'.format(m))
print('centenas: {}'.format(c))
print('dezenas:  {}'.format(d))
print('unidades: {}'.format(u))
