from utilidades_daniel import mensagem


def menu():
    print('\033[1;33m', '~' * 42)
    print(f'{"MENU PRINCIPAL":^42}')
    print('~' * 42, '\033[m')
    print("""\033[1;33m1 - \033[1;34mVer pessoas cadastradas,
\033[1;33m2 - \033[1;34mCadastrar nova pessoa,
\033[1;33m3 - \033[1;34mSair do sistema""")
    print('\033[1;33m', '~' * 42, '\033[m')

    try:
        escolha = int(input('\033[1;32mSua opção: \033[m'))
    except ValueError:
        mensagem('\033[1;31mERRO! Por favor digite uma opção válida')
    else:
        if escolha == 1:
            mensagem(cor='\033[1;34m', msg='PESSOAS CADASTRADAS', firula='-')
        elif escolha == 2:
            mensagem(cor='\033[1;34m', msg='CADASTRAR PESSOA', firula='-')
        elif escolha == 3:
            print('Fim do programa. Volte sempre!')
        else:
            mensagem('\033[1;31mERRO! Por favor digite uma opção válida')
        print()
        return escolha