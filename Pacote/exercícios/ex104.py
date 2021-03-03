def leiaInt(msg):
    num = input(msg)
    if num.isnumeric():
        print(f'Você digitou o número {num}.')
        return True
    else:
        print('\033[1;31mERRO! Digite um número inteiro\033[m')
        return False


n = leiaInt('Digite um n: ')
while not n:
    n = leiaInt('Digite um n: ')
print('Esse valor é inteiro.')
