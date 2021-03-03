lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        cont = 0
        while cont < len(lista):
            if n <= lista[cont]:
                lista.insert(cont, n)
                print(f'Adicionado na posição {cont} da lista')
                break
            cont += 1

print(lista)
