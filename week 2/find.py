import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.school
scores = db.scores

def find(type='exam', minimum=0, maximum=100, amount=10):
	if type not in ['exam', 'homework', 'quiz']:
		print 'I don\'t know what is', type	
		return

	print "find, reporting for duty"
	query = {'type': type, 'score': {'$gt': minimum, '$lt': maximum}}
	selector = {'student_id': 1, '_id': 0, 'score': 1}

	try:
		iterator = scores.find(query, selector)
	except:
		print "Unexpected error:", sys.exc_info()[0]

	sanity = 0
	for doc in iterator:
		print doc
		sanity += 1
		if (sanity>amount):
			break


def find_one(student_id=10):
	print "find one, reporting for duty"
	query = {'student_id': student_id}
	selector = {'student_id': 1, '_id': 0}

	try:
		doc = scores.find_one(query, selector)
	except:
		print "Unexpected error:", sys.exc_info()[0]

	print doc

find('homework', 20, 70, 20)
find_one(23)
