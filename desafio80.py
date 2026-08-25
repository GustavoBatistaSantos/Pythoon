expr = str(input('digite uma expressão: '))
esquerda = direita = 0
for simb in expr:#string é uma lista de caracteres
    if simb == '(':
        esquerda +=1
    elif simb == ')':
        direita += 1
if esquerda == direita:
    print('A expressão esta correta')
else:
    print('A expressão não está correta')
