'''
Example loading a large json holding fake names and details
'''
import json

names = None
with open('./../Data/names.json') as f:
	names = json.load(f)
	print(names)
