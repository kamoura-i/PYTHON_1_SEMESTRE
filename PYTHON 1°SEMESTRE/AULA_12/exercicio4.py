quantidade = int(input("Digite a quantidade numeros: "))
cont = 0
cont_par = 0
cont_impar = 0
soma_par = 0
soma_impar = 0

while cont < quantidade:
    num = int(input("Digite os numeros: "))
    if num % 2 == 0:
        cont_par +=1
        soma_par += num
    else:
        cont_impar +=1
        soma_impar += num
    cont +=1


media_par = soma_par / cont_par
media_impar = soma_impar / cont_impar


print(f'Médias numeros pares: {media_par}')
print(f'Média numeros impares: {media_impar}')