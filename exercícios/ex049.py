n1 = int(input('Qual tabuada? '))
n2 = int(input('Multiplicar até que número? '))
for c in range(1, n2 + 1):
    print('| {} X {} = {}'.format(c, n1, c * n1))
