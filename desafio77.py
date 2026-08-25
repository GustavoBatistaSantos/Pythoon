valores = []
for c in range(0,5):
    num = int(input('digite um valor'))
    if c == 0:
        valores.append(num)
    elif num >valores[-1]:#para saber o último elemento da lista
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores): #varrendo a lista
            if num <= valores[pos]:
                valores.insert(pos, num)# na posição pos vai por o valor de n
                break
            pos+=1
print(f"Os valores digitados em ordem foram {valores}")