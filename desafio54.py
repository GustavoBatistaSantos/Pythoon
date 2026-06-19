sexo = str(input('Informe seu dados [m/f]').strip().lower())[0]
while sexo not in 'mf':
    sexo = str(input('dados inconsistentes informe novamente').strip().lower())
    sexo.lower()[0]
print(f'O seu sexo é {sexo}')
    