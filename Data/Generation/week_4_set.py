import json
from faker import Faker
import random

N_students = 1000
N_exams = 5  #5 exams per student

#Secret bounds for each subject

subject_mean = {
	'Maths': 40,
	'English': 50,
	'Science': 45,
	'Physics':60,
	'Chemistry':20,
	'French':70,
	'Programming':80,
	'Cooking':85
}

subject_var = {
	'Maths': 10,
	'English': 10,
	'Science': 15,
	'Physics':10,
	'Chemistry':5,
	'French':20,
	'Programming':20,
	'Cooking':15
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

def choose_student(students):
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
	# Genenerate some grades
	grades = {}
	# Pick between 3 and 5 subjects for each student
	subjects = choose_subjects(random.randint(3,5))
	for subject in subjects:
		# Now to generate some random scores
		subject_scores = []
		for result in range(random.randint(2, 5)):
			score = random.gauss(subject_mean[subject], subject_var[subject])
			subject_scores.append(round(score,2))
		grades[subject] = subject_scores

	# Add the scores to the student
	students.append({
			'name': name,
			'id': studentID,
			'age': random.randint(18,50),
			'scores': grades
	})

#Create some fake data
students = []
for student in range(N_students):
	choose_student(students)

#Shuffle the students and grades
random.shuffle(students)


with open('week_4_data.json','w') as file:
	json.dump(students,file,indent=4)
