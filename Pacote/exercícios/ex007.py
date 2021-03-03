n1 = float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
m = (n1+n2)/2
limpa = '\033[m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'
print('a média entre {}{:.1f}{} e {}{:.1f}{} é {}{:.1f}{}'.format(roxo, n1, limpa, ciano, n2, limpa, cinza, m, limpa))
