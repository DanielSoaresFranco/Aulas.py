nome = input('Escreva seu nome: ').strip()
nomes = nome.split()
numnomes = len(nome.split())
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}\nE seu último nome é {}'.format(nomes[0], nomes[numnomes-1]))
