def notas(*num, sit=False):
    """
    -> Esse programa analisa notas dadas pelo usuário
    :param num: é onde entram as notas a serem analisadas
    :param sit: define se vai querer mostrar a situação da turma
    :return: um dicionário com as informações obtidas através das notas
    """
    info = {
        'qtd notas': len(num),
        'Maior': max(num),
        'Menor': min(num),
        'Média': sum(num)/len(num),
    }
    if sit:
        if info['Média'] > 6.9:
            info['Situação'] = 'BOA'
        elif info['Média'] > 4.9:
            info['Situação'] = 'RAZOÁVEL'
        else:
            info['Situação'] = 'RUIM'
    return info


resp = notas(7.5, 10, 6.5, 5, 9, 7, 3, sit=True)
print(resp)
help(notas)
