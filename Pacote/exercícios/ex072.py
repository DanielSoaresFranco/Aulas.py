números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if -1 < n < 21:
            break
        print('Tente novamente.', end=' ')
    print(' ')
    print(f'Você digitou o número {números[n]}')
    print(' ')
    cont = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
    print(' ')
    if cont == 'n':
        print('Programa encerrado. Volte sempre!')
        break
