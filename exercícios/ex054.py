from datetime import date
ma = 0
me = 0
for c in range(0, 7):
    ano = int(input('Em que ano nasceu a {}ª pessoa? '.format(c + 1)))
    idade = date.today().year - ano
    if idade > 20:
        ma += 1
    else:
        me += 1
print('ao todo temos {} pessoas maiores de idade e {} menores de idade.'.format(ma, me))