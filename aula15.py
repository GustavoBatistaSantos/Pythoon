# teste = []
# teste.append('gustavo')
# teste.append(30)
# galera = []
# #galera.append(teste)
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# #galera.append(teste)muda a lista de cima pois eu estou ligando as listas
# galera.append(teste[:]) #agora ele ta fazendo uma copia e não ligando as listas
# print(teste)
# print(galera)

# galera = [['Joao',19],['Ana',33],['Joaquim', 13],['Maria',45]] #declaração de 4 listas dentro da principal.
# print(galera[2][1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')
#     # print(p[1]) para mostrar apenas a idade

galera = []
dado = []
tomai = tomen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    #galera.append(dado) assim vai apagar as duas listas porque estão conectadas 
    dado.clear()
print(galera)

for p in galera:
    if p[1] >=18:
        print(f'{p[0]} é maior de idade')
        tomai += 1
    else:
        print(f'{p[0]} é menor de idade')
        tomen += 1
print(f'Temos {tomai} maiores de idade e {tomen} menores de idade')