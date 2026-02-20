#1 Exercício append

# nomes_de_animais = []
# nomes_de_animais.append('Gato')
# nomes_de_animais.append('Cachorro')
# nomes_de_animais.append('Papagaio')
# print(nomes_de_animais)

#2 Exercício insert

# numeros = [200,300,400]
# print(numeros)
# numeros.insert(1,100)
# print(numeros)

#3 Exercício del

# cores = ['Vermelho', 'Amarelo', 'Azul', 'Verde', 'Branco']
# print(cores)
# del cores[2]
# print(cores)

#4 Exercício remove

# frutas = ['banana', 'maca', 'pera']
# print(frutas)
# frutas.remove('banana')
# print(frutas)

#Exercício final
lista_de_numeros = []
for n in range(1,11):
    lista_de_numeros.append(int(input('Digite um numero para a lista: ')))

for cont in lista_de_numeros:
    if cont > 10:
        print(f'o numero {cont} é maior')
    else:
        print(f'o numero {cont} não é maior que 10')