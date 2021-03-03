s = 0
n = 0
for c in range(3, 501, 6):
    s += c
    n += 1
print('A soma de todos os {} números solicitados é {}'.format(n, s))
