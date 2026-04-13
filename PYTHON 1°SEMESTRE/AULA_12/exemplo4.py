# Solicatar a idade N pessoas e calcular a média das idades

cont = 0
soma = 0

while True:
    idade = int(input("Informe a idade: "))
    if idade < 0:
        break
    soma += idade
    cont +=1

media = soma / cont
print(f'Média das idade: {media:.2f}')