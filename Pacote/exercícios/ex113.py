def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Esse não é um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Esse valor não é decimal!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num

