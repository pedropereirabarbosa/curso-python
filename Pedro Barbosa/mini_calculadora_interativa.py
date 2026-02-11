print("=== Mini Calculadora ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Escolha uma operação (1 a 4): ")
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if operacao == "1":
    print("Resultado:", numero_1 + numero_2)
elif operacao == "2":
    print("Resultado:", numero_1 - numero_2)
elif operacao == "3":
    print("Resultado:", numero_1 * numero_2)
elif operacao == "4":
    if numero_2 != 0:
        print("Resultado:", numero_1 / numero_2)
    else:
        print("Erro: divisão por zero.")
elif operacao == "5":
    print("Resultado:", numero_1 % numero_2)
elif operacao == "6":
    print("Resultado:", numero_1 ** numero_2)

else:
    print("Operação inválida.")