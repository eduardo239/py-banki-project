import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox


def connection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("storage/contacts.sqlite")

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
    sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
        )"""

    query = QSqlQuery()
    query.exec_(sql)
    print(sql)


def insert_into(table_name, **kwargs):
    name = "linda"
    job = "web"
    email = "linda@at.com"

    sql = f"""INSERT INTO {table_name} 
        (name, job, email) 
        VALUES 
        ('{name}', '{job}', '{email}')"""

    query = QSqlQuery()
    query.exec_(sql)
    print(sql)


def list_all_tables():
    sql = """SELECT name, job, email FROM users"""
    querySelect = QSqlQuery()
    querySelect.exec_(sql)
    print(sql)

    name, job, email = range(3)

    while querySelect.next():
        print(querySelect.value(name), querySelect.value(email))


def drop_table(table_name):
    sql = f"""DROP TABLE IF EXISTS {table_name}"""
    query = QSqlQuery()
    query.exec_(sql)
    print(sql)


def update_table(table_name, **kwargs):
    sql = f"""UPDATE {table_name} SET 'name' = 'lorena' 
    WHERE id = 1 """
    query = QSqlQuery()
    query.exec_(sql)
    print(sql)


def select_by_id(table_name, **kwargs):
    sql = f"""SELECT * FROM '{table_name}' 
    WHERE '{kwargs["field"]}' = '{kwargs["value"]}'"""
    q = QSqlQuery()
    q.exec_(sql)
    print(sql)
