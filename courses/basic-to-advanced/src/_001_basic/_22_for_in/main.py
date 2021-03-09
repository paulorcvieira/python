"""
For in
Iterando string com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'
for letra in texto:
    print(letra)

for n, letra in enumerate(texto):
    print(n, letra)

for numero in range(5, 60, 2):
    print(numero)

print('#################')

for n in range(100):
    if n % 8 == 0:
        print(n)

nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
