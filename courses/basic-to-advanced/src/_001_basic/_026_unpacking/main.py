"""
Desempacotamento de lista
"""

lista = ['Paulo', 'Caroline', 'Carmen', 1, 2, 3, 4, 5, 6, 7, 100]

n1, n2, n3, *_outra_lista, penultimo_da_lista, ultimo_da_lista = lista

print(n1, n2, n3, _outra_lista)
print('penultimo_da_lista: ', penultimo_da_lista)
print('ultimo_da_lista: ', ultimo_da_lista)
