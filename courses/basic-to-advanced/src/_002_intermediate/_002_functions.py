"""
Função: def - return
"""


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 4)

if divide:
    print(divide)
else:
    print('Conta inválida!')


def fn(var):
    print(var)


def dumb():
    return fn


var = dumb()
var('Imprimir')
