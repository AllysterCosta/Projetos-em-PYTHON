""" Exercicio 1 estruturas de decisão """
# Solução 1
a = 10
b = 20
if(a>b):
    maior = a
else:
    maior = b
print(f'O maior número é: {maior}')

#Solução 2
a = 10
b = 20
maior = a
if(b>maior):
    maior = b
print(f'O maior número é: {maior}')

s = 0
for i in range(5):
    s += 3*i
print(s)

s = 0
a = 1
while s < 5:
    s = 3*a
    a += 1
    print(s)




