import statistics
import math
import json
import matplotlib.pyplot as plt

subject = "Maths"
target_score = 50

Data = None
with open('./../Data/Generation/week_4_data.json') as f:
    Data = json.load(f)

all_scores = []
for student in Data:
    if (subject in student['scores']):
        student_scores = student['scores'][subject]
        for score in student_scores:
            all_scores.append(score)

print(f"Found {len(all_scores)} valid {subject} scores")

# Do some maths to compute probablility
mean = statistics.mean(all_scores)
stddev = statistics.stdev(all_scores)
Z = (target_score - mean)/stddev
Pr = 1 - 0.5*(1 + math.erf(Z/math.sqrt(2)))
print(f"Chance of {subject} score being more than {target_score} is {round(Pr*100, 2)} %")

# Create histogram

# Pretty
plt.hist(all_scores, bins=20, edgecolor='black')

# Plain (default)
# plt.hist(all_scores)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f'Histogram of {subject} scores')
# Show plot
plt.show()
