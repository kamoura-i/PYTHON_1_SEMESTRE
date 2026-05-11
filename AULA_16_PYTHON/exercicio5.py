import random
lista = []

for i in range(100):
    numeros_aleatorios = random.randint(1,100)
    lista.append(numeros_aleatorios)

num = int(input("Digite algum número: "))
contador = 0
for n in lista:
    if n == num:
        contador +=1
print(lista)
print(f'O número aparece {contador} vezes')