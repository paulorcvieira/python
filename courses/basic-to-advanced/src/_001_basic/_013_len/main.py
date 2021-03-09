usuario = input('Usuário: ')
qnt_caracteres = len(usuario)

print('usuário:', usuario, 'caracteres', qnt_caracteres)

if qnt_caracteres < 6:
    usuario = input('Usuário: ')

print(len(usuario))
print(usuario.__len__())
