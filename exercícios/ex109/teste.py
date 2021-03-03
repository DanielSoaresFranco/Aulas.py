import moeda
valor = float(input('Digite um valor: '))
aument = 10
dimin = 13
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'{moeda.moeda(valor)} aumentado em {aument}% é {moeda.aumentar(valor, aument, True)}')
print(f'{moeda.moeda(valor)} diminuído em {dimin}% é {moeda.diminuir(valor, dimin, True)}')
