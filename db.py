import pyodbc

#MSSQL PROCESSING

#connection
serverName = '127.0.0.1'
databaseName = 'formatting'

uri = "DRIVER={ODBC Driver 17 for SQL server};SERVER=localhost;DATABASE=formatting;UID=sa;PWD=ECABank1"

try:
    connection = pyodbc.connect(uri)
    print('connected')


    #create database structure
    
    cursor = connection.cursor()

    #cursor.execute("")
    cursor.commit()
    cursor.close()  
except pyodbc.Error as ex:
    print('connection failed', ex)

