from random import choice
n1 = input('1° nome: ')
n2 = input('2° nome: ')
n3 = input('3° nome: ')
n4 = input('4° nome: ')
r = [n1, n2, n3, n4]
print('o aluno sorteado é o/a \033[7;30m{}\033[m'.format(choice(r)))
