import sys
from datetime import datetime

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from PyQt5.QtWidgets import QMessageBox

from typo import *

db_name = 'contacts.sqlite'


def connection():
    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName("storage/" + db_name)

    if not con.open():
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        sys.exit(1)

    if con.isOpen():
        return con, 'Conectado com o banco de dados.'


def create_table(table_name, **kwargs):
    sql1 = f"""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(46) NOT NULL,
        email VARCHAR(46) NOT NULL UNIQUE,
        password VARCHAR(46) NOT NULL
        )"""

    sql2 = f"""CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(46) NOT NULL,
        email VARCHAR(46) NOT NULL UNIQUE,
        gender VARCHAR(10),
        account_number VARCHAR(12) NOT NULL UNIQUE,
        account_type VARCHAR(3) NOT NULL,
        password VARCHAR(46) NOT NULL
        );"""

    sql_conta = f"""CREATE TABLE IF NOT EXISTS account(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        saldo REAL,
        account_id INTEGER,
        FOREIGN KEY(account_id) REFERENCES clients(account_number)
        );"""

    q = QSqlQuery()
    q.exec_(sql_conta)
    print(sql_conta)


def insert_into(table_name, **kwargs):
    sql_fields = ''
    sql_values = ''

    for key in kwargs:
        sql_fields += f"""{key} ,"""

    for key in kwargs:
        sql_values += f"""'{kwargs[key]}' ,"""

    fields = sql_fields[:-2]
    values = sql_values[:-2]
    print(fields)
    print(values)
    try:

        sql = f"""INSERT INTO {table_name} ({fields}) VALUES ({values});"""
    except QSqlError:
        print(QSqlError)
        return

    q = QSqlQuery()
    q.exec_(sql)
    print(sql)


def list_all_tables():
    sql = """SELECT * FROM users;"""
    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    name, password, email = range(3)
    result = []

    while q.next():
        print(q.value(name), q.value(password), q.value(email))
        result.append([q.value(name), q.value(password), q.value(email)])
    return result


def drop_table(table_name):
    sql = f"""DROP TABLE IF EXISTS {table_name};"""
    query = QSqlQuery()
    query.exec_(sql)
    print(sql)


def update_table(table_name, **kwargs):
    sql = f"""UPDATE {table_name} SET 'name' = 'lorena' 
    WHERE 'email' = {kwargs["email"]};"""
    query = QSqlQuery()
    query.exec_(sql)
    print(sql)


def select_by(table_name, **kwargs):
    sql = f"""SELECT name, email FROM {table_name} WHERE {kwargs["field"]} = '{kwargs["value"]}';"""
    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    name, email = range(2)
    results = []

    while q.next():
        results.append([q.value(name), q.value(email)])

    return results


def select_all(table_name):
    sql = f"""SELECT name, email, gender, account_number, account_type FROM {table_name};"""
    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    results = []

    while q.next():
        results.append([q.value(0), q.value(1), q.value(2), q.value(3), q.value(4)])
    return results


def register_user(**kwargs):
    try:
        sql = f"""INSERT INTO users (name, email, password) 
        VALUES('{kwargs["name"]}', '{kwargs["email"]}', '{kwargs["password"]}')"""

        q = QSqlQuery()
        q.exec_(sql)
        print(sql)
    except QSqlError:
        print(QSqlError)
        return


def register_client(**kwargs):
    try:
        sql = f"""INSERT INTO clients (name ,email ,gender, account_number, account_type, password) 
        VALUES('{kwargs["name"]}', '{kwargs["email"]}', '{kwargs["gender"]}', 
        '{kwargs["account_number"]}', '{kwargs["account_type"]}', '{kwargs["password"]}')"""

        q = QSqlQuery()
        q.exec_(sql)
        print(sql)
    except QSqlError:
        print(QSqlError)
        return


'''client login'''


def client_login(table_name, **kwargs):
    sql = f"""SELECT name, email, account_number, account_type FROM {table_name} 
    WHERE {kwargs["field"]} = '{kwargs["value"]}';"""
    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    name, email, account_number, account_type = range(4)
    results = []

    while q.next():
        results.append([q.value(name), q.value(email), q.value(account_number), q.value(account_type)])

    return results


def account_client(table_name='clients', **kwargs):
    sql = f"""SELECT saldo, account_id FROM {table_name} WHERE account_id = '{kwargs["account_id"]}'"""
    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    saldo, account_id = range(2)

    results = []

    while q.next():
        results.append([q.value(saldo), q.value(account_id)])

    return results


