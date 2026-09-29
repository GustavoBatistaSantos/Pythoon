from random import randint
from time import sleep
from operator import itemgetter#ordena items
jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)
        }
ranking =[]
print('valores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#0 ordena por chaves e o 1 por valores, reverse faz ficar decrescente
print('Ranking de jogadores')
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    #+1 porque o indice começa com zero
    sleep(1)

