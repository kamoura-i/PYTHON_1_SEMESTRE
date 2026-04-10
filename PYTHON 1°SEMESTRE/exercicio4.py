print("Códigos das palestras")
print("1 - Linux")
print("2- Banco de Dados")
print("3- Windows Server")
print("4- Lógica de Programação")
code = int(input("Digite o código da palestra: "))

match code:
    case 1:
        print("Palestra Linux no Auditório 1")
    case 2:
        print("Palestra Banco de Dados no Auditório 2")
    case 3:
        print("Palestra Windows Server no Auditório 3")
    case 1:
        print("Palestra Lógica de Programação no Auditório Principal")
    case _:
        print("ERRO: OPÇÃO INVALÍDA")