''''
2007-01-01 10:00:00'
YYYY-MM-DD HH:MM:SS
TABLES - - - - - - -

CREATE TABLE funcionario (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nome TEXT NOT NULL,
email TEXT UNIQUE,
senha TEXT NOT NULL,
cargo TEXT,
data_nascimento TEXT,
data_registro TEXT
);

CREATE TABLE cliente (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nome TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
senha TEXT NOT NULL,
genero TEXT,
numero_conta INTEGER,
data_nascimento TEXT,
data_registro TEXT
);

CREATE TABLE conta (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
numero_conta INTEGER UNIQUE,
agencia TEXT,
tipo_conta TEXT,
saldo REAL,
data_registro TEXT,
FOREIGN KEY(numero_conta) REFERENCES cliente(numero_conta)
);


CREATE TABLE historico (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
numero_conta INTEGER,
conta_recebe INTEGER,
saldo_anterior TEXT,
saldo_atual TEXT,
valor REAL,
operacao TEXT,
data TEXT,
FOREIGN KEY(numero_conta) REFERENCES cliente(numero_conta)
);


https://realpython.com/python-pyqt-database/#running-sql-queries-with-pyqt

CREATE TABLE cliente (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nome TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
senha TEXT NOT NULL,
genero TEXT,
numero_conta INTEGER UNIQUE,
data_nascimento TEXT,
data_registro TEXT
);

CREATE TABLE conta (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
numero_conta INTEGER UNIQUE,
agencia TEXT,
tipo_conta TEXT,
saldo REAL DEFAULT 0,
data_registro TEXT,
FOREIGN KEY(numero_conta) REFERENCES cliente(numero_conta)
);

CREATE TABLE historico (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
numero_conta INTEGER,
valor REAL,
saldo_anterior TEXT,
saldo_atual TEXT,
operacao TEXT,
conta_destino INTEGER,
data TEXT,
FOREIGN KEY(numero_conta) REFERENCES cliente(numero_conta)
);

CREATE TABLE funcionario (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nome TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
senha TEXT NOT NULL,
cargo TEXT,
salario REAL,
data_nascimento	TEXT,
data_registro	TEXT
);
'''
""" - - - - - - - - - - - - - - registro - - - - - - - - - - - - - - """


def registrar_funcionario(dados):
    data_formatada = datetime.strptime(dados["data_nascimento"], "%d/%m/%Y")
    data_atual = datetime.now()

    try:
        sql = f"""INSERT INTO funcionario (nome, email, senha, cargo, salario, data_nascimento, data_registro) 
        VALUES('{dados["nome"]}', '{dados["email"]}', '{dados["senha"]}', '{dados["cargo"]}', {dados["salario"]}, 
        '{data_formatada}', '{data_atual}')"""

        q = QSqlQuery()
        q.exec_(sql)
        print(sql)

        if q.result().lastError().text():
            mensagem = q.result().lastError().text()
            print(mensagem)
            return False, mensagem
        else:
            return True, ''

    except QSqlError as qc:
        print(qc.result().lastError().text())


def registrar_cliente(**kwargs):
    data_formatada = datetime.strptime(kwargs["data_nascimento"], "%d/%m/%Y")

    try:
        sql_cliente = f"""INSERT INTO cliente 
        (nome, email, senha, genero, numero_conta, data_nascimento, data_registro) 
        VALUES
        ('{kwargs["nome"]}', '{kwargs["email"]}', '{kwargs["senha"]}', '{kwargs["genero"]}', 
        {kwargs["numero_da_conta"]}, '{data_formatada}', '{datetime.now()}')"""

        q = QSqlQuery()
        q.exec_(sql_cliente)
        print(sql_cliente)

        mensagem = q.result().lastError().text()
        if mensagem:
            print(q.result().lastError().text())
            return False, mensagem
        else:
            sql_conta = f"""INSERT INTO conta
            (numero_conta, agencia, tipo_conta, saldo, data_registro)
            VALUES 
            ({kwargs["numero_da_conta"]}, '{kwargs["agencia"]}', '{kwargs["tipo_da_conta"]}',
            {kwargs["saldo"]}, '{datetime.now()}');"""

            qc = QSqlQuery()
            qc.exec_(sql_conta)
            print(sql_conta)

            mensagem = qc.result().lastError().text()
            if not mensagem:
                return True, mensagem
            else:
                print(qc.result().lastError().text())
                print(2)
                return False, ''

    except QSqlError as qc:
        print(qc.result().lastError().text())
        print('erro ao registrar o cliente')


""" - - - - - - - - - - - - - - login - - - - - - - - - - - - - - """


def login_funcionario(**kwargs):
    sql = f"""SELECT nome, email, cargo FROM funcionario WHERE email = '{kwargs["email"]}'"""

    try:
        q = QSqlQuery()
        q.exec_(sql)
        print(sql)

        if q.first():
            nome = q.value(0)
            email = q.value(1)
            cargo = q.value(3)
            return [nome, email, cargo]
        else:
            return []
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print("BD: erro ao logar com o funcionario")


