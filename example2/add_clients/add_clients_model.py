from add_clients.add_clients import Ui_AddNewClient
from PyQt5 import QtWidgets

class AddNewClient(Ui_AddNewClient):
    def __init__(self):
        super(AddNewClient, self).__init__()
    
    def binding(self, container, main_windows):

        # Add Client
        def add_client():
            rowPosition = main_windows.clients_table.rowCount()
            main_windows.clients_table.insertRow(rowPosition)

            client_name = self.client_name.text()
            address = self.address.text()
            ruc = self.ruc.text()

            main_windows.clients_table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(client_name))
            if not address == 'nan':
                main_windows.clients_table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(address))
            if not ruc == 'nan':
                main_windows.clients_table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(ruc))

            container.close()

        self.add_client.clicked.connect(add_client)

        # Reset Fields
        def reset_fileds():
            for elem in [self.client_name, self.address, self.ruc]:
                elem.clear()
        self.reset_fileds.clicked.connect(reset_fileds)

        # Close
        self.cancel.clicked.connect(lambda : container.close())