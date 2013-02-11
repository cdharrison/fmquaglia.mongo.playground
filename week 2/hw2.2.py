import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db         = connection.students
grades     = db.grades 

def get_sorted_set_by_type(type_of_grade='homework', sort_criteria=[('student_id', 1), ('score', 1)]):
	try:
		return grades.find({'type': type_of_grade}).sort(sort_criteria)

	except:
		print "Unexpected error:", sys.exc_info()[0]

def remove_lowest_grade_for_score(iterator):
	current_student_id = ""
	for item in iterator:
		if(current_student_id != ""):
			print "\n****************************"
			print "Student id",item['student_id']
		if(item['student_id'] != current_student_id):
			print "\tNew student!", item['student_id']
			current_student_id = item['student_id']
			print "\t\t--> Removing lowest student grade", item['student_id'], item['score']
			try:
				if grades.remove({'_id': item['_id']}):
					continue
			except:
				print "Unexpected error:", sys.exc_info()[0]

		print "\t\t(.) Remaining student grade", item['student_id'], item['score']


iterator = get_sorted_set_by_type()
print iterator.count()

remove_lowest_grade_for_score(iterator)


