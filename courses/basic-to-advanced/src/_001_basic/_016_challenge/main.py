num_int = input('Digite um número inteiro: ')
num_int_2 = num_int


def is_digit(val: str) -> bool:
    if val.isdigit():
        return True
    return False


def convert_to_int(val: str) -> int:
    return int(val)


def verifyIfParOrImpar(val: int):
    if not val % 2 == 0:
        return print(f'{val} é impar')
    else:
        return print(f'{val} é par')


def greetings(val: int):
    if val < 0 or val > 23:
        return print('A hora deve esta entre 0 e 23')
    else:
        if val <= 11:
            return print('Bom dia')
        elif val <= 17:
            return print('Boa tarde')
        else:
            return print('Boa noite')


def len_name(val: int):
    if val <= 4:
        return print('Seu nome é curto int')
    elif val <= 6:
        return print('Seu nome tem o tamnho normal')
    else:
        return print('Seu nome é longo')


if is_digit(num_int):
    num_int = convert_to_int(num_int)

    if num_int % 2 == 0:
        print(f'{num_int} é par')
    else:
        print(f'{num_int} é impar')
else:
    print('Não é um número inteiro')


if not is_digit(num_int_2):
    print('Não é um número inteiro')
else:
    num_int_2 = convert_to_int(num_int_2)

    verifyIfParOrImpar(num_int_2)

hour = input('Digite uma hora (0-23): ')

if is_digit(hour):
    hour = convert_to_int(hour)

    greetings(hour)
else:
    print('Por favor, digite um horário ente 0 e 23.')


name = input('Digite seu nome: ')
length_name = len(name)
len_name(length_name)
