r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
m1 = 'Essas retas podem formar um triângulo'
m2 = 'Essas retas não podem formar um triângulo'

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(m1)
else:
    print(m2)
