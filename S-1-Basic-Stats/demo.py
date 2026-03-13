'''
Example computing the average age
'''
import json
import statistics

names = None
with open('./../Data/names.json') as f:
	names = json.load(f)

# Create an empty list holding ages
ages = []
for name in names:
	ages.append(name['age'])

# Compute the mean, median and standard deviation
average_age = statistics.mean(ages)
print(f"The average age is {average_age} years.")

deviation_age = statistics.stdev(ages)
print(f"The standard deviation is {deviation_age}")

median_age = statistics.median(ages)
print(f"The median age is {median_age}") 
