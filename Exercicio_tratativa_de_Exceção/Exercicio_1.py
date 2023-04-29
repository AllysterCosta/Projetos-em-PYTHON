""" Exercicio 1 tratar exceção """
# Implementar uma solução que faça o tratamento de exceção para verificar 
# se uma entrada é numerica e que, além disso, insista que o usuário
# digite um número valido

while True:
    try:
        x = int(input('Entre com um número: '))
        break
    except:
        print('A entrada não é um número tente novamente!')
print(f'O número digitado foi {x}')

""" Para esse codigo eu usei um laço de repetição while que testa a condição true
assim o codigo fica em loop até que o break pela a saida do codigo, fazendo assim com que
o codigo só pare de ser executado quando a entrada de dados for a esperada,
esse foi meu primeiro codigo sozinho tratando entrada de dados. """