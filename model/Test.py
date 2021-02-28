from model.Cliente import Cliente
from model.Conta import Conta
from model.Funcionario import Funcionario
from model.Pessoa import Pessoa

c = Conta(30102, 100.34)
b = Conta(10003, 1000)

c.resumo()
c.sacar(100)
c.resumo()
c.depositar(1000)
c.resumo()

