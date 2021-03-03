nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('Sua média foi {:.1f}.'.format(media))

if media < 5:
    print('Média abaixo de 5. Reprovado.')
elif 4.9 < media < 7:
    print('Média entre 5.0 e 6.9. Recuperação.')
else:
    print('Média igual ou superior a 7.0. Aprovado.')