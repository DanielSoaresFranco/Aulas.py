def dobro(n=0, f=False):
    res = n * 2
    return res if not f else moeda(res)


def metade(n=0, f=False):
    res = n / 2
    return res if not f else moeda(res)


def aumentar(n1=0, n2=0, f=False):
    res = n1 + (n1 * n2 / 100)
    return res if not f else moeda(res)


def diminuir(n1=0, n2=0, f=False):
    res = n1 - (n1 * n2 / 100)
    return res if not f else moeda(res)


def moeda(n=0.0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
