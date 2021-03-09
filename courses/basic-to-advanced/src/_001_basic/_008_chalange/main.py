from datetime import datetime

nome = 'Paulo'
idade = 34
altura = 1.70
peso = 94.8
e_maior = idade > 18
imc = peso / altura ** 2

now = datetime.now()
ano_atual = now.year
nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura:.1f} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
