"""
Listas
fatiamento
apend, insert, pop, del, clear, extend, +
min, max
range
"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1.extend(l2)
print('extend: ', l1)
l1.append('a')
print('append: ', l1)
l1.insert(-1, 'b')
print('insert: ', l1)
l1.pop()
print('pop: ', l1)
del(l1[3:4])
print('del 3:4: ', l1)
del(l1[-1])
print('del l1[-1]: ', l1)
print('min: ', min(l1))
print('max: ', max(l1))

l3 = list(range(0, 100, 8))
print(l3)
l3 = list(range(0, 10))
print(l3)

secret = 'Opa!'.upper()
digitadas = []
chances = len(secret)

while True:
    if chances <= 0:
        print('Você PERDEU!')
        break

    print(digitadas)

    letter = input('Digite apenas uma letra: ')

    if len(letter) > 1:
        print('Ahhh!, isso não vale, digite apenas uma letra.')
        continue

    if letter.upper() in secret and letter.upper() != '':
        print(
            f'Uhulll! o caractere "{letter.upper()}" existe na palavra secreta.')
        digitadas.append(letter.upper())
    else:
        print(
            f'AFFF! o caractere "{letter.upper()}" NÃO existe na palavra secreta.')
        chances -= 1

    secret_temp = ''.upper()
    for letter_secret in secret:
        if letter_secret.upper() in digitadas:
            secret_temp += letter_secret.upper()
        else:
            secret_temp += '*'

    if secret_temp == secret:
        print(
            f'Você GANHOU!, a palavra secreta "{secret.upper()}" já foi encontrada.')

        logout = input('Deseja sair? [s]im ou [n]ão: ')
        if logout.lower() == 's':
            break

        continue
    else:
        print(f'A palavra secreta está assim "{secret_temp}"')

    if letter.upper() not in secret or letter.upper() == '':
        chances -= 1

    print(f'Você ainda tem "{chances}" chances.\n')
