import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel


con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

# create the application
app = QApplication(sys.argv)

# try to open the connection and handles the possible errors
if not con.open():
    QMessageBox.critical(
        None,
        "App Name - Error!",
        "Database Error: %s" % con.lastError().databaseText(),
    )
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    """
)

print(con.tables())

# dynamic
name = "linda2"
job = "web2"
email = "linda2@at.com"

query = QSqlQuery()
query.exec_(
    f"""INSERT INTO contacts (name, job, email) 
    VALUES ('{name}', '{job}', '{email}')"""
)

# using prepare
insertQuery = QSqlQuery()
insertQuery.prepare(
    """INSERT INTO contacts (
    name,
    job,
    email
    ) 
    VALUES 
    (?, ?, ?)
    """
)

data = [
    ("Joe", "Senior Web Developer", "joe@example.com"),
    ("Lara", "Project Manager", "lara@example.com"),
    ("David", "Data Analyst", "david@example.com"),
    ("Jane", "Senior Python Developer", "jane@example.com"),
]

# Use .addBindValue() to insert data
for name, job, email in data:
    insertQuery.addBindValue(name)
    insertQuery.addBindValue(job)
    insertQuery.addBindValue(email)

print(insertQuery)
querySelect = QSqlQuery()
querySelect.exec_(
    """SELECT name, job, email FROM contacts"""
)

name, job, email = range(3)

print(querySelect.last())

while querySelect.previous():
    print(querySelect.value(name), querySelect.value(email))

# print(querySelect.value(name))
# print(querySelect.value(email))
# Create the application's window

'''
https://realpython.com/python-pyqt-database/#closing-and-removing-database-connections
'''

if con.isOpen():
    con.close()

# remove database connection

# before remove, everything that use connection is deleted
# or set to use a different data source

print(QSqlDatabase.connectionNames())
QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
print(QSqlDatabase.connectionNames())


win = QLabel("Connection Successfully Opened!")
win.setWindowTitle("App Name")
win.resize(200, 100)
win.show()
sys.exit(app.exec_())

