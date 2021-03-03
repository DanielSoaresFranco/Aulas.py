largura = float(input('largura da parede: '))
h = float(input('altura da parede: '))
a = largura * h
tinta = a / 2
print('Sua parede tem \033[1;31m{}x{}m\033[m e a sua área é de \033[1;32m{}m²\033[m.'.format(largura, h, a))
print('Para pintar essa parede você precisa de \033[1;34m{:.3f}l\033[m de tinta'.format(tinta))
