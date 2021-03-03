números = []
while True:
    n1 = int(input('Digite um número: '))
    c = str(input('Quer continuar? ')).strip().lower()[0]
    if n1 not in números:
        números.append(n1)
    if c == 'n':
        break
números.sort()
print(f'Números da lista em ordem crescente: {números}')
