alunos = []
aluno = []
notas_aluno = []
while True:
    aluno.clear()
    notas_aluno.clear()
    aluno.append(str(input('Qual o nome do aluno? ')))
    notas_aluno.append(float(input('Qual a 1ª nota? ')))
    notas_aluno.append(float(input('Qual a 2ª nota? ')))
    notas_aluno.append((notas_aluno[0] + notas_aluno[1]) / 2)
    cont = str(input('Quer continuar? '))
    aluno.append(notas_aluno[:])
    alunos.append(aluno[:])
    if cont == 'n':
        break
print('-=' * 20)
print(f'nº  {"NOME":<15} MÉDIA')
print('-' * 30)
for c in range(0, len(alunos)):
    print(f'{c:<4}{alunos[c][0]:<15}{alunos[c][1][2]:.1f}')
while -1 < proc_aluno < len(alunos):
    proc_aluno = int(input(f'\nMostrar notas de que aluno? (Digite um número maior que {len(alunos) - 1} para encerrar o programa) '))
    if proc_aluno > len(alunos) - 1 or proc_aluno < 0:
        break
    print(f'\nAs notas de {alunos[proc_aluno][0]} são {alunos[proc_aluno][1][0]} e {alunos[proc_aluno][1][1]}')
print('Programa encerrado. Volte sempre!')
