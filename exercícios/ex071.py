notas50 = notas20 = notas10 = notas1 = 0
print('-' * 30)
print('Caixa eletrônico com sistema DANI: sistema de \nDistribuição \nAutomatizada de \nNotas \nIntegrado.')
print('-' * 30)
valor = int(input('Digite o valor a ser sacado: '))
while True:
    if valor >= 50:
        notas50 += 1
        valor -= 50
    elif valor >= 20:
        notas20 += 1
        valor -= 20
    elif valor >= 10:
        notas10 += 1
        valor -= 10
    elif valor >= 1:
        notas1 += 1
        valor -= 1
    else:
        break
print('Para esse valor serão necessárias: ')
if notas50 > 0:
    print(f'{notas50} notas de 50 reais')
if notas20 > 0:
    print(f'{notas20} notas de 20 reais')
if notas10 > 0:
    print(f'{notas10} notas de 10 reais')
if notas1 > 0:
    print(f'{notas1} notas de 1 real')
print('Volte sempre!')