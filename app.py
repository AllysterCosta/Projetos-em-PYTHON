
# exercicios para as aulas da faculdade sobre Python Básico
import time
#Exercicio 1 entrada de dados usando input
nome = input('Entre com o seu nome: ')
print('Seu nome é: '+nome)
##########################################################################################
# Para tratar os dados apresentados como númerios é preciso usar a função
# eval() juntamente com a função input()
numero = eval(input('Digite um número inteiro: '))
print(numero)
##########################################################################################
#Exercicio da aula 1 Python Básico, calculadora IMC usando input e print
peso = eval(input('Informe seu peso: '))
altura = eval(input('Informe sua altura: '))
print('Calculando IMC...')
imc = peso/(altura**2)
time.sleep(2)
print('Seu IMC é: ', imc)
##########################################################################################
#Formatando saida de dados usando format()
hora = 10
minutos = 30
segundos = 16
print('{} : {} : {}'.format(hora, minutos, segundos))

print(f'{hora} : {minutos} : {segundos}')

#Também é possível especificar a largura de campo para exibir um inteiro.
# Se a largura não for especificada, ela será determinada pela quantidade 
# de dígitos do valor a ser impresso.

""" '{:4}, {:5}'.format(10, 100) """
#O método format() também pode ser usado para imprimir valores de ponto flutuante com a precisão definida.
""" '{:8.5}'.format(10.3) """
#Ao usar {:8.5}, estamos determinando que a impressão será com 8 espaços, mas apenas 5 serão utilizados.
##########################################################################################
#Imprimindo sequencias
seq = [1,3,5]
print(seq)
#Para imprimir uma substring, por exemplo, basta utilizar os colchetes para indicar o intervalo 
# de índices que deve ser impresso. Vale lembrar que o primeiro caractere da string é indexado com 0.

minhastr = 'Hello World'
print(minhastr[0:4])
print(minhastr[4:11])

#Também é possível imprimir a string como lida da direita para a esquerda. 
# Para isso, deve-se utilizar [: : -1]. Esse valor -1 indica que a leitura dos 
# caracteres será feita no sentido oposto ao tradicional.

print(minhastr[::-1])
print(minhastr[8:2:-1])




