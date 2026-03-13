import json
from faker import Faker
import random

N_students = 1000
N_exams = 5  #5 exams per student

#Secret bounds for each subject

min_bounds = {
	'Maths': 40,
	'English': 50,
	'Science': 45,
	'Physics':60,
	'Chemistry':20,
	'French':70,
	'Programming':80,
	'Cooking':85
}

def choose_subjects(N=5):
	candidate_subjects = ['Maths','English','Science','Physics','Chemistry','French','Programming', 'Cooking']
	subjects = []
	for i in range(N):
		while (True):
			random_subject_index = random.randint(0,len(candidate_subjects)-1)
			random_subject = candidate_subjects[random_subject_index]
			if random_subject not in subjects:
				subjects.append(random_subject)
				break

	return subjects

def choose_student(students, grades, N_exams=5):
	#There is a chance this person is called Matt Smith
	chance = random.random()
	name = None
	studentID = f"E{random.randint(1000000,1999999)}"
	if (chance < 0.005):
		name = "Matt Smith"
	else:
		fake = Faker()
		name = fake.name()
	# Add the student
	students.append({
		'name': name,
		'id': studentID,
		'age': random.randint(18,50)
	})
	# Now add some grades
	subjects = choose_subjects(N_exams)
	for subject in subjects:
		grades.append({
			'id': studentID,
			'subject': subject,
			'score': random.randint(min_bounds[subject],100)
		})


#Create some fake data
students = []
grades = []
for student in range(N_students):
	choose_student(students, grades)

#Shuffle the students and grades
random.shuffle(students)
random.shuffle(grades)

# Dump these to JSON
with open('grades.json','w') as file:
	json.dump(grades,file,indent=4)

with open('names.json','w') as file:
	json.dump(students,file,indent=4)
