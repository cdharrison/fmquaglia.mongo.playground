import pymongo
import datetime
import sys

def insert():
	connection = pymongo.Connection('mongodb://localhost', safe=True)
	db = connection.school
	people = db.people

	fabricio = {'name': 'Fabricio', 'company': 'Deviget', 'interests': ['programming', 'sax', 'photography']}	
	angeles = {'_id': 'angeles', 'name': 'Angeles', 'company': 'Molnar INC', 'interests': ['music', 'guitar', 'cats']}

	try:
		people.insert(fabricio)
		people.insert(angeles)

	except:
		print "Unexpected error: ", sys.exc_info()[0]

	print people.find()

def using_save():
	connection = pymongo.Connection('mongodb://localhost', safe=True)
	db = connection.school
	scores = db.scores

	try:
		score = scores.find_one({'student_id': 1, 'type': 'homework'})
		print 'before', score

		score['review_date'] = datetime.datetime.utcnow()
		scores.save(score)

		score = scores.find_one({'student_id': 1, 'type': 'homework'})
		print "after", score

	except:
		print "Unexpected error: ", sys.exc_info()[0]

def using_update():
	connection = pymongo.Connection('mongodb://localhost', safe=True)
	db = connection.school
	scores = db.scores
	criteria = {'student_id': 1, 'type': 'homework'}

	try:
		score = scores.find_one(criteria)
		print 'before', score

		score['review_date'] = datetime.datetime.utcnow()

		scores.update(criteria, score)
		print "after", score

	except:
		print "Unexpected error: ", sys.exc_info()[0]

def using_set(): # This is far more eficient
	connection = pymongo.Connection('mongodb://localhost', safe=True)
	db = connection.school
	scores = db.scores
	criteria = {'student_id': 1, 'type': 'homework'}

	try:
		score = scores.find_one(criteria)
		print 'before', score

		scores.update(criteria, {'$set': 
								{'review_date': datetime.datetime.utcnow()}
								}) # because you only update a small part of the document
		
		score = scores.find_one(criteria)
		print "after", score

	except:
		print "Unexpected error: ", sys.exc_info()[0]


def remove_review_date():
	connection = pymongo.Connection('mongodb://localhost', safe=True)
	db = connection.school
	scores = db.scores
	criteria = {'student_id': 1, 'type': 'homework'}

	try:
		score = scores.find_one(criteria)
		print 'before', score

		scores.update({}, {'$unset': {'review_date':1}}, multi=True)

		score = scores.find_one(criteria)
		print 'after', score
	except:
		print "Unexpected error: ", sys.exc_info()[0]



remove_review_date()