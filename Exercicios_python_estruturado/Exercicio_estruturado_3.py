""" Implementar solução em Python que resolva a questão
    - Calcular o valor de uma compra, sendo que o preço unitário é 10,00
     Se for feita uma compra até 10 unidades, não há descontos
     Para compras entr 11 e 20 unidades é dado 10% de desconto
     Acima de 20 unidades, é dado 20% de desconto """

valor = 10.00
quantidade_itens = eval(input('Informe a quantidade comprada: '))
valor_total = valor * quantidade_itens
desconto10 = 0.1
desconto20 = 0.2

if(quantidade_itens <= 10):
    print(f'O valor total de compras é de: R${valor_total}')
elif(quantidade_itens <= 19):
    desconto = valor_total * desconto10
    valor_com_desconto = valor_total * (1-desconto10)
    print(f'O valor original é: R${valor_total}')
    print(f'O valor do desconto é: R${desconto}')
    print(f'O valor com o desconto é de: R${valor_com_desconto}')
else:
    desconto = valor_total * desconto20
    valor_com_desconto = valor_total * (1-desconto20)
    print(f'O valor original é de: R${valor_total}')
    print(f'O valor do desconto é de: R${desconto}')
    print(f'O valor com desconto é de R$: {valor_com_desconto}')
