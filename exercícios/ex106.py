from utilidades_daniel import mensagem


def ajuda():
    global funbib
    mensagem('\033[1;36;43m', 'ME_AJUDA.PY', '~')
    funbib = input('\033[mQual função ou biblioteca? ').strip()
    if funbib.lower() == 'fim':
        return False
    else:
        mensagem('\033[1;34;40m', f'Acessando o manual do comando/biblioteca {funbib}', '~')
        print('\033[1;34;40m')
        help(funbib)
        return True


funbib = ''
while ajuda():
    ajuda()
    if funbib.lower == 'fim':
        break
mensagem('\033[1;31;40m', 'ATÉ LOGO', '~')
