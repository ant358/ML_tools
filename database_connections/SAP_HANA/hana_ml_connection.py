
# Connect to the SAP Datawarehouse and upload some tables from our local db
import pandas as pd
import hana_ml.dataframe as dataframe
import sqlalchemy as sq
# Import the Connection details
import Parameters as p

# connect to local data
engine = sq.create_engine('sqlite:///../data/local.db')

# connect to HANA
conn = dataframe.ConnectionContext(
    address=p.address,
    port=p.port,
    user=p.user,
    password=p.password,
    encrypt=p.encrypt,
    sslValidateCertificate=p.sslValidateCertificate,
    databaseName=p.databaseName
)
if conn:
    print('User connected to HANA successfully')
# check the connection
assert conn.get_current_schema() == 'SPACE#USER', (
       "Not connected to the correct schema")


def load_table(schema_name='SPACE#USER',
               table_name=None,
               local_name=None):
    """Upload a table from local db to SAP HANA
    does not return anything a connection to SAP DWC (conn)
    and the local db (engine) should be available

    Args:
        schema_name (str): the schema name to upload to
        table_name (str): the table name to upload
        local_name (str): the local table name to upload from

    Returns:
        None
    """
    assert table_name is not None, "Input the SAP HANA table name"
    assert local_name is not None, "Input the name of the local db table"

    # load table from local db
    df = pd.read_sql_table(local_name, con=engine)
    assert len(df) > 0, "Table did not load correctly"
    # Persist the data from the file into a table in HANA
    upload = dataframe.create_dataframe_from_pandas(
        connection_context=conn,
        pandas_df=df,
        table_name=table_name,
        schema=schema_name,
        force=True,
        replace=True)

    upload = conn.table(table_name, schema=schema_name)
    print('Success!\n', upload.head(1).collect())
