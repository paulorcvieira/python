"""
For / Else
"""

names = ['Paulo', 'Caroline', 'Carmen']
letter = 'C'
start_with_letter = False

for name in names:
    if name.lower().startswith(letter.lower()):
        print(name, '-', f'Começa com "{letter}"\n')
        start_with_letter = True
        break
    else:
        print(name, '-', f'Não começa com "{letter}"\n')

if start_with_letter:
    print(f'Existe um nome que começa com "{letter}"\n')
else:
    print(f'Não existe um nome que começa com "{letter}"\n')
