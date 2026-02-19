#Exercício 1

# nome = "Pedro"
# idade = "26 anos"
# cidade = "São Paulo"
# print(f'Olá, meu nome é {nome}, tenho {idade} e moro em {cidade}.')

# Exercício 2

# filmeFavorito = input("Digite seu filme favorito: ")
# print(f'Seu filme favorito é {filmeFavorito}!!!')

#Exercício 3

# numeroDigitado = input("Digite um numero: ")
# while(numeroDigitado != '0'):
#     print(numeroDigitado)
#     numeroDigitado = input("Digite outro numero: ")

#Exercício 4

# for numero in range(1, 11):
#     print(numero)

#Exercício 5

# numero = int(input('Digite um número: '))
# for n in range(1,11):
#     print(f'{n} * {numero} = {n*numero}')

sacola = 0
for n in range(1,101):
    print(n)
    sacola += n
print(sacola)