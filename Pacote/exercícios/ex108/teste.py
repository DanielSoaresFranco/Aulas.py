import moeda
valor = float(input('Digite um valor: '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'{moeda.moeda(valor)} aumentado em 20% é {moeda.moeda(moeda.aumentar(valor, 20))}')
print(f'{moeda.moeda(valor)} diminuído em 20% é {moeda.moeda(moeda.diminuir(valor, 20))}')
