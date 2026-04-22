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
# list_products = []
# for produto in range(1,6):
#     new_product = input("Digite um novo produto para a lista: ")
#     list_products.append(new_product)
# retira_produto = input("Digite o produto a ser retirado: ")
# for produto in list_products:
#     if produto == retira_produto:
#         list_products.remove(produto)
#     elif len(produto) == len(list_products):
#         print(f"Não encontramos este produto na lista.")
#         break
# print(list_products)

# 12
# soma_total = 0
# numero_usuario = 0
# cont = 0
# while True:
#     cont += 1
#     numero_usuario = int(input("Digite um numero para a soma: "))
#     soma_total += numero_usuario
#     if soma_total > 100:
#         break
# print(f"O numero total de numeros digitados foi de {cont}")
# print(f"A soma final foi de {soma_total}")

# 13
# lista_alunos = []
# lista_notas = []
# nota = ''
# nota_media = 0

# for indice in range(1,6):
#     lista_alunos.append(input("Digite o nome do aluno: "))
#     nota = input("Digite a nota  do aluno: ")
#     nota_media += int(nota)
#     lista_notas.append(nota)
# for indice in range(0,5):
#     print(f"{lista_alunos[indice]}, {lista_notas[indice]} ")
# print(nota_media/len(lista_notas))

# # 14
# lista_notas = []
# lista_aprovados = []
# nota = ''
# soma_notas = 0.0
# media_turma = 0.0
# notasAprovadas = 0.0
# for i in range(1,7):
#     nota = (input(f'Digite a {i}ª nota para inserir na lista: '))
#     lista_notas.append(float(nota))
# print(lista_notas)
# for var in range(len(lista_notas)):
#     soma_notas += lista_notas[var]
#     print(soma_notas)
#     if lista_notas[var] >= 6:
#         notasAprovadas += 1
#         lista_aprovados.append(var)
#     if len(lista_aprovados) == 0:
#         lista_aprovados.append('Nenhum aluno foi aprovado')
# media_turma = soma_notas/len(lista_notas)
# # media das notas
# print(media_turma)
# # quantas notas ficaram acima da media
# print(notasAprovadas)
# # quais são as notas aprovadas
# print(lista_aprovados)

# # 15
# lista_frases = []
# for frase in range(0,3):
#     lista_frases.append(input('Digite uma frase para ser gravada no arquivo: '))
# print(lista_frases)
# arquivo = open("frases.txt", "w")
# for index in lista_frases:
#     arquivo.write(f"Frase 1: {index}\n")
# arquivo.close()

# 16
# with open("frases.txt") as list:
#     for line in list:
#         print(line.strip())

# 17
# contador = 0
# with open("frases.txt") as list:
#     for line in list:
#         contador += 1
# print(contador)

# 18