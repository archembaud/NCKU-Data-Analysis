import json
import random

# actually create an empty list
students_data = []

no_students = 10
for student in range(no_students):
	name = f"student_{student}"
	grades = {
		'Mathematics': random.randint(50,100),
                'Science': random.randint(50,100),
		'English': random.randint(50,100),
	}
	student_data = {
		'id': student,
		'name': name,
		'grades': grades
	}
	# Check if the student is failing or not
	failing = False
	for grade in grades:
		if (grades[grade]) < 60:
			failing = True
	# Add this to the student data
	student_data['isFailing'] = failing

	# Now add your new student in
	students_data.append(student_data)

# Now create the object
data = {
	'students': students_data
}

with open('tutorial_2.json','w') as json_file:
	json.dump(data,json_file,indent=4)
