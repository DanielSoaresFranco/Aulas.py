números = []
pares = []
ímpares = []
while True:
    números.append(int(input('Digite um número: ')))
    c = str(input('Quer continuar? ')).strip().lower()[0]
    if c == 'n':
        break
for c in range(0, len(números)):
    if números[c] % 2 == 0:
        pares.append(números[c])
    else:
        ímpares.append(números[c])
print(f'Resumo: \nnúmeros digitados: {números} \npares: {pares} \nímpares: {ímpares}')
