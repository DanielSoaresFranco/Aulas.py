from random import shuffle
n1 = input('1° nome: ')
n2 = input('2° nome: ')
n3 = input('3° nome: ')
n4 = input('4° nome: ')
lista = [n1, n2, n3, n4]
limpa = '\033[m'
shuffle(lista)
print('a ordem dos alunos é: ')
print('\033[36m', lista, limpa)
