from PyQt5 import QtCore, QtWidgets
from ui import Login as Funcionario_Window, Usuario_Login as Usuario_Window, test
from ui.styles import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setStyleSheet(lbl_simple)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.btn_usuario = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_usuario.setStyleSheet(button_green)
        self.btn_usuario.setObjectName("btn_usuario")
        self.verticalLayout_2.addWidget(self.btn_usuario)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setStyleSheet(lbl_simple)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.btn_funcionario = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_funcionario.setStyleSheet(button_green_dark)
        self.btn_funcionario.setObjectName("btn_funcionario")
        self.verticalLayout_2.addWidget(self.btn_funcionario)
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Sobre = QtWidgets.QMenu(self.menubar)
        self.menu_Sobre.setObjectName("menu_Sobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Sobre = QtWidgets.QAction(MainWindow)
        self.action_Sobre.setObjectName("action_Sobre")
        self.menu_File.addAction(self.action_Exit)
        self.menu_Sobre.addAction(self.action_Sobre)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Sobre.menuAction())

        '''edited'''
        self.window = QtWidgets.QMainWindow()
        self.ui = test.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        self.btn_usuario.clicked.connect(self.usuario_window)
        self.btn_funcionario.clicked.connect(self.funcionario_window)
        self.action_Exit.triggered.connect(lambda: MainWindow.close())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Usuário"))
        self.btn_usuario.setText(_translate("MainWindow", "Entrar"))
        self.btn_usuario.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.label_6.setText(_translate("MainWindow", "Funcionário"))
        self.btn_funcionario.setText(_translate("MainWindow", "Entrar"))
        self.btn_funcionario.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.menu_File.setTitle(_translate("MainWindow", "&Arquivo"))
        self.menu_Sobre.setTitle(_translate("MainWindow", "&Ajuda"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setStatusTip(_translate("MainWindow", "Sair do programa"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_Sobre.setText(_translate("MainWindow", "&Sobre"))

        '''edited'''
    def usuario_window(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Usuario_Window.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def funcionario_window(self):
        MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Funcionario_Window.Ui_MainWindow()
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
