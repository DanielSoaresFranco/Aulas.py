from math import sqrt
c1 = float(input('comprimento do cateto: '))
c2 = float(input('digite o outro cateto: '))
h = sqrt(c1**2 + c2**2)
print('sendo os catetos \033[1;33m{}\033[m e \033[1;33m{}\033[m a hipotenusa é \033[1;31m{:.2f}\033[m.'.format(c1, c2, h))
