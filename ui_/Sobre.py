from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(327, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: \'#333A44\';")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lbl_total_funcionarios_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_total_funcionarios_2.setFont(font)
        self.lbl_total_funcionarios_2.setStyleSheet("color: \'#333A44\';")
        self.lbl_total_funcionarios_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_funcionarios_2.setObjectName("lbl_total_funcionarios_2")
        self.verticalLayout.addWidget(self.lbl_total_funcionarios_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: \'#333A44\';")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lbl_total_funcionarios = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_total_funcionarios.setFont(font)
        self.lbl_total_funcionarios.setStyleSheet("color: \'#333A44\';")
        self.lbl_total_funcionarios.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_funcionarios.setObjectName("lbl_total_funcionarios")
        self.verticalLayout.addWidget(self.lbl_total_funcionarios)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: \'#333A44\';")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lbl_ultimo_funcionario = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ultimo_funcionario.setFont(font)
        self.lbl_ultimo_funcionario.setStyleSheet("color: \'#333A44\';")
        self.lbl_ultimo_funcionario.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ultimo_funcionario.setObjectName("lbl_ultimo_funcionario")
        self.verticalLayout.addWidget(self.lbl_ultimo_funcionario)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_fechar = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.btn_fechar.setFont(font)
        self.btn_fechar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_fechar.setStyleSheet(" padding: 10px; background-color: \'#00C569\'; border: none; color: \'#ffffff\';")
        self.btn_fechar.setObjectName("btn_fechar")
        self.verticalLayout.addWidget(self.btn_fechar)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 327, 21))
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

        '''atr'''
        self.btn_fechar.clicked.connect(lambda: MainWindow.close())
        self.action_Exit.triggered.connect(lambda: MainWindow.close())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "App"))
        self.lbl_total_funcionarios_2.setText(_translate("MainWindow", "Banki"))
        self.label_6.setText(_translate("MainWindow", "Desenvolvido por:"))
        self.lbl_total_funcionarios.setText(_translate("MainWindow", "Eduardo Silva"))
        self.label_4.setText(_translate("MainWindow", "Email:"))
        self.lbl_ultimo_funcionario.setText(_translate("MainWindow", "eduardo.ar.85@gmail.com"))
        self.btn_fechar.setText(_translate("MainWindow", "&Fechar"))
        self.menu_Arquivo.setTitle(_translate("MainWindow", "&Arquivo"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())