frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('{} é uma frase palíndroma'.format(frase))
else:
    print('{} não é uma frase palíndroma'.format(frase))
