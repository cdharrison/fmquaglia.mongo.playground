import pymongo
import bottle

@bottle.route('/')
def index():
	from pymongo import Connection
	connection = Connection("localhost", 27017)
	db = connection.test
	names = db.names
	item = names.find_one()
	return "<p>Hello %s</p>" % item['name']

bottle.run(host="localhost", port=8089)
