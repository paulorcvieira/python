nome = 'Paulo'
idade = 34
altura = 1.70
e_maior = idade > 18
peso = 94.8
imc = peso / altura ** 2

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{1} - {0} tem {1} anos de idade - imc é {2}'.format(nome, idade, imc))
print('{im:.2f} - {n} - {i} - {im}'.format(n=nome, i=idade, im=imc))
