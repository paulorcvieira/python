from random import randint


def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}.')


saudacao('Bem-vindo!', 'Paulo')


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(5, 9, 3)


def juros(valor, juros) -> float:
    return valor + (valor * (juros / 100))


j = juros(50, 10)
print(j)


def fizzBuzz(val: float) -> str:
    if val % 5 == 0 and val % 3 == 0:
        return f'FizzBuzz, "{val}" é divisivel por 3 e 5'
    if val % 5 == 0:
        return f'buzz, "{val}" é divisivel por 5'
    if val % 3 == 0:
        return f'fizz, "{val}" é divisivel por 3'
    return f'"{val}" NÃO é divisivel por 3 e 5'


for i in range(100):
    aleatorio = randint(0, 100)
    print(fizzBuzz(aleatorio))
