c = float(input('temperatura em °C: '))
f = 9 * c / 5 + 32
print('a temperatura de \033[1;35m{}°C\033[m corresponde a \033[1;37m{}°F\033[m'.format(c, f))
