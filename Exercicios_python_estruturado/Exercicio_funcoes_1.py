""" Implemente uma solução onde é feita a busca do menor valor de uma lista usando uma função """


def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo

lista_teste = [2, 10, 3, 1, 4 ,5]
menor = encontrar_minimo(lista_teste)
print("O menor valor do elemento da lista é: [{}]".format(menor))