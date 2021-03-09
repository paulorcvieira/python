"""
Operador Ternário
"""

logged_user = False
msg = 'Usuário logado' if logged_user else 'Usuário precisa logar.'

print(msg)

idade = input('Qual é a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    maior = idade >= 18
    msg = 'Pode acessar' if maior else 'Não pode acessar.'

    print(msg)
