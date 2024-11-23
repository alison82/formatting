# formatting

Requisites
docker v27.x
anaconda environment v3 
python v3.x 
ODBC v17


Proposal
Environment configuration

docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=ECABank1" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest



Libraries
pandas, pyodbc
