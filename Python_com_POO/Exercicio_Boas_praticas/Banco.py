""" Exercicio EXTRA incluir a classe Banco que irá armazenar as contas e clientes """

from Cliente import Cliente
from Conta import Conta


class Banco:
    def __init__ (self, contas, clientes):
        self.contas = contas
        self.clientes = clientes

    def gerirClientes(self):
        listaCilentes = ', '.join([cliente.nome for cliente in self.clientes])
        print(f'Os clientes do banco são: {listaCilentes}')

    def gerirContas(self):
        listaContas = ', '.join(str(contas.numero) for contas in self.contas)
        print(f'As contas do banco são: {listaContas}')
    

