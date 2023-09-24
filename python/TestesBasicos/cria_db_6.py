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

# Inserindo vários documentos com id's específicos:
# O primeiro passo é montar uma lista:
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"},
 { "_id": 15, "name": "Carlos", "address": "Antônio Francisco de Andrade 421/ap.101"}
]
# O segundo passo é a inclusão propriamente dita:
x = mycol.insert_many(mylist)

# Mostrando os id's das últimas inserções:
print(x.inserted_ids)
print("Documentos incluídos com sucesso!")

# FIM