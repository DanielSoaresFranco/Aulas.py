c = 0
while True:
    n1 = int(input('Digite um número (digite número negativo para parar o programa): '))
    if n1 < 0:
        print('Programa encerrado.')
        break
    else:
        while c != 10:
            c += 1
            n2 = n1 * c
            print(f'{n1} x {c} = {n2}')
        c = 0