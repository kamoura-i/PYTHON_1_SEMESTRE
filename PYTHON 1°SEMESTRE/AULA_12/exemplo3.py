# Solicatar a idade N pessoas e calcular a média das idades

quantidade = int(input("Informe a quantidade de pessoas: "))

cont = 0
soma = 0

while cont < quantidade:
    idade = int(input("Informe a idade: "))
    soma += idade
    cont +=1

media = soma / quantidade
print(f'Médias das idades: {media:.2f}')
print(f'Pessoas: {quantidade}')