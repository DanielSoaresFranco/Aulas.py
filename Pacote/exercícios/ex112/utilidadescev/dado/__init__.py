def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO! \"{entrada}\" não é um preço válido!')
        else:
            válido = True
            return float(entrada)
