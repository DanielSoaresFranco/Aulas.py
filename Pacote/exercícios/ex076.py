produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
c = 0
msg = 'LISTAGEM DE PREÇOS'
print('-' * 40)
print(f'{msg:^40}')
print('-' * 40)
while True:
    print(f'|{produtos[c]:.<30}R${produtos[c + 1]: >6.2f}|')
    c += 2
    if c == 18:
        print('-' * 40)
        break
