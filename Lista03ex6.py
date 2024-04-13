dentro_intervalo = 0
fora_intervalo = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if 10 <= numero <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"Quantidade de números dentro do intervalo: {dentro_intervalo}")
print(f"Quantidade de números fora do intervalo: {fora_intervalo}")
