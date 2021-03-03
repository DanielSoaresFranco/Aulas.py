números = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        números[0].append(n)
    else:
        números[1].append(n)
    números[0].sort()
    números[1].sort()
print(f'Os números pares são: {números[0]}')
print(f'E os ímpares são: {números[1]}')
