lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

frequencia = {}

for numero in lista:
    if numero in frequencia:
        frequencia[numero] += 1
    else:
        frequencia[numero] = 1

numero_repetido = max(frequencia, key=frequencia.get)

print("O número que se repete mais vezes é:", numero_repetido)