km = float(input('Quantos Km? '))
if km > 200:
    print('O preço da passagem é de R${:.2f}'.format(km * 0.45))
else:
    print('O preço da passagem é de R${:.2f}'.format(km * 0.5))