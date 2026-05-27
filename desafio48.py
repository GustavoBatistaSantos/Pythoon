primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + 10 * razao #formula de PA
for c in range(primeiro, decimo , razao):
    print(f'{c}', end=' -> ')
print('Acabou')
