import numpy as np

def calcular_raizes(a, b, c, delta):
    if (delta < 0):
        resultado = 'A equação não possui raízes nos números reais'
    elif (delta == 0):
        x = -b/(2*a)
        resultado = f'A equação possui apenas a raiz: {x}'
    else:
        x1 = (-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.sqrt(delta))/(2*a)
        resultado = f'A equaçãp possui as raízes: {x1} e {x2}'
    return resultado

def entrada_de_dados():
    coeficiente = quantidade = eval(input("Digite um valor do coeficiente: "))
    return coeficiente

def calc_delta(a, b, c):
    delta = b * b - 4 * a * c
    return delta

# Entrada de dados
a = entrada_de_dados()
b = entrada_de_dados()
c = entrada_de_dados()

delta = calc_delta(a, b, c)

resultado = calcular_raizes(a, b, c, delta)
print(resultado)

