from PyQt5 import QtCore,  QtWidgets
from db import *

con, message = connection()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(199, 231)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_create_table = QtWidgets.QPushButton(self.groupBox)
        self.btn_create_table.setObjectName("btn_create_table")
        self.verticalLayout.addWidget(self.btn_create_table)
        self.btn_list_users = QtWidgets.QPushButton(self.groupBox)
        self.btn_list_users.setObjectName("btn_list_users")
        self.verticalLayout.addWidget(self.btn_list_users)
        self.btn_drop = QtWidgets.QPushButton(self.groupBox)
        self.btn_drop.setObjectName("btn_drop")
        self.verticalLayout.addWidget(self.btn_drop)
        self.btn_insert = QtWidgets.QPushButton(self.groupBox)
        self.btn_insert.setObjectName("btn_insert")
        self.verticalLayout.addWidget(self.btn_insert)
        self.btn_update = QtWidgets.QPushButton(self.groupBox)
        self.btn_update.setObjectName("btn_update")
        self.verticalLayout.addWidget(self.btn_update)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 199, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ###
        self.btn_create_table.clicked.connect(lambda: create_table('users'))
        self.btn_list_users.clicked.connect(lambda: list_all_tables())
        self.btn_insert.clicked.connect(lambda: insert_into('users',
                                                            name='name',
                                                            password=123,
                                                            email='email@test.com'))
        self.btn_drop.clicked.connect(lambda: drop_table('users'))
        self.btn_update.clicked.connect(lambda: update_table('users'))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "teste"))
        self.btn_create_table.setText(_translate("MainWindow", "create_table"))
        self.btn_list_users.setText(_translate("MainWindow", "list_users"))
        self.btn_drop.setText(_translate("MainWindow", "drop_table"))
        self.btn_insert.setText(_translate("MainWindow", "insert_into"))
        self.btn_update.setText(_translate("MainWindow", "update_users"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
