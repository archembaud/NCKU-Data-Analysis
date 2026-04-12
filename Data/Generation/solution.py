import json
import statistics
import math

target_subject = 'Maths'
target_score = 50


Data = None
with open('week_4_data.json') as f:
	Data = json.load(f)

print(Data)
all_scores = []
for student in Data:
	print(student)
	if target_subject in student['scores']:
		# This student did this subject, get the data
		student_scores = student['scores'][target_subject]
		for score in student_scores:
			all_scores.append(score)

print(f"All scores = {all_scores}")
mean_score = statistics.mean(all_scores)
std_dev = statistics.stdev(all_scores)
print(f"Mean = {mean_score}, standard dev = {std_dev}")
z = (target_score-mean_score)/std_dev;
Pr = 1 - 0.5*(1 + math.erf(z/math.sqrt(2)))
print(f"Percentage chance of getting higher than {target_score} in {target_subject}  = {round(Pr*100,2)}")
