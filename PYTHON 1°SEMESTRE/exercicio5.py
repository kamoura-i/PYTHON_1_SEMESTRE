print("--- Cardápio ---")
print("1 - Picanha       (R$ 25.00)")
print("2 - Lasanha       (R$ 20.00)")
print("3 - Strogonoff    (R$ 20.00)")
print("4 - Bife Acebolado(R$ 15.00)")
print("5 - Pão com Ovo   (R$ 5.00)")

opcao = int(input("\nDigite o número do prato desejado: "))

nome_prato = ""
preco_base = 0

match opcao:
    case 1:
        nome_prato, preco_base = "Picanha", 50.00
    case 2:
        nome_prato, preco_base = "Lasanha", 35.00
    case 3:
        nome_prato, preco_base = "Strogonoff", 30.00
    case 4:
        nome_prato, preco_base = "Bife Acebolado", 25.00
    case 5:
        nome_prato, preco_base = "Pão com Ovo", 10.00
    case _:
        nome_prato = "Inválido"

taxa = int(input(f"Deseja adicionar 10% de taxa no {nome_prato}? (1-SIM / 0-NÃO): "))

match taxa:
    case 1:
            valor_final = preco_base * 1.10
            print(f"\nPedido: {nome_prato}")
            print(f"Total com taxa (10%): R$ {valor_final:.2f}")
    case 0:
            print(f"\nPedido: {nome_prato}")
            print(f"Total: R$ {preco_base:.2f}")
    case _:
            print("\nOpção de taxa inválida! Considerando valor sem taxa.")
            print(f"Pedido: {nome_prato}")
            print(f"Total: R$ {preco_base:.2f}")