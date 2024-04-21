cachorro = {
    'nome': 'Dante',
    'idade': 3
}

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-3333'},
    'giovanna@g,ail.com': {'nome': 'Giovanna', 'telefone': '3333-3333'},
    'chappin@gmail.com': {'nome': 'Chappin', 'telefone': '3333-3333'}
}

# print(contatos.items())
for chave, valor in contatos.items():
    print(chave, valor)


print(contatos.get('guilherme@gmail.com'))

for chave, valor in contatos.items():
    print(valor.get('nome'))
