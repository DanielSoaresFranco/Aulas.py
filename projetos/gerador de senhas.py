from random import randint
senha = []
opções = []
tamanho = int(input('Qual o tamanho da senha? '))
minusculas = str(input('Letras minúsculas? s/n ')).strip().lower()[0]
maiusculas = str(input('Letras maiúsculas? s/n ')).strip().lower()[0]
simbolos = str(input('símbolos? s/n ')).strip().lower()[0]
numeros = str(input('números? s/n ')).strip().lower()[0]
if minusculas == 's':
    letras_min = 'qwertyuiopasdfghjklzxcvbnm'
    for c in range(0, len(letras_min)):
        opções.append(letras_min[c])
if maiusculas == 's':
    letras_mai = 'MNBVCXZLKJHGFDSAPOIUYTREWQ'
    for c in range(0, len(letras_mai)):
        opções.append(letras_mai[c])
if simbolos == 's':
    s = '!@#$%&*()?/_-'
    for c in range(0, len(s)):
        opções.append(s[c])
if numeros == 's':
    n = '1234567890'
    for c in range(0, len(n)):
        opções.append(n[c])
print('Sua senha é: ', end='\033[1;32m')
for c in range(0, tamanho):
    letra = randint(0, len(opções))
    senha.append(opções[letra])
    print(senha[c], end='')
print('\033[m\nNão compartilhe sua senha! \nVolte sempre!')
