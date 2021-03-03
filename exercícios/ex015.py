t = int(input('quantos dias? '))
d = float(input('quantos Km? '))
p = (60*t) + (0.15*d)
print('o preço do aluguel é de \033[4;32mR${:.2f}'.format(p))
