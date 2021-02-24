from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from db import *
from ui import ListaDeUsuarios, test


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("padding: 10px;\n"
"color: \'#00C569\';\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("color: \'#333A44\';")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setStyleSheet("font: 10pt \"Calibri\";")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.inp_nome_completo = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_nome_completo.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_nome_completo.setObjectName("inp_nome_completo")
        self.verticalLayout_3.addWidget(self.inp_nome_completo)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.inp_data_nascimento = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_data_nascimento.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_data_nascimento.setObjectName("inp_data_nascimento")
        self.verticalLayout_3.addWidget(self.inp_data_nascimento)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.inp_email = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_email.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_email.setObjectName("inp_email")
        self.verticalLayout_3.addWidget(self.inp_email)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.inp_telefone = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_telefone.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_telefone.setObjectName("inp_telefone")
        self.verticalLayout_3.addWidget(self.inp_telefone)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rad_masculino = QtWidgets.QRadioButton(self.groupBox_4)
        self.rad_masculino.setObjectName("rad_masculino")
        self.horizontalLayout_2.addWidget(self.rad_masculino)
        self.rad_feminino = QtWidgets.QRadioButton(self.groupBox_4)
        self.rad_feminino.setObjectName("rad_feminino")
        self.horizontalLayout_2.addWidget(self.rad_feminino)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.inp_agencia = QtWidgets.QLineEdit(self.groupBox_3)
        self.inp_agencia.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_agencia.setObjectName("inp_agencia")
        self.verticalLayout_2.addWidget(self.inp_agencia)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.inp_numero_conta = QtWidgets.QLineEdit(self.groupBox_3)
        self.inp_numero_conta.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_numero_conta.setObjectName("inp_numero_conta")
        self.verticalLayout_2.addWidget(self.inp_numero_conta)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.cmb_tipo = QtWidgets.QComboBox(self.groupBox_3)
        self.cmb_tipo.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;")
        self.cmb_tipo.setObjectName("cmb_tipo")
        self.cmb_tipo.addItem("")
        self.cmb_tipo.addItem("")
        self.cmb_tipo.addItem("")
        self.verticalLayout_2.addWidget(self.cmb_tipo)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setStyleSheet("font: 10pt \"Calibri\";\n"
"margin-top: 10px;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.inp_id = QtWidgets.QLineEdit(self.groupBox_3)
        self.inp_id.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_id.setObjectName("inp_id")
        self.verticalLayout_2.addWidget(self.inp_id)
        self.btn_registrar = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_registrar.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 8px;\n"
"background-color: \'#00C569\'; \n"
"color: white;\n"
"border: none;\n"
"margin: 4px 0;")
        self.btn_registrar.setObjectName("btn_registrar")
        self.verticalLayout_2.addWidget(self.btn_registrar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.lbl_messages = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_messages.setFont(font)
        self.lbl_messages.setStyleSheet("color: \'#333A44\';\n"
"padding: 10px;")
        self.lbl_messages.setObjectName("lbl_messages")
        self.verticalLayout.addWidget(self.lbl_messages)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Usu_rio = QtWidgets.QMenu(self.menubar)
        self.menu_Usu_rio.setObjectName("menu_Usu_rio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setStyleSheet("margin: 2px;")
        self.toolBar.setIconSize(QtCore.QSize(20, 20))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Abrir = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/4798580041582004495-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Abrir.setIcon(icon)
        self.action_Abrir.setObjectName("action_Abrir")
        self.action_Salvar = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/2058131601582004490-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Salvar.setIcon(icon1)
        self.action_Salvar.setObjectName("action_Salvar")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/20635100751582004491-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon2)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Novo = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/14787197661582004498-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Novo.setIcon(icon3)
        self.action_Novo.setObjectName("action_Novo")
        self.action_Perfil = QtWidgets.QAction(MainWindow)
        self.action_Perfil.setObjectName("action_Perfil")
        self.action_Logout = QtWidgets.QAction(MainWindow)
        self.action_Logout.setObjectName("action_Logout")
        self.actionLista_de_Usu_rios = QtWidgets.QAction(MainWindow)
        self.actionLista_de_Usu_rios.setObjectName("actionLista_de_Usu_rios")

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/5724063391582004496-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLista_de_Usu_rios.setIcon(icon4)

        self.menu_File.addAction(self.action_Novo)
        self.menu_File.addAction(self.action_Abrir)
        self.menu_File.addAction(self.action_Salvar)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Usu_rio.addAction(self.action_Perfil)
        self.menu_Usu_rio.addAction(self.action_Logout)
        self.menu_Usu_rio.addAction(self.actionLista_de_Usu_rios)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Usu_rio.menuAction())
        self.toolBar.addAction(self.action_Novo)
        self.toolBar.addAction(self.action_Abrir)
        self.toolBar.addAction(self.action_Salvar)
        self.toolBar.addAction(self.actionLista_de_Usu_rios)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Exit)

        ###
        self.actionLista_de_Usu_rios.triggered.connect(self.user_list_window)
        self.btn_registrar.clicked.connect(self.client_register)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Registro de Cliente"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Informações do Cliente"))
        self.label.setText(_translate("MainWindow", "Nome Completo"))
        self.label_2.setText(_translate("MainWindow", "Data de Nascimento"))
        self.label_3.setText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "Telefone"))
        self.label_9.setText(_translate("MainWindow", "Gênero"))
        self.rad_masculino.setText(_translate("MainWindow", "Masculino"))
        self.rad_feminino.setText(_translate("MainWindow", "Feminino"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Informações da Conta"))
        self.label_5.setText(_translate("MainWindow", "Agência"))
        self.label_6.setText(_translate("MainWindow", "Número da Conta"))
        self.label_7.setText(_translate("MainWindow", "Tipo"))
        self.cmb_tipo.setItemText(0, _translate("MainWindow", "A"))
        self.cmb_tipo.setItemText(1, _translate("MainWindow", "B"))
        self.cmb_tipo.setItemText(2, _translate("MainWindow", "C"))
        self.label_8.setText(_translate("MainWindow", "ID"))
        self.btn_registrar.setText(_translate("MainWindow", "Registrar"))
        self.lbl_messages.setText(_translate("MainWindow", "Messages"))
        self.menu_File.setTitle(_translate("MainWindow", "A&rquivo"))
        self.menu_Usu_rio.setTitle(_translate("MainWindow", "&Usuário"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Abrir.setText(_translate("MainWindow", "&Abrir"))
        self.action_Abrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Salvar.setText(_translate("MainWindow", "&Salvar"))
        self.action_Salvar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_Novo.setText(_translate("MainWindow", "&Novo"))
        self.action_Novo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Perfil.setText(_translate("MainWindow", "&Perfil"))
        self.action_Perfil.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_Logout.setText(_translate("MainWindow", "&Logout"))
        self.action_Logout.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionLista_de_Usu_rios.setText(_translate("MainWindow", "Lista de Usuários"))

    ###
    def user_list_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ListaDeUsuarios.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def client_register(self):
        email = self.inp_email.text()
        name = self.inp_nome_completo.text()
        birth = self.inp_data_nascimento.text()
        phone = self.inp_telefone.text()
        gender = lambda x: 'masculino' if self.rad_masculino.isChecked() else 'feminino'

        try:
            insert_into('users',
                        email=email,
                        name=name,
                        birth=birth,
                        phone=phone,
                        gender=gender
                        )
        except:
            m = 'Erro ao registrar um novo usuário.'
            print(m)
            self.lbl_messages.setText(m)

    '''
    def teste(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = test.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    '''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
