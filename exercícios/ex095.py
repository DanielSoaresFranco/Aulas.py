time = []
gols = []
jogador = {}
firulas = {'firula1': '-=' * 45, 'firula2': '-' * 60}
while True:
    gols.clear()
    jogador.clear()
    jogador['código'] = len(time)
    jogador['nome'] = str(input('Qual o nome do jogador? ')).strip().capitalize()
    jogador['partidas'] = int(input('Quantas partidas jogou? '))
    jogador['total'] = 0
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jogador['total'] += gols[c]
    jogador['gols'] = gols[:]
    time.append(jogador.copy())
    cont = str(input('Quer continuar? ')).strip().lower()[0]
    while cont not in 'sn':
        print('ERRO! Digite sim ou não')
        cont = str(input('Quer continuar? ')).strip().lower()[0]
    if cont == 'n':
        break
print(f"""{firulas['firula1']}
cod|{'nome':^20}|{'gols':^20}|total
{firulas['firula2']}""")
for c in range(0, len(time)):
    carac_gols = len(time[c]['gols']) * 3
    if time[c]['gols'] == 0:
        carac_gols = 2
    espacos = 20 - carac_gols
    print(f"""{c}   {time[c]['nome']:^20}  {time[c]['gols']}{' ' * espacos}{time[c]['total']}""")
print(firulas['firula2'])
while True:
    proc_jogador = int(input('Quer ver as informações de qual jogador? (999 para encerrar o programa) '))
    if proc_jogador == 999:
        break
    elif proc_jogador > len(time) - 1:
        print(f'ERRO: Não existe jogador com o código {proc_jogador}')
    else:
        print(f"""-Levantamento do jogador {time[proc_jogador]['nome']}:""")
        for c in range(0, time[proc_jogador]['partidas']):
            print(f'Na partida {c + 1} ele fez {time[proc_jogador]["gols"][c]} gols')
print('Programa encerrado. Volte sempre!')
