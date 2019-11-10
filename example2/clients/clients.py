# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clients/clients.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientsViewer(object):
    def setupUi(self, ClientsViewer):
        ClientsViewer.setObjectName("ClientsViewer")
        ClientsViewer.resize(892, 393)
        self.centralwidget = QtWidgets.QWidget(ClientsViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.clients_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.clients_groupBox.setGeometry(QtCore.QRect(10, 290, 861, 61))
        self.clients_groupBox.setObjectName("clients_groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.clients_groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_client = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_client.setMinimumSize(QtCore.QSize(0, 30))
        self.add_client.setObjectName("add_client")
        self.horizontalLayout.addWidget(self.add_client)
        self.save_clients = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_clients.setMinimumSize(QtCore.QSize(0, 30))
        self.save_clients.setObjectName("save_clients")
        self.horizontalLayout.addWidget(self.save_clients)
        self.remove_client = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.remove_client.setMinimumSize(QtCore.QSize(0, 30))
        self.remove_client.setObjectName("remove_client")
        self.horizontalLayout.addWidget(self.remove_client)
        self.clients_table = QtWidgets.QTableWidget(self.centralwidget)
        self.clients_table.setGeometry(QtCore.QRect(10, 10, 861, 271))
        self.clients_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.clients_table.setColumnCount(3)
        self.clients_table.setObjectName("clients_table")
        self.clients_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.clients_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clients_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.clients_table.setHorizontalHeaderItem(2, item)
        self.clients_table.horizontalHeader().setCascadingSectionResizes(False)
        self.clients_table.horizontalHeader().setStretchLastSection(True)
        self.clients_table.verticalHeader().setCascadingSectionResizes(False)
        self.clients_table.verticalHeader().setStretchLastSection(False)
        ClientsViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ClientsViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 22))
        self.menubar.setObjectName("menubar")
        ClientsViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ClientsViewer)
        self.statusbar.setObjectName("statusbar")
        ClientsViewer.setStatusBar(self.statusbar)

        self.retranslateUi(ClientsViewer)
        QtCore.QMetaObject.connectSlotsByName(ClientsViewer)

    def retranslateUi(self, ClientsViewer):
        _translate = QtCore.QCoreApplication.translate
        ClientsViewer.setWindowTitle(_translate("ClientsViewer", "Base de dados de clientes"))
        self.clients_groupBox.setTitle(_translate("ClientsViewer", "Clientes"))
        self.add_client.setText(_translate("ClientsViewer", "Adicionar Cliente"))
        self.save_clients.setText(_translate("ClientsViewer", "Guardar Cambios"))
        self.remove_client.setText(_translate("ClientsViewer", "Remover cliente"))
        item = self.clients_table.horizontalHeaderItem(0)
        item.setText(_translate("ClientsViewer", "Cliente"))
        item = self.clients_table.horizontalHeaderItem(1)
        item.setText(_translate("ClientsViewer", "Dirección"))
        item = self.clients_table.horizontalHeaderItem(2)
        item.setText(_translate("ClientsViewer", "RUC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientsViewer = QtWidgets.QMainWindow()
    ui = Ui_ClientsViewer()
    ui.setupUi(ClientsViewer)
    ClientsViewer.show()
    sys.exit(app.exec_())

