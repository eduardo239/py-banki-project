class Pessoa:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def setnome(self, nome):
        self.__nome = nome

    def getnome(self):
        return self.__nome

    nome = property(getnome, setnome)
    '''email'''
    def setemail(self, email):
        self.__email = email

    def getemail(self):
        return self.__email

    email = property(getemail, setemail)

    '''data nascimento'''
    def setdatanascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def getdatanascimento(self):
        return self.__data_nascimento

    data_nascimento = property(getdatanascimento, setdatanascimento)

    '''senha'''
    def setsenha(self, senha):
        self.__senha = senha

    def getsenha(self):
        return self.__senha

    senha = property(getsenha, setsenha)


