# nomes = ["marieta", "Josefa", "joão"]
# print(nomes)
# print(nomes[0])
# print(nomes[1])
# print(nomes[2])
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numeros)
# print(numeros[1])
# print(numeros[6])
# print(numeros[9])

# marcas_de_roupas = []

# print(marcas_de_roupas)


# marcas_de_roupas.append("nike")
# print(marcas_de_roupas)
# marcas_de_roupas.append("adidas")
# print(marcas_de_roupas)
# marcas_de_roupas.append("puma")
# print(marcas_de_roupas)

# for n in range(1,4):
#     value = input("Digite uma marca de roupa: ")
#     marcas_de_roupas.append(value)
# print(marcas_de_roupas)

# sobrenomes = []

# sobrenomes.append('Correa')
# sobrenomes.insert(0, 'Jesus')
# print(sobrenomes)
# sobrenomes.remove('Correa')
# print(sobrenomes)
# sobrenomes.append('Oliveira')
# print(sobrenomes)
# del sobrenomes[0]
# print(sobrenomes)

# nomes = []
# for n in range(1,6):
#     nomes.insert(n, input('Digite um nome: '))
# print(nomes)

# crie uma lista com frutas e apague o segundo elemento usando del
frutas = []
for n in range(1,6):
    frutas.insert(n, input('Digite uma fruta: '))
print(frutas)
del frutas[1]
print(frutas)