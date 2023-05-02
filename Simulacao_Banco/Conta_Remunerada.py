""" Criando a conta Remunerada em nosso Banco """
from Conta import Conta
from ContaCliente import Poupança

class ContaRemuneradaPoupança(Conta, Poupança):
    def __init__ (self, TaxadeRemuneraçao, clientes, numero, saldo, taxaremuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupança.__init__(self, TaxadeRemuneraçao)
        self.taxaremuneracao = taxaremuneracao

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao
