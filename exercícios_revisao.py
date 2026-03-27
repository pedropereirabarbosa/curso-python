# # Média com quantidade definida pelo usuário - 03
# notas = []
# qtd = int(input("Digite quantas notas você deseja informar: "))
# for i in range(1, qtd):
#     nota = float(input("Digite uma nota: "))
#     notas.append(nota)
# print (f"A quantidade de notas foi {len(notas)}")
# print(f"A soma total de notas é {sum(notas)}")
# print(f"A média de notas foi {sum(notas) / len(notas)}")


# # 04
# numeros = []
# for i in range(1,11):
#     numero = int(input("Digite um numero: "))
#     numeros.append(numero)
# valor_maior = 0
# valor_menor = 0
# for numero in numeros:
#     if numero > valor_maior:
#         valor_maior = numero
#     if numero > valor_menor:
#         valor_menor = numero
# print(f"O maior valor é {valor_maior} e o menor é {valor_menor}")

# # 05
# lista_nome = []
# for i in range(1,6):
#     nome = input("Digite seu nome: ")
#     lista_nome.append(nome)
# print(lista_nome)
# print(len(lista_nome))
# print(f"O primeiro nome é {lista_nome[0]} e o último é {lista_nome[len(lista_nome) -1]}")

# # 06
# lista_num = []
# for i in range(1,11):
#     num = int(input("Digite um numero: "))
#     lista_num.append(num)

# list_im = []
# list_par= []
# for n in lista_num:
#     if n % 2 == 0:
#         list_par.append(n)
#     if n % 2 != 0:
#         list_im.append(n)

# print(lista_num)
# print(list_im)
# print(list_par)

# 07
# name_list = []
# print("Menu")
# print("1 - Cadastro de Nome")
# print("2 - Lista de Nomes")
# print("3 - Sair")
# while True:
#     new_name = ""
#     option = input("Digite uma opção: ")
#     if option == "1":
#         new_name = input("Digite um nome: ")
#         name_list.append(new_name)
#         print("Nome cadastrado com sucesso")
#     elif option == "2":
#         for name in name_list:
#             print(f"Os nomes cadastrados são {name_list}")
#     elif option == "3":
#         break
#     else:
#         print("Opção Incorreta. Tente Novamente.")

# 08
# palavra = input("Digite uma palavra: ")
# print(f"A quantidade total de letras é {len(palavra)}")
# print(f"A quantidade de vezes que a letra a aparece é {palavra.count("a")}")

# 09
# num_inicial = int(input("Digite um numero inicial: "))
# num_final= int(input("Digite um numero final: "))
# for num in range(num_inicial, num_final+1):
#     for multiplicação in range(1,6):
#         print(num*multiplicação)

# 10
# list_of_names = []
# for name in range(1,7):
#     nome = input("Insira um nome na lista: ")
#     list_of_names.append(nome)
# nome_buscado = input("Digite um nome para busca: ")
# if nome_buscado in list_of_names:
#     print(f"O nome {nome_buscado} está na lista.")
# else:
#     print(f"O nome {nome_buscado}  não está na lista")

# 11
list_products = []
for produto in range(1,6):
    new_product = input("Digite um novo produto para a lista: ")
    list_products.append(new_product)
retira_produto = input("Digite o produto a ser retirado: ")
for produto in list_products:
    if retira_produto == produto:
        list_products.remove(produto)
    else:
        print(f"Não encontramos este produto na lista.")
        break       
print(list_products)