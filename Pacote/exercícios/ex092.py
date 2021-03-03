from datetime import date
info = {
    'nome': str(input('Digite o seu nome: ')),
    'idade': date.today().year - int(input('Digite o seu ano de nascimento: ')),
    'ctps': int(input('Digite a Carteira de Trabalho (0 não tem): '))
}
if info['ctps'] != 0:
    info['ano da contratação'] = int(input('Digite o ano de contratação: '))
    info['salário'] = float(input('Digite o salário: R$'))
    info['idade da aposentadoria'] = (info['ano da contratação'] - (date.today().year - info['idade'])) + 35
for c, d in info.items():
    print(f'{c} = {d}')