aluno ={}
aluno['Nome'] = str(input('Qual é o seu nome '))
aluno['media'] = float(input('Qual é a sua média '))
if aluno['media'] >= 6.0:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(aluno)