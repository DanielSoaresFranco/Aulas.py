n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Sua média foi boa! PARABÉNS!' if m >= 6.0 else 'Sua média foi ruim! ESTUDE MAIS!')
