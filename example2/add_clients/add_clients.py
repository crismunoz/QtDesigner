# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_clients/add_clients.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddNewClient(object):
    def setupUi(self, AddNewClient):
        AddNewClient.setObjectName("AddNewClient")
        AddNewClient.resize(399, 150)
        self.gridLayoutWidget = QtWidgets.QWidget(AddNewClient)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.client_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.client_name.setObjectName("client_name")
        self.gridLayout.addWidget(self.client_name, 0, 1, 1, 1)
        self.address = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 1, 1, 1, 1)
        self.ruc = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ruc.setObjectName("ruc")
        self.gridLayout.addWidget(self.ruc, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(AddNewClient)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_client = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_client.setObjectName("add_client")
        self.horizontalLayout.addWidget(self.add_client)
        self.reset_fileds = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset_fileds.setObjectName("reset_fileds")
        self.horizontalLayout.addWidget(self.reset_fileds)
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)

        self.retranslateUi(AddNewClient)
        QtCore.QMetaObject.connectSlotsByName(AddNewClient)

    def retranslateUi(self, AddNewClient):
        _translate = QtCore.QCoreApplication.translate
        AddNewClient.setWindowTitle(_translate("AddNewClient", "Dialog"))
        self.label.setText(_translate("AddNewClient", "Cliente"))
        self.label_3.setText(_translate("AddNewClient", "RUC"))
        self.label_2.setText(_translate("AddNewClient", "Dirección"))
        self.add_client.setText(_translate("AddNewClient", "Adicionar"))
        self.reset_fileds.setText(_translate("AddNewClient", "Limpiar Campos"))
        self.cancel.setText(_translate("AddNewClient", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewClient = QtWidgets.QDialog()
    ui = Ui_AddNewClient()
    ui.setupUi(AddNewClient)
    AddNewClient.show()
    sys.exit(app.exec_())

