pessoas = []
dados = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cont = str(input('Quer continuar? ')).strip().lower()[0]
    if len(pessoas) == 1:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    if cont == 'n':
        break
print(f"""Você cadastrou ao todo {len(pessoas)} pessoas. 
O maior peso foi de {maiorpeso:.1f}Kg, sendo o peso de """, end='')
for pessoa in pessoas:
    if pessoa[1] == maiorpeso:
        print(pessoa[0], end=', ')
print(f'\nO menor peso é de {menorpeso:.1f}Kg, sendo o peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menorpeso:
        print(pessoa[0], end=', ')
