def fatorial(n):
    f = 1
    for c in range(0, n):
        f *= (c + 1)
    return f


num = int(input('Digite um número:'))