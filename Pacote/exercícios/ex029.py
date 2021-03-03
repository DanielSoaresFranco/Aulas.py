v = float(input('Qual a velocidade em km/h? '))
print('Você foi multado! \nA multa é de R${:.2f}'.format((v - 80) * 7) if v > 80 else 'Velocidade permitida.')
print('Bom dia e dirija com segurança!')
