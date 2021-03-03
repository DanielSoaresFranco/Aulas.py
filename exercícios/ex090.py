dados_aluno = {'Nome': str(input('Digite o nome do aluno: '))}
dados_aluno['Média'] = float(input(f'Digite a média de {dados_aluno["Nome"]}: '))
if dados_aluno['Média'] > 6.9:
    dados_aluno['Situação'] = 'Aprovado'
elif 4.9 < dados_aluno['Média'] < 7:
    dados_aluno['Situação'] = 'Recuperação'
else:
    dados_aluno['Situação'] = 'Reprovado'
for i, v in dados_aluno.items():
    print(f'{i} = {v}')
