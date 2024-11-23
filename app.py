import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import pyodbc

#EXCEL PROCESSING

file = 'DataRequestandSourceField.xlsx'

#sheet_names = ['Field 21', 'Field 23', 'Field 24', 'Field 804, 806', 'Field 723', 'Field 724', 'OS Data - Accounts (Debra)',  'Clients (Lorraine)', 'Persons (Lorraine)', 'OS Data - Transaction (Sophie)', 'Person to Client-Reln (Sophie)'] 

#xls_sheets = pd.read_excel(file, sheet_name = sheets_names)

xls_file = pd.ExcelFile(file)

#table structure from 6 to 10

# Get the list of sheet names
sheet_names = xls_file.sheet_names
#print(sheet_names)

# Get the list of sheets
dfs = {}

for name in sheet_names:
    dfs[name] = pd.read_excel(file, name)

#print(dfs[sheet_names[6]])

#Get table structure
df_structure = dfs[sheet_names[6]]

#colums names
cn_tmp = df_structure.columns

cn = list(filter(lambda value: not('Unnamed' in value), cn_tmp))

#print(cn)

table_names = cn

#getting values
field_names = df_structure.iloc[2:49, 0]

#getting field info
field_info = []
c = 2

for name in field_names:
    field_info.append(df_structure.iloc[c, 1:6])   

#[x, y] -> x row, y colum
#print(field_info[1][4])

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

    #create accounts table
    query = "CREATE TABLE " + table_names[0] + "("

    c = 0
    for name in field_names:
        query += name + " " + field_info[c][0] + " "
        
        if (field_info[c][0] == 'date'):
            query += "" + name + ""
            True
        else:
            False


        + " " + field_info[c][0] +  "({})".format(field_info[c][1])  + ","
        c += 1

    print("".format(query))

    #cursor.execute("")
    cursor.commit()
    cursor.close()  
except pyodbc.Error as ex:
    print('connection failed', ex)