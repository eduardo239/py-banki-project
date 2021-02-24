import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel


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
        return 'Conectado com o banco de dados.'
