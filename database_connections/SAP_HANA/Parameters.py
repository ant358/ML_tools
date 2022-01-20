# Internet host name for the database
address= 'xxxxxxxxxxxxxxx.hana.prod-us10.hanacloud.ondemand.com'
dbHost= 'xxxxxxxxxxxxxxxx.hana.prod-us10.hanacloud.ondemand.com'

#define here the port number of your HANA Server
port= 443
dbPort=443
#define here the username/password of your HANA user to access the Server
user= 'SPACE#USER'
dbUser = 'SPACE#USER'
password='V%6(6[I/;N_UI+nR'
dbPwd='V%6(6[I/;N_UI+nR'
dbIngestionSchema= 'SPACE#USER'
dbConsumptionSchema= 'SPACE'
dbExampleTable= 'A_TABLE'
#define whether to use encryption - HANA Cloud requires encryption
encrypt=True 

#define whether to use ssl certificate validation - HANA Cloud does required validation
sslValidateCertificate=False

#define here the tenant name of your HANA system -HANA Cloud does not expose tenants
databaseName=None
