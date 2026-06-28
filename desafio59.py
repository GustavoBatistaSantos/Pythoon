print('Gerador de PA')
print('-=-'*10)
primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10# termos iniciais
while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais '))
print(f'Progressão finalizada com {total} termos')