"""
Operadores Relacionais
== > >= < <= !=
"""
print('2 == 2 ', 2 == 2)
print('2 == 1', 2 == 1)
print('2 == "2" ', 2 == '2')
print('2 > 2 ', 2 > 2)
print('2 >= 2 ', 2 >= 2)
print('2 < 2 ', 2 < 2)
print('2 <= 2 ', 2 <= 2)
print('2 != 2 ', 2 != 2)

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
min_idade = 18
max_idade = 60

if idade >= min_idade and idade <= max_idade:
    print(f'{nome} é maior de idade mas não é velho')
elif idade >= min_idade and idade >= max_idade:
    print(f'{nome} é maior de idade mas é velho')
else:
    print(f'{nome} NÃO é maior de idade')
