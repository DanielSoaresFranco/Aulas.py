r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('Essas retas podem formar um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Essas retas podem formar um triângulo isósceles.')
    else:
        print('Essas retas podem formar um triângulo escaleno.')
else:
    print('Essas retas não podem formar um triângulo')
