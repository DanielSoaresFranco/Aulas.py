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


def resumo(n=0, aum=10, dim=5):
    from utilidades_daniel import mensagem
    mensagem('\033[m', '     RESUMO DO VALOR      ', '-')
    print(f'Preço analisado: \t{moeda(n):>10}')
    print(f'Dobro do preço: \t{dobro(n, True):>10}')
    print(f'Metade do preço: \t{metade(n, True):>10}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True):>10}')
    print(f'{dim}% de diminuição: \t{diminuir(n, dim, True):>10}')
    print('-' * 30)