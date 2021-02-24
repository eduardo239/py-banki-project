from PyQt5 import QtCore, QtGui, QtWidgets
from db import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 490)
        MainWindow.setFixedSize(300, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("color: \'#333A44\';")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.inp_email = QtWidgets.QLineEdit(self.groupBox)
        self.inp_email.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_email.setObjectName("inp_email")
        self.gridLayout.addWidget(self.inp_email, 2, 0, 1, 1)
        self.inp_senha = QtWidgets.QLineEdit(self.groupBox)
        self.inp_senha.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inp_senha.setObjectName("inp_senha")
        self.gridLayout.addWidget(self.inp_senha, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("font: 10pt \"Calibri\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.btn_registrar = QtWidgets.QPushButton(self.groupBox)
        self.btn_registrar.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 8px;\n"
"background-color: \'#00C569\'; \n"
"color: white;\n"
"border: none;\n"
"margin: 4px 0;")
        self.btn_registrar.setObjectName("btn_registrar")
        self.gridLayout.addWidget(self.btn_registrar, 9, 0, 1, 1)
        self.inp_senha_novamente = QtWidgets.QLineEdit(self.groupBox)
        self.inp_senha_novamente.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_senha_novamente.setObjectName("inp_senha_novamente")
        self.gridLayout.addWidget(self.inp_senha_novamente, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.inp_nome_completo = QtWidgets.QLineEdit(self.groupBox)
        self.inp_nome_completo.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_nome_completo.setObjectName("inp_nome_completo")
        self.gridLayout.addWidget(self.inp_nome_completo, 8, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 11, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("padding: 10px;\n"
"color: \'#00C569\';\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lbl_messages = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_messages.setFont(font)
        self.lbl_messages.setObjectName("lbl_messages")
        self.gridLayout.addWidget(self.lbl_messages, 10, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Login = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Login.setIcon(icon)
        self.action_Login.setObjectName("action_Login")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setWhatsThis("")
        self.action_Exit.setObjectName("action_Exit")
        self.menuFile.addAction(self.action_Login)
        self.menuFile.addAction(self.action_Exit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inp_email, self.inp_senha)
        MainWindow.setTabOrder(self.inp_senha, self.inp_senha_novamente)
        MainWindow.setTabOrder(self.inp_senha_novamente, self.inp_nome_completo)
        MainWindow.setTabOrder(self.inp_nome_completo, self.btn_registrar)

        ###
        self.btn_registrar.clicked.connect(self.register)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Registrar"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Senha Novamente"))
        self.btn_registrar.setText(_translate("MainWindow", "Registrar"))
        self.label_4.setText(_translate("MainWindow", "Nome Completo"))
        self.label_5.setText(_translate("MainWindow", "Registro"))
        self.lbl_messages.setText(_translate("MainWindow", ""))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.action_Login.setText(_translate("MainWindow", "&Login"))
        self.action_Login.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setStatusTip(_translate("MainWindow", "Sair do programa"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))

    def register(self):
        email = self.inp_email.text().strip()
        password = self.inp_senha.text().strip()
        name = self.inp_nome_completo.text().strip()
        insert_into('users',
                    email=email,
                    password=password,
                    name=name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
