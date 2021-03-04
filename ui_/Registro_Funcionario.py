from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from ui_ import Login_Funcionario, Login_Usuario
from db import registrar_funcionario
from helpers import box_mensagem_ok, box_mensagem_fail
from style import *
from typo import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 465)
        MainWindow.setStyleSheet(window)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setStyleSheet(lbl_title_green)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout_3.addWidget(self.lbl_title)
        self.groupBox_Full = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Full.setTitle("")
        self.groupBox_Full.setObjectName("groupBox_Full")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_Full)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_Full)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet(lbl_small_grey)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inp_nome = QtWidgets.QLineEdit(self.groupBox)
        self.inp_nome.setStyleSheet(inp_default)
        self.inp_nome.setObjectName("inp_nome")
        self.verticalLayout.addWidget(self.inp_nome)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet(lbl_small_grey)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.inp_email = QtWidgets.QLineEdit(self.groupBox)
        self.inp_email.setStyleSheet(inp_default)
        self.inp_email.setObjectName("inp_email")
        self.verticalLayout.addWidget(self.inp_email)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet(lbl_small_grey)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.inp_senha = QtWidgets.QLineEdit(self.groupBox)
        self.inp_senha.setStyleSheet(inp_default)
        self.inp_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inp_senha.setObjectName("inp_senha")

        self.verticalLayout.addWidget(self.inp_senha)

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet(lbl_small_grey)
        self.label_5.setObjectName("label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.inp_senha_novamente = QtWidgets.QLineEdit(self.groupBox)
        self.inp_senha_novamente.setStyleSheet(inp_default)
        self.inp_senha_novamente.setText("")
        self.inp_senha_novamente.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inp_senha_novamente.setObjectName("inp_senha_novamente")

        self.verticalLayout.addWidget(self.inp_senha_novamente)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_Full)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setStyleSheet(lbl_small_grey)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.inp_salario = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_salario.setStyleSheet(inp_default)
        self.inp_salario.setObjectName("inp_salario")
        self.verticalLayout_2.addWidget(self.inp_salario)

        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setStyleSheet(lbl_small_grey)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.inp_cargo = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_cargo.setStyleSheet(inp_default)
        self.inp_cargo.setObjectName("inp_cargo")
        self.verticalLayout_2.addWidget(self.inp_cargo)

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet(lbl_small_grey)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.inp_data_nascimento = QtWidgets.QDateEdit(self.groupBox_2)
        self.inp_data_nascimento.setStyleSheet(inp_data)
        self.inp_data_nascimento.setObjectName("inp_data_nascimento")
        self.verticalLayout_2.addWidget(self.inp_data_nascimento)
        self.btn_registro = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_registro.setStyleSheet(btn_green)
        self.verticalLayout_2.addWidget(self.btn_registro)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.groupBox_Full)
        self.lbl_mensagem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mensagem.setStyleSheet(lbl_mensagem_default)
        self.lbl_mensagem.setText("")
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.verticalLayout_3.addWidget(self.lbl_mensagem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        self.menuA_juda = QtWidgets.QMenu(self.menubar)
        self.menuA_juda.setObjectName("menuA_juda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Login = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Login.setIcon(icon)
        self.action_Login.setObjectName("action_Login")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./assets/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setObjectName("action_Exit")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionContato = QtWidgets.QAction(MainWindow)
        self.actionContato.setObjectName("actionContato")
        self.menu_Arquivo.addAction(self.action_Login)
        self.menu_Arquivo.addAction(self.action_Exit)
        self.menuA_juda.addAction(self.actionSobre)
        self.menuA_juda.addAction(self.actionContato)
        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.menubar.addAction(self.menuA_juda.menuAction())
        self.label.setBuddy(self.inp_nome)
        self.label_2.setBuddy(self.inp_email)
        self.label_3.setBuddy(self.inp_senha)
        self.label_5.setBuddy(self.inp_senha_novamente)
        self.label_6.setBuddy(self.inp_cargo)
        self.label_7.setBuddy(self.inp_salario)
        self.label_4.setBuddy(self.inp_data_nascimento)

        '''atr'''
        self.action_Exit.triggered.connect(lambda: MainWindow.close())
        self.btn_registro.clicked.connect(self.registrar)
        self.btn_registro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registro.setAutoDefault(True)
        self.action_Login.triggered.connect(self.login)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inp_nome, self.inp_email)
        MainWindow.setTabOrder(self.inp_email, self.inp_senha)
        MainWindow.setTabOrder(self.inp_senha, self.inp_senha_novamente)
        MainWindow.setTabOrder(self.inp_senha_novamente, self.inp_salario)
        MainWindow.setTabOrder(self.inp_salario, self.inp_cargo)
        MainWindow.setTabOrder(self.inp_cargo, self.inp_data_nascimento)
        MainWindow.setTabOrder(self.inp_data_nascimento, self.btn_registro)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "Registro de Funcionário"))
        self.groupBox.setTitle(_translate("MainWindow", "Informações"))
        self.label.setText(_translate("MainWindow", "Nome Completo"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Senha"))
        self.label_5.setText(_translate("MainWindow", "Senha Novamente"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dados do Funcionário"))
        self.label_6.setText(_translate("MainWindow", "Cargo"))
        self.label_7.setText(_translate("MainWindow", "Salário"))
        self.label_4.setText(_translate("MainWindow", "Data de Nascimento"))
        self.btn_registro.setText(_translate("MainWindow", "Registrar"))
        self.menu_Arquivo.setTitle(_translate("MainWindow", "&Arquivo"))
        self.menuA_juda.setTitle(_translate("MainWindow", "A&juda"))
        self.action_Login.setText(_translate("MainWindow", "&Login"))
        self.action_Login.setStatusTip(_translate("MainWindow", "Voltar para tela de Login"))
        self.action_Login.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setStatusTip(_translate("MainWindow", "Fechar o aplicativo"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionContato.setText(_translate("MainWindow", "Contato"))

    '''met'''
    def registrar(self):
        # self.reset_campos()

        nome = self.inp_nome.text().strip()
        email = self.inp_email.text().strip()
        senha = self.inp_senha.text()
        senha_novamente = self.inp_senha_novamente.text()
        cargo = self.inp_cargo.text().strip()
        salario = self.inp_salario.text() or 0
        data_nascimento = self.inp_data_nascimento.text()

        dados = {
            'nome': nome,
            'email': email,
            'senha': senha,
            'cargo': cargo,
            'salario': salario,
            'data_nascimento': data_nascimento
        }

        ok, mensagem = registrar_funcionario(dados)

        if ok:
            self.lbl_mensagem.setText(suc_registro_funcionario)
            self.lbl_mensagem.setStyleSheet(lbl_mensagem_success)
            box_mensagem_ok('registrar')
        else:
            self.atualizar_campos(err_registro_generico)
            self.lbl_mensagem.setText(mensagem)
            box_mensagem_fail('invalido')

    def login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login_Funcionario.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def reset_campos(self):
        self.lbl_mensagem.setText('')
        self.lbl_mensagem.setStyleSheet(lbl_mensagem_default)

    def atualizar_campos(self, tipo):
        self.lbl_mensagem.setText(tipo)
        self.lbl_mensagem.setStyleSheet(lbl_mensagem_error)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
