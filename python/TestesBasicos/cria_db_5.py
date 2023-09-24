'''
FUNÇÕES DESTE PROGRAMA:
    - CONECTA NO MONGO-DB ATLAS;
    - OBTÉM OS DATABASES;
    - SELECIONA UM DOS DATABASES;
    - OBTÉM AS COLLECTIONS DO MESMO.
    - INCLUI UM REGISTRO NUMA NOVA TABELA.

    OBS.: PARA ENTENDIMENTO É IMPORTANTE LER OS COMENTÁRIOS.
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


# -----------------------------------------------------------------


# Verifica se a Collection existe.
collist = mydb.list_collection_names()
if "customers" in collist:
  print('A collection "customers" já existe.')
  mycol = mydb["customers"]
  mycol.drop()
  print("Atenção! A collection foi encontrada e dropada e será criada automaticamente adiante...")
else:
  print('A collection "customers" não existe mas será criada automaticamente.')

# Seleciona (se já existir)/cria (se não exiustir) a Collection; caso não exista, a Colletcion será criado automaticamente.
mycol = mydb["customers"]

# Insere documento na collection:
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print("Um registro foi incluído com sucesso!")

# FIM