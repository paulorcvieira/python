"""
Iniciar com letra, pode conter números, separa _, letras minúsculas
"""

nome = 'Paulo'
idade = 34
altura = 1.70
e_maior = idade > 18
peso = 94.8
imc = peso / altura ** 2

print(nome, type(nome))
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade?', e_maior)

print('Idade * altura', idade * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
