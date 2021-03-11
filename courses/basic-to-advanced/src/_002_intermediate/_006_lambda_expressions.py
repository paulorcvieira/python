def fn(arg, arg2):
    return arg * arg2


var = fn(2, 2)

# =


def a(x, y): return x * y


print(a)

# Ordered Lists
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


lista.sort(key=func, reverse=True)
print(lista)

lista.sort(key=lambda item: item[1])
print(lista)

# sem alterar a lista inicial
print(sorted(lista, key=lambda i: i[1], reverse=True))

print(sorted(lista, key=lambda i: i[0], reverse=True))
