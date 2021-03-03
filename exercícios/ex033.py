n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro valor: '))
# Definindo mensagens
m1 = ' é o maior valor'
m2 = ' é o menor valor'
# Verificando o maior
if n1 >= n2 and n1 >= n3:
    print(n1, m1)
elif n2 >= n1 and n2 >= n3:
    print(n2, m1)
elif n3 >= n1 and n3 >= n2:
    print(n3, m1)
# Verificando o  menor
if n1 <= n2 and n1 <= n3:
    print(n1, m2)
elif n2 <= n1 and n2 <= n3:
    print(n2, m2)
elif n3 <= n1 and n3 <= n2:
    print(n3, m2)
