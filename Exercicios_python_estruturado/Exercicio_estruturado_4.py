""" Supondo que temos uma lista de numeros [10,2,5,7,6,3] devemos fazer a solução que traga a soma
somente de números pares, no caso o resultado será 18 """

# Solução 1
lista = [10, 2, 5, 7, 6, 3]
n = len(lista)
soma = 0

for i in range(n):
    if (lista[i]%2==0):
        soma = soma+lista[i]
print(f'O somatório de números pares é de {soma}')


# Solução 2 
# Usando programação funcional, nas aulas melhor indicado pelo professor
soma = 0
for num in lista:
    if (num % 2 ==0):
        soma = soma + num
print(f'O somatório de itens pares é {soma}')
