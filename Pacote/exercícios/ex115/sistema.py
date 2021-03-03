from exercícios.ex115.lib.menu import menu
from exercícios.ex115.lib.cadastro import *
from exercícios.ex113 import leiaInt

opção = 1
arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while opção != 3:
    opção = menu()
    if opção == 1:
        lerArquivo(arquivo)
    elif opção == 2:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
