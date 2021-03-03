matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = soma3coluna = maior2linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha}x{coluna}: '))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
for c in range(0, 3):
    soma3coluna += matriz[c][2]
    if c == 0 or matriz[1][c] > maior2linha:
        maior2linha = matriz[1][c]
print('Matriz: \n')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
print(f"""\nA soma dos valores pares é {somapares}, 
a soma dos valores da 3ª coluna é {soma3coluna}
e o maior valor da 2ª linha é {maior2linha}.""")
