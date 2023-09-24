'''
FUNÇÕES DESTE PROGRAMA:
    - CONECTA NO MONGO-DB ATLAS;
    - OBTÉM OS DATABASES;
    - SELECIONA UM DOS DATABASES;
    - OBTÉM AS COLLECTIONS DO MESMO.
'''

# BIBLIOTECAS:
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# STRING DE CONEXÃO:
# uri = "mongodb+srv://<NOME-DO-DATABASSE>:<SENHA>@cluster0.ahz1ode.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://db-teste:aaa111@cluster0.ahz1ode.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# OBTENDO A LISTA DE DATABASES:
dblist = client.list_database_names()
print(dblist)

# Seleciona/cria o Database; caso não exista, o Database será criado automaticamente.
mydb = client["db-teste"]

# OBTENDO COLLECTIONS DO DB-TESTE:
collist = mydb.list_collection_names()
print(collist)

# FIM