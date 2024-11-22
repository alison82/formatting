import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import pyodbc

#EXCEL PROCESSING

#open excel file
sheet = pd.read_excel('DataRequestandSourceField.xlsx');

#print(sheet)

#MSSQL PROCESSING

#connection
serverName = '127.0.0.1'
databaseName = 'formatting'

uri = "DRIVER={ODBC Driver 17 for SQL server};SERVER=localhost;DATABASE=master;UID=sa;PWD=ECABank1"

try:
    connection = pyodbc.connect(uri)
    print('connected')

    cursor = connection.cursor()

    cursor.execute("")
    cursor.commit()
    cursor.close()  
except pyodbc.Error as ex:
    print('connection failed', ex)
