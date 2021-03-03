def área(largura, comprimento):
    print(f'A área de um terreno de {largura}X{comprimento} é de {largura * comprimento}m² ')


print(' Controle de Terrenos')
print('----------------------')
área(float(input('Digite a largura(em metros): ')), float(input('Digite o comprimento(em metros): ')))
