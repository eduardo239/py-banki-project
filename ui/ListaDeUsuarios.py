from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 545)
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
        self.inp_nome_completo.setFocus()
        self.inp_nome_completo.returnPressed.connect(self.search)
        self.verticalLayout_3.addWidget(self.inp_nome_completo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.inp_numero_conta = QtWidgets.QLineEdit(self.groupBox_3)
        self.inp_numero_conta.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 4px;\n"
"margin-bottom: 10px;")
        self.inp_numero_conta.setObjectName("inp_numero_conta")
        self.inp_nome_completo.returnPressed.connect(self.search)
        self.verticalLayout_2.addWidget(self.inp_numero_conta)
        self.btn_buscar = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_buscar.setStyleSheet("font: 10pt \"Calibri\";\n"
"padding: 8px;\n"
"background-color: \'#00C569\'; \n"
"color: white;\n"
"border: none;\n"
"margin: 4px 0;")
        self.btn_buscar.setObjectName("btn_buscar")
        self.btn_buscar.setAutoDefault(True)
        self.verticalLayout_2.addWidget(self.btn_buscar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.lbl_message = QtWidgets.QLabel(self.centralwidget)
        self.lbl_message.setStyleSheet("color: \'#333A44\';\n"
"padding: 10px;")
        self.lbl_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_message.setObjectName("lbl_message")
        self.verticalLayout.addWidget(self.lbl_message)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        #
        self.model = QSqlTableModel()
        self.model.setTable("clients")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Nome")
        self.model.setHeaderData(2, Qt.Horizontal, "Email")
        self.model.setHeaderData(3, Qt.Horizontal, "Gênero")
        self.model.setHeaderData(4, Qt.Horizontal, "Número da Conta")
        self.model.setHeaderData(5, Qt.Horizontal, "Tipo da Conta")
        self.model.setHeaderData(6, Qt.Horizontal, "Password")
        self.model.removeColumn(6)
        self.model.select()

        #
        self.tab_resultado = QtWidgets.QTableView(self.groupBox_4)
        self.tab_resultado.setObjectName("tab_resultado")
        self.tab_resultado.setModel(self.model)
        self.tab_resultado.resizeColumnsToContents()
        self.tab_resultado.resizeRowsToContents()
        self.verticalLayout_4.addWidget(self.tab_resultado)
        #
        self.verticalLayout.addWidget(self.groupBox_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        self.menuAr_quivo = QtWidgets.QMenu(self.menubar)
        self.menuAr_quivo.setObjectName("menuAr_quivo")
        self.menuRelat_rio = QtWidgets.QMenu(self.menubar)
        self.menuRelat_rio.setObjectName("menuRelat_rio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Nova_Busca = QtWidgets.QAction(MainWindow)
        self.action_Nova_Busca.setObjectName("action_Nova_Busca")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Imprimir = QtWidgets.QAction(MainWindow)
        self.action_Imprimir.setObjectName("action_Imprimir")
        self.menuAr_quivo.addAction(self.action_Nova_Busca)
        self.menuAr_quivo.addAction(self.action_Exit)
        self.menuRelat_rio.addAction(self.action_Imprimir)
        self.menubar.addAction(self.menuAr_quivo.menuAction())
        self.menubar.addAction(self.menuRelat_rio.menuAction())

        # self.client_list = select_all('clients')

        '''edited'''
        self.action_Exit.triggered.connect(lambda: MainWindow.close())

        self.btn_buscar.clicked.connect(self.search)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bankii - Lista de Clientes"))
        self.label_10.setText(_translate("MainWindow", "Lista de Cliente"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Buscar Cliente"))
        self.label.setText(_translate("MainWindow", "Nome Completo"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Informações da Conta"))
        self.label_6.setText(_translate("MainWindow", "Número da Conta"))
        self.btn_buscar.setText(_translate("MainWindow", "Buscar"))
        self.lbl_message.setText(_translate("MainWindow", ""))
        self.groupBox_4.setTitle(_translate("MainWindow", "Resultado"))
        self.menuAr_quivo.setTitle(_translate("MainWindow", "Ar&quivo"))
        self.menuRelat_rio.setTitle(_translate("MainWindow", "Relatório"))
        self.action_Nova_Busca.setText(_translate("MainWindow", "&Nova Busca"))
        self.action_Nova_Busca.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_Imprimir.setText(_translate("MainWindow", "&Imprimir"))
        self.action_Imprimir.setShortcut(_translate("MainWindow", "Ctrl+I"))

    def search(self):

        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
