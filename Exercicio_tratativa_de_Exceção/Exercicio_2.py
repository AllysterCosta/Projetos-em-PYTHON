""" Implemente uma solução onde seja feita a tratativa de uma exceção
de divisão por zero """

while True:
    try:
        num1 = int(input('Entre com o 1 numero da divisão: '))
        num2 = int(input('Entre com o 2 numero da divisão: '))
        divisao = num1 / num2
        print('Divisão feita com sucesso')
        break
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')
        print('Por favor, tente novamente.')
print(f'O resultado da divisão é {divisao}')

"""  """

