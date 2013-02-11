import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db         = connection.school
students   = db.students 

def get_sorted_students(sort_criteria=[('_id', 1)]):
	try:
		return students.find().sort(sort_criteria)

	except:
		print "Unexpected error:", sys.exc_info()[0]


def get_lowest_score_by_type(scores, type_of_score='homework'):
	print scores
	lowest_score = 100
	homework_to_be_removed = None
	for score in scores:
		if(score['type'] == type_of_score):
			print score['type'], ':', score['score']
			if(score['score']<lowest_score):
				lowest_score=score['score']
				homework_to_be_removed = score
	print "lowest score: ", lowest_score
	print "score: ", homework_to_be_removed
	return homework_to_be_removed

		# if(item['student_id'] != current_student_id):
		# 	print "\tNew student!", item['student_id']
		# 	current_student_id = item['student_id']
		# 	print "\t\t--> Removing lowest student grade", item['student_id'], item['score']
		# 	try:
		# 		if grades.remove({'_id': item['_id']}):
		# 			continue
		# 	except:
		# 		print "Unexpected error:", sys.exc_info()[0]

for student in get_sorted_students():
	scores = student['scores']
	lowest_homework = get_lowest_score_by_type(scores)
	scores.remove(lowest_homework)
	print scores
	print "------------------------------------------------"
	print "Updating Student: ",student['_id']
	try:
		students.update({'_id': student['_id']},{'scores': scores})
	except:
		print "Unexpected Error: ", sys.exc_info()[0]
	print "------------------------------------------------\n\n"



