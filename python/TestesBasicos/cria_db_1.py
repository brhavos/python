### INÍCIO ###

# -------------------------------------------------------------------------------------------------
# NOME DO PROGRAMA: CRIA_DB_1.PY
# AUTOR...........: CARLOS - 08/09/2023
# FUNÇÃO..........: 1-) SELECIONA/CRIA UM DATABASE
#                   2-) SELECIONA/CRIA UMA COLLECTION
#                   3-) INCLUR UM DOCUMENTO NA COLLECTION
# PONTO DE ATENÇÃO: a-) Um database sem collection jamais serácriado;
#                   b-) Uma collection sem documentos jamais será criada;
#                   c-) Conclusão: Ao criar um database tem que já criar ao menos uma collection
#                       povoada com pelo menos um documento.
# -------------------------------------------------------------------------------------------------

# Bibliotecas:
import pymongo

# Corpo do programa:

# Conecta MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#print(myclient.list_database_names())
print("Databases existentes no localhost do MongoDB:")
print(myclient.list_database_names())
print("-----------------------------------------------------------------------------")

# Obtem a lista dos databases do servidor:
dblist = myclient.list_database_names()

# Procura pelo database desejado:
if "mydatabase" not in dblist:
  print("O database " + '"' + "mydatabase" + '"' + " não existe.")
else:
  print("O database " + '"' + "mydatabase" + '"' + " existe.")

# Seleciona/cria o Database; caso não exista, o Database será criado automaticamente.
mydb = myclient["mydatabase"]

# Verifica se a Collection existe.
collist = mydb.list_collection_names()
if "customers" in collist:
  print('A collection "customers" já existe.')
else:
  print('A collection "customers" não existe mas será criada automaticamente.')

# Seleciona (se já existir)/cria (se não exiustir) a Collection; caso não exista, a Colletcion será criado automaticamente.
mycol = mydb["customers"]

# Insere documento na collection:
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

### FIM ###