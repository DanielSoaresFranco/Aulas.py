from datetime import date
ano_nasc = int(input('Que ano você nasceu?'))
idade = date.today().year - ano_nasc

print('Você tem ou vai fazer {} anos esse ano.'.format(idade))

if idade < 10:
    print('Atleta MIRIM.')
elif idade < 15:
    print('Atleta INFANTIL.')
elif idade < 20:
    print('Atleta JÚNIOR.')
elif idade < 26:
    print('Atleta SÊNIOR.')
else:
    print('Atleta MASTER.')
