import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from PyQt5.QtWidgets import QMessageBox

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
    sql = f"""SELECT name, email, account_number, account_type FROM {table_name} WHERE {kwargs["field"]} = '{kwargs["value"]}';"""
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


'''
