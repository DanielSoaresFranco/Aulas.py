sexo = ' '
while sexo not in 'MmFf':
    sexo = str(input('Digite o seu sexo: ')).strip()[0]
    if sexo not in 'MmFf':
        print('Sexo inválido. Tente novamente digitando M ou F')
    else:
        print('Ok, sexo registrado')
