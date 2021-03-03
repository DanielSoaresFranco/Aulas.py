n = []
posmaior = []
posmenor = []
for c in range(0, 5):
    n.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = n[c]
        posmaior.append(c)
        posmenor.append(c)
    else:
        if n[c] >= maior:
            if n[c] > maior:
                maior = n[c]
                posmaior = [c]
            else:
                posmaior.append(c)
        if n[c] <= menor:
            if n[c] < menor:
                menor = n[c]
                posmenor = [c]
            else:
                posmenor.append(c)
print(f'Você digitou os valores {n}')
print(f"""Entre os 5 valores citados, {maior} é o maior e está na posição {posmaior}, 
e {menor} é o menor, estando na posição {posmenor}""")
