# def saudacao():
#     print('hello world!')
#     print('hello world!')
#     print('hello world!')

# def soma():
#     print(f'soma 2 + 2: {2+2}')
#     print(f'soma 2 + 2: {2+2}')
#     print(f'soma 2 + 2: {2+2}')

# def soma_com_parametro(num_one, num_two):
#     print(num_one + num_two)

# soma_com_parametro(10, 20)

#divide

# def divisao(numerador, denominador):
#     print(numerador/denominador)

# divisao(10,2)

#multiplica

# def multiplicacao(num1, num2):
#     print(num1*num2)

# multiplicacao(5, 10)

#subtrai

# def subtracao(num1, num2):
#     print(num1 - num2)

# subtracao(5, 5)

#cria uma função que recebe uma lista de números e retorna uma lista de numeros pares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def recebeLista(list):
    for n in list:
        if n % 2 == 0:
            print(list[n])

recebeLista(lista)

#consertar funçao acima