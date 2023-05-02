from Conta import Conta
from Banco import Banco


conta1 = Conta(1, 123,'João', 0)
conta2 = Conta(2, 456, 'Maria', 0)

conta1.depositar(1000)
conta1.transfereValor(conta2, 500)
print('Conta1 Saldo: ', conta1.saldo)
print('Conta2 Saldo: ',conta2.saldo)


