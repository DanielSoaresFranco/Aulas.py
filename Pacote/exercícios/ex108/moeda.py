def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def aumentar(n1=0, n2=0):
    res = n1 + (n1 * n2 / 100)
    return res


def diminuir(n1=0, n2=0):
    res = n1 - (n1 * n2 / 100)
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
