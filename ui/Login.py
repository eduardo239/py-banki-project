from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp
from db import *
from ui.styles import *
from ui import Registro, RegistroDeClientes

con, message = connection()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 360)
        MainWindow.setFixedSize(300, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(grey_color)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
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
        self.btn_login = QtWidgets.QPushButton(self.groupBox)
        self.btn_login.setStyleSheet(green_button)
        self.btn_login.setObjectName("btn_login")
        self.btn_login.setAutoDefault(True)
        self.gridLayout.addWidget(self.btn_login, 5, 0, 1, 1)
        self.inp_email = QtWidgets.QLineEdit(self.groupBox)
        self.inp_email.setStyleSheet(inp_reset)
        self.inp_email.setObjectName("inp_email")
        self.inp_email.setFocus()
        self.inp_email.returnPressed.connect(self.login)
        self.gridLayout.addWidget(self.inp_email, 2, 0, 1, 1)
        self.inp_senha = QtWidgets.QLineEdit(self.groupBox)
        self.inp_senha.setStyleSheet(inp_reset)
        self.inp_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inp_senha.setObjectName("inp_senha")
        self.inp_senha.returnPressed.connect(self.login)
        self.gridLayout.addWidget(self.inp_senha, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet(lbl_reset)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet(lbl_reset)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lbl_messages = QtWidgets.QLabel(self.groupBox)
        self.lbl_messages.setObjectName("lbl_messages")
        self.gridLayout.addWidget(self.lbl_messages, 6, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Register = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/15586770221582004499-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Register.setIcon(icon)
        self.action_Register.setWhatsThis("")
        self.action_Register.setObjectName("action_Register")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_File.addAction(self.action_Register)
        self.menu_File.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inp_email, self.inp_senha)
        MainWindow.setTabOrder(self.inp_senha, self.btn_login)

        '''edited'''
        self.action_Exit.triggered.connect(qApp.quit)
        self.action_Register.triggered.connect(self.register_window)
        self.btn_login.clicked.connect(self.login)
        self.action_Exit.triggered.connect(lambda: MainWindow.close())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bankii - Login"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "Login"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.lbl_messages.setText(_translate("MainWindow", message + ' ' + db_name))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.action_Register.setText(_translate("MainWindow", "&Register"))
        self.action_Register.setStatusTip(_translate("MainWindow", "Registrar um novo usuário"))
        self.action_Register.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setStatusTip(_translate("MainWindow", "Sair do aplicativo"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))

    '''edited'''
    def register_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Registro.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def client_register_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = RegistroDeClientes.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    ###
    def login(self):
        email = self.inp_email.text().strip()
        password = self.inp_senha.text()

        self.inp_email.setStyleSheet(inp_reset)
        self.inp_senha.setStyleSheet(inp_reset)
        self.lbl_messages.setStyleSheet(lbl_reset)
        self.lbl_messages.setText('')

        if email != '':

            try:
                login = select_by('users', field='email', value=email)

                if login:
                    self.client_register_window()
                else:
                    self.inp_email.setStyleSheet(inp_error)
                    self.inp_senha.setStyleSheet(inp_error)
                    self.lbl_messages.setText('Usuário e/ou senha não encontrados.')
            except QSqlError:
                m = 'Erro ao fazer o login.'

                print(m)
                self.lbl_messages.setText(m)
        else:
            self.lbl_messages.setText('Os campos precisam ser preenchidos.')
            self.lbl_messages.setStyleSheet(lbl_error)
            self.inp_email.setStyleSheet(inp_error)
            self.inp_senha.setStyleSheet(inp_error)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
