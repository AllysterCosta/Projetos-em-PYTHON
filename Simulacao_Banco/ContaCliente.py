""" A classe poupança foi criada com taxa de remunuração """
""" A classe ContaCliente foi definida como uma classe abstrata atraves do ABC (Abstract Base Classes) """
from abc import ABC, abstractmethod
import datetime
from typing import Any

class Poupança:
    def __init__ (self, TaxadeRemuneracao):
        self.TaxadeRemuneracao = TaxadeRemuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneraçaoConta(self):
        self.saldo += self.saldo * self.TaxadeRemuneracao


class ContaCliente(ABC):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR 
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento
    def CalcularRendimento(self):
        pass
    def Extrato(self):
        print(f'O saldo atual da conta {self.numero} é {self.valorinvestido:10.2f}')

