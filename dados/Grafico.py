from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from db import extrato

dados, lista = extrato(102)

lst_datasx = []
lst_valores = []

for i in lista:
    d = datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S.%f")
    r = datetime.strftime(d, "%Y-%m-%d")
    lst_datasx.append(r)
for x in lista: lst_valores.append(x[0])

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        fig.autofmt_xdate()
        self.ax.plot(lst_datasx, lst_valores)
        super().__init__(fig)
        self.ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
        self.ax.set(xlabel='time s', ylabel='voltage', title='Title')
        self.ax.grid()


class Ui_MainWindow(object):
    def __init__(self, usuario):
        self.usuario = usuario
        self.dados, self.lista = extrato(self.usuario[2])

        self.lst_data = []
        self.lst_valores = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.chart = Canvas(self)

        self.verticalLayout_2.addWidget(self.chart)

        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "Gráfico"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menu_Arquivo.setTitle(_translate("MainWindow", "&Arquivo"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
