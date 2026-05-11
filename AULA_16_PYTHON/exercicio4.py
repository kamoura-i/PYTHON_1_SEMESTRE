lista_nome = []
lista_idade = []

for i in range(5):
    idade = int(input("Digite sua idade: "))
    lista_idade.append(idade)
    nome = input("Escreva o seu nome: ")
    lista_nome.append(nome)


print("Pessoas com 18 anos +")

for i in range(5):
    if lista_idade[i] >=18:
        print(lista_nome[i])