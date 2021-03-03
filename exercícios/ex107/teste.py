import moeda
valor = float(input('Digite um valor: '))
valor = valor
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'{valor} aumentado em 20% é {moeda.aumentar(valor, 20)}')
print(f'{valor} diminuído em 20% é {moeda.diminuir(valor, 20)}')
