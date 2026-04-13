cont = 0
cont_par = 0
cont_impar = 0
while cont < 10:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        cont_par +=1
    else:
        cont_impar +=1
    cont +=1

print(f'São {cont} números')
print(f'São {cont_par} números pares')
print(f'São {cont_impar} números impares')
