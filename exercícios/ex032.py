from datetime import date
a = int(input('Qual ano? 0 para o ano atual. '))
m1 = 'Esse ano não é bissexto'
m2 = 'Esse ano é bissexto'
if a == 0:
    ano =date.today().year
if a % 4 == 0:  # Determina se é divisível por 4
    if a % 100 == 0:  # Determina se não é divisível por 100 caso seja divisível por 4
        if a % 400 == 0:  # Determina se é divisível por 400, caso seja divisível por 4 e por 100
            print(m2)
        else:
            print(m1)
    else:
        print(m2)
else:
    print(m1)