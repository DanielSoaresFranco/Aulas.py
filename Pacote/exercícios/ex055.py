maior = 0
menor = 0
for c in range(0, 5):
    peso = int(input('Digite o peso da {}ª pessoa em kg: '.format(c + 1)))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi {:.1f} kg e o menor foi {:.1f} kg'.format(maior, menor))
