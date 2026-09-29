from datetime import datetime
dados = {}
dados ['nome']= str(input('Digite o seu nome: '))
nasc = int(input('Digite o ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input('Carteira de trabalho(0 caso não tenha )'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = ((dados['contratação']+ 35) - datetime.now().year)
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')