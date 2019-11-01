from clientes import Ui_ClientsViewer
from adicionar_clientes import Ui_AddNewClient
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import pandas as pd
from os.path import join 

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

class ClientsVisualizationUI(Ui_ClientsViewer):
    def __init__(self):
        super(ClientsVisualizationUI, self).__init__()      
        config_path='example2\\config.json'
        self.config = json.load(open(config_path, 'rb'))        
        
    def setupUi(self, parent):
        super().setupUi(parent)
        
        # Open Database
        df_clients_path = join(self.config['home_path'],'baseclientes.csv')
        df_clients = pd.read_csv(df_clients_path)

        # Fill the Table
        for _,row in df_clients.iterrows():
            rowPosition = self.clients_table.rowCount()
            self.clients_table.insertRow(rowPosition)
            self.clients_table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(row['Cliente'])))
            if not str(row['Dirección'])=='nan':
                self.clients_table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(row['Dirección'])))
            if not str(row['RUC'])=='nan':
                self.clients_table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(int(row['RUC']))))            
        self.clients_table.resizeColumnsToContents()

        # Add Client
        self.add_client.clicked.connect(self.add_client_callback)

        # Remove Client
        def remove_row():
            index_list = [QtCore.QPersistentModelIndex(row)
                            for row in self.clients_table.selectionModel().selectedRows()]

            for index in index_list:
                self.clients_table.removeRow(index.row())

        self.remove_client.clicked.connect(remove_row)

        # Save Clients Database
        def save_clients():
            allRows = self.clients_table.rowCount()
            new_df = pd.DataFrame(columns=['Cliente','Dirección','RUC'])
            for row in range(allRows):
                client = self.clients_table.item(row,0)
                address = self.clients_table.item(row,1)
                ruc = self.clients_table.item(row,2)
                
                client = client.text() if client else ""
                address= address.text() if address else ""
                ruc = ruc.text() if ruc else ""
                new_df=new_df.append({'Cliente':client, 'Dirección':address, 'RUC':ruc}, ignore_index=True)
            new_df.to_csv(df_clients_path, index=False)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Base de datos actualizada")
            msg.setWindowTitle("Información de Usuario")
            msg.exec()
        # TODO: Sorted
        self.save_clients.clicked.connect(save_clients)

        
    def add_client_callback(self):
        diag = QtWidgets.QDialog()
        ac = AddNewClient()
        ac.setupUi(diag)
        ac.binding(diag, self)
        diag.setWindowTitle('Adicionar Nuevo Cliente')
        diag.exec_()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ClientsVisualizationUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())