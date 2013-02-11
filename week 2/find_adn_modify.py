import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.test
counters = db.counters

def get_next_sequence_numbers(name):
	try:
		counter = counters.find_and_modify(query  = {'type':name},
			                               update = {'$inc':{'value':1}}, 
			                               upsert = True, 
			                               new    = True) #new means that the new value must be returned, not the old one
		
		counter_value = counter['value']
		return counter_value

	except:
		print "Unexpected error", sys.exc_info()[0]

print get_next_sequence_numbers('uid')
print get_next_sequence_numbers('uid')
print get_next_sequence_numbers('uid')
print get_next_sequence_numbers('uid')
