import copy

d1 = {'chave1': 'valor da chave'}
print(d1, type(d1))
d1['nova_chave'] = 'Valor da nova chave'

print(d1)
print(d1['chave1'])

d2 = dict(chave3='Valor chave 3', chave4='valor da outra chave 4')
print(d2, type(d2))

d3 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla',
}

print(d3[(1, 2, 3, 4)])
print(d3)

# d3['nao_existe'] = 'Agora existe'
if 'nao_existe' in d3:
    print(d3['nao_existe'])

# ou
if d3.get('nao_existe') is not None:
    print(d1.get('nao_existe'))

d3.update({'chave_updade': 'valor updade'})

print(d3)

del d3['str']

print(d3)

print('str' in d3)
print(123 in d3.keys())
print('Tupla' in d3.values())

print(len(d3))

for k in d3:
    print(k)

for v in d3.values():
    print(v)

for k, v in d3.items():
    print(k, v)

clients = {
    'client_01': {
        'name': 'Paulo',
        'last_name': 'Vieira'
    },
    'client_02': {
        'name': 'Caroline',
        'last_name': 'Lima'
    },
}

for clients_k, clients_v in clients.items():
    print(f'Exibindo {clients.items()}')
    for dados_k, dados_v in clients_v.items():
        print(f'\t{dados_k} = {dados_v}')

d4 = {1: 'a', 2: 'b', 3: 'c', 4: ['Paulo', 'Caroline']}
v = d4.copy()
v[1] = 'Paulo'
v[4][0] = 'Carmen'

print(d4)
print(v)

d5 = {1: 'a', 2: 'b', 3: 'c', 4: ['Paulo', 'Caroline']}
v = copy.deepcopy(d5)

v[1] = 'Paulo'
v[4][0] = 'Carmen'

print(d4)
print(v)

lista = [
    ('c1', 1),
    ('c2', 2),
    ['c3', 3],
]

d6 = dict(lista)

print(d6)

d6.pop('c2')
print(d6)
d6.popitem()
print(d6)

lista_2 = {
    'a': 'b',
    'c': 'd',
    'e': 'f',
}

d6.update(lista_2)
print(d6)
