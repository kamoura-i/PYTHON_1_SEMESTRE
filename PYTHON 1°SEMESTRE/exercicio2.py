num = float(input("Digite um numero: "))
print("Selecione uma das opções abaixo")
print("1- Quero o dobro")
print("2- Quero a metade")
print("3- Quero 10% desse valor")
opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        print(f'O dobro do número é {num}')
    case 2:
        print(f'A metade do número é {num}')
    case 3:
        print(f'10% de {num} é {num*0.10}')

