from PyQt5 import QtCore, QtGui, QtWidgets
from db import *
from ui import Minha_Conta
from ui.styles import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 343)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_nome_usuario = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_usuario.setFont(font)
        self.lbl_nome_usuario.setObjectName("lbl_nome_usuario")
        self.verticalLayout_2.addWidget(self.lbl_nome_usuario)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setStyleSheet(lbl_simple)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.inp_numero_conta = QtWidgets.QLineEdit(self.groupBox_3)
        self.inp_numero_conta.setStyleSheet(inp_reset)
        self.inp_numero_conta.setReadOnly(False)
        self.inp_numero_conta.setObjectName("inp_numero_conta")

        self.inp_numero_conta.setFocus()
        self.inp_numero_conta.returnPressed.connect(self.login)
        self.verticalLayout_2.addWidget(self.inp_numero_conta)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.inp_senha = QtWidgets.QLineEdit(self.groupBox_3)
        self.inp_senha.setStyleSheet(inp_reset)
        self.inp_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inp_senha.setReadOnly(False)
        self.inp_senha.setObjectName("inp_senha")

        self.inp_senha.returnPressed.connect(self.login)
        self.verticalLayout_2.addWidget(self.inp_senha)
        self.btn_entrar = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_entrar.setStyleSheet(button_green)
        self.btn_entrar.setObjectName("btn_entrar")

        self.btn_entrar.setAutoDefault(True)
        self.verticalLayout_2.addWidget(self.btn_entrar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.lbl_mensagem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mensagem.setStyleSheet(lbl_reset)
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.verticalLayout.addWidget(self.lbl_mensagem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_Arquivo.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_Arquivo.menuAction())

        '''edited'''
        self.btn_entrar.clicked.connect(self.login)
        self.action_Exit.triggered.connect(lambda : MainWindow.close())
        self.usuario = {}

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Fazer Login"))
        self.lbl_nome_usuario.setText(_translate("MainWindow", "Login"))
        self.label_6.setText(_translate("MainWindow", "Número da Conta"))
        self.label_7.setText(_translate("MainWindow", "Senha"))
        self.btn_entrar.setText(_translate("MainWindow", "Entrar"))
        self.lbl_mensagem.setText(_translate("MainWindow", "TextLabel"))
        self.menu_Arquivo.setTitle(_translate("MainWindow", "&Arquivo"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))

    '''def'''
    def my_account_window(self):
        self.lbl_mensagem.setText('')
        self.lbl_mensagem.setStyleSheet(lbl_reset)
        self.inp_numero_conta.setStyleSheet(inp_reset)
        self.inp_senha.setStyleSheet(inp_reset)

        self.window = QtWidgets.QMainWindow()
        self.ui = Minha_Conta.Ui_MainWindow(self.usuario)
        self.ui.setupUi(self.window)
        self.window.show()

    def login(self):
        conta = self.inp_numero_conta.text().strip()
        senha = self.inp_senha.text()

        if conta != '':
            try:
                resultado = client_login('clients', field='email', value=conta)
                if resultado:
                    self.usuario = {'usuario': resultado[0]}
                    self.my_account_window()
                else:
                    self.lbl_mensagem.setStyleSheet(lbl_error)
                    self.inp_numero_conta.setStyleSheet(inp_error)
                    self.inp_senha.setStyleSheet(inp_error)
                    self.lbl_mensagem.setText(not_auth)
            except:
                self.lbl_mensagem.setText(error_login)
        else:
            self.lbl_mensagem.setText(empty_field)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
