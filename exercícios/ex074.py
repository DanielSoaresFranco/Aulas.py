from random import randint
a = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = max(a)
menor = min(a)
print(f'Os valores são:', end=' ')
for n in a:
    print(f'{n},', end=' ')
print(' ')
print(f'O maior valor é {maior} e')
print(f'O menor valor é {menor}')
