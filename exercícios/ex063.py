num = int(input('Quantos termos? '))
t1 = 0
t2 = 1
c = 0
print('{}'.format(t1), end=' -> ')
print('{}'.format(t2), end=' -> ')
while c < num - 2:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print('{}'.format(t3), end=' -> ')
