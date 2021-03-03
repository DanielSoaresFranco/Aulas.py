def ficha(nome='<desconhecido>', gol='0'):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')


jogador = str(input('Qual o nome do jogador? '))
gols = str(input('Quantos gols ele fez? '))
if jogador == gols == '':
    ficha()
elif jogador == '' and gols != '':
    ficha(gol=gols)
elif jogador != '' and gols == '':
    ficha(jogador)
else:
    ficha(jogador, gols)
