n1 = int(input("Digite algum numero: "))
n2 = int(input("Digite algum numero: "))
while n1 == n2:
    print("Digite valores diferentes!")
    n1 = int(input("Digite algum numero: "))
    n2 = int(input("Digite algum numero: "))

soma = n1 + n2

print(f'Soma: {soma}')