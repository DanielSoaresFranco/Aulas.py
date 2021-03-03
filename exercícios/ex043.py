peso = float(input('Peso em kg: '))
altura = float(input('Altura em metros: '))
imc = altura ** 2 / peso

print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida')
