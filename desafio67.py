print('-'*15)
print('loja super baratão')
print('-'*15)
total = totmil = menor = cont= 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [s/n]')).strip().lower()[0]
    if continuar in 'n':
        break
print('Fim do programa')
print(f'O total da compra foi {total:.2f}')
print(f'temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')


    