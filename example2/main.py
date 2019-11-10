from clients.clients import Ui_ClientsViewer
from add_clients.add_clients_model import AddNewClient
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import pandas as pd
from os.path import join 
from utils import qt_utils,my_utils

class ClientsVisualizationUI(Ui_ClientsViewer):
    def __init__(self):
        super(ClientsVisualizationUI, self).__init__()      
        config_path='config.json'
        self.config = json.load(open(config_path, 'rb'))        
        self.df_clients_path = join(self.config['resource'],'baseclientes.csv')

    def setupUi(self, parent):
        super().setupUi(parent)
        
        # Open Database
        df_clients = pd.read_csv(self.df_clients_path)

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
            my_utils.write_client_database(self.df_clients_path, self.clients_table)
            qt_utils.show_message(title="Información de Usuario",\
                                    text="Base de datos actualizada")
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