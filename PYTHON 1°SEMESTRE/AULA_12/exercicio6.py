cont = 1
menor = 0
while cont < 10:
    nums = int(input(f"Digite 10 números: "))
    if cont == 1:
        menor = nums
    else:
        if nums < menor:
            menor = nums
    cont +=1 

print(menor)

