soma_idades = 0
contador = 0

while True:
    idade = input("Digite uma idade (ou 'fim' para encerrar): ")
    if idade.lower() == 'fim':
        break
    idade = int(idade)
    soma_idades += idade
    contador += 1

if contador > 0:
    media = soma_idades / contador
    print(f"A média das idades apresentadas é: {media}")
else:
    print("Nenhuma idade foi apresentada.")