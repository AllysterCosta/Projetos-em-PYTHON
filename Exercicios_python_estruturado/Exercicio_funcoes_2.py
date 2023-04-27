""" Implementar uma função que faça a soma de todos os numeros pares de uma lista """

def somar_num(lista):
    soma = 0
    for num in lista:
        if( num % 2 == 0):
            soma += num
    return soma

lista_exemplo = [2, 3, 6, 4, 1, 5, 7]
soma = somar_num(lista_exemplo)
print('A soma é [{}]'.format(soma))
