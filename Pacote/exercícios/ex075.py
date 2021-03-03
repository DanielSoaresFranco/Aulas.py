n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite o último valor: ')))
num9 = n.count(9)
if 3 in n:
    pos3 = f'o número 3 está na {n.index(3) + 1}ª posição'
else:
    pos3 = f'não há número 3'
pares = 0
c = 0
while True:
    if c > 3:
        break
    elif n[c] % 2 == 0:
        pares += 1
    c += 1

print(f'Entre esses números temos {num9} vezes o número 9, {pos3} e há {pares} números pares')
