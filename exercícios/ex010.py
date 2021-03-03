R = float(input('quantos reais tem na sua carteira? R$'))
US = R / 3.27
limpa = '\033[m'
print('com \033[1;33mR${:.2f}{} você pode comprar \033[1;34mUS${:.2f}{}.'.format(R, limpa, US, limpa))
