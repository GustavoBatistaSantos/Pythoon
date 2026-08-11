cont = 0
n1 = (int(input('Digite um número ')), int(input('Digite outro número ')), 
      int(input('Digite mais um número ')), int(input('Digite o último  número ')))
print(f'Você digitou os valores {n1}')
print(f'o número 9 foi digitado {n1.count(9)} vezes')
if 3 in n1:
    print(f'o valor 3 apareceu na {n1.index(3)+1}º posição')
else:
    print('O valor de 3 não foi encontrado')#tem que fazer o if para não dar erro caso o valor de 3 não for digitado
print(f'Os valores pares digitados foram ', end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
