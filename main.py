from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from ui_ import Registro_Cliente, Registro_Funcionario, Login_Usuario, Login_Funcionario, Sobre
from db import connection
from style import *

con, message = connection()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(307, 316)
        MainWindow.setStyleSheet(window)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setStyleSheet(lbl_title_green)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setStyleSheet(lbl_small_grey)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.btn_registro_cliente = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_registro_cliente.setStyleSheet(btn_disabled)
        self.btn_registro_cliente.setObjectName("btn_registro_cliente")
        self.verticalLayout_2.addWidget(self.btn_registro_cliente)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet(lbl_small_grey)
        self.verticalLayout_2.addWidget(self.label_4)
        self.btn_registro_funcionario = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_registro_funcionario.setStyleSheet(btn_green)
        self.btn_registro_funcionario.setObjectName("btn_registro_funcionario")
        self.verticalLayout_2.addWidget(self.btn_registro_funcionario)
        self.verticalLayout.addWidget(self.groupBox_2)

        '''add'''
        self.lbl_login_usuario = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_login_usuario.setStyleSheet(lbl_small_grey)
        self.lbl_login_usuario.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.lbl_login_usuario)

        self.btn_login_cliente = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_login_cliente.setStyleSheet(btn_disabled)
        self.btn_login_cliente.setObjectName("btn_login_cliente")
        self.verticalLayout_2.addWidget(self.btn_login_cliente)

        '''login funcionario'''
        self.lbl_login_funcionario = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_login_funcionario.setStyleSheet(lbl_small_grey)
        self.lbl_login_funcionario.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.lbl_login_funcionario)

        self.btn_login_funcionario = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_login_funcionario.setStyleSheet(btn_green)
        self.btn_login_funcionario.setObjectName("btn_login_funcionario")
        self.verticalLayout_2.addWidget(self.btn_login_funcionario)

        self.lbl_mensagem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mensagem.setStyleSheet("color: \'#333A44\'; padding: 8px;")
        self.lbl_mensagem.setText("")
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.verticalLayout.addWidget(self.lbl_mensagem)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        '''add'''
        self.lbl_mensagem.setText(message)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 307, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        self.menuA_juda = QtWidgets.QMenu(self.menubar)
        self.menuA_juda.setObjectName("menuA_juda")
        MainWindow.setMenuBar(self.menubar)
        self.action_Registro_Funcionario = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Registro_Funcionario.setIcon(icon)
        self.action_Registro_Funcionario.setObjectName("action_Registro_Funcionario")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setObjectName("action_Exit")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        # self.actionContato = QtWidgets.QAction(MainWindow)
        # self.actionContato.setObjectName("actionContato")
        self.action_Visualizar = QtWidgets.QAction(MainWindow)
        self.action_Visualizar.setObjectName("action_Visualizar")
        self.action_Informa_es = QtWidgets.QAction(MainWindow)
        self.action_Informa_es.setObjectName("action_Informa_es")
        self.menu_Arquivo.addAction(self.action_Exit)
        self.menuA_juda.addAction(self.actionSobre)
        # self.menuA_juda.addAction(self.actionContato)
        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.menubar.addAction(self.menuA_juda.menuAction())

        '''edited'''
        self.btn_login_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registro_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registro_funcionario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login_funcionario.setCursor(QCursor(Qt.PointingHandCursor))

        '''var'''
        self.action_Exit.triggered.connect(lambda: MainWindow.close())
        self.actionSobre.triggered.connect(self.sobre_window)
        self.btn_registro_cliente.clicked.connect(self.registro_cliente)
        self.btn_registro_funcionario.clicked.connect(self.registro_funcionario)
        self.btn_login_cliente.clicked.connect(self.login_cliente)
        self.btn_login_funcionario.clicked.connect(self.login_funcionario)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "Main"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Main"))
        self.label_5.setText(_translate("MainWindow", "Registro de Clientes"))
        self.btn_registro_cliente.setText(_translate("MainWindow", "Regi&stro RCLI Ctrl+S"))
        self.btn_registro_cliente.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.label_4.setText(_translate("MainWindow", "Registro Funcionários"))
        self.btn_registro_funcionario.setText(_translate("MainWindow", "&Registro RFUN Ctrl+R"))
        self.btn_registro_funcionario.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.lbl_login_usuario.setText(_translate("MainWIndow", "Login dos Cliente"))
        self.btn_login_cliente.setText(_translate("MainWindow", "Login &Cliente LCLI Ctrl+C"))
        self.btn_login_cliente.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.lbl_login_funcionario.setText(_translate("MainWindow", "Login dos Funcionários"))
        self.btn_login_funcionario.setText(_translate("MainWindow", "Login &Funcionario LFUN Ctrl+F"))
        self.btn_login_funcionario.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.menu_Arquivo.setTitle(_translate("MainWindow", "&Arquivo"))
        self.menuA_juda.setTitle(_translate("MainWindow", "A&juda"))
        self.action_Registro_Funcionario.setText(_translate("MainWindow", "&Registro de Funcionários"))
        self.action_Registro_Funcionario.setStatusTip(_translate("MainWindow", "Voltar para tela de Login"))
        self.action_Registro_Funcionario.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setStatusTip(_translate("MainWindow", "Fechar o aplicativo"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        # self.actionContato.setText(_translate("MainWindow", "Contato"))
        self.action_Visualizar.setText(_translate("MainWindow", "&Visualizar"))
        self.action_Visualizar.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_Informa_es.setText(_translate("MainWindow", "&Informações"))

    '''def'''
    def login_cliente(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Login_Usuario.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def login_funcionario(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Login_Funcionario.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def registro_cliente(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Registro_Cliente.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def registro_funcionario(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Registro_Funcionario.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def sobre_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Sobre.Ui_MainWindow()
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
