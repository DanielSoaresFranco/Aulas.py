pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
for c in range(0, 10):
    print('{} -> '.format(pt), end='')
    pt = pt + r
print('ACABOU')
