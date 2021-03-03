def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número passado, podendo ou não mostrar a conta
    :param num: fatorial escolhido
    :param show: (opcional)se quer ou não mostrar a multiplicação na tela
    :return: se show=True, mostra a conta e o resultado, senão mostra apenas a conta
    """
    f = 1
    print('-' * 30)
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)


n = int(input('Digite um número para saber seu fatorial: '))
fatorial(n, show=True)
