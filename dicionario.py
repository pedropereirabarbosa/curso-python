# pessoa = {
#     "profissao": "professor",
#     "nacionalidade": "brasileira",
#     "idade": 45,
#     "estado_civil": "solteiro"
# }

# print(pessoa["estado_civil"])
# print(pessoa["idade"])
# print(pessoa["profissao"])
# print(pessoa["nacionalidade"])

# pessoa["nome"] = "João"
# print(pessoa["nome"])

# pessoa["cor_dos_olhos"] = "Castanhos"
# pessoa["altura"] = "178cm"
# pessoa["peso"] = "74kg"

# print(pessoa["cor_dos_olhos"])
# print(pessoa["altura"])
# print(pessoa["peso"])

# print(pessoa)

#estrutura de repetição
def contador_crescente():
    contador = 0
    while contador <= 5:
        if contador == 3:
            print("Encontrei o número 3!!")
            break # para o fluxo do while
        print(f"Funcionou!  {contador}")
        contador +=1 # incremento

def contador_decrescente():
    contador = 5
def menu():
    while contador >= 0:
        if contador == 0:
            print("Feliz ano novo!!")
        else:
            print(f"funcionou! {contador}")
        contador -= 1

    print("menu")
    print("digite 1 - atendente")
    print("digite 2 - segunda via de boleto")
    print("digite 3 - sair do chat")

    cont = 1
    while cont <= 3:
        opcao = input("digite sua opção: ")
        if opcao == '1':
            print("olá, sou joão...")
        if opcao == '2':
            print("informe seu cpf...")
        if opcao == '3':
            print("estamos encerrando seu atendimento...")
            break
        cont += 1

def menu_personalizado():
    while True:
        num_inicial = int(input("Digite o numero inicial: "))
        num_final = int(input("Digite o numero final: "))
        num_incremento = int(input("Digite o numero do incremento: "))
        if num_inicial > num_final:
            print("Insira outro numero: ")
        else:
            while num_inicial <= num_final:
                print(f"funcionando {num_inicial}")
                num_inicial += num_incremento
            break
menu_personalizado()