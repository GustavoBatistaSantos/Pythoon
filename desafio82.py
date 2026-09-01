valores = []
temp = []
impar = []
par = []
for c in range(0,7):
    temp.append(int(input('digite um valor')))
    valores.append(temp[:])
    if temp[0] % 2 ==0:
        par.append(temp[:])
    else:
        impar.append(temp[:])
    temp.clear()
impar.sort()
par.sort()
print(f'Os valores pares em ordem crescente foram {par} e os impares{impar}')