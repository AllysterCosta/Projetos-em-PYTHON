from Conta import Conta
from Cliente import Cliente
from Banco import Banco

from ContaCliente import ContaCliente
from ContaComum import ContaComum
from ContaClienteRemunerada import ContaRemunerada


cliente1 = Cliente(123, 'João', "Rua 1")
cliente2 = Cliente(456, 'Maria', 'Rua 2')
cliente3 = Cliente(789, 'Ricardo', 'Rua 3')

""" conta1 = Conta([cliente1, cliente2], 1, 2000)
conta2 = Conta(cliente3, 2, 2300)
conta3 = Conta([cliente2, cliente3], 3, 1250) """
""" ContaPoupança = Poupança(0.1) """

Contacliente1 = ContaCliente(1, 0.01, 0.1, 2000, 0.05)
Contacomum1 = ContaComum(2, 0.01, 0.1, 2000, 0.05)
ContaRemunerada1 = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

banco1 = Banco(1, "TESTE")

banco1.adicionaconta(Contacliente1)
banco1.adicionaconta(Contacomum1)
banco1.adicionaconta(ContaRemunerada1)
banco1.calcularredimentomensal()
banco1.imprimisaldocontas()

""" conta1.transfereValor(conta2, 200)
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()

conta1.extrato.extrato(conta1.numero)

banco1.gerirClientes()
banco1.gerirContas()
 """