# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt
# from db import *
#
#
# class TableModel(QtCore.QAbstractTableModel):
#
#     def __init__(self, data):
#         super(TableModel, self).__init__()
#         self._data = data
#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             # See below for the nested-list data structure.
#             # .row() indexes into the outer list,
#             # .column() indexes into the sub-list
#             return self._data[index.row()][index.column()]
#
#     def rowCount(self, index):
#         # The length of the outer list.
#         return len(self._data)
#
#     def columnCount(self, index):
#         # The following takes the first sub-list, and returns
#         # the length (only works if all rows are an equal length)
#         return len(self._data[0])
#
# #
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.table = QtWidgets.QTableView()
#
#         data = [
#           [4, 9, 2],
#           [1, 0, 0],
#           [3, 5, 0],
#           [3, 3, 2],
#           [7, 8, 9],
#         ]
#
#         self.model = TableModel(data)
#         self.table.setModel(self.model)
#
#         self.setCentralWidget(self.table)
#

# app=QtWidgets.QApplication(sys.argv)
# window=MainWindow()
# window.show()
# app.exec_()


# def f(x):
#     result = {
#         'a': lambda x: x * 25,
#         'b': lambda x: x + 7,
#         'c': lambda x: x - 2
#     }[x](x)
#     return result
#
#
# print(f(3))


'''
paired by color
int represent each color
how many pairs of stock matching colors
return int
'''


def sockMerchant(n, ar):
    pears = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
        else:
            pears += 1
            color.remove(ar[i])
    return pears


sockMerchant(7, [1, 2, 1, 2, 1, 2, 3])

def countingValleys(steps, path):
    level = 0
    valley = 0
    for i in range(steps):
        if path[i] == 'U':
            level += 1
        else:
            level -= 1

        if level == 0 and path[i] == 'U':
            valley += 1

    return valley

print('- - -')
a = countingValleys(10, 'DUDDDUUDUU')
print(a)