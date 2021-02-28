from model.Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, name, email, data_nascimento, senha, cargo, data_registro):
        self.cargo = cargo
        self.data_registro = data_registro

        super().__init__(name, email, data_nascimento, senha)

        def setcargo(self, cargo):
            self.cargo = cargo

        def getcargo(self):
            return self.cargo

        cargo = property(getcargo, setcargo)
