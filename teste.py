pessoas = []
for i in range(1, 5):
    print(f"Pessoa {i}:")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    pessoas.append([idade, altura])

print("Dados salvos na lista:")
print(pessoas)

