"""
Formatando valores com modificadores

:s - Texto (str)
:d - Inteiro (int)
:f - números de ponto flutuante (float)
:. (Número) f - Quantidade de casas deciamais
:(CARACTERE) (> ou < ou ^)(Quantidade de tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{num_1:0>10}')  # na esquerda
print(f'{num_1:0^10}')  # no centro
print(f'{num_1:0<10}')  # na direita
print(f'{num_1:0>10.2f}')  # na esquerda com flutuante
print(f'{num_1:0^10.2f}')  # no centro com flutuante
print(f'{num_1:0<10.2f}')  # na direita com flutuante

nome = ' Paulo '
sobrenome = ' Vieira '
print((80 - len(nome)) / 2)
print(f'{nome:#^50}')

nome_formatado = '{:@>15}'.format(nome)
print(nome_formatado)
nome_formatado = '{:@>15}'.format(nome)
print(nome_formatado)
nome_formatado = '{n:#>50}{n:#<50}'.format(n=nome)
print(nome_formatado)
nome_formatado = '{0:#>50}{1:#<50}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.split('u'))
print(nome.upper())
print(nome.ljust(50, '#'))
print(nome.rjust(50, '#'))
print(nome.lower())
print(nome.title())
print(nome.encode())
