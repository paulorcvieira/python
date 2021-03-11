l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]
print('Ex 1: ', ex1)

ex2 = [v * 2 for v in l1]
print('Ex 2: ', ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print('Ex 3: ', ex3)

l2 = ['Paulo', 'Caroline', 'Carmen']
ex4 = [v.replace('a', '@') for v in l2]
print('Ex 4: ', ex4)

t1 = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in t1]
print('Ex 5: ', ex5)

l3 = list(range(100))
ex5 = [v for v in l3 if v % 2 == 0]
print('Ex 5 - Pares: ', ex5)

ex6 = [v for v in l3 if v % 3 == 0]
print('Ex 6 - Impares: ', ex6)

ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print('Ex 7 - Impares e Divisíveis por 8: ', ex7)

ex8 = [v if v % 3 == 0 else 'Não' for v in l3]
print('Ex 8 - É impar? ', ex8)

ex9 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print('Ex 9 - É impar e divisível por 8? ', ex9)
