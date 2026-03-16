# Tutorials

These are the class activities we will complete during class time.

We'll go over their solution during class time.

## Tutorial 16th March

The code for the solution can be found [here](./grades_solution.py). Probably the most important part of the code is this:

```python
subject_lists = {}

for exam in grades:
	if exam['subject'] not in subject_lists:
		subject_lists[exam['subject']] = []
	# Add the subject score to that list
	subject_lists[exam['subject']].append(exam['score'])
```
We have an empty dictionary (subject_lists) which initially contains nothing. When a new subject is found (one which has no record in the subject_lists dictionary) we create an empty list in the dictionary to store grades in.

Later, when continuing to process the list of grades, we simply append each exam score (exam['score']) to the list for that subject. When we are done, the subject_lists dictionary looks like:

```python
subject_lists = {
    'Maths': [28, 100, ....., 85],
    'Cooking': [28, 100, ....., 85],
    'French': [16, 22, ..., 19]
    etc
}
```
Finally, we simply need to load each of these lists to get the statistics for each subject:

```python
for subject in subject_lists:
	subject_data = subject_lists[subject]
	avg = statistics.mean(subject_data)
	stddev = statistics.stdev(subject_data)
	median = statistics.median(subject_data)
```

And that's it! See, computing the mean, standard deviation and median for this data isn't the hardest part - the harder part is processing the data and getting it into a form which we can use to compute these properties. This is typical of any data analysis problem. So, go practice your Python!