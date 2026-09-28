# pessoas = {'nome': 'Gustavo', 'sexo': 'm', 'idade':22}
# # print(pessoas[0])#da erro porque deveria ser nome
# print(pessoas['nome'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# brasil = []
# estado1 = {'uf': 'Rio de janeiro', 'sigla':'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])

estado = {}
brasil = []
for c in range(0,3):
    estado ['uf'] = str(input('Unidade federativa: '))
    estado ['sigla'] = str(input('Sigla do estado: '))
    # brasil.append(estado[:]) em dicionarios não se pode fazer fatiamento
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():#k e a chave do item e, e v o valor sendo items da lista brasil.
        print(f'O campo {k} tem valor {v}')