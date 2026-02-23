# # contador = 1

# # while contador <= 10:
# #     print(f"contador: {contador}")
# #     contador = contador + 1
# # cria uma variavel nota e coloque as seguintes regras
# # 7 -> Aprovado
# # 5 e 6 -> Recuperação
# # abaixo -> Reprovado

# nota = float(input("Digite a nota do aluno: "))

# if nota >= 7:
#     print("Aprovado")
# elif nota >= 5:
#     print("Recuperação")
# else:
#     print("Reprovado")

# contador = 1
# while contador <= 5:
#     print("Disparo")
#     # contador = contador + 1
#     contador += 1

# contador = 10
# while contador >= 0:
#     # print(contador)
#     if contador == 2:
#         print("Eu achei")
#     elif contador == 0:
#         print("Feliz Ano Novo!!")
#     else:
#         print(contador)
#     contador -= 1

# while True:
#     var = input("Digite o que deseja ou falar com atendente para sair... ")

#     if var == "falar com atendente":
#         print("Não temos atendente")
#         continue
#     else:
#         print("Aguarde... estamos resolvendo para você")

# for numero in range(0, 5):
#     if numero == 2:
#         print("achei")
#     else:
#         print(numero)

# for alo in range(5, 0, -1):
#     print(alo)

# for contador in range(0 , 11, 2):
#     print(contador)

# 0 a 20, se for par, mostre no terminal
# for num in range(0, 21):
#     if num % 2 == 0:
#         print(num)

for n in "olá, tudo bem?":
    if n == "u":
        print(f"achei{n}")
    print(n)