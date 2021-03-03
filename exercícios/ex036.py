valor_casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
tempo = int(input('Em quantos anos vai pagar o empréstimo? '))

prestacao_mensal = valor_casa / (tempo * 12)

print('O valor da prestação mensal é de R${:.2f}.'.format(prestacao_mensal))

if prestacao_mensal > (salario / 100 * 30):
    print('Empréstimo negado, pois a prestação mensal equivale a {:.0f}% do salário, excedendo, portanto, 30% do salário.'.format((salario / 100) * (prestacao_mensal / 100)))
else:
    print('Empréstimo aprovado.')
