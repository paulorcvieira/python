"""
Funções (def) - *args **kwargs
"""


def fn(a1, a2, a3, a4, a5=None, a6=None):
    print(a1, a2, a3, a4, a5, a6)


fn(1, 2, 3, 4, a5='Paulo', a6='6')


def fn2(*args, **kwargs):
    print('**kwarg: ', kwargs)

    name = kwargs.get('nome')
    print('**kwarg.get: ', name)

    for v in args:
        print('*arg: ', v)

    age = kwargs.get('idade')

    if age is not None:
        print(age)
    else:
        print('Idade não existe')


nums = [9, 8, 7]
fn2(*nums, 6, 5, 4, nome='Paulo')


lista = [1, 2, 3, 4, 5]
print(*lista, sep='-')

variavel = 'valor'


def fn3():
    print(variavel)


def fn4():
    global variavel
    variavel = 'Outro valor'
    print(variavel)
