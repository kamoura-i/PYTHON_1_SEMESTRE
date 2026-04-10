valor_total = float(input("Digite o valor total da compra: "))
cliente = input("Você é  um cliente comum (C), funcionário (F) ou vip (V): ").lower()


match cliente:
    case "c":
        print(f"O valor a ser pago é {valor_total} sem descontos")
    case "f":
        print(f"O valor a ser pago é {valor_total * 0.9}")
    case "v":
        print(f"O valor a ser pago é {valor_total * 0.95}")