import pyodbc
import os

path_to_procedures = './create_db_elements/create_procedures'
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-1OJ7R9S\SQLEXPRESS;DATABASE=test', autocommit = True)
cursor = connection.cursor()
for item in os.listdir(path_to_procedures):
    if os.path.isfile(os.path.join(path_to_procedures,item)):
        with open(os.path.join(path_to_procedures,item), 'r') as f:
            statement = f.read()
            cursor.execute(statement)
connection.close()