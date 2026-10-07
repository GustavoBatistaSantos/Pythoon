galera = []
pessoa = ()
soma = media = 0
while True: 
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [m/f] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [s/n]'))
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma/len(galera)
print(f'A media de idade é de {media:f} anos')
print('As mulheres cadastradas foram', end='')
for p in galera:
