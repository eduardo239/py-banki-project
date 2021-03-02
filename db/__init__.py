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
conta_recebe INTEGER,
saldo_anterior TEXT,
saldo_atual TEXT,
valor REAL,
operacao TEXT,
data TEXT,
FOREIGN KEY(numero_conta) REFERENCES cliente(numero_conta)
);

CREATE TABLE funcionario (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
nome TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
senha TEXT NOT NULL,
cargo TEXT,
data_nascimento	TEXT,
data_registro	TEXT
);
'''
""" - - - - - - - - - - - - - - registro - - - - - - - - - - - - - - """


def registrar_funcionario(**kwargs):
    data_formatada = datetime.strptime(kwargs["data_nascimento"], "%d/%m/%Y")

    try:
        sql = f"""INSERT INTO funcionario (nome, email, senha, cargo, data_nascimento, data_registro) 
        VALUES(
        '{kwargs["nome"]}', '{kwargs["email"]}', '{kwargs["senha"]}', '{kwargs["cargo"]}', 
        '{data_formatada}', '{datetime.now()}'
        )"""

        try:
            q = QSqlQuery()
            q.exec_(sql)
            print(sql)

            if q.result().lastError().text():
                mensagem = q.result().lastError().text()
                return False, mensagem
            else:
                return True, ''
        except QSqlError as qc:
            print(qc.result().lastError().text())
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
            return saldo
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_buscar_saldo)


""" - - - - - - - - - - - - - - métodos - - - - - - - - - - - - - - """


def logger(tipo, **kwargs):
    def log_depositar():
        numero_conta = int(kwargs['numero_da_conta'])
        valor = float(kwargs['valor'])
        saldo_atual = float(kwargs['saldo_atual'])
        saldo_anterior = float(kwargs['saldo_anterior'])
        data = datetime.now()

        sql = f"""INSERT INTO historico (numero_conta, saldo_anterior, saldo_atual, valor, operacao, data)
        VALUES ({numero_conta}, {saldo_anterior}, {saldo_atual}, {valor} , 'depositar', '{str(data)}' )"""

        q = QSqlQuery()
        q.exec_(sql)
        print(sql)

    def log_sacar():
        numero_conta = int(kwargs['numero_da_conta'])
        valor = float(kwargs['valor'])
        saldo_atual = float(kwargs['saldo_atual'])
        saldo_anterior = float(kwargs['saldo_anterior'])
        data = datetime.now()

        sql = f"""INSERT INTO historico (numero_conta, saldo_anterior, saldo_atual, valor, operacao, data)
                VALUES ({numero_conta}, {saldo_anterior}, {saldo_atual}, {valor} , 'sacar', '{data}' )"""

        q = QSqlQuery()
        q.exec_(sql)
        print(sql)

    def log_transferir():
        conta_envia = kwargs['conta_envia']
        saldo_anterior_envia = kwargs['saldo_antes_envia']
        saldo_atual_envia = kwargs['saldo_atual_envia']
        valor = kwargs['valor']
        conta_recebe = kwargs['conta_recebe']
        data = datetime.now()

        sql = f"""INSERT INTO historico 
        (numero_conta, conta_recebe, saldo_anterior, saldo_atual, valor, operacao, data)
        VALUES ({conta_envia}, {conta_recebe}, {saldo_anterior_envia}, {saldo_atual_envia}, {valor}, 
        'transferir', '{data}' )"""

        q = QSqlQuery()
        q.exec_(sql)
        print(sql)

    if tipo == 'transferir':
        log_transferir()
    elif tipo == 'sacar':
        log_sacar()
    elif tipo == 'depositar':
        log_depositar()
    else:
        print('Opção não encontrada.')


def depositar(conta, saldo_atual, valor, saldo_anterior):
    print('- ' * 50)
    sql_depositar = f"""UPDATE conta SET saldo = {float(saldo_atual)} WHERE numero_conta = {int(conta)}"""

    try:
        q = QSqlQuery()
        q.exec_(sql_depositar)
        print(sql_depositar)
        logger('depositar', numero_da_conta=conta, saldo_anterior=saldo_anterior,
               valor=valor, saldo_atual=saldo_atual)
    except Exception as e:
        print(e)


def sacar(conta, saldo_anterior, valor, saldo_atual):
    print('- ' * 50)
    sql_saque = f"""UPDATE conta SET saldo = {float(saldo_atual)} WHERE numero_conta = {int(conta)}"""

    try:
        q = QSqlQuery()
        q.exec_(sql_saque)
        print(sql_saque)
        logger('sacar', numero_da_conta=conta, saldo_anterior=saldo_anterior,
               valor=valor, saldo_atual=saldo_atual)
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_sacar)


def transferir(conta_envia, saldo_antes_envia, saldo_atual_envia, conta_recebe,
               saldo_antes_recebe, saldo_atual_recebe, valor):
    print('- ' * 50)
    try:
        sacar(conta_envia, saldo_antes_envia, valor, saldo_atual_envia)
        try:
            depositar(conta_recebe, saldo_atual_recebe, valor, saldo_antes_recebe)

            logger('transferir', conta_envia=conta_envia, saldo_antes_envia=saldo_antes_envia,
                   saldo_atual_envia=saldo_atual_envia, valor=valor, conta_recebe=conta_recebe)

        except QSqlError as qc:
            print(qc.result().lastError().text())
            print(err_depositar_transferencia)
    except QSqlError as qc:
        print(qc.result().lastError().text())
        print(err_sacar_transferencia)


def extrato(numero_conta):
    sql = f"""SELECT saldo_anterior, saldo_atual, valor, operacao, data FROM historico_conta
        WHERE numero_conta = {numero_conta}"""
    lista = []

    q = QSqlQuery()
    q.exec_(sql)
    print(sql)

    while q.next():
        saldo_anterior = q.value(0)
        saldo_atual = q.value(1)
        valor = q.value(2)
        operacao = q.value(3)
        data = q.value(4)
        lista.append([saldo_anterior, saldo_atual, valor, operacao, data])

    return lista


'''
return -1
'''
