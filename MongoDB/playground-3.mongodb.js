use('db-teste')


db.cidades.updateOne
(
	{
		"_id" : "2"
	},
	{
		$set :
		{
			"nome" : "aaa bbb ccc",
            "uf":"yy"
		}
	}
)

db.cidades.find({_id: "2"})

// FIM //