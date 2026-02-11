idadeUsuario = int(input("Insira sua idade: "))
documentoUsuario = input("Você possui documento? Insira s ou n: ")
if (idadeUsuario >= 18 and documentoUsuario == 's'):
    print("Acesso permitido")
else:
    print("Acesso negado")

