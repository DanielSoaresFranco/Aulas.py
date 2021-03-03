s = float(input('qual é o seu salário? R$'))
if s > 1250:
    print('seu novo salário com aumento de 10% é de R${:.2f}'.format(s * 1.1))
else:
    print('Seu novo salário com aumento de 15% é de R${:.2f}'.format(s * 1.15))