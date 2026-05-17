# 03 -  Média Com Quantidade Definida Pelo Usuário - 03

# notas = []
# qtd = int(input("Digite quantas notas você deseja informar: "))
# for i in range(1, qtd):
#     nota = float(input("Digite uma nota: "))
#     notas.append(nota)
# print (f"A quantidade de notas foi {len(notas)}")
# print(f"A soma total de notas é {sum(notas)}")
# print(f"A média de notas foi {sum(notas) / len(notas)}")


# 04 - Maior e Menor Número Digitado

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

# # 05 - Cadastro de Nomes em Lista

# lista_nome = []
# for i in range(1,6):
#     nome = input("Digite seu nome: ")
#     lista_nome.append(nome)
# print(lista_nome)
# print(len(lista_nome))
# print(f"O primeiro nome é {lista_nome[0]} e o último é {lista_nome[len(lista_nome) -1]}")

# 06 - Separação de Números Pares e Ímpares

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

# 07 - Menu Simples com Repetição

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

# 08 - Contador de Letras

# palavra = input("Digite uma palavra: ")
# print(f"A quantidade total de letras é {len(palavra)}")
# print(f"A quantidade de vezes que a letra a aparece é {palavra.count("a")}")

# 09 - Tabuada com Vários Numeros

# num_inicial = int(input("Digite um numero inicial: "))
# num_final= int(input("Digite um numero final: "))
# for num in range(num_inicial, num_final+1):
#     for multiplicação in range(1,6):
#         print(num*multiplicação)

# 10 - Lista com Nomes e Busca

# list_of_names = []
# for name in range(1,7):
#     nome = input("Insira um nome na lista: ")
#     list_of_names.append(nome)
# nome_buscado = input("Digite um nome para busca: ")
# if nome_buscado in list_of_names:
#     print(f"O nome {nome_buscado} está na lista.")
# else:
#     print(f"O nome {nome_buscado}  não está na lista")

# 11 - Remoção de Itens de uma Lista

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

# 12 - Soma com Condição de Parada

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

# 13 - Registro de Alunos

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

# # 14 - Relatório de Notas Acima da Média

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

# # 15 - Gravar Frases em um Arquivo

# lista_frases = []
# for frase in range(0,3):
#     lista_frases.append(input('Digite uma frase para ser gravada no arquivo: '))
# print(lista_frases)
# arquivo = open("frases.txt", "w")
# for index in lista_frases:
#     arquivo.write(f"Frase 1: {index}\n")
# arquivo.close()

# 16 - Leitura de Arquivo e Exibição de Conteúdo

# with open("frases.txt") as list:
#     for line in list:
#         print(line.strip())

# 17 - Contador de Linhas em um Arquivo

# contador = 0
# with open("frases.txt") as list:
#     for line in list:
#         contador += 1
# print(contador)

# 18 - Cadastro de Tarefas em Arquivo

# user_tasks = []
# for task in range(0,5):
#     user_tasks.append(input("Insira uma tarefa nova: "))
# arquivo = open("tarefas.txt", "w")
# for archive_task in user_tasks:
#     arquivo.write(f"{archive_task}\n")
# arquivo.close()
# print(f"5 tarefas foram salvas com sucesso.")

# 19 - Leitura e Numeração de Linhas

# with open("tarefas.txt", "r") as archive:
#     content = archive.readlines()
# for line, task in enumerate(content, start=1):
#     print(line,task)

# 20 - Sistema de Notas com Menu

# user_selection = 0
# students_grades = []
# while True:
#     print(f"1 - Adicionar Nota\n 2 - Mostrar Notas\n 3 - Mostrar Média\n 4 - Salvar Notas em Arquivo\n 5 - Sair\n")
#     user_selection = int(input(f"Insira uma das opções acima: "))
#     if user_selection == 1:
#         grade = float(input("Insira a nota: "))
#         if grade > 10.0 or grade < 0:
#             print("Insira a nota novamente, pois notas maiores que 10 ou menores que 0 não serão permitidas.")
#         else:
#             students_grades.append(grade)
#     elif user_selection == 2:
#         print(f"{students_grades}\n")
#     elif user_selection == 3:
#         mean = 0
#         for grade in students_grades:
#             mean += grade
#         print(mean/len(students_grades))
#     elif user_selection == 4:
#         archive = open("Notas Salvas.txt", "w")
#         for grade in students_grades:
#             archive.write(f"{grade}\n")
#         archive.close()
#     elif user_selection == 5:
#         break

# 21 - Lista com Números Únicos

# numbers = [1,2,3,4,5,6,7,8]
# # Loop para pedir 8 numeros para o usuario
# for number in range(0,8):
#     # Input que será inserido numa nova lista
#     new_number = int(input("Insira um novo numero na lista: "))
#     # Loop percorrendo a lista de numeros para comparação
#     for index, number in enumerate(numbers, start=1):
#         # Caso o numero inserido seja igual ao valor na lista
#         if new_number == number:
#             print("Repetido")
#             break
#         # Caso o numero seja diferente do valor na lista e a lista esteja no final
#         elif new_number != number and index == len(numbers):
#             numbers.append(new_number)
#             break
# print(numbers)

# # 22 - Mostrar uma lista na ordem inversa da inserção
# user_list = []
# for item in range(0,6):
#     user_list.append(int(input("Insira um número na lista: ")))
# #Loop para percorrer a lista ao contrário, iniciando no final e terminando no inicio com decréscimo indicado no for
# for index in range(5,-1,-1):
#     print(user_list[index])

# 23 - Mostrar palavras com mais de 5 letras
# word_list = []
# for word in range(0,7):
#     word_list.append(input("Insira uma palavra na lista: "))
# for inserted_word in word_list:
#     if len(inserted_word) > 5:
#         print(inserted_word)

# 24 - Relatório de arquivo com filtro
# numbers_sum = 0
# pair_numbers = 0

# with open("numeros.txt", "r") as archive:
#     for line_number, line in enumerate(archive, start=1):
#         actual_num = int(line.strip())

#         numbers_sum += actual_num

#         if line_number == 1:
#             major_number = actual_num
#             minor_number = actual_num
#         else:
#             if actual_num > major_number:
#                 major_number = actual_num
#             if actual_num < minor_number:
#                 minor_number = actual_num

#         if actual_num % 2 == 0:
#             pair_numbers += 1

#         print(actual_num)

# print(f"A soma dos números é: {numbers_sum}.")
# print(f"O maior número é: {major_number}.")
# print(f"O menor número é: {minor_number}.")
# print(f"A quantidade de números pares é de: {pair_numbers}.")

# 25 - Diário de Bordo do Usuário
# counter = 0
# archive = open("diário.txt", "w")
# while True:
#     frase = input("Digite uma frase para escrita em arquivo.\nDigite fim para encerrar o programa: ")
#     if frase == "fim":
#         archive.close()
#         print(f"O numero de frases inseridas é de {counter}.")
#         break
#     else:
#         archive.write(frase + "\n")
#         counter += 1