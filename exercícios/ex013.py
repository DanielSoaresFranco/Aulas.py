s = float(input('qual o salário? R$'))
j = int(input('quanto % de aumento? (apenas o número) '))
ns = s + s * j / 100
print('novo salário com \033[1;30m{}%\033[m de aumento: \033[1;37mR${:.2f}\033[m'.format(j, ns))
