def voto():
    from datetime import date
    nascimento = int(input('Em que ano você nasceu? '))
    anos = date.today().year - nascimento
    if anos < 16:
        return f'Com {anos} anos o voto é NEGADO'
    elif 18 > anos or anos > 64:
        return f'Com {anos} anos o voto é OPCIONAL'
    else:
        return f'Com {anos} anos o ano é OBRIGATÓRIO'


voto = voto()
print(voto)
