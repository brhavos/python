/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('db-teste');

// Apaga a tabela (para criá-la adiante):
db.cidades.drop()

// Criação automática através de:
//Insert a few documents into the sales collection.
db.getCollection('cidades').insertMany([
  { '_id': '1', 'nome': 'Campinas', 'uf': 'SP'},
  { '_id': '2', 'nome': 'Americana', 'uf': 'SP'},
  { '_id': '3', 'nome': 'Jaguariúna', 'uf': 'SP'},
  { '_id': '4', 'nome': 'Limeira', 'uf': 'SP'},
  { '_id': '5', 'nome': 'Piracicaba', 'uf': 'SP'},  
]);

// Exibição dos registros por ordem cronológica:
//db.cidades.find()

// Exibição dos registros por ordem de nome descendente:
db.cidades.find().sort({nome: -1})

/*
FIM
*/