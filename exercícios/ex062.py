pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = 2
c = 0
nt = 10
ta = pt
while c != 10:
    t2 = str('{} -> '.format(ta))
    print(t2)
    ta += r
    c += 1
t = int(input('Quer mostrar mais quantos termos? '))
nt += t
while t > 0:
    while t > 0:
        t2 = str('{} -> '.format(ta))
        ta += r
        print(t2)
        t -= 1
    t = int(input('Quer mostrar mais quantos termos? '))
    nt += t
print('Você recebeu {} termos da PA'.format(nt))
