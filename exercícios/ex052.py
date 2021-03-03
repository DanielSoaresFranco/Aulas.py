n1 = int(input('Número: '))
t = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[1;33m', end='')
        t += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')
print(' ')
print('O número {} foi divisível {} vezes'.format(n1, t))
if t == 2:
    print('E por isso o número {} é primo'.format(n1))
else:
    print('E por isso o número {} não é primo'.format(n1))
