import pandas as pd
import sqlalchemy as sq
# Import the Connection details
import Parameters as p

# creation of central connection objects
engine = sq.create_engine(f'hana://{p.dbUser}:{p.dbPwd}@{p.dbHost}:{p.dbPort}',
                          connect_args={
                                        'sslTrustStore': "",
                                        'encrypt': 'true',
                                        # 'databaseName': 'None',
                                        'sslValidateCertificate': 'false',
                                        'sslHostNameInCertificate': '*'
                                       },
                          # Set echo=True, if you need a log
                          echo=False)
# check the connection
tables = engine.table_names()
assert len(tables) > 0
# check communication with the database
sql = f"""SELECT * FROM {tables[0]} LIMIT 10"""
df = pd.read_sql_query(sql, con=engine)
assert len(df) > 0
# load a test table
df = pd.read_csv("test.csv")
df.to_sql('test_table',
          con=engine,
          schema=p.dbIngestionSchema,
          if_exists='replace')
