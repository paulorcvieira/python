"""
 add, update, clear, discard
 union | (une)
 intersection & (todos os elementos presentes nos dois sets)
 difference - (elementos apenas no set da esquerda)
 symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

s1 = {1, 2, 3, 4, 5, 6}
print(s1)

for v in s1:
    print(v)

# vazio
s2 = set()
s2.add(1)
s2.add(2)
s2.add((1, 2, 3, 'Paulo'))
print(s2)

s2.discard(1)
print(s2)

s2.update('Python')
print(s2)

s2.update([1, 2, 3, 4, 5], {5, 6, 7, 8})
print(s2)

l1 = [1, 2, 3, 4, 5, 4, 4, 3, 2, 4, 5, 5, 6, 6, 6, 7, 5, 5, 4, 6, 8, 9, ]
s3 = set(l1)
print('list -> set: ', s3)
print(type(s3))

l1 = [1, 2, 3, 4, 5, 4, 4, 3, 2, 4, 5, 5, 6, 6, 6, 7, 5, 5, 4, 6, 8, 9, ]
s3 = set(l1)
l1 = list(l1)
print('list -> set -> list: ', s3)
print(type(l1))

# union
s4 = {1, 2, 3, 4}
s5 = {3, 4, 5, 6, 7, 8}
s6 = s4 | s5
print('union', s6)

# intersection
s4 = {1, 2, 3, 4}
s5 = {3, 4, 5, 6, 7, 8}
s6 = s4 & s5
print('intersection', s6)

# difference
s4 = {1, 2, 3, 4}
s5 = {3, 4, 5, 6, 7, 8}
s6 = s4 - s5
print('difference (s4 - s5): ', s6)
s6 = s5 - s4
print('difference (s5 - s4): ', s6)

# symmetric_difference
s4 = {1, 2, 3, 4}
s5 = {3, 4, 5, 6, 7, 8}
s6 = s4 ^ s5
print('symmetric_difference: ', s6)

list_01 = ['Paulo', 'Caroline', 'Carmen', 'Paulo', 'Caroline']
list_02 = ['Paulo', 'Caroline', 'Carmen', 'Carmen', 'Carmen']

print(list_01 == list_02)

if set(list_01) == set(list_02):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')
