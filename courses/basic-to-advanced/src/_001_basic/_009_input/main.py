"""
Entrada de dados - Aula 3
- por padrão sempre retorna o valor do input como string
"""
from datetime import datetime

now = datetime.now()
ano_atual = now.year


nome = input("Qual o seu nome? ")
idade = input("Qual sua idade ")

nascimento = ano_atual - int(idade)

print(f'O usuário digitou {nome} e o tipo da variável é ' f'{type(nome)}')
print(f'Idade {idade} e nascido em {nascimento}')

numero_1 = int(input("Digite um número: "))
numero_2 = input("Digite outro número: ")
numero_2 = int(numero_2)

print(f'A potencia é {numero_1 ** numero_2}')
