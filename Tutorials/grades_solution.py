# Solution to class problem given out on the 16th of March.
# The problem is to read in the grades and names data, and then find the average age of all the Matts, and the average score of all the Matts.

import json
import statistics

grades = None
with open('./../Data/grades.json') as file:
	grades=json.load(file)

names = None
with open('./../Data/names.json') as file:
	names = json.load(file)

# PART A: Find statistics around Matt Smith's age and average score

matt_list = []
age_list = []
for name in names:
	if name['name'] == 'Matt Smith':
		matt_list.append(name)
		age_list.append(name['age'])

avg_age = statistics.mean(age_list)
print(f'Average age of all Matt Smiths is {avg_age} years')

# Note: this is not as efficient as it could be, because we are looping through the grades for each Matt Smith. A more efficient way would be to loop through the grades once,
# and keep track of the scores for each Matt Smith in a dictionary. This is how we solve PART B. But this is easier to understand for now.
for matt in matt_list:
	score_list = []
	for grade in grades:
		if grade['id'] == matt['id']:
			score_list.append(grade['score'])

	avg_score = statistics.mean(score_list)
	print(f'Average score of Matt Smith with id {matt["id"]} is {avg_score}')


# PART B: Find statistics around all the subjects. For each subject, find the average score, standard deviation and median score.
# Start with an empty dictionary to store the scores for each subject. The keys will be the subject names, and the values will be lists of scores for that subject.
subject_lists = {
}

for exam in grades:
	if exam['subject'] not in subject_lists:
		subject_lists[exam['subject']] = []
	#Add the subject score to that list
	subject_lists[exam['subject']].append(exam['score'])

#Now we can find the statistics
for subject in subject_lists:
	print(f"==== Looking at subject = {subject} ====")
	subject_data = subject_lists[subject]
	avg = statistics.mean(subject_data)
	stddev = statistics.stdev(subject_data)
	median = statistics.median(subject_data)
	print(f"Mean = {avg},\t Standard Deviation = {stddev},\tMedian = {median}")

