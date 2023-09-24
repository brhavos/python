### INÍCIO ###

# --------------------------------------------------------------------------------------------------------------------
# NOME DO PROGRAMA: CRIA_DB_2.PY
# AUTOR...........: CARLOS - 08/09/2023
# FUNÇÃO..........: 1-) SELECIONA/CRIA UM DATABASE
#                   2-) SELECIONA/CRIA UMA COLLECTION
#                   3-) INCLUR DOCUMENTOS NA COLLECTION
# PONTO DE ATENÇÃO: a-) Um database sem collection NUNCA será criado;
#                   b-) Uma collection sem documentos NUNCA será criada;
#                   c-) Conclusão: Ao selecionar/criar um database tem que já selecionar/criar ao menos uma collection
#                       povoada com pelo menos um documento.
# --------------------------------------------------------------------------------------------------------------------

# Bibliotecas:
import pymongo

# Corpo do programa:

# Conecta com o servidor MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Verifica se o database existe:
dblist = myclient.list_database_names()
if "mydatabase" not in dblist:
    print("O Database não existia, porém, ao ser setado foi criado automaticamente.")

# Seleciona o database; caso não exista, será criado automaticamente:
mydb = myclient["mydatabase"]

# Lista todos os databases do servidor localhost:
print(myclient.list_database_names())

# Verifica se a collection existe no database:
# Se existir, apaga.
collist = mydb.list_collection_names()
if "customers" in collist:
  mycol = mydb["customers"]
  mycol.drop()
  print("Atenção! A collection foi encontrada e dropada!")

# Seleciona a collection; caso a mesma não exista, ela será criada:
mycol = mydb["customers"]

# Insere um documento:
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

# Inserindo vários documentos com id's automáticos:
# O primeiro passo é montar uma lista:
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
# O segundo passo é a inclusão propriamente dita:
x = mycol.insert_many(mylist)

# Mostrando os id's das últimas inserções:
print(x.inserted_ids)

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
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
# O segundo passo é a inclusão propriamente dita:
x = mycol.insert_many(mylist)

# Mostrando os id's das últimas inserções:
print(x.inserted_ids)

### FIM ###