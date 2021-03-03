n1 = float(input('qual é o preço? R$'))
x = int(input('quanto % de desconto?(apenas o número) '))
n2 = n1 - (n1 * x / 100)
print('o produto que custava \033[1;31mR${:.2f}\033[m com desconto de \033[1;34m{}%\033[m custará \033[1;33mR${:.2f}\033[m'.format(n1, x, n2))
