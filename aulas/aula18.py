galera = list()
dados = list()
limite = 3
maior = menor = 0
for c in range(0, limite):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Nesse grupo de pessoas temos {maior} maiores de idade e {menor} menores de idade.')