def login_cliente(**kwargs):
    print('- ' * 50)
    cliente = []
    conta = []
    try:
        cliente = get_cliente(**kwargs)
        try:
            conta = get_conta(cliente)
        except QSqlError as qc:
            print(qc.result().lastError().text())
            print(err_conta_nao_encontrada)
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_cliente_nao_encontrado)
    return cliente + conta


""" - - - - - - - - - - - - - - get - - - - - - - - - - - - - - """


def get_cliente(**kwargs):
    print('- ' * 50)
    sql = f"""SELECT nome, email, numero_conta FROM cliente WHERE email = '{kwargs["email"]}';"""

    try:
        q_ = QSqlQuery()
        q_.exec_(sql)
        print(sql)

        if q_.first():
            nome = q_.value(0)
            email = q_.value(1)
            numero_da_conta = q_.value(2)
            return [nome, email, numero_da_conta]
        else:
            return []
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_cliente_nao_encontrado)


def get_conta(cliente):
    print('- ' * 50)
    sql = f"""SELECT agencia, tipo_conta, saldo FROM conta WHERE numero_conta = {int(cliente[2])};"""

    try:
        q2 = QSqlQuery()
        q2.exec_(sql)
        print(sql)

        if q2.first():
            agencia = q2.value(0)
            tipo_da_conta = q2.value(1)
            saldo = q2.value(2)
            return [agencia, tipo_da_conta, saldo]
        else:
            return []
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_conta_nao_encontrada)


def get_saldo(numero_da_conta):
    print('- ' * 50)
    sql = f"""SELECT saldo FROM conta WHERE numero_conta = {numero_da_conta};"""

    try:
        q_ = QSqlQuery()
        q_.exec_(sql)
        print(sql)

        if q_.first():
            saldo = q_.value(0)
            return float(saldo)
        else:
            return False
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_buscar_saldo)


""" - - - - - - - - - - - - - - logs - - - - - - - - - - - - - - """


def log_depositar(dados):
    numero_conta = dados['numero_conta_d']
    valor = dados['valor']
    data = str(datetime.now())

    saldo_atual = get_saldo(numero_conta)
    saldo = saldo_atual - valor

    sql = f"""INSERT INTO historico (numero_conta, valor, saldo_anterior, saldo_atual, operacao, data)
    VALUES ({numero_conta}, {valor}, {saldo}, {saldo_atual} , 'depositar', '{data}')"""

    q = QSqlQuery()
    q.exec_(sql)
    print(sql)
    return saldo_atual


def log_sacar(dados):
    numero_conta = dados['numero_conta_s']
    valor = dados['valor']
    data = str(datetime.now())

    saldo_atual = get_saldo(numero_conta)
    saldo = saldo_atual + valor

    sql = f"""INSERT INTO historico (numero_conta, valor, saldo_anterior, saldo_atual, operacao, data)
            VALUES ({numero_conta}, {valor}, {saldo}, {saldo_atual} , 'sacar', '{data}')"""

    q = QSqlQuery()
    q.exec_(sql)
    print(sql)
    return saldo_atual


def log_transferir(dados):
    numero_conta = dados['numero_conta_s']
    conta_destino = dados['numero_conta_d']
    valor = dados['valor']
    data = str(datetime.now())

    saldo_atual = get_saldo(numero_conta)
    saldo = saldo_atual + valor

    sql_t = f"""INSERT INTO historico (numero_conta, valor, saldo_anterior, saldo_atual, 
    operacao, conta_destino, data)
    VALUES ({numero_conta},{valor}, {saldo}, {saldo_atual}, 
    'transferir' ,{conta_destino} , '{data}')"""

    try:
        q = QSqlQuery()
        q.exec_(sql_t)
        print(sql_t)

    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_deposito)


""" - - - - - - - - - - - - - - métodos - - - - - - - - - - - - - - """


def sacar(dados):
    print(dados)
    print('- ' * 50)

    saldo = get_saldo(dados['numero_conta_s'])
    saldo_atual = saldo - dados['valor']

    sql_s = f"""UPDATE conta SET saldo = {saldo_atual} 
    WHERE numero_conta = {dados['numero_conta_s']}"""

    try:
        q = QSqlQuery()
        q.exec_(sql_s)
        print(sql_s)
        return saldo_atual

    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_sacar)


def depositar(dados):
    print(dados)
    print('- ' * 50)

    saldo = get_saldo(dados['numero_conta_d'])
    saldo_atual = saldo + dados['valor']

    sql_d = f"""UPDATE conta SET saldo = {saldo_atual} 
    WHERE numero_conta = {dados['numero_conta_d']}"""

    try:
        q = QSqlQuery()
        q.exec_(sql_d)
        print(sql_d)
        print(saldo_atual)
        return saldo_atual

    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_deposito)


