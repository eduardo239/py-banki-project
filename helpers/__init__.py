from PyQt5.QtWidgets import QMessageBox

from typo import *


def box_mensagem_ok(tipo):
    msg = QMessageBox()
    msg.setWindowTitle('Sucesso')
    msg.setIcon(QMessageBox.Information)

    if tipo == 'depositar':
        msg.setText(suc_deposito)
    elif tipo == 'sacar':
        msg.setText(suc_saque)
    elif tipo == 'transferir':
        msg.setText(suc_transferencia)
    elif tipo == 'registrar':
        msg.setText(suc_registro_cliente)
    msg.exec_()


def box_mensagem_fail(tipo):
    msg = QMessageBox()
    msg.setWindowTitle('Erro')
    msg.setIcon(QMessageBox.Information)

    if tipo == 'vazio':
        msg.setText(err_campos_vazios)
    elif tipo == 'invalido':
        msg.setText('invalido')
    elif tipo == 'nao_encontrado':
        msg.setText('nao encontrado')
    msg.exec_()
