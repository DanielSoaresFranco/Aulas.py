from math import radians, sin, cos, tan
a = float(input('digite o ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
amarelo = '\033[1;33m'
limpa = '\033[m'
print('e a tangente de {}{}°{} é {:.4f}{}'.format(a, t))
print('O seno de {}{}°{} é \033[1;32m{:.4f}{}'.format(amarelo, a, limpa, s, limpa))
print('O cosseno de {}{}°{} é \033[1;33m{:.4f}{}'.format(amarelo, a, limpa, c, limpa))
print('E a tangente de {}{}°{} é \033[1;34m{:.4f}{}'.ormat(amarelo, a, limpa, t, limpa))