def transferir(dados):
    print('- ' * 50)
    try:
        sacar(dados)
        try:
            print(1)
            depositar(dados)

            saldo_atual = get_saldo(dados['numero_conta_s'])
            return saldo_atual

        except QSqlError as qc:
            print('erro 1')
            print(qc.result().lastError().text())
            print(err_depositar_transferencia)
    except QSqlError as qc:
        print('erro 2')
        print(qc.result().lastError().text())
        print(err_sacar_transferencia)


""" - - - - - - - - - - - - - - informações - - - - - - - - - - - - - - """
connection()
def extrato(numero_conta):
    print('- ' * 50)
    sql_e = f"""SELECT valor, saldo_anterior, saldo_atual, operacao, data FROM historico
        WHERE numero_conta = {numero_conta}"""

    sql_t = f"""SELECT saldo_atual, data FROM historico WHERE numero_conta = {numero_conta}"""

    dados = {
        'valor': 0,
        'saldo_anterior': 0,
        'saldo_atual': 0,
        'operacao': '',
        'data': '',
    }

    lista = []

    try:
        q = QSqlQuery()
        q.exec_(sql_e)
        print(sql_e)

        q_2 = QSqlQuery()
        q_2.exec_(sql_t)

        if q.first():
            dados['valor'] = q.value(0)
            dados['saldo_anterior'] = q.value(1)
            dados['saldo_atual'] = q.value(2)
            dados['operacao'] = q.value(3)
            dados['data'] = q.value(4)
        else:
            print('Nada encontrado')

        while q_2.next():
            lista.append([q_2.value(0), q_2.value(1)])

    except QSqlError as qc:
            print(qc.result().lastError().text())

    return dados, lista


""" - - - - - - - - - - - - - - dados gerais - - - - - - - - - - - - - - """


def get_total_clientes():
    sql = f"""SELECT nome, email, genero, data_registro FROM cliente;"""

    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    q_last = QSqlQuery()
    q_last.exec_(sql)

    clientes = {
        'total': 0,
        'masculino': 0,
        'feminino': 0,
        'ultimo': ''
    }

    if q_last.last():
        clientes['ultimo'] = str(q_last.value(3))

    while q.next():
        clientes['total'] += 1
        if q.value(2) == 'masculino':
            clientes['masculino'] += 1
        else:
            clientes['feminino'] += 1

    return clientes


def get_total_contas():
    sql = """SELECT tipo_conta FROM conta;"""
    sum = """SELECT sum(saldo) FROM conta;"""

    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    qsum = QSqlQuery()
    qsum.exec_(sum)

    contas = {
        'tipo': {
            'corrente': 0,
            'salario': 0,
            'poupanca': 0,
            'simples': 0
        },
        'saldo_total': 0
    }

    if q.first():
        while q.next():
            if q.value(0) == 'Salário':
                contas['tipo']['salario'] += 1
            elif q.value(0) == 'Poupança':
                contas['tipo']['poupanca'] += 1
            elif q.value(0) == 'Corrente':
                contas['tipo']['corrente'] += 1
            elif q.value(0) == 'Simples':
                contas['tipo']['simples'] += 1
            else:
                pass

    if qsum.first():
        contas['saldo_total'] = qsum.value(0)

    return contas


def get_total_funcionarios():
    sql = """SELECT nome, email, cargo, salario, data_nascimento, data_registro FROM funcionario;"""
    sql_menor_salario = """SELECT min(salario) FROM funcionario"""
    sql_maior_salario = """SELECT max(salario) FROM funcionario"""
    sql_mais_velho = """SELECT min(data_nascimento) FROM funcionario;"""

    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    q_min = QSqlQuery()
    q_min.exec_(sql_menor_salario)

    q_max = QSqlQuery()
    q_max.exec_(sql_maior_salario)

    q_velho = QSqlQuery()
    q_velho.exec_(sql_mais_velho)

    funcionarios = {
        'ultimo_nome': '',
        'ultimo_data': '',
        'ultimo_email': '',
        'salario': 0,
        'mais_velho': '',
        'mais_novo': '',
        'maior_salario': 0,
        'menor_salario': 0
    }

    if q_min.first():
        funcionarios['menor_salario'] = str(q.value(0))

    if q_max.first():
        funcionarios['maior_salario'] = str(q.value(0))

    if q_velho.first():
        funcionarios['mais_velho'] = str(q.value(0))

    if q.last():
        funcionarios['ultimo_nome'] = str(q.value(0))
        funcionarios['ultimo_email'] = str(q.value(1))
        funcionarios['ultimo_data'] = str(q.value(5))

    return funcionarios

