from datetime import date

sexo = int(input('Qual sexo? \n1 = homem, \n2 = mulher: '))
if sexo == 1:
    ano_nascimento = int(input('Em que ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        if idade == 17:
            print('Você ainda é muito jovem. Tem {} anos. Falta 1 ano para você se alistar.'.format(idade))
        else:
            print('Você ainda é muito jovem. Tem {} anos. Faltam {} anos para você se alistar.'.format(idade, 18 - idade))
        print('você vai se alistar em {}'.format(ano_atual + (18 - idade)))
    elif idade == 18:
        print('É hora de você se alistar.')
    elif idade > 18:
        if idade == 19:
            print('Já passou 1 ano do tempo do alistamento')
        else:
            print('Já se passaram {} anos do tempo do alistamento, já que você tem {} anos'.format(idade - 18, idade))
        print('você devia ter se alistado em {}'.format(ano_nascimento + 18))
elif sexo == 2:
    print('Você não precisa fazer o alistamento.')