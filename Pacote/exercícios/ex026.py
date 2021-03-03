frase = str(input('Escreva uma frase: ')).split().lower()
print('Quantas letras A? {}'.format(frase.count('a')))
print('Qual a posição do primeiro A? {}'.format(frase.find('a') + 1))
print('Qual a posição do último A? {}'.format(frase.rfind('a') + 1))
