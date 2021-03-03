idade = maiores = homens = mulheres_sub_20 = 0
sexo = continua = ' '
while True:
    idade = int(input('Digite a idade: '))
    if sexo not in 'mf':
        while sexo not in 'mf':
            sexo = str(input('Digite o sexo: [M/F] ')).lower().strip()[0]
    if idade > 17:
        maiores += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres_sub_20 += 1
    if continua not in 'sn':
        while continua not in 'sn':
            continua = str(input('Quer continuar? [S/N] ')).lower().strip()
    if continua == 'n':
        break
print(f"""Entre as pessoas cadastradas:
{maiores} têm 18 anos ou mais,
{homens} são homens e 
{mulheres_sub_20} são mulheres e tem menos de 20 anos.""")
