class Conta:
    def __init__(self,numero_da_conta, saldo=0):
        self.saldo = saldo
        self.numero_conta = numero_da_conta

    def resumo(self):
        print(f"Conta de número: {self.numero_conta} tem saldo de {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor: self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

