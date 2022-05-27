from cliente import Cliente
from conta import Conta

cliente1= Cliente('lucas','060.028.091-80',18)


conta1= Conta(cliente1, 10.50)
print(conta1.cliente)

conta1.depositar(1000)
print(conta1.consultar_saldo())

conta1.sacar(500)
print(conta1.consultar_saldo())

conta1.sacar(1000)
