"""
Operadores Lógicos
and, or, not
in e not in
"""

idade = int(input('Qual a sua idade? '))
idade_min = 18
idade_max = 45

# AND as duas precisam ser verdadeiras
if idade >= idade_min and idade <= idade_max:
    print('Está entre a idade mínima e a máxima')

# OR uma ou outra precisam ser verdadeira
if idade >= idade_min or idade <= idade_max:
    print('Não está entre a idade mínima e a máxima')

if not idade:
    print('A idade não se enquadra')

nome = input('Qual o seu nome? ')
letra = 'a'
if letra in nome:
    print(f'Existe "{letra}" em seu nome')
elif letra not in nome:
    print(f'Não exite "{letra}" em seu nome')


usuario = input('Usuário: ')
senha = input('Senha: ')

usuario_bd = 'paulo'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('Logado')
else:
    print('Usuário ou senha inválidos')
