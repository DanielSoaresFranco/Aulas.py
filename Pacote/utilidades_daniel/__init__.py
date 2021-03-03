def mensagem(cor='', msg='', firula='', tamanho=0):
    if '\n' in msg:
        linha = msg.find('\n')
    else:
        linha = len(msg)
    limpa = '\033[m'
    if tamanho == 0:
        tamanho = firula * (linha + 4)
    if firula == '':
        print(f'{cor}  {msg}  {limpa}')
    else:
        print(f'{cor}{tamanho}{limpa}')
        print(f'{cor}  {msg}  \033[m')
        print(f'{cor}{tamanho}{limpa}')
