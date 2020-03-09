import pyodbc


with open('./create_tables_and_db_script.sql', 'r') as f:
    create_db_statement = f.readline(2)
    create_tables_statement = f.read()
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-1OJ7R9S\SQLEXPRESS;', autocommit = True)
cursor = connection.cursor()
cursor.execute(create_db_statement)
cursor.execute(create_tables_statement)
