import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.reddit
stories = db.stories

def find(search_query='title', value_to_match={'$regex':'Google'}, selector={'title': 1, '_id': 0}, sort_criteria=[('_id', pymongo.ASCENDING)], skip_documents=0, limit_documents=10, amount=10):
	
	if(amount>limit_documents):
		amount=limit_documents
	print "Geeting Reddit Science titles for", search_query, "with value", value_to_match
	query = { search_query: value_to_match}

	try:
		iterator = stories.find(query, selector).sort(sort_criteria)
		iterator.skip(skip_documents)
		iterator.limit(limit_documents)
	except:
		print "Unexpected error:", sys.exc_info()[0]

	sanity = 0
	for doc in iterator:
		print doc
		sanity += 1
		if (sanity>amount):
			break



find(search_query='title', value_to_match={'$regex': 'the'}, sort_criteria=[('title', pymongo.DESCENDING)])
