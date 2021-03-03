n = 1
c = p = i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    c += 1
    if n != 0:
        if n % 2 == 1:
            i += 1
        else:
            p += 1
print('Você digitou {} números! \n{} são ímpares e {} são pares'.format(c, i, p))
print('Acabou')
