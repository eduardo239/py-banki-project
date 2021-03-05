from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QPixmap, QIcon
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt
import time

from db import *
from typo import *
from style import *
from ui_ import Sobre, Contato
from helpers import *

from dados import Grafico


class Ui_MainWindow(object):
    def __init__(self, usuario):
        self.usuario = usuario
        self.nome_do_cliente = str(self.usuario[0]).title()
        self.email_do_cliente = self.usuario[1]
        self.numero_da_conta = int(self.usuario[2])
        self.agencia_do_cliente = self.usuario[3]
        self.tipo_da_conta_do_cliente = self.usuario[4]
        self.saldo_do_cliente = self.usuario[5]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)

        MainWindow.setStyleSheet(window)
        self.validate = QRegExpValidator(QRegExp("[0-9.]{12}"))

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
        self.lbl_meu_nome = QtWidgets.QLabel(self.groupBox)
        self.lbl_meu_nome.setStyleSheet(lbl_meu_nome)
        self.lbl_meu_nome.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_meu_nome.setObjectName("lbl_meu_nome")
        self.horizontalLayout.addWidget(self.lbl_meu_nome)
        self.verticalLayout.addWidget(self.groupBox)
        self.tab_minha_conta = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_minha_conta.setStyleSheet(tab_default)
        self.tab_minha_conta.setIconSize(QtCore.QSize(16, 16))
        self.tab_minha_conta.setObjectName("tab_minha_conta")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setStyleSheet(lbl_small_grey)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.inp_agencia = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_agencia.setStyleSheet(inp_default)
        self.inp_agencia.setPlaceholderText("")
        self.inp_agencia.setObjectName("inp_agencia")
        self.verticalLayout_2.addWidget(self.inp_agencia)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setStyleSheet(lbl_small_grey)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.inp_numero_conta = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_numero_conta.setStyleSheet(inp_default)
        self.inp_numero_conta.setPlaceholderText("")
        self.inp_numero_conta.setObjectName("inp_numero_conta")
        self.inp_numero_conta.setValidator(self.validate)
        self.verticalLayout_2.addWidget(self.inp_numero_conta)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet(lbl_small_grey)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.inp_tipo_conta = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_tipo_conta.setStyleSheet(inp_default)
        self.inp_tipo_conta.setPlaceholderText("")
        self.inp_tipo_conta.setObjectName("inp_tipo_conta")
        self.verticalLayout_2.addWidget(self.inp_tipo_conta)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setStyleSheet(lbl_small_grey)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lbl_saldo_atual = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_saldo_atual.setStyleSheet(lbl_title_green)
        self.lbl_saldo_atual.setObjectName("lbl_saldo_atual")
        self.verticalLayout_3.addWidget(self.lbl_saldo_atual)

        '''info matplotlib'''
        self.info = QtWidgets.QPushButton(self.groupBox_3)
        self.info.setStyleSheet(btn_green)
        self.info.setObjectName("btn_info")
        self.verticalLayout_3.addWidget(self.info)
        self.info.setText('Gráfico dos últimos dias')

        self.label_image = QtWidgets.QLabel()
        self.pixmap = QPixmap('./assets/1388560951582004484-128.png')
        self.label_image.setPixmap(self.pixmap)
        self.label_image.resize(self.pixmap.width(), self.pixmap.height())
        self.verticalLayout_3.addWidget(self.label_image)
        ''''''

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_minha_conta.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lbl_sacar = QtWidgets.QLabel(self.tab_2)
        self.lbl_sacar.setStyleSheet(lbl_title_secondary)
        self.lbl_sacar.setObjectName("lbl_sacar")
        self.verticalLayout_9.addWidget(self.lbl_sacar)

        '''tab extrato'''
        self.model = QSqlTableModel()
        self.model.setTable('historico')
        self.model.setFilter(f'numero_conta = {self.numero_da_conta}')
        self.model.setSort(6, Qt.SortOrder(Qt.DescendingOrder))
        self.model.removeColumn(1)
        # self.model.setHeaderData(1, Qt.Horizontal, "Número da Conta")
        self.model.setHeaderData(1, Qt.Horizontal, "Valor")
        self.model.setHeaderData(2, Qt.Horizontal, "Saldo Anterior")
        self.model.setHeaderData(3, Qt.Horizontal, "Saldo Atual")
        self.model.setHeaderData(4, Qt.Horizontal, "Operação")
        self.model.setHeaderData(5, Qt.Horizontal, "Conta Destino")
        self.model.setHeaderData(6, Qt.Horizontal, "Data")
        self.model.select()

        self.tab_extrato = QtWidgets.QTableView(self.tab_2)

        self.tab_extrato.setObjectName("tab_extrato")
        self.tab_extrato.resizeColumnsToContents()
        self.tab_extrato.resizeRowsToContents()
        self.tab_extrato.horizontalHeader().setStretchLastSection(True)
        self.tab_extrato.setModel(self.model)
        self.tab_extrato.hideColumn(0)

        self.verticalLayout_9.addWidget(self.tab_extrato)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./assets/9104314201582004494-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_minha_conta.addTab(self.tab_2, icon1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setStyleSheet(lbl_small_grey)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.inp_valor_d = QtWidgets.QLineEdit(self.groupBox_5)
        self.inp_valor_d.setStyleSheet(inp_default)
        self.inp_valor_d.setPlaceholderText("")
        self.inp_valor_d.setObjectName("inp_valor_d")
        self.inp_valor_d.setValidator(self.validate)
        self.verticalLayout_8.addWidget(self.inp_valor_d)
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setStyleSheet(lbl_small_grey)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.inp_numero_conta_d = QtWidgets.QLineEdit(self.groupBox_5)
        self.inp_numero_conta_d.setStyleSheet(inp_default)
        self.inp_numero_conta_d.setPlaceholderText("")
        self.inp_numero_conta_d.setObjectName("inp_numero_conta_d")
        self.verticalLayout_8.addWidget(self.inp_numero_conta_d)
        self.btn_depositar = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_depositar.setStyleSheet(btn_green)
        self.btn_depositar.setObjectName("btn_depositar")
        self.verticalLayout_8.addWidget(self.btn_depositar)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_5.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setStyleSheet(lbl_small_grey)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_5.addWidget(self.groupBox_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./assets/13467909091582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_minha_conta.addTab(self.tab_3, icon2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setStyleSheet(lbl_small_grey)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.inp_agencia_t = QtWidgets.QLineEdit(self.groupBox_6)
        self.inp_agencia_t.setStyleSheet(inp_default)
        self.inp_agencia_t.setPlaceholderText("")
        self.inp_agencia_t.setObjectName("inp_agencia_t")
        self.inp_agencia_t.setFocus()
        self.inp_agencia_t.setPlaceholderText("AG-00000")
        self.inp_agencia_t.setText("AG-")
        self.verticalLayout_5.addWidget(self.inp_agencia_t)
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setStyleSheet(lbl_small_grey)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.inp_numero_conta_t = QtWidgets.QLineEdit(self.groupBox_6)
        self.inp_numero_conta_t.setStyleSheet(inp_default)
        self.inp_numero_conta_t.setPlaceholderText("")
        self.inp_numero_conta_t.setObjectName("inp_numero_conta_t")
        self.inp_numero_conta_t.setValidator(self.validate)
        self.inp_numero_conta_t.setPlaceholderText('00000')
        self.verticalLayout_5.addWidget(self.inp_numero_conta_t)
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setStyleSheet(lbl_small_grey)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.inp_tipo_conta_t = QtWidgets.QLineEdit(self.groupBox_6)
        self.inp_tipo_conta_t.setStyleSheet(inp_default)
        self.inp_tipo_conta_t.setPlaceholderText("")
        self.inp_tipo_conta_t.setObjectName("inp_tipo_conta_t")
        self.inp_tipo_conta_t.setPlaceholderText("tipo da conta")
        self.verticalLayout_5.addWidget(self.inp_tipo_conta_t)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_4.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.groupBox_7)
        self.label_16.setStyleSheet(lbl_small_grey)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.inp_valor_t = QtWidgets.QLineEdit(self.groupBox_7)
        self.inp_valor_t.setStyleSheet(inp_default)
        self.inp_valor_t.setPlaceholderText("")
        self.inp_valor_t.setObjectName("inp_valor_t")
        self.inp_valor_t.setValidator(self.validate)
        self.verticalLayout_6.addWidget(self.inp_valor_t)
        self.label_17 = QtWidgets.QLabel(self.groupBox_7)
        self.label_17.setStyleSheet(lbl_small_grey)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.inp_nome_cliente_t = QtWidgets.QLineEdit(self.groupBox_7)
        self.inp_nome_cliente_t.setStyleSheet(inp_default)
        self.inp_nome_cliente_t.setPlaceholderText("")
        self.inp_nome_cliente_t.setObjectName("inp_nome_cliente_t")
        self.verticalLayout_6.addWidget(self.inp_nome_cliente_t)
        self.btn_transferir = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_transferir.setStyleSheet(btn_green)
        self.btn_transferir.setObjectName("btn_transferir")
        self.verticalLayout_6.addWidget(self.btn_transferir)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_4.addWidget(self.groupBox_7)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./assets/17419230201582004492-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_minha_conta.addTab(self.tab_4, icon3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_21 = QtWidgets.QLabel(self.groupBox_9)
        self.label_21.setStyleSheet(lbl_small_grey)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21)
        self.inp_valor_s = QtWidgets.QLineEdit(self.groupBox_9)
        self.inp_valor_s.setStyleSheet(inp_default)
        self.inp_valor_s.setPlaceholderText("")
        self.inp_valor_s.setObjectName("inp_valor_s")
        self.inp_valor_s.setFocus()
        self.inp_valor_s.setValidator(self.validate)
        self.verticalLayout_4.addWidget(self.inp_valor_s)
        self.label_22 = QtWidgets.QLabel(self.groupBox_9)
        self.label_22.setStyleSheet(lbl_small_grey)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.inp_numero_conta_s = QtWidgets.QLineEdit(self.groupBox_9)
        self.inp_numero_conta_s.setStyleSheet(inp_default)
        self.inp_numero_conta_s.setPlaceholderText("")
        self.inp_numero_conta_s.setObjectName("inp_numero_conta_s")
        self.verticalLayout_4.addWidget(self.inp_numero_conta_s)
        self.btn_sacar = QtWidgets.QPushButton(self.groupBox_9)
        self.btn_sacar.setStyleSheet(btn_green)
        self.btn_sacar.setObjectName("btn_sacar")

        self.verticalLayout_4.addWidget(self.btn_sacar)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_3.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_18 = QtWidgets.QLabel(self.groupBox_10)
        self.label_18.setStyleSheet(lbl_small_grey)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_10.addWidget(self.label_18)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem10)
        self.horizontalLayout_3.addWidget(self.groupBox_10)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./assets/19543194281582004490-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_minha_conta.addTab(self.tab_5, icon4, "")
        self.verticalLayout.addWidget(self.tab_minha_conta)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        self.menuA_juda = QtWidgets.QMenu(self.menubar)
        self.menuA_juda.setObjectName("menuA_juda")
        MainWindow.setMenuBar(self.menubar)

        self.action_Registro_Funcionario = QtWidgets.QAction(MainWindow)
        self.action_Registro_Funcionario.setIcon(icon)
        self.action_Registro_Funcionario.setObjectName("action_Registro_Funcionario")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./assets/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon5)
        self.action_Exit.setObjectName("action_Exit")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./assets/9468673611582004493-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSobre.setIcon(icon6)
        self.actionSobre.setObjectName("actionSobre")
        self.actionContato = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./assets/2198796101582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContato.setIcon(icon7)
        self.actionContato.setObjectName("actionContato")
        self.action_Visualizar = QtWidgets.QAction(MainWindow)
        self.action_Visualizar.setObjectName("action_Visualizar")
        self.action_Informa_es = QtWidgets.QAction(MainWindow)
        self.action_Informa_es.setObjectName("action_Informa_es")
        self.menu_Arquivo.addAction(self.action_Exit)
        self.menuA_juda.addAction(self.actionSobre)
        self.menuA_juda.addAction(self.actionContato)
        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.menubar.addAction(self.menuA_juda.menuAction())

        self.label_2.setBuddy(self.inp_agencia)
        self.label_3.setBuddy(self.inp_agencia)
        self.label_4.setBuddy(self.inp_agencia)
        self.label_11.setBuddy(self.inp_agencia)
        self.label_12.setBuddy(self.inp_agencia)
        self.label_13.setBuddy(self.inp_agencia)
        self.label_14.setBuddy(self.inp_agencia)
        self.label_15.setBuddy(self.inp_agencia)
        self.label_16.setBuddy(self.inp_agencia)
        self.label_17.setBuddy(self.inp_agencia)
        self.label_21.setBuddy(self.inp_agencia)
        self.label_22.setBuddy(self.inp_agencia)

        '''atr'''
        self.action_Exit.triggered.connect(lambda: MainWindow.close())
        self.actionSobre.triggered.connect(self.sobre_window)
        self.actionContato.triggered.connect(self.contato_window)

        self.btn_sacar.clicked.connect(self.sacar_)
        self.btn_sacar.setAutoDefault(True)
        self.btn_transferir.clicked.connect(self.transferir)
        self.btn_transferir.setAutoDefault(True)
        self.btn_depositar.clicked.connect(self.depositar)
        self.btn_depositar.setAutoDefault(True)

        self.inp_numero_conta_t.returnPressed.connect(self.transferir)
        self.inp_agencia_t.returnPressed.connect(self.transferir)
        self.inp_tipo_conta_t.returnPressed.connect(self.transferir)
        self.inp_valor_t.returnPressed.connect(self.transferir)
        self.inp_nome_cliente_t.returnPressed.connect(self.transferir)

        self.inp_valor_d.returnPressed.connect(self.depositar)
        self.inp_numero_conta_d.returnPressed.connect(self.depositar)

        self.inp_valor_s.returnPressed.connect(self.sacar_)
        self.inp_numero_conta_s.returnPressed.connect(self.sacar_)

        self.inp_agencia.setText(self.agencia_do_cliente)
        self.inp_tipo_conta.setText(self.tipo_da_conta_do_cliente)

        self.inp_numero_conta.setEnabled(False)
        self.inp_agencia.setEnabled(False)
        self.inp_tipo_conta.setEnabled(False)
        self.inp_numero_conta.setText(str(self.numero_da_conta))

        '''teste'''
        self.info.clicked.connect(self.info_window)

        self.retranslateUi(MainWindow)
        self.tab_minha_conta.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "Bankii"))
        self.lbl_meu_nome.setText(_translate("MainWindow", self.nome_do_cliente))
        self.label_2.setText(_translate("MainWindow", "Agência"))
        self.label_3.setText(_translate("MainWindow", "Número da Conta"))
        self.label_4.setText(_translate("MainWindow", "Tipo da Conta"))
        self.label_5.setText(_translate("MainWindow", "Saldo Atual"))
        self.lbl_saldo_atual.setText(_translate("MainWindow", ""))
        self.tab_minha_conta.setTabText(self.tab_minha_conta.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.lbl_sacar.setText(_translate("MainWindow", "Extrato Bancário"))
        self.tab_minha_conta.setTabText(self.tab_minha_conta.indexOf(self.tab_2), _translate("MainWindow", "Extrato"))
        self.label_11.setText(_translate("MainWindow", "Valor"))
        self.label_12.setText(_translate("MainWindow", "Número da Conta"))
        self.btn_depositar.setText(_translate("MainWindow", "Depositar"))
        self.label_19.setText(_translate("MainWindow", "Depositar"))
        self.tab_minha_conta.setTabText(self.tab_minha_conta.indexOf(self.tab_3), _translate("MainWindow", "Depositar"))
        self.label_13.setText(_translate("MainWindow", "Agência"))
        self.label_14.setText(_translate("MainWindow", "Número da Conta"))
        self.label_15.setText(_translate("MainWindow", "Tipo da Conta"))
        self.label_16.setText(_translate("MainWindow", "Valor"))
        self.label_17.setText(_translate("MainWindow", "Nome do Cliente"))
        self.btn_transferir.setText(_translate("MainWindow", "Transferir"))
        self.tab_minha_conta.setTabText(self.tab_minha_conta.indexOf(self.tab_4),
                                        _translate("MainWindow", "Transferir"))
        self.label_21.setText(_translate("MainWindow", "Valor"))
        self.label_22.setText(_translate("MainWindow", "Número da Conta"))
        self.btn_sacar.setText(_translate("MainWindow", "Sacar"))
        self.label_18.setText(_translate("MainWindow", "Extrato do Último mês"))
        self.tab_minha_conta.setTabText(self.tab_minha_conta.indexOf(self.tab_5), _translate("MainWindow", "Sacar"))
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

        self.atualiza_mensagem(self.saldo_do_cliente)

    '''def'''

    '''tst'''

    def info_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Grafico.Ui_MainWindow(self.usuario)
        self.ui.setupUi(self.window)
        self.window.show()

    def sacar_(self):
        self.reset_campos()

        valor = self.inp_valor_s.text() or 0

        if valor != 0:
            try:
                dados = {
                    'numero_conta_s': self.numero_da_conta,
                    'valor': float(valor)
                }
                saldo_atual = sacar(dados)
                log_sacar(dados)

                self.lbl_mensagem.setText(atualizando)
                self.label_18.setText(sacar_ok)
                self.lbl_mensagem.setStyleSheet(lbl_mensagem_success)
                box_mensagem_ok('sacar')
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(str(e))
                error_dialog.exec_()
                self.lbl_mensagem.setText(sacar_fail)
            finally:
                time.sleep(1)
                self.inp_valor_s.setText('')
                self.atualiza_mensagem(saldo_atual)
                self.model.select()
        else:
            self.label_19.setText(err_valor_zero)
            self.atualizar_campos(err_valor_zero)

    def depositar(self):
        self.reset_campos()

        valor = self.inp_valor_d.text() or 0

        if valor != 0:
            try:
                dados = {
                    'numero_conta_d': self.numero_da_conta,
                    'valor': float(valor)
                }

                saldo_atual = depositar(dados)
                log_depositar(dados)

                self.lbl_mensagem.setText(atualizando)
                self.label_19.setText(depositar_ok)
                self.lbl_mensagem.setStyleSheet(lbl_mensagem_success)
                box_mensagem_ok('depositar')
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(str(e))
                error_dialog.exec_()
                self.lbl_mensagem.setText(sacar_fail)
            finally:
                time.sleep(1)
                self.inp_valor_d.setText('')
                self.atualiza_mensagem(saldo_atual)
                self.model.select()
        else:
            self.label_19.setText(err_valor_zero)
            self.atualizar_campos(err_valor_zero)

    def transferir(self):
        self.reset_campos()

        valor = self.inp_valor_t.text() or 0
        conta_destino = self.inp_numero_conta_t.text() or 0

        if conta_destino == 0:
            self.lbl_mensagem.setText(err_conta_nao_encontrada)
            self.lbl_mensagem.setStyleSheet(lbl_mensagem_error)
            return

        if valor != 0:
            try:
                dados = {
                    'numero_conta_s': self.numero_da_conta,
                    'numero_conta_d': int(conta_destino),
                    'valor': float(valor)
                }

                saldo_atual = transferir(dados)
                log_transferir(dados)

                self.lbl_mensagem.setText(transferir_ok)
                self.lbl_mensagem.setStyleSheet(lbl_mensagem_success)
                box_mensagem_ok('transferir')
                saldo = get_saldo(self.numero_da_conta)
                self.lbl_saldo_atual.setText(str(saldo))
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(str(e))
                error_dialog.exec_()
                self.lbl_mensagem.setText(sacar_fail)
            finally:
                self.atualiza_mensagem(saldo_atual)
                self.model.select()
        else:
            self.label_19.setText(err_valor_zero)
            self.atualizar_campos(err_valor_zero)

    def atualiza_mensagem(self, valor):
        self.lbl_saldo_atual.setText("${:,.2f}".format(valor))
        self.lbl_mensagem.setText("${:,.2f}".format(valor))
        self.label_19.setText("Saldo atual ${:,.2f}".format(valor))
        self.label_18.setText("Saldo atual ${:,.2f}".format(valor))

    def reset_campos(self):
        self.lbl_mensagem.setText('')
        self.lbl_mensagem.setStyleSheet(lbl_mensagem_default)

    def atualizar_campos(self, tipo):
        self.lbl_mensagem.setText(tipo)
        self.lbl_mensagem.setStyleSheet(lbl_mensagem_error)

    def sobre_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Sobre.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def contato_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Contato.Ui_MainWindow()
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
