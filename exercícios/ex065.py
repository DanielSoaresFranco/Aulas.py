maior = menor = media = soma = n = c = 0
r = ' '
while r not in 'Nn':
    n = int(input('Digite um valor: '))
    soma += n
    if c == 0:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    r = str(input('Quer continuar digitando [S/N]? ')).strip()[0]
    if r not in 'Nn':
        c += 1
media = soma / c
print("""Entre os {} valores digitados:
{} é a média entre eles, 
{} é o maior e 
{} é o menor""".format(c, media, maior, menor))
