# Soma de Valores Positivos
soma_numeros = 0
contador_negativo = 0

for num in range(1,9):
    numero = int(input("Digite um numero para soma: "))
    soma_numeros += numero
    if numero < 0:
        contador_negativo += 1
print(soma_numeros)
print(contador_negativo)