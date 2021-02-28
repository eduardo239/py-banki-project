from model.Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, cpf):
        self.cpf = cpf


