# 01
def fn2():
    return 'Boa tarde!'


def fn1(fn):
    return fn()


executando = fn1(fn2)
print(executando)

# 02


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala, 'Paulo')
executando2 = mestre(saudacao, 'Paulo', saudacao='Bom dia!')
print(executando)
print(executando2)
