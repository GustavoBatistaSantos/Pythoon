valor = []
continuar = 's'
while continuar == 's':
    num =int(input('Digite um valor'))
    if num in valor:
        print('valor duplicado! não vou adicionar')
    else:
        valor.append(num)
        print('Valor adicionado com sucesso')
    continuar = str(input('Quer continuar?')).lower().strip()[0]
valor.sort()
print(f'Você digitou os valores {valor}')