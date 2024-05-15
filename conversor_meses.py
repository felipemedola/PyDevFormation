meses = ["january", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

numero = int(input("Digite um número de 1 a 12: "))

if 1 <= numero <= 12:
    nome = meses[numero - 1]
    print(nome.title())
else:
    print("Opção inválida!")