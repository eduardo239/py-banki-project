# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sacar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(292, 279)
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
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.inp_valor = QtWidgets.QLineEdit(self.groupBox_3)
        self.inp_valor.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_valor.setObjectName("inp_valor")
        self.verticalLayout_2.addWidget(self.inp_valor)
        self.btn_sacar = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_sacar.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 8px;\n"
"background-color: \'#00C569\'; \n"
"color: white;\n"
"border: none;\n"
"margin: 4px 0;")
        self.btn_sacar.setObjectName("btn_sacar")
        self.verticalLayout_2.addWidget(self.btn_sacar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.lbl_mensagem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mensagem.setStyleSheet("color: \'#333A44\';\n"
"padding: 10px;")
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.verticalLayout.addWidget(self.lbl_mensagem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 21))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Informações da Conta"))
        self.lbl_nome_usuario.setText(_translate("MainWindow", "Sacar"))
        self.label_7.setText(_translate("MainWindow", "Valor"))
        self.btn_sacar.setText(_translate("MainWindow", "Sacar"))
        self.lbl_mensagem.setText(_translate("MainWindow", "TextLabel"))
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
