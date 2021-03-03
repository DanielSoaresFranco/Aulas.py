s = 0
m = 0
for c in range(1, 7):
    n = int(input('{}° Número: '.format(c)))
    if n % 2 == 0:
        s += n
        m += 1
print('A soma dos {} valores pares digitados é {}'.format(m, s))
