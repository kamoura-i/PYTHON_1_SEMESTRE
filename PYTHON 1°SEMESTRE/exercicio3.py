num = int(input("Digite um número: "))

match num % 3:
    case 0:
        print(f"O numéro {num} é múltiplo de 3")
    case _:
        print(f"O número {num} não é múltiplo de 3")