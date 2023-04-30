""" Definindo a Classe conta """

import datetime
from Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato() 

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(['DEPOSITO', valor, "Data", datetime.datetime.today ()])

    def sacar(self, valor):
        if( self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True
        
    def transfereValor(self, contaDestino, valor):
        if(self.saldo < valor):
            return ('Saldo insuficiente!')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return ('Transferencia realizada')
    
    def gerarsaldo(self):
        print(f"Numero: {self.numero}\nSaldo:{self.saldo}")

    

# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script
