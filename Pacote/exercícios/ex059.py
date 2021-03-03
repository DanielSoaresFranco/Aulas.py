from time import sleep

n = 1
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
while n != 5:
    print(' ')
    n = int(input("""Digite a operação: 
    [ 1 ] = Soma
    [ 2 ] = Multiplicação
    [ 3 ] = Verificar qual é o maior
    [ 4 ] = Digitar novos números
    [ 5 ] = Sair do programa
    Escolha: """))
    print(' ')
    if n == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif n == 2:
        print('O produto entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    elif n == 3:
        if n1 > n2:
            print('{} é maior do que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior do que {}'.format(n2, n1))
        else:
            print('{} e {} são iguais'.format(n1, n2))
    elif n == 4:
        print('Ok. Processando...')
        sleep(1)
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif n == 5:
        print('Ok. Encerrando...')
        sleep(3)
    else:
        print('Código inválido. Tente novamente.')
    print('=-=' * 10)
print('Programa finalizado. Volte sempre!')