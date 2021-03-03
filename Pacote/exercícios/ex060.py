n = int(input('Digite um número para descobrir seu fatorial: '))
fat1 = n
fat2 = fat1 - 1
print('{}! = {} x '.format(n, fat1), end='')
while fat2 >= 1:
    fat1 *= fat2
    if fat2 != 1:
        print('{} x '.format(fat2), end='')
    else:
        print('{} = {}'.format(fat2, fat1))
    fat2 -= 1