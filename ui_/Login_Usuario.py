from PyQt5 import QtCore, QtGui, QtWidgets

from db import *
from ui_ import Minha_Conta, Registro_Cliente
from typo import *
from style import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 365)
        MainWindow.setStyleSheet(window)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_title = QtWidgets.QLabel(self.groupBox)
        self.lbl_title.setStyleSheet(lbl_title_green)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayout.addWidget(self.lbl_title)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setStyleSheet(lbl_small_grey)
        self.verticalLayout_2.addWidget(self.label_7)
        self.inp_email_conta = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_email_conta.setStyleSheet(inp_default)
        self.inp_email_conta.setPlaceholderText("")
        self.inp_email_conta.setObjectName("inp_email_conta")
        self.verticalLayout_2.addWidget(self.inp_email_conta)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet(lbl_small_grey)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.inp_senha = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_senha.setStyleSheet(inp_default)
        self.inp_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inp_senha.setPlaceholderText("")
        self.inp_senha.setObjectName("inp_senha")
        self.verticalLayout_2.addWidget(self.inp_senha)
        self.btn_login = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(btn_green)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout_2.addWidget(self.btn_login)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.lbl_mensagem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mensagem.setStyleSheet(lbl_mensagem_default)
        self.lbl_mensagem.setText("")
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.verticalLayout.addWidget(self.lbl_mensagem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 322, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        self.menuA_juda = QtWidgets.QMenu(self.menubar)
        self.menuA_juda.setObjectName("menuA_juda")
        MainWindow.setMenuBar(self.menubar)

        self.action_Registro_Funcionario = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/15808962761582004492-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Registro_Funcionario.setIcon(icon)
        self.action_Registro_Funcionario.setObjectName("action_Registro_Funcionario")

        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./assets/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setObjectName("action_Exit")

        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionContato = QtWidgets.QAction(MainWindow)
        self.actionContato.setObjectName("actionContato")
        self.action_Visualizar = QtWidgets.QAction(MainWindow)
        self.action_Visualizar.setObjectName("action_Visualizar")
        self.action_Informa_es = QtWidgets.QAction(MainWindow)
        self.action_Informa_es.setObjectName("action_Informa_es")
        self.action_Registrar = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./assets/15586770221582004499-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Registrar.setIcon(icon2)
        self.action_Registrar.setObjectName("action_Registrar")
        self.menu_Arquivo.addAction(self.action_Registrar)
        self.menu_Arquivo.addAction(self.action_Exit)
        self.menuA_juda.addAction(self.actionSobre)
        self.menuA_juda.addAction(self.actionContato)
        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.menubar.addAction(self.menuA_juda.menuAction())
        self.label_7.setBuddy(self.inp_email_conta)

        '''atr'''
        self.dados_usuario = ''
        self.btn_login.clicked.connect(self.login)
        self.action_Registrar.triggered.connect(self.registrar)
        self.action_Exit.triggered.connect(lambda: MainWindow.close())
        self.inp_email_conta.returnPressed.connect(self.login)
        self.inp_senha.returnPressed.connect(self.login)
        self.btn_login.setAutoDefault(True)
        self.inp_email_conta.setText("nome@")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App - Init Window"))
        self.lbl_title.setText(_translate("MainWindow", "Login do Usuário"))
        self.label_7.setText(_translate("MainWindow", "Email/Número da Conta"))
        self.label_4.setText(_translate("MainWindow", "Senha"))
        self.btn_login.setText(_translate("MainWindow", "Fazer Login"))
        self.menu_Arquivo.setTitle(_translate("MainWindow", "&Arquivo"))
        self.menuA_juda.setTitle(_translate("MainWindow", "A&juda"))
        self.action_Registro_Funcionario.setText(_translate("MainWindow", "&Registro de Funcionários"))
        self.action_Registro_Funcionario.setStatusTip(_translate("MainWindow", "Voltar para tela de Login"))
        self.action_Registro_Funcionario.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setStatusTip(_translate("MainWindow", "Fechar o aplicativo"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionContato.setText(_translate("MainWindow", "Contato"))
        self.action_Visualizar.setText(_translate("MainWindow", "&Visualizar"))
        self.action_Visualizar.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_Informa_es.setText(_translate("MainWindow", "&Informações"))
        self.action_Registrar.setText(_translate("MainWindow", "&Registrar"))
        self.action_Registrar.setShortcut(_translate("MainWindow", "Ctrl+R"))

    '''def'''

    def minha_conta(self):
        self.lbl_mensagem.setText('')
        self.lbl_mensagem.setStyleSheet(lbl_mensagem_default)
        self.window = QtWidgets.QMainWindow()
        self.ui = Minha_Conta.Ui_MainWindow(self.dados_usuario)
        self.ui.setupUi(self.window)
        self.window.show()

    def login(self):
        email = self.inp_email_conta.text()
        senha = self.inp_senha.text()

        if email != '':
            self.lbl_mensagem.setText("")
            self.lbl_mensagem.setStyleSheet(lbl_mensagem_default)

            try:
                resultado = login_cliente(email=email, senha=senha)
                self.dados_usuario = resultado
                self.minha_conta()
                self.lbl_mensagem.setText(suc_login)
                self.lbl_mensagem.setStyleSheet(lbl_mensagem_success)
            except Exception as e:
                print(e)
                self.lbl_mensagem.setText(err_usuario_nao_encontrado)
                self.lbl_mensagem.setStyleSheet(lbl_mensagem_error)
        else:
            self.lbl_mensagem.setText(err_campos_vazios)
            self.lbl_mensagem.setStyleSheet(lbl_mensagem_error)

    def registrar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Registro_Cliente.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
