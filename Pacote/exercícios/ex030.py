n1 = int(input('Digite o número: '))
n2 = n1 % 2
if n1 == 0:
    print('Número inválido')
elif n2 == 1:
    print('O número {} é ímpar'.format(n1))
else:
    print('O número {} é par'.format(n1))
