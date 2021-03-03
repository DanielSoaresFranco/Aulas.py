somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhersub20 = 0
for p in range(1, 5):
    print('----------{}ª PESSOA----------''')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhersub20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.1f} anos'.format(mediaidade))
print('O homem mais velho é o {} e ele tem {} anos'.format(nomevelho, maioridadehomem))
print('Nesse grupo há {} mulheres com menos de 21 anos'.format(mulhersub20))
