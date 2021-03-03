pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
ta = pt
while c != 10:
    print('{} -> '.format(ta), end='')
    ta += r
    c += 1
print('Acabou')
