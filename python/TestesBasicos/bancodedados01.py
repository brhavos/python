# Create a database called "mydatabase" no localhost
import pymongo

#-----------------------------------------------------------

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print("")
print("Características da conexão: ")
print(myclient)

meus_databases = myclient.list_database_names()
print("Meus Databases: ")
print(meus_databases)
print ("Quantidade de databases:", len(meus_databases))
print("-------------------------------------------------------")

for db in enumerate(meus_databases):
    print (db)

print("-------------------------------------------------------")

print (meus_databases[0])
print (meus_databases[1])
print (meus_databases[2])
print (meus_databases[3])
print (meus_databases[4])

db_corrente = meus_databases[2]

print(db_corrente)
print ("Banco corrente:", db_corrente)

minha_colecao = db_corrente["db-teste"]

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'dbname'
mongo = PyMongo(app)



# Fim.