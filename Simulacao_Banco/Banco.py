""" Exercicio EXTRA incluir a classe Banco que irá armazenar as contas e clientes """

from Cliente import Cliente
from Conta import Conta


class Banco:
    def __init__ (self, codigo, nome):
        self.condigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self, contacliente):
        self.contas.append(contacliente)

    def calcularredimentomensal(self):
        for c in self.contas:
            c.CalcularRendimento()
    def imprimisaldocontas(self):
        for c in self.contas:
            c.Extrato()

