from sqlalchemy import create_engine

server = "XXXXXXX"
database = "XXXXXX"

engine = create_engine('mssql+pyodbc://' + server + '/' +
                       database + '?trusted_connection=yes&'
                       'driver=ODBC+Driver+13+for+SQL+Server')
# check the connection worked
engine.table_names()
