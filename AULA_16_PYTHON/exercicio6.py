notas = []

nota = float(input("Digite a sua nota: "))
notas.append(nota)
while nota > 0:
    nota = float(input("Digite a sua nota: "))
    if nota >= 0:
        notas.append(nota)

print(f'Quantidade de notas: {len(notas)}')
media = sum(notas) / len(notas)
print(f'A média das notas foi de {media:.2f}')

contador = 0

for n in notas:
    if n > media:
        contador +=1
print(f'{contador} notas ficaram acima da média')
print("Notas na ordem em que foram informadas:")
for n in notas:
    print(n)