from Conta import Conta
from Cliente import Cliente
from Banco import Banco



cliente1 = Cliente(123, 'João', "Rua 1")
cliente2 = Cliente(456, 'Maria', 'Rua 2')
cliente3 = Cliente(789, 'Ricardo', 'Rua 3')

conta1 = Conta([cliente1, cliente2], 1, 2000)
conta2 = Conta(cliente3, 2, 2300)
conta3 = Conta([cliente2, cliente3], 3, 1250)

banco1 = Banco([conta1, conta2, conta3] , [cliente1, cliente2, cliente3])

conta1.transfereValor(conta2, 200)
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()

conta1.extrato.extrato(conta1.numero)

banco1.gerirClientes()
banco1.gerirContas()
