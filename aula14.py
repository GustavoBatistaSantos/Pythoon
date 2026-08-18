# num = [2,5,9,1]
# num[2] = 3 #pode modificar a lista
# # num [4] = 7 #vai dar erro porque não tem esse índice na lista
# num.append(7)
# num.sort()
# num.sort(reverse=True)
# num.insert(2,0) #adiciona na posição 2 o valor de zero empurrando os outros elementos.
# num.insert(2,2) #adiciona na posição 2 o valor de zero empurrando os outros elementos.
# num.remove(2) # remove a primeira ocorrência
# num.remove(3) #da erro pois não exite o númro  4
# if 4 in num:
#     num.remove(4)#maneira certa de remover
# else:
#     print('não achei o número 4')
# num.pop(2)#elimina o elemento 2
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []
# for cont in range(0,5):
#     valores.append(int(input('digite um valor')))
# for c,v in enumerate(valores): #mostra o indice e os valores.
#     print(f'na posição {c} encontrei o valor {v}....', end='')
# print('cheguei ao final da lista')

a = [2,3,4,7]
# b = a liga as duas listas
b = a[:] #copia todos os itens da lista
b[2] = 8 #mexe nas duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
