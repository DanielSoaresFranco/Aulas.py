m = float(input('quantos metros? '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
limpa = '\033[m'
print('{}{}{} m equivale a: '.format('\033[4;34', m, limpa))
print('{}{}{} Km.'.format('\033[4;31m', km, limpa))
print('{}{}{} Hm.'.format('\033[4;32m', hm, limpa))
print('{}{}{} Dam.'.format('\033[4;33m', dam, limpa))
print('{}{}{} M.'.format('\033[4;34m', m, limpa))
print('{}{}{} Dm.'.format('\033[4;35m', dm, limpa))
print('{}{}{} Cm'.format('\033[4;36m', cm, limpa))
print('{}{}{} Mm'.format('\033[4;37m', mm, limpa))
