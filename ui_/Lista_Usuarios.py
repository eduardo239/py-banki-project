from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

from typo import *
from style import *
from ui_ import Sobre


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 530)
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
        self.groupBox_Full.setStyleSheet("")
        self.groupBox_Full.setTitle("")
        self.groupBox_Full.setObjectName("groupBox_Full")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_Full)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_Full)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet(lbl_small_grey)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inp_email = QtWidgets.QLineEdit(self.groupBox)
        self.inp_email.setStyleSheet(inp_default)
        self.inp_email.setObjectName("inp_email")
        self.verticalLayout.addWidget(self.inp_email)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_Full)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setStyleSheet(lbl_small_grey)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.inp_numero_conta = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_numero_conta.setStyleSheet(inp_default)
        self.inp_numero_conta.setObjectName("inp_numero_conta")
        self.verticalLayout_2.addWidget(self.inp_numero_conta)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_Full)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_pesquisar = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_pesquisar.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_pesquisar.setStyleSheet(btn_green)
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.verticalLayout_5.addWidget(self.btn_pesquisar)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.verticalLayout_3.addWidget(self.groupBox_Full)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setStyleSheet("color: \'#333A44\';")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        '''model'''
        self.model = QSqlTableModel()
        self.model.setTable('cliente')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Nome")
        self.model.setHeaderData(2, Qt.Horizontal, "Email")
        # self.model.setHeaderData(3, Qt.Horizontal, "Senha")
        self.model.removeColumn(3)

        self.model.setHeaderData(3, Qt.Horizontal, "Genênro")
        self.model.setHeaderData(4, Qt.Horizontal, "Número da Conta")
        self.model.setHeaderData(5, Qt.Horizontal, "Data de Nascimento")
        self.model.setHeaderData(6, Qt.Horizontal, "Data de Registro")
        self.model.select()

        '''table'''
        self.tab_lista_usuarios = QtWidgets.QTableView(self.groupBox_3)
        self.tab_lista_usuarios.resizeColumnsToContents()
        self.tab_lista_usuarios.resizeRowsToContents()
        self.tab_lista_usuarios.setObjectName("tab_lista_usuarios")
        self.tab_lista_usuarios.setModel(self.model)
        self.tab_lista_usuarios.resizeColumnsToContents()

        '''menu'''

        self.verticalLayout_4.addWidget(self.tab_lista_usuarios)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.lbl_mensagem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mensagem.setStyleSheet("color: \'#333A44\'; padding: 8px;")
        self.lbl_mensagem.setText("")
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.verticalLayout_3.addWidget(self.lbl_mensagem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        self.menuA_juda = QtWidgets.QMenu(self.menubar)
        self.menuA_juda.setObjectName("menuA_juda")
        self.menu_Lista_de_Clientes = QtWidgets.QMenu(self.menubar)
        self.menu_Lista_de_Clientes.setObjectName("menu_Lista_de_Clientes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.action_Registro_Funcionario = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.action_Registro_Funcionario.setIcon(icon)
        # self.action_Registro_Funcionario.setObjectName("action_Registro_Funcionario")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./assets/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setObjectName("action_Exit")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        # self.actionContato = QtWidgets.QAction(MainWindow)
        # self.actionContato.setObjectName("actionContato")
        self.action_Visualizar = QtWidgets.QAction(MainWindow)
        self.action_Visualizar.setObjectName("action_Visualizar")
        # self.action_Informa_es = QtWidgets.QAction(MainWindow)
        # self.action_Informa_es.setObjectName("action_Informa_es")
        # self.menu_Arquivo.addAction(self.action_Registro_Funcionario)
        self.menu_Arquivo.addAction(self.action_Exit)
        self.menuA_juda.addAction(self.actionSobre)
        # self.menuA_juda.addAction(self.actionContato)
        self.menu_Lista_de_Clientes.addAction(self.action_Visualizar)
        # self.menu_Lista_de_Clientes.addAction(self.action_Informa_es)
        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.menubar.addAction(self.menu_Lista_de_Clientes.menuAction())
        self.menubar.addAction(self.menuA_juda.menuAction())
        self.label.setBuddy(self.inp_email)
        self.label_7.setBuddy(self.inp_numero_conta)

        '''atr'''
        self.actionSobre.triggered.connect(self.sobre_window)
        self.action_Exit.triggered.connect(lambda: MainWindow.close())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inp_email, self.inp_numero_conta)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "Lista de Usuários"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.inp_email.setPlaceholderText(_translate("MainWindow", "email@email.com"))
        self.label_7.setText(_translate("MainWindow", "Número da Conta"))
        self.inp_numero_conta.setPlaceholderText(_translate("MainWindow", "00000"))
        self.btn_pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Resultados"))
        self.menu_Arquivo.setTitle(_translate("MainWindow", "&Arquivo"))
        self.menuA_juda.setTitle(_translate("MainWindow", "A&juda"))
        self.menu_Lista_de_Clientes.setTitle(_translate("MainWindow", "&Clientes"))
        # self.action_Registro_Funcionario.setText(_translate("MainWindow", "&Registro de Funcionários"))
        # self.action_Registro_Funcionario.setStatusTip(_translate("MainWindow", "Voltar para tela de Login"))
        # self.action_Registro_Funcionario.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setStatusTip(_translate("MainWindow", "Fechar o aplicativo"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        # self.actionContato.setText(_translate("MainWindow", "Contato"))
        self.action_Visualizar.setText(_translate("MainWindow", "&Visualizar"))
        self.action_Visualizar.setShortcut(_translate("MainWindow", "Ctrl+D"))
        # self.action_Informa_es.setText(_translate("MainWindow", "&Dados"))

    '''met'''

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
