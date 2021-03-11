"""
Não pode alterar os valores da tupla
"""

t1 = (1, 2, 3, 'a', 'Paulo')
print(type(t1))
print(t1)
print(t1[4])

for v in t1:
    print(v)

print(t1[2:])

# quando precisar declarar com apenas um valor, precisa de uma virgula no final
t2 = 2,
print(t2, type(t2))

t3 = 1, 'Paulo', 3, 4
t4 = 5, 6, 7, 8
t4 = t3 + t4
print(t4)

n1, n2, n3, *_, n8 = t4

print(n8)

t5 = (1, 2, 3, 4, 5) * 5
print(t5)

t6 = (1, 2, 3, 4, 5)
t6 = list(t6)
t6[1] = 3000
print(t6, type(t6))
t6 = tuple(t6)
print(t6, type(t6))
