def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    finally:
        a.close()


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        print(a.read())
    finally:
        a.close()


def cadastrar(arquivo, nome='<desconhecido>', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'\t{nome:<30}{idade:>3} anos\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
        finally:
            a.close()
