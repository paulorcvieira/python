"""
split, join, enumerate
* split: dividir uma string # str
* join: juntar uma lista # str
* enumerate: enumerar elementos da lista # list / iteraveis
"""

string = 'O Brasil é o país do futebol, e do samba!'
lista_01 = string.split(' ')
lista_02 = string.split(',')

for valor in lista_01:
    print(
        f'A palavra "{valor}" apareceu "{lista_01.count(valor)}" vezes na frase\n')

palavra = ''
contagem = 0
for valor in lista_01:
    qtd_vezes = lista_01.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)\n')

for valor in lista_02:
    print(valor.strip().capitalize())

print()
print()

lista_03 = ','.join(lista_01)
print(lista_03)

for index, valor in enumerate(lista_01):
    print(index, valor)

for index, valor in enumerate(lista_01, 13):
    print(index, valor)

teste = ['valor 01', 'valor 02', 'valor 03']
n1, n2, n3 = teste
print(n2)
