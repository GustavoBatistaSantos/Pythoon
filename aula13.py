lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
#lanche[1] = 'Refrigerante'#vai dar erro pois as tuplas são imutaveis
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('comi pra caramba')
print(len(lanche))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #outra forma de fazer


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche)) #ordena em ordem alfabética
a = (2, 5, 4)
b = (5,8,1,2)
print(a)
print(b)
c = a + b
print(c)
print(len(c))
print(c.count(5)) #quantas vezes esta aparecendo o 5 em c
print(c.index(8)) #mostra a posição pegando a primeira ocorrencia
print(c.index(5, 2)) # começa a partir da posição 2


pessoa = ('Gustavo', 30, 'm', 92)# as tuplas aceitam diferentes tipos de dados
print(pessoa)
del pessoa# apaga a tupla
del pessoa[2]#não apaga apenas um item
print(pessoa)