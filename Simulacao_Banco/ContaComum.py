""" Implementando a conta comum """

from ContaCliente import ContaCliente
class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)
    def CalcularRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)


