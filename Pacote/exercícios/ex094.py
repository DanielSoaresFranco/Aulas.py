mulheres = []
pessoas = []
pessoa = {}
s = m = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo: ')).strip().lower()[0]
    while pessoa['sexo'] not in 'mf':
        print('Erro! Digite M ou F.')
        pessoa['sexo'] = str(input('Sexo: ')).strip().lower()[0]
    cont = str(input('Quer continuar? ')).strip().lower()[0]
    s += pessoa['idade']
    pessoas.append(pessoa.copy())
    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa['nome'])
    if cont == 'n':
        print('-=' * 40)
        break
    while cont not in 'sn':
        print('Erro! Responda S ou N.')
        cont = str(input('Quer continuar? ')).strip().lower()[0]
m = s / len(pessoas)
print(f"""- O grupo tem {len(pessoas)} pessoas
- A média de idade é de {m:.0f} anos
- As mulheres cadastradas foram {mulheres}
-lista das pessoas que estão acima da média de idade: """)
for a in range(0, len(pessoas)):
    if pessoas[a]['idade'] >= m:
        for d, e in pessoas[a].items():
            print(f'{d} = {e},', end=' ')
        print()
print('<<ENCERRADO>>')
