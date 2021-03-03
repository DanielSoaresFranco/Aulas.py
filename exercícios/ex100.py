from random import randint


def sorteia(n):
    print('Sorteando os números:', end=' ')
    for c in range(0, 5):
        n.append(randint(0, 10))
        print(n[c], end=' ')
    print()


def somaPar(n):
    soma = 0
    for c in range(0, len(n)):
        if n[c] % 2 == 0:
            soma += n[c]
    print(f'A soma dos valores pares é {soma}')


números = []
sorteia(números)
somaPar(números)
