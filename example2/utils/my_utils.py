import pandas as pd

def write_client_database(df_clients_path, clients_table):
    allRows = clients_table.rowCount()
    new_df = pd.DataFrame(columns=['Cliente','Dirección','RUC'])
    for row in range(allRows):
        client = clients_table.item(row,0)
        address = clients_table.item(row,1)
        ruc = clients_table.item(row,2)
        
        client = client.text() if client else ""
        address= address.text() if address else ""
        ruc = ruc.text() if ruc else ""
        new_df=new_df.append({'Cliente':client, 'Dirección':address, 'RUC':ruc}, ignore_index=True)
    new_df.to_csv(df_clients_path, index=False)