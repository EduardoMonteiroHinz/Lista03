numeros = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(numero)

numeros.sort()

print("Números em ordem crescente:")
for numero in numeros:
    print(numero)