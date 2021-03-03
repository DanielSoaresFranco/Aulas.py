pilha = []
exp = str(input('Digite a expressão: '))
for c in range(0, len(exp)):
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) != 0:
    print('Expressão Inválida!')
else:
    print('Expressão Válida!')
