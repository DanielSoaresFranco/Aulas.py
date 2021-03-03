def maior(*números):
    if len(números) == 0:
        maior_número = 0
    else:
        pass
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in range(0, len(números)):
        if c == 0:
            maior_número = números[c]
        else:
            if números[c] > maior_número:
                maior_número = números[c]

    print(f'Os números passados foram {números}')
    print(f'O maior entre os {len(números)} números digitados é {maior_número}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
