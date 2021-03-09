x = 0
while x < 5:
    if x == 3:
        x = x + 1
        continue

    if x == 4:
        break

    print(x)
    x = x + 1

print('Finish')

c = 0  # column
while c < 10:
    l = 0  # line
    while l < 5:
        print(f'({c},{l})')
        l += 1
    c += 1
print('Finish')

while True:
    print()
    num_1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    num_2 = input('Digite outro número: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print(num_1 / num_2)

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break

print('Finish')
