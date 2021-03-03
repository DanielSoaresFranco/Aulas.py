preco = float(input('Qual o preço do produto? R$'))
print('Qual o meio de pagamento?')
meio_pag = int(input('1 = à vista com dinheiro/cheque, 2 = à vista no cartão, \n3 = em até 2x no cartão, 4 = 3x ou mais no cartão: '))

if meio_pag == 1:
    total = preco - preco * 0.1
    print('O preço do produto à vista no dinheiro/cheque, com desconto de 10%, é de R${:.2f}.'.format(total))
elif meio_pag == 2:
    total = preco - preco * 0.05
    print('O preço do produto à vista no cartão, com desconto de 5% é de R${:.2f}.'.format(total))
elif meio_pag == 3:
    total = preco
    num_parc = int(input('Quantas parcelas? '))
    parcela = (total / num_parc)
    print('O preço do produto em 2x no cartão é de R${:.2f}.'.format(total))
elif meio_pag == 4:
    total = preco + preco * 20 / 100
    num_parc = int(input('Quantas parcelas? '))
    parcela = total / num_parc
    print('O preço do produto em 3x ou mais no cartão, com 20% de juros, é de R${:.2f},'.format(parcela * num_parc))
    print('Sendo cada parcela R${:.2f}'.format(parcela))
else:
    total = preco
    print('Digite um meio de pagamento válido.')
