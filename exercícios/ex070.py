c = valor_mais_barato = s = cont1000 = 0
mais_barato = continuar = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]'))
    s += preco
    c += 1
    if c == 1 or preco < valor_mais_barato:
        valor_mais_barato = preco
        mais_barato = nome
    if preco > 1000:
        cont1000 += 1
    if continuar == 'n':
        break
print(f"""Entre os {c} valores citados:
R${s:.2f} é o preço total gasto na compra,
tem {cont1000} produtos que custam mais de 1000 reais e 
o produto mais barato é {mais_barato}, que custa R${valor_mais_barato:.2f}""")
