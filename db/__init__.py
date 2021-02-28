import sys
from datetime import datetime

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from PyQt5.QtWidgets import QMessageBox

from typo import *

db_name = 'contacts.sqlite'


def connection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("storage/" + db_name)

    # try to open the connection and handles the possible errors
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

    sql2 = f"""CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(46) NOT NULL,
        email VARCHAR(46) NOT NULL,
        gender VARCHAR(15),
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
email TEXT,
senha TEXT NOT NULL,
cargo TEXT,
data_nascimento datetime,
data_de_registro datetime CURRENT_TIMESTAMP
);


CREATE TABLE cliente (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nome TEXT NOT NULL,
email TEXT,
senha TEXT NOT NULL,
genero TEXT,
numero_da_conta INTEGER,
data_nascimento datetime,
data_de_registro datetime CURRENT_TIMESTAMP
);


CREATE TABLE conta (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
numero_da_conta INTEGER,
agencia TEXT,
tipo_da_conta TEXT,
saldo REAL,
data_de_registro datetime CURRENT_TIMESTAMP,
FOREIGN KEY(numero_da_conta) REFERENCES cliente(numero_da_conta)
);


https://realpython.com/python-pyqt-database/#running-sql-queries-with-pyqt
'''


def registrar_funcionario(**kwargs):
    data_formatada = datetime.strptime(kwargs["data_nascimento"], "%d/%m/%Y")

    try:
        sql = f"""INSERT INTO funcionario (nome, email, senha, cargo, data_nascimento, data_de_registro) 
        VALUES(
        '{kwargs["nome"]}', '{kwargs["email"]}', '{kwargs["senha"]}', '{kwargs["cargo"]}', 
        '{data_formatada}', '{datetime.now()}'
        )"""

        q = QSqlQuery()
        q.exec_(sql)
        print(sql)

    except QSqlError:
        print(QSqlError)
        return


def registrar_cliente(**kwargs):
    data_formatada = datetime.strptime(kwargs["data_nascimento"], "%d/%m/%Y")

    try:
        sql_cliente = f"""INSERT INTO cliente 
        (nome, email, senha, genero, numero_da_conta, data_nascimento, data_de_registro) 
        VALUES
        ('{kwargs["nome"]}', '{kwargs["email"]}', '{kwargs["senha"]}', '{kwargs["genero"]}', 
        {kwargs["numero_da_conta"]}, '{data_formatada}', '{datetime.now()}')"""

        q = QSqlQuery()
        q.exec_(sql_cliente)
        print(sql_cliente)

        try:
            sql_conta = f"""INSERT INTO conta
            (numero_da_conta, agencia, tipo_da_conta, saldo, data_de_registro)
            VALUES 
            ({kwargs["numero_da_conta"]}, '{kwargs["agencia"]}', '{kwargs["tipo_da_conta"]}',
            {kwargs["saldo"]}, '{datetime.now()}');"""

            qc = QSqlQuery()
            qc.exec_(sql_conta)
            print(sql_conta)

            print(qc.result().lastError().text())

        except:
            print(qc.result().lastError().text())
            print('erro ao cadastrar conta')
    except QSqlError:
        print(qc.result().lastError().text())
        print('erro ao registrar o cliente')

        return


def login_funcionario(table_name='funcionario', **kwargs):
    sql = f"""SELECT nome, email, cargo FROM {table_name} WHERE email = '{kwargs["email"]}'"""

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
    except:
        print("BD: erro ao logar com o funcionario")


""" - - - - - - - - - - - - - - login cliente - - - - - - - - - - - - - - """


def login_cliente(**kwargs):
    print('- ' * 50)
    cliente = []
    conta = []
    try:
        cliente = get_cliente(**kwargs)
        try:
            conta = get_conta(cliente)
        except:
            print(err_conta_nao_encontrada)
    except:
        print(err_cliente_nao_encontrado)
    return cliente + conta


def get_cliente(**kwargs):
    print('- ' * 50)
    sql = f"""SELECT nome, email, numero_da_conta FROM cliente WHERE email = '{kwargs["email"]}';"""

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
    except:
        print(err_cliente_nao_encontrado)


def get_conta(cliente):
    print('- ' * 50)
    sql = f"""SELECT agencia, tipo_da_conta, saldo FROM conta WHERE numero_da_conta = {int(cliente[2])};"""

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
    except:
        print(err_conta_nao_encontrada)


def depositar(numero_da_conta, valor_atual):
    print('- ' * 50)
    sql_depositar = f"""UPDATE conta SET saldo = {float(valor_atual)} WHERE numero_da_conta = {int(numero_da_conta)}"""

    try:
        q = QSqlQuery()
        q.exec_(sql_depositar)
        print(sql_depositar)
    except:
        print(err_deposito)


def sacar(numero_da_conta, valor_atual):
    print('- ' * 50)
    sql_saque = f"""UPDATE conta SET saldo = {float(valor_atual)} WHERE numero_da_conta = {int(numero_da_conta)}"""

    try:
        q = QSqlQuery()
        q.exec_(sql_saque)
        print(sql_saque)
    except:
        print(err_sacar)


def transferir(numero_conta_envia, numero_conta_recebe, valor_envia=0,  valor_recebe=0):
    print('- ' * 50)
    try:
        sacar(numero_conta_envia, valor_envia)
        try:
            depositar(numero_conta_recebe, valor_recebe)
        except:
            print(err_depositar_transferencia)
    except:
        print(err_sacar_transferencia)


def get_saldo(numero_da_conta):
    print('- ' * 50)
    sql = f"""SELECT saldo FROM conta WHERE numero_da_conta = {numero_da_conta};"""

    try:
        q_ = QSqlQuery()
        q_.exec_(sql)
        print(sql)

        if q_.first():
            saldo = q_.value(0)
            return saldo
    except:
        print(err_buscar_saldo)
