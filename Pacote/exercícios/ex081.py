n = []
while True:
    n.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar: ')).strip().lower()[0]
    if continuar == 'n':
        break
n.sort(reverse=True)
print(f"""Resumo:
{len(n)} é o número de valores digitados, 
{n} é a lista em ordem decrescente e """)
if 5 not in n:
    print('Não tem o número cinco.')
else:
    print(f'O número cinco aparece nessa lista.')
