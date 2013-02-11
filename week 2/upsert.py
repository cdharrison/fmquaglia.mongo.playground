import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.test
things = db.things

def using_upsert():
	print "updating with upsert"

	try:
		things.drop()
		
		things.update({'thing':'apple'},{'$set':{'color':'red'}}, upsert=True)
		things.update({'thing':'pear'},{'color':'green'}, upsert=True)

		apple = things.find_one({'thing': 'apple'})
		pear = things.find_one({'thing': 'pear'})

		print "apple:", apple
		print "pear:", pear

	except:
		print "Unexpected error", sys.exc_info()[0]

using_upsert()